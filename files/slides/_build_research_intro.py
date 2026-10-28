#!/usr/bin/env python3
"""5-slide expert briefing. Palette: premium academic blue."""

from lxml import etree
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# Premium blue
DEEP = RGBColor(0x0A, 0x1F, 0x3D)
PRIMARY = RGBColor(0x12, 0x3A, 0x63)
MID = RGBColor(0x1E, 0x4E, 0x7A)
ACCENT = RGBColor(0x3A, 0x7C, 0xA5)
PALE = RGBColor(0xC5, 0xD6, 0xE6)
WASH = RGBColor(0xE8, 0xF0, 0xF6)
BG = RGBColor(0xF4, 0xF7, 0xFB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x12, 0x20, 0x33)
MUTED = RGBColor(0x5B, 0x6B, 0x7C)
LINE = RGBColor(0xD0, 0xDC, 0xE6)
SOFT = RGBColor(0xB8, 0xCD, 0xDE)

CN = "微软雅黑"
EN = "Calibri"
PT = "/tmp/research-intro-portrait.png"


def rgb_hex(c):
    return f"{c[0]:02X}{c[1]:02X}{c[2]:02X}"


def set_run_font(run, size, color, bold=False, name=CN):
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = name
    rpr = run._r.get_or_add_rPr()
    latin = rpr.get_or_add_latin()
    latin.set("typeface", name)
    ea = rpr.find(qn("a:ea"))
    if ea is None:
        ea = etree.SubElement(rpr, qn("a:ea"))
    ea.set("typeface", CN)


def add_box(slide, left, top, width, height, fill=None, line=None, radius=None):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(kind, left, top, width, height)
    shape.shadow.inherit = False
    if radius:
        # 0.05–0.12 keeps a quiet corner; larger values look bubbly.
        try:
            shape.adjustments[0] = radius
        except Exception:
            pass
    if fill is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Emu(6350)
    return shape


def set_linear_gradient(shape, hex1, hex2, angle=270):
    spPr = shape._element.spPr
    for tag in ("a:solidFill", "a:gradFill", "a:noFill"):
        el = spPr.find(qn(tag))
        if el is not None:
            spPr.remove(el)
    grad = etree.SubElement(spPr, qn("a:gradFill"))
    gs_lst = etree.SubElement(grad, qn("a:gsLst"))
    for pos, col in ((0, hex1), (100000, hex2)):
        gs = etree.SubElement(gs_lst, qn("a:gs"))
        gs.set("pos", str(pos))
        srgb = etree.SubElement(gs, qn("a:srgbClr"))
        srgb.set("val", col)
    lin = etree.SubElement(grad, qn("a:lin"))
    lin.set("ang", str(int(angle * 60000)))
    lin.set("scaled", "0")


def add_text(slide, left, top, width, height, lines, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.margin_left = Inches(0.04)
    tf.margin_right = Inches(0.04)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    try:
        tf._txBody.bodyPr.set(
            "anchor",
            {MSO_ANCHOR.TOP: "t", MSO_ANCHOR.MIDDLE: "ctr", MSO_ANCHOR.BOTTOM: "b"}[anchor],
        )
    except Exception:
        pass
    for i, item in enumerate(lines):
        text, size, color, bold = item[:4]
        space_after = item[4] if len(item) > 4 else 0
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.clear()
        run = p.add_run()
        run.text = text
        set_run_font(run, size, color, bold)
        p.space_after = Pt(space_after)
        p.line_spacing = 1.18
    return box


def add_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def set_bg(slide, color=BG):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def deco_circle(slide, left, top, size, fill):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
    shape.shadow.inherit = False
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    # soften by setting transparency on the solid fill
    spPr = shape._element.spPr
    solid = spPr.find(qn("a:solidFill"))
    if solid is not None:
        srgb = solid.find(qn("a:srgbClr"))
        if srgb is not None:
            alpha = etree.SubElement(srgb, qn("a:alpha"))
            alpha.set("val", "18000")  # 18%
    return shape


def footer(slide, page, total=4):
    add_box(slide, Inches(0), Inches(7.26), SLIDE_W, Inches(0.24), fill=DEEP)
    add_text(
        slide,
        Inches(0.5),
        Inches(7.26),
        Inches(10.2),
        Inches(0.24),
        [("徐安察    浙江工商大学统计与数据科学学院", 10, SOFT, False)],
        anchor=MSO_ANCHOR.MIDDLE,
    )
    add_text(
        slide,
        Inches(11.5),
        Inches(7.26),
        Inches(1.4),
        Inches(0.24),
        [(f"{page:02d}  /  {total:02d}", 10, PALE, False)],
        align=PP_ALIGN.RIGHT,
        anchor=MSO_ANCHOR.MIDDLE,
    )


def header(slide, kicker, title):
    bar = add_box(slide, Inches(0), Inches(0), SLIDE_W, Inches(0.08), fill=DEEP)
    set_linear_gradient(bar, "0A1F3D", "1E4E7A", angle=0)
    add_text(slide, Inches(0.55), Inches(0.26), Inches(12.2), Inches(0.26), [(kicker, 12, ACCENT, False)])
    add_text(slide, Inches(0.55), Inches(0.52), Inches(12.2), Inches(0.44), [(title, 24, DEEP, True)])
    add_box(slide, Inches(0.55), Inches(1.02), Inches(0.42), Inches(0.04), fill=ACCENT)


def make_portrait():
    im = Image.open("/workspace/images/ancha.png").convert("RGB")
    w, h = im.size
    side = w
    top = max(int(h * 0.02), 0)
    if top + side > h:
        top = max(h - side, 0)
    face = im.crop((0, top, w, top + side)).resize((900, 900), Image.Resampling.LANCZOS)
    bg = Image.new("RGB", (900, 900), (10, 31, 61))
    mask = Image.new("L", (900, 900), 0)
    ImageDraw.Draw(mask).ellipse((10, 10, 889, 889), fill=255)
    bg.paste(face, (0, 0), mask)
    ImageDraw.Draw(bg).ellipse((8, 8, 891, 891), outline=(58, 124, 165), width=12)
    bg.save(PT)


def build():
    make_portrait()
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # ------------------------------------------------------------------
    # 1  个人简介
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s, BG)
    head = add_box(s, Inches(0), Inches(0), SLIDE_W, Inches(1.92), fill=DEEP)
    set_linear_gradient(head, "0A1F3D", "123A63", angle=0)
    deco_circle(s, Inches(11.6), Inches(-0.7), Inches(2.4), RGBColor(0x1E, 0x4E, 0x7A))
    s.shapes.add_picture(PT, Inches(0.42), Inches(0.22), Inches(1.48), Inches(1.48))
    add_text(s, Inches(2.10), Inches(0.28), Inches(8.5), Inches(0.44), [("徐安察", 26, WHITE, True)])
    add_text(s, Inches(2.10), Inches(0.74), Inches(8.5), Inches(0.28), [("教授、博士生导师", 14, ACCENT, False)])
    add_text(
        s,
        Inches(2.10),
        Inches(1.06),
        Inches(10.5),
        Inches(0.64),
        [
            ("浙江工商大学统计与数据科学学院", 13, PALE, False, 3),
            ("主要研究退化数据分析、寿命数据与贝叶斯推断。", 13, SOFT, False),
        ],
    )
    footer(s, 1)

    cols1 = [
        (
            ACCENT,
            "教学与人才培养",
            [
                "本科承担统计质量管理、贝叶斯数据分析、概率论等课程；研究生开设可靠性、贝叶斯计算等。",
                "指导博士、硕士研究生。学生获国家奖学金，并有多人进入南京理工大学、温州大学等高校工作。",
                "两次获评「我心目中的好导师」。指导学生参加挑战杯，作品获全国二等奖。",
            ],
        ),
        (
            PRIMARY,
            "科学研究",
            [
                "以第一或通讯作者发表论文六十余篇，其中 ESI 高被引论文 6 篇。刊物包括 NRL、SJS、JQT、EJOR、IEEE TR、IISE Transactions。",
                "2025 年出版专著《随机退化过程与统计建模》。",
                "主持国家自然科学基金青年项目 1 项、面上项目 3 项，以及浙江省自然科学基金重点项目等。获浙江省自然科学奖。",
            ],
        ),
        (
            DEEP,
            "社会服务",
            [
                "中国运筹学会可靠性分会副理事长。",
                "中国现场统计研究会可靠性工程分会、大数据统计分会常务理事。Statistical Theory and Related Fields 副主编。",
                "与华为等企业合作开展小子样可靠性分析、隐患预警等工作，并整理公开退化与可靠性数据集。",
            ],
        ),
    ]
    for i, (bar, title, bullets) in enumerate(cols1):
        x = Inches(0.42) + i * Inches(4.28)
        add_box(s, x, Inches(2.14), Inches(4.12), Inches(4.90), fill=WHITE, line=LINE, radius=0.05)
        add_box(s, x, Inches(2.14), Inches(4.12), Inches(0.06), fill=bar)
        add_text(s, x + Inches(0.18), Inches(2.30), Inches(3.76), Inches(0.40), [(title, 16, DEEP, True)])
        lines = []
        for b in bullets:
            lines.append((b, 13, INK, False, 10))
        add_text(s, x + Inches(0.18), Inches(2.78), Inches(3.76), Inches(4.10), lines)
    add_notes(
        s,
        "按三块讲。教学点课程和学生去向。科研点论文、专著和基金。社会服务点学会职务和企业合作。",
    )

    # ------------------------------------------------------------------
    # 2  研究背景
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "背景", "研究背景")
    footer(s, 2)

    add_box(s, Inches(0.50), Inches(1.22), Inches(12.30), Inches(2.55), fill=WHITE, line=LINE, radius=0.04)
    add_box(s, Inches(0.50), Inches(1.22), Inches(0.07), Inches(2.55), fill=ACCENT)
    add_text(
        s,
        Inches(0.78),
        Inches(1.36),
        Inches(11.80),
        Inches(2.28),
        [
            ("质量强国、制造强国战略对高端装备、电子元器件和航空产品的质量与可靠性提出了更高要求。", 15, INK, False, 7),
            ("这类产品通常具有高可靠、长寿命的特点。有限试验期内难以获得足够失效，寿命数据以删失为主，信息有限。", 15, INK, False, 7),
            ("与此同时，试验和服役过程中可以连续观测电流、裂纹、光强、转矩等性能指标。退化轨迹比失效时间包含更丰富的过程信息，已成为可靠性评估的重要依据。", 15, INK, False, 7),
            ("围绕高质量发展和重大装备自主可控，需要在小样本条件下给出可核验的评估与预测。", 15, INK, False),
        ],
    )

    add_text(s, Inches(0.50), Inches(3.94), Inches(12.3), Inches(0.30), [("由此形成的四个问题", 14, DEEP, True)])
    constraints = [
        ("样本量偏小", "失效稀少，先验设定对后验影响大"),
        ("指标多元相依", "多个性能量同时退化，尾部常相关"),
        ("个体异质性", "随机效应、两阶段变化和双尺度"),
        ("监测持续到达", "数据以流的形式进入，需及时更新"),
    ]
    for i, (t, d) in enumerate(constraints):
        x = Inches(0.50) + i * Inches(3.18)
        add_box(s, x, Inches(4.32), Inches(3.05), Inches(2.70), fill=WHITE, line=LINE, radius=0.05)
        add_text(s, x + Inches(0.16), Inches(4.48), Inches(2.75), Inches(0.36), [(t, 15, DEEP, True)])
        add_text(s, x + Inches(0.16), Inches(4.92), Inches(2.75), Inches(0.90), [(d, 13, MUTED, False)])
    add_notes(
        s,
        "先讲质量强国、制造强国，再落到高可靠、少失效和退化轨迹。四个问题与下一页一一对应。",
    )

    # ------------------------------------------------------------------
    # 3  主要研究工作
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "工作", "主要研究工作")
    footer(s, 3)
    add_text(
        s,
        Inches(0.50),
        Inches(1.18),
        Inches(12.30),
        Inches(0.36),
        [("针对上述四个问题，相应工作如下。", 14, MUTED, False)],
    )

    works = [
        ("样本量偏小", "客观贝叶斯与试验设计", "建立参考先验并讨论后验正常性；研究加速寿命、加速退化及小样本评估，包括永磁制动器等对象。"),
        ("指标多元相依", "多元退化过程", "建立多元 Wiener 过程与多元 Student-t 过程，刻画退化速率、波动及尾部的相依结构。"),
        ("个体异质性", "随机效应与变点模型", "在逆高斯框架下处理两阶段变化和双尺度，并引入随机效应。"),
        ("监测持续到达", "在线贝叶斯推断", "利用共轭或近似共轭结构作递推更新，给出剩余寿命预测，并用于维修决策。"),
    ]
    for i, (prob, title, body) in enumerate(works):
        col, row = i % 2, i // 2
        x = Inches(0.50) + col * Inches(6.40)
        y = Inches(1.62) + row * Inches(2.15)
        add_box(s, x, y, Inches(6.20), Inches(2.00), fill=WHITE, line=LINE, radius=0.05)
        add_box(s, x, y, Inches(0.07), Inches(2.00), fill=ACCENT if row == 0 else PRIMARY)
        add_text(s, x + Inches(0.24), y + Inches(0.14), Inches(5.75), Inches(0.26), [(prob, 12, ACCENT, False)])
        add_text(s, x + Inches(0.24), y + Inches(0.42), Inches(5.75), Inches(0.34), [(title, 16, DEEP, True)])
        add_text(s, x + Inches(0.24), y + Inches(0.84), Inches(5.75), Inches(0.98), [(body, 13, INK, False)])

    band = add_box(s, Inches(0.50), Inches(6.02), Inches(12.30), Inches(1.02), fill=DEEP, radius=0.04)
    set_linear_gradient(band, "0A1F3D", "1E4E7A", angle=0)
    add_text(
        s,
        Inches(0.72),
        Inches(6.16),
        Inches(11.90),
        Inches(0.76),
        [
            ("有关工作发表于 NRL、SJS、JQT、EJOR、IEEE TR、IISE Transactions 等。2025 年出版《随机退化过程与统计建模》。", 13, WHITE, False, 4),
            ("在研国家自然科学基金面上项目关注多维偏态厚尾退化及其贝叶斯最优设计。", 13, PALE, False),
        ],
    )
    add_notes(
        s,
        "按四个问题对讲。每块点一项代表工作即可，不必报齐刊物。",
    )

    # ------------------------------------------------------------------
    # 4  后续工作
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "展望", "后续工作")
    footer(s, 4)
    add_text(
        s,
        Inches(0.50),
        Inches(1.18),
        Inches(12.30),
        Inches(0.40),
        [("拟结合数据流、多中心数据、联邦学习和人工智能系统可靠性等方向继续开展工作。", 14, MUTED, False)],
    )

    futures = [
        ("数据流", "监测数据持续到达时，研究在线更新后的区间校准与覆盖率，使剩余寿命预测在流式场景下仍可核验。"),
        ("多中心数据", "不同试验室、批次和服役现场的数据往往不可直接合并。拟研究中心间异质性，并讨论信息综合的方法。"),
        ("联邦学习", "在数据不出域的约束下开展剩余寿命预测。已有航空发动机方面的尝试，拟进一步与过程模型和贝叶斯更新结合。"),
        ("人工智能系统可靠性", "一方面把统计建模与深度学习结合，用于预后与健康管理；另一方面讨论智能模型与智能装备自身的可靠性评估。"),
    ]
    for i, (t, d) in enumerate(futures):
        col, row = i % 2, i // 2
        x = Inches(0.50) + col * Inches(6.40)
        y = Inches(1.68) + row * Inches(2.10)
        add_box(s, x, y, Inches(6.20), Inches(1.96), fill=WHITE, line=LINE, radius=0.05)
        add_box(s, x, y, Inches(0.07), Inches(1.96), fill=ACCENT if i < 2 else PRIMARY)
        add_text(s, x + Inches(0.24), y + Inches(0.16), Inches(5.75), Inches(0.36), [(t, 16, DEEP, True)])
        add_text(s, x + Inches(0.24), y + Inches(0.58), Inches(5.75), Inches(1.20), [(d, 13, INK, False)])

    band = add_box(s, Inches(0.50), Inches(6.02), Inches(12.30), Inches(1.02), fill=DEEP, radius=0.04)
    set_linear_gradient(band, "0A1F3D", "1E4E7A", angle=0)
    add_text(
        s,
        Inches(0.72),
        Inches(6.18),
        Inches(8.4),
        Inches(0.72),
        [("以上汇报请各位批评指正。", 14, WHITE, False)],
        anchor=MSO_ANCHOR.MIDDLE,
    )
    add_text(
        s,
        Inches(9.10),
        Inches(6.16),
        Inches(3.50),
        Inches(0.76),
        [
            ("xuancha@mail.zjgsu.edu.cn", 12, WHITE, False, 2),
            ("www.xu-ancha.com", 12, PALE, False),
        ],
        anchor=MSO_ANCHOR.MIDDLE,
    )
    add_notes(
        s,
        "四块各举一句。联邦学习可提已有航空发动机工作。最后停在请批评指正。",
    )

    out = "/workspace/files/slides/research-intro-experts.pptx"
    prs.save(out)
    print(out)


if __name__ == "__main__":
    build()

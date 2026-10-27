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


def footer(slide, page, total=5):
    add_box(slide, Inches(0), Inches(7.26), SLIDE_W, Inches(0.24), fill=DEEP)
    add_text(
        slide,
        Inches(0.5),
        Inches(7.26),
        Inches(10.2),
        Inches(0.24),
        [("徐安察  ·  随机退化过程与贝叶斯可靠性推断", 10, SOFT, False)],
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
    add_text(slide, Inches(0.55), Inches(0.26), Inches(12.2), Inches(0.26), [(kicker, 12, ACCENT, True)])
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
    # 1  个人研究与业绩
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s, BG)
    rail = add_box(s, Inches(0), Inches(0), Inches(4.05), SLIDE_H, fill=DEEP)
    set_linear_gradient(rail, "0A1F3D", "123A63", angle=200)
    deco_circle(s, Inches(-1.1), Inches(-1.0), Inches(3.2), RGBColor(0x3A, 0x7C, 0xA5))
    deco_circle(s, Inches(2.3), Inches(5.6), Inches(2.6), RGBColor(0x1E, 0x4E, 0x7A))

    s.shapes.add_picture(PT, Inches(0.78), Inches(0.55), Inches(2.48), Inches(2.48))
    add_text(s, Inches(0.25), Inches(3.22), Inches(3.55), Inches(0.48), [("徐安察", 28, WHITE, True)], align=PP_ALIGN.CENTER)
    add_text(
        s,
        Inches(0.25),
        Inches(3.72),
        Inches(3.55),
        Inches(0.32),
        [("教授  ·  博士生导师", 13, ACCENT, True)],
        align=PP_ALIGN.CENTER,
    )
    add_box(s, Inches(1.70), Inches(4.14), Inches(0.64), Inches(0.03), fill=ACCENT)
    add_text(
        s,
        Inches(0.25),
        Inches(4.32),
        Inches(3.55),
        Inches(1.15),
        [
            ("浙江工商大学", 13, PALE, False, 3),
            ("统计与数据科学学院", 13, PALE, False, 10),
            ("xuancha@mail.zjgsu.edu.cn", 11, SOFT, False, 3),
            ("www.xu-ancha.com", 11, SOFT, False),
        ],
        align=PP_ALIGN.CENTER,
    )

    add_text(s, Inches(4.45), Inches(0.32), Inches(8.4), Inches(0.24), [("研究工作简介  ·  同行专家交流", 12, ACCENT, True)])
    add_text(s, Inches(4.45), Inches(0.58), Inches(8.4), Inches(0.46), [("个人研究与业绩", 28, DEEP, True)])
    add_box(s, Inches(4.45), Inches(1.10), Inches(0.42), Inches(0.04), fill=ACCENT)

    add_text(s, Inches(0.25), Inches(6.55), Inches(3.55), Inches(0.50), [("可靠性统计  ·  退化过程  ·  贝叶斯推断", 11, SOFT, False)], align=PP_ALIGN.CENTER)

    add_text(s, Inches(4.45), Inches(1.26), Inches(8.4), Inches(0.22), [("研究方向", 11, ACCENT, True)])
    fields = ["退化数据分析与建模", "贝叶斯在线学习", "客观贝叶斯方法", "寿命数据分析"]
    for i, name in enumerate(fields):
        col, row = i % 2, i // 2
        x = Inches(4.45) + col * Inches(4.30)
        y = Inches(1.50) + row * Inches(0.40)
        add_box(s, x, y, Inches(4.15), Inches(0.34), fill=WASH, radius=0.5)
        add_text(s, x, y, Inches(4.15), Inches(0.34), [(name, 12, PRIMARY, True)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    stats = [
        ("60+", "一作 / 通讯 SCI"),
        ("2,478", "Scholar 引用"),
        ("29", "h 指数"),
        ("6", "ESI 高被引"),
    ]
    for i, (val, lab) in enumerate(stats):
        x = Inches(4.45) + i * Inches(2.15)
        add_box(s, x, Inches(2.42), Inches(2.05), Inches(1.00), fill=WHITE, line=LINE, radius=0.08)
        add_text(s, x, Inches(2.48), Inches(2.05), Inches(0.48), [(val, 22, PRIMARY, True)], align=PP_ALIGN.CENTER)
        add_text(s, x, Inches(2.94), Inches(2.05), Inches(0.36), [(lab, 11, MUTED, False)], align=PP_ALIGN.CENTER)

    add_box(s, Inches(4.45), Inches(3.60), Inches(4.20), Inches(3.32), fill=WHITE, line=LINE, radius=0.06)
    add_box(s, Inches(4.45), Inches(3.60), Inches(0.07), Inches(3.32), fill=ACCENT)
    add_text(s, Inches(4.72), Inches(3.72), Inches(3.75), Inches(0.28), [("代表性成果", 13, ACCENT, True)])
    add_text(
        s,
        Inches(4.72),
        Inches(4.06),
        Inches(3.75),
        Inches(2.70),
        [
            ("专著《随机退化过程与统计建模》", 13, DEEP, True, 2),
            ("科学出版社，2025；入选统计与数据科学丛书", 12, MUTED, False, 10),
            ("论文见于 NRL、SJS、JQT、EJOR、", 13, INK, False, 2),
            ("IEEE TR、IISE Transactions", 13, INK, False, 10),
            ("主持国自然青年 1 项、面上 3 项", 13, INK, False, 2),
            ("在研面上项目 72571246", 12, MUTED, False, 10),
            ("浙江省自然科学基金重点项目等十余项", 13, INK, False),
        ],
    )

    add_box(s, Inches(8.85), Inches(3.60), Inches(4.00), Inches(3.32), fill=WHITE, line=LINE, radius=0.06)
    add_box(s, Inches(8.85), Inches(3.60), Inches(0.07), Inches(3.32), fill=PRIMARY)
    add_text(s, Inches(9.12), Inches(3.72), Inches(3.55), Inches(0.28), [("奖励与学术服务", 13, ACCENT, True)])
    add_text(
        s,
        Inches(9.12),
        Inches(4.06),
        Inches(3.55),
        Inches(2.70),
        [
            ("浙江省自然科学奖", 13, DEEP, True, 2),
            ("福建省自然科学奖、全国统计科技进步奖", 12, MUTED, False, 10),
            ("省高校院士专家结对培养青年英才", 13, INK, False, 2),
            ("省特支计划教育青年人才", 12, MUTED, False, 10),
            ("中国运筹学会可靠性分会副理事长", 13, INK, False, 10),
            ("Statistical Theory and Related Fields", 13, INK, False, 2),
            ("Associate Editor", 12, MUTED, False),
        ],
    )
    add_notes(
        s,
        "开场 1 分钟。先报姓名、单位、职称，再报四个研究方向。"
        "业绩只点三句：六十余篇一作通讯、一本专著、国自然青年加三项面上。"
        "奖项和服务各报一项：省自然科学奖、可靠性分会副理事长。下一页再讲为什么做这件事。",
    )

    # ------------------------------------------------------------------
    # 2  研究背景与定位
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "01   背景与定位", "先看研究背景，再落到我们的定位")
    footer(s, 2)

    add_box(s, Inches(0.50), Inches(1.24), Inches(0.46), Inches(0.28), fill=DEEP, radius=0.4)
    add_text(s, Inches(0.50), Inches(1.24), Inches(0.46), Inches(0.28), [("01", 11, WHITE, True)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(1.08), Inches(1.24), Inches(3.0), Inches(0.28), [("研究背景", 14, DEEP, True)], anchor=MSO_ANCHOR.MIDDLE)
    add_box(s, Inches(0.50), Inches(1.62), Inches(12.30), Inches(1.48), fill=WHITE, line=LINE, radius=0.05)
    add_box(s, Inches(0.50), Inches(1.62), Inches(0.07), Inches(1.48), fill=ACCENT)
    add_text(
        s,
        Inches(0.78),
        Inches(1.74),
        Inches(11.80),
        Inches(1.26),
        [
            ("电子器件、机电系统和航空装备的可靠度持续提高。传统寿命试验在有限工期内往往只能拿到大量删失，很难观测到足够失效。", 14, INK, False, 5),
            ("产品在试验或服役中会留下连续的性能轨迹：电流漂移、裂纹扩展、光强衰减、制动转矩下降。", 14, INK, False, 5),
            ("退化轨迹比失效时间携带更多过程信息，正在成为高可靠产品评估与预测的主要数据来源。", 14, INK, False),
        ],
    )

    add_box(s, Inches(0.50), Inches(3.26), Inches(0.46), Inches(0.28), fill=DEEP, radius=0.4)
    add_text(s, Inches(0.50), Inches(3.26), Inches(0.46), Inches(0.28), [("02", 11, WHITE, True)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(1.08), Inches(3.26), Inches(5.0), Inches(0.28), [("由此形成的统计困难", 14, DEEP, True)], anchor=MSO_ANCHOR.MIDDLE)

    constraints = [
        ("小样本", "失效稀少，先验一旦定偏，后验会被先验主导"),
        ("多维相依", "多个性能指标联合退化，尾部与波动往往相关"),
        ("个体异质", "随机效应、亚总体、两阶段与双尺度"),
        ("在线流式", "监测陆续到达，不能每次全样本重跑 MCMC"),
    ]
    for i, (t, d) in enumerate(constraints):
        x = Inches(0.50) + i * Inches(3.18)
        add_box(s, x, Inches(3.66), Inches(3.05), Inches(1.22), fill=WHITE, line=LINE, radius=0.06)
        add_box(s, x, Inches(3.66), Inches(3.05), Inches(0.05), fill=ACCENT)
        add_text(s, x + Inches(0.16), Inches(3.76), Inches(2.75), Inches(0.30), [(t, 15, DEEP, True)])
        add_text(s, x + Inches(0.16), Inches(4.08), Inches(2.75), Inches(0.68), [(d, 12, MUTED, False)])

    add_box(s, Inches(0.50), Inches(5.04), Inches(0.46), Inches(0.28), fill=DEEP, radius=0.4)
    add_text(s, Inches(0.50), Inches(5.04), Inches(0.46), Inches(0.28), [("03", 11, WHITE, True)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(1.08), Inches(5.04), Inches(4.0), Inches(0.28), [("因此，研究定位", 14, DEEP, True)], anchor=MSO_ANCHOR.MIDDLE)

    band = add_box(s, Inches(0.50), Inches(5.42), Inches(12.30), Inches(1.62), fill=DEEP, radius=0.04)
    set_linear_gradient(band, "0A1F3D", "1E4E7A", angle=0)
    add_text(
        s,
        Inches(0.72),
        Inches(5.52),
        Inches(11.90),
        Inches(0.62),
        [
            ("用随机过程与贝叶斯方法，从退化监测数据和寿命数据中", 15, WHITE, False, 2),
            ("评估高可靠产品的可靠性，并给出可递归更新的剩余寿命预测。", 15, WHITE, False),
        ],
    )
    chips = [
        ("退化建模", "Wiener / IG / Gamma"),
        ("在线贝叶斯", "共轭与递归更新"),
        ("客观贝叶斯", "小样本寿命评估"),
        ("试验与现场", "加速试验与数据融合"),
    ]
    for i, (t, d) in enumerate(chips):
        x = Inches(0.72) + i * Inches(3.05)
        add_text(s, x, Inches(6.22), Inches(2.90), Inches(0.26), [(t, 12, ACCENT, True)])
        add_text(s, x, Inches(6.46), Inches(2.90), Inches(0.26), [(d, 12, PALE, False)])

    add_notes(
        s,
        "这页按三步讲，不要倒过来先报定位。"
        "第一步研究背景：高可靠导致寿命试验失效太少，退化轨迹成为主要信息。"
        "第二步四个困难各举半句现场例子：永磁制动器是小样本，重型机床是多指标，激光器常有个体差异，航空发动机是流式监测。"
        "第三步才读出定位那两句，并点名四条主线。",
    )

    # ------------------------------------------------------------------
    # 3  过程建模
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "02   过程", "随机退化过程：让模型贴合轨迹，且便于推断")
    footer(s, 3)

    add_text(
        s,
        Inches(0.55),
        Inches(1.20),
        Inches(12.20),
        Inches(0.48),
        [
            ("Wiener、逆高斯、Gamma 对应不同机理。我们做的不是再造过程族，而是在可识别、可计算的前提下扩展相依、变点、尺度与尾部。", 14, MUTED, False),
        ],
    )

    models = [
        ("多元相依", "二元 / 层次贝叶斯 Wiener；退化速率与波动可以相关", "IEEE TR  2018 · 2026"),
        ("厚尾相依", "多元 Student-t 过程，刻画尾部加权与指标联合退化", "IISE Trans.  2025"),
        ("两阶段寿命", "重参数化逆高斯加变点，给出两阶段剩余寿命", "EJOR  2024"),
        ("双尺度异质", "统一随机效应逆高斯，兼容两套时间尺度", "IISE Trans.  Featured"),
    ]
    for i, (t, d, cite) in enumerate(models):
        col, row = i % 2, i // 2
        x = Inches(0.50) + col * Inches(6.40)
        y = Inches(1.80) + row * Inches(1.72)
        add_box(s, x, y, Inches(6.20), Inches(1.58), fill=WHITE, line=LINE, radius=0.05)
        add_box(s, x, y, Inches(0.07), Inches(1.58), fill=ACCENT if row == 0 else PRIMARY)
        add_text(s, x + Inches(0.28), y + Inches(0.16), Inches(5.70), Inches(0.32), [(t, 16, DEEP, True)])
        add_text(s, x + Inches(0.28), y + Inches(0.52), Inches(5.70), Inches(0.50), [(d, 13, INK, False)])
        add_text(s, x + Inches(0.28), y + Inches(1.10), Inches(5.70), Inches(0.28), [(cite, 11, ACCENT, False)])

    band = add_box(s, Inches(0.50), Inches(5.36), Inches(12.30), Inches(1.66), fill=DEEP, radius=0.04)
    set_linear_gradient(band, "0A1F3D", "1E4E7A", angle=0)
    add_text(s, Inches(0.74), Inches(5.50), Inches(11.85), Inches(0.24), [("系统整理", 11, ACCENT, True)])
    add_text(
        s,
        Inches(0.74),
        Inches(5.78),
        Inches(11.85),
        Inches(1.00),
        [
            ("专著《随机退化过程与统计建模》（徐安察、汤银才、庄亮亮，科学出版社，2025）", 14, WHITE, False, 4),
            ("在研：面向多维偏态厚尾退化数据的可靠性评估与贝叶斯最优设计  ·  国自然面上 72571246", 13, PALE, False),
        ],
    )
    add_notes(
        s,
        "机理仍用 Wiener / IG / Gamma，扩展集中在相依、变点、双尺度和尾部。"
        "点两篇即可：Student-t（IISE）与两阶段 rIG（EJOR）。专著一句收口。",
    )

    # ------------------------------------------------------------------
    # 4  在线推断
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "03   推断", "贝叶斯在线学习：递归更新，而不是每次重估")
    footer(s, 4)

    add_text(
        s,
        Inches(0.55),
        Inches(1.20),
        Inches(12.20),
        Inches(0.40),
        [("监测数据流式到达。我们利用共轭或可解析的更新，把后验写成递推，使剩余寿命预测可在线进行。", 14, MUTED, False)],
    )

    steps = [
        ("01", "共轭结构", "Gamma / 逆高斯在合适参数化下存在共轭或近似共轭先验"),
        ("02", "递归更新", "新观测进入后，后验超参数闭式或近闭式刷新"),
        ("03", "RUL 预测", "由当前后验直接给出剩余寿命分布，不必重跑全样本"),
        ("04", "稳健识别", "异常点下的隐状态识别，避免一次离群拉偏轨迹"),
    ]
    for i, (num, t, d) in enumerate(steps):
        x = Inches(0.50) + i * Inches(3.18)
        dark = i in (1, 2)
        add_box(s, x, Inches(1.72), Inches(3.05), Inches(1.78), fill=DEEP if dark else WHITE, line=None if dark else LINE, radius=0.06)
        add_text(s, x + Inches(0.16), Inches(1.84), Inches(2.75), Inches(0.24), [(num, 11, ACCENT, True)])
        add_text(s, x + Inches(0.16), Inches(2.12), Inches(2.75), Inches(0.34), [(t, 16, WHITE if dark else DEEP, True)])
        add_text(s, x + Inches(0.16), Inches(2.50), Inches(2.75), Inches(0.82), [(d, 12, PALE if dark else MUTED, False)])

    papers = [
        ("递归贝叶斯 RUL", "Gamma 过程加共轭先验，剩余寿命可递推", "Scand. J. Statist.  2026"),
        ("逆高斯在线估计", "高效在线估计与 RUL，避免全样本重估", "Naval Res. Logist.  2025"),
        ("预后驱动维修", "贝叶斯深度学习把 RUL 接到预测性维修", "RESS  2023  ·  ESI 热点"),
        ("联邦学习 RUL", "数据不出域的航空发动机剩余寿命预测", "Appl. Soft Comput.  2025  ·  ESI 高被引"),
    ]
    for i, (t, d, cite) in enumerate(papers):
        col, row = i % 2, i // 2
        x = Inches(0.50) + col * Inches(6.40)
        y = Inches(3.70) + row * Inches(1.58)
        add_box(s, x, y, Inches(6.20), Inches(1.44), fill=WHITE, line=LINE, radius=0.05)
        add_text(s, x + Inches(0.22), y + Inches(0.14), Inches(5.80), Inches(0.30), [(t, 15, DEEP, True)])
        add_text(s, x + Inches(0.22), y + Inches(0.48), Inches(5.80), Inches(0.40), [(d, 13, INK, False)])
        add_text(s, x + Inches(0.22), y + Inches(0.96), Inches(5.80), Inches(0.28), [(cite, 11, ACCENT, False)])

    add_notes(
        s,
        "关键句：我们要的是可递归的后验，不是更快的 MCMC。"
        "中间四格从左到右讲。统计同行点 SJS 与 NRL；工业同行可多讲航空发动机。",
    )

    # ------------------------------------------------------------------
    # 5  评估与讨论
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    set_bg(s)
    header(s, "04   评估与展望", "小样本评估，以及希望和专家讨论的问题")
    footer(s, 5)

    cols = [
        (
            ACCENT,
            "客观贝叶斯与小样本",
            [
                "参考先验、无信息先验与后验正常性",
                "屏蔽数据、竞争失效、加速寿命与加速退化",
                "Birnbaum–Saunders、Weibull 等寿命模型",
                "代表工作见于 IEEE TR、CSDA、JSPI",
            ],
        ),
        (
            PRIMARY,
            "接到真实系统上",
            [
                "永磁制动器小样本贝叶斯评估（IEEE TR）",
                "华为：Weibull 核心算法、隐患预警",
                "动态环境下的系统可靠性与竞争失效",
                "加速试验与现场数据联合建模（STARF）",
            ],
        ),
        (
            DEEP,
            "希望讨论的开放问题",
            [
                "多维偏态厚尾退化的可识别参数化",
                "在线更新下的校准：覆盖率能否守住",
                "试验信息外推到现场时，偏差如何分解",
                "贝叶斯最优设计如何同时服务评估与预测",
            ],
        ),
    ]
    for i, (bar, title, bullets) in enumerate(cols):
        x = Inches(0.50) + i * Inches(4.20)
        add_box(s, x, Inches(1.24), Inches(4.02), Inches(4.00), fill=WHITE, line=LINE, radius=0.05)
        add_box(s, x, Inches(1.24), Inches(4.02), Inches(0.06), fill=bar)
        add_text(s, x + Inches(0.20), Inches(1.46), Inches(3.62), Inches(0.50), [(title, 15, DEEP, True)])
        lines = [(f"·  {b}", 13, INK, False, 8) for b in bullets]
        add_text(s, x + Inches(0.20), Inches(2.06), Inches(3.62), Inches(2.95), lines)

    band = add_box(s, Inches(0.50), Inches(5.42), Inches(12.30), Inches(1.62), fill=DEEP, radius=0.04)
    set_linear_gradient(band, "0A1F3D", "1E4E7A", angle=0)
    add_text(
        s,
        Inches(0.74),
        Inches(5.60),
        Inches(8.4),
        Inches(1.20),
        [
            ("后面的工作会沿着偏态厚尾建模、在线校准和试验—现场融合继续做。", 14, WHITE, False, 6),
            ("欢迎批评，也欢迎在具体数据或问题上合作。", 13, PALE, False),
        ],
    )
    add_text(
        s,
        Inches(9.30),
        Inches(5.66),
        Inches(3.25),
        Inches(1.15),
        [
            ("欢迎批评与合作", 13, ACCENT, True, 6),
            ("xuancha@mail.zjgsu.edu.cn", 12, WHITE, False, 3),
            ("www.xu-ancha.com", 12, WHITE, False),
        ],
    )
    add_notes(
        s,
        "这页留给讨论。前两列各举一例。开放问题按听者选一两个。"
        "业绩已在第 1 页说过，这里不要再报数字。最后停在欢迎批评。",
    )

    out = "/workspace/files/slides/research-intro-experts.pptx"
    prs.save(out)
    print(out)


if __name__ == "__main__":
    build()

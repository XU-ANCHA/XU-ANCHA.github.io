#!/usr/bin/env python3
"""Build a 5-slide expert briefing deck for Ancha Xu's research intro."""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

# Widescreen 16:9
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

NAVY = RGBColor(0x1B, 0x36, 0x5D)
NAVY_SOFT = RGBColor(0x2F, 0x4F, 0x73)
INK = RGBColor(0x1C, 0x1C, 0x1C)
MUTED = RGBColor(0x5A, 0x64, 0x6E)
RULE = RGBColor(0xD0, 0xD5, 0xDC)
WASH = RGBColor(0xF2, 0xF4, 0xF7)
CARD = RGBColor(0xE7, 0xED, 0xF3)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT = RGBColor(0xA8, 0x45, 0x2B)
CN = "微软雅黑"
EN = "Calibri"


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
        from lxml import etree

        ea = etree.SubElement(rpr, qn("a:ea"))
    ea.set("typeface", CN)


def add_box(slide, left, top, width, height, fill=None, line=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.shadow.inherit = False
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


def add_text(slide, left, top, width, height, lines, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    """lines: list of (text, size, color, bold)."""
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.margin_left = Inches(0.06)
    tf.margin_right = Inches(0.06)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    try:
        tf._txBody.bodyPr.set("anchor", {MSO_ANCHOR.TOP: "t", MSO_ANCHOR.MIDDLE: "ctr", MSO_ANCHOR.BOTTOM: "b"}[anchor])
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
        p.line_spacing = 1.15
    return box


def add_notes(slide, text):
    notes = slide.notes_slide.notes_text_frame
    notes.text = text


def footer(slide, page, total=5):
    add_box(slide, Inches(0), Inches(7.28), SLIDE_W, Inches(0.22), fill=NAVY)
    add_text(
        slide,
        Inches(0.4),
        Inches(7.28),
        Inches(10),
        Inches(0.22),
        [("徐安察  ·  随机退化过程与贝叶斯可靠性推断", 10, WHITE, False)],
        anchor=MSO_ANCHOR.MIDDLE,
    )
    add_text(
        slide,
        Inches(11.6),
        Inches(7.28),
        Inches(1.4),
        Inches(0.22),
        [(f"{page}  /  {total}", 10, WHITE, False)],
        align=PP_ALIGN.RIGHT,
        anchor=MSO_ANCHOR.MIDDLE,
    )


def header(slide, kicker, title):
    add_box(slide, Inches(0), Inches(0), SLIDE_W, Inches(0.08), fill=NAVY)
    add_text(slide, Inches(0.5), Inches(0.22), Inches(12.3), Inches(0.28), [(kicker, 12, ACCENT, True)])
    add_text(slide, Inches(0.5), Inches(0.48), Inches(12.3), Inches(0.46), [(title, 26, NAVY, True)])
    add_box(slide, Inches(0.5), Inches(1.00), Inches(1.2), Inches(0.045), fill=ACCENT)


def card(slide, left, top, width, height, title, bullets, tag=None):
    add_box(slide, left, top, width, height, fill=WASH, line=RULE)
    add_box(slide, left, top, Inches(0.07), height, fill=NAVY)
    y = top + Inches(0.12)
    if tag:
        add_text(slide, left + Inches(0.18), y, width - Inches(0.28), Inches(0.22), [(tag, 11, ACCENT, True)])
        y += Inches(0.22)
    add_text(slide, left + Inches(0.18), y, width - Inches(0.28), Inches(0.32), [(title, 15, NAVY, True)])
    y += Inches(0.34)
    lines = []
    for b in bullets:
        lines.append((b, 13, INK, False, 6))
    add_text(slide, left + Inches(0.18), y, width - Inches(0.28), height - (y - top) - Inches(0.1), lines)


def add_picture_cover(slide, path, left, top, width, height):
    """Crop a photo to the box aspect ratio, then place it."""
    from PIL import Image

    im = Image.open(path).convert("RGB")
    iw, ih = im.size
    box_ratio = height / width
    img_ratio = ih / iw
    if img_ratio > box_ratio:
        new_h = int(iw * box_ratio)
        top_cut = max((ih - new_h) // 5, 0)  # bias toward the face
        im = im.crop((0, top_cut, iw, top_cut + new_h))
    else:
        new_w = int(ih / box_ratio)
        left_cut = (iw - new_w) // 2
        im = im.crop((left_cut, 0, left_cut + new_w, ih))
    tmp = "/tmp/research-intro-portrait.jpg"
    im.save(tmp, quality=90)
    return slide.shapes.add_picture(tmp, left, top, width=width, height=height)


def build():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # ------------------------------------------------------------------
    # Slide 1  个人研究与业绩
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    add_box(s, Inches(0), Inches(0), Inches(3.55), SLIDE_H, fill=NAVY)
    add_picture_cover(
        s,
        "/workspace/images/yixing.jpg",
        Inches(0.45),
        Inches(0.40),
        Inches(2.65),
        Inches(3.35),
    )
    add_text(s, Inches(0.35), Inches(3.90), Inches(2.85), Inches(0.50), [("徐安察", 26, WHITE, True)], align=PP_ALIGN.CENTER)
    add_text(
        s,
        Inches(0.28),
        Inches(4.42),
        Inches(3.00),
        Inches(1.35),
        [
            ("教授、博士生导师", 14, RGBColor(0xF0, 0xC4, 0xB0), True, 6),
            ("浙江工商大学", 13, RGBColor(0xD7, 0xDE, 0xE7), False, 2),
            ("统计与数据科学学院", 13, RGBColor(0xD7, 0xDE, 0xE7), False, 10),
            ("xuancha@mail.zjgsu.edu.cn", 11, RGBColor(0xB8, 0xC3, 0xD0), False, 2),
            ("www.xu-ancha.com", 11, RGBColor(0xB8, 0xC3, 0xD0), False),
        ],
        align=PP_ALIGN.CENTER,
    )

    add_text(s, Inches(3.85), Inches(0.28), Inches(9.0), Inches(0.26), [("研究工作简介  ·  同行专家交流", 12, ACCENT, True)])
    add_text(s, Inches(3.85), Inches(0.54), Inches(9.0), Inches(0.48), [("个人研究与业绩", 28, NAVY, True)])
    add_box(s, Inches(3.85), Inches(1.06), Inches(1.15), Inches(0.04), fill=ACCENT)

    add_text(s, Inches(3.85), Inches(1.22), Inches(9.0), Inches(0.24), [("研究方向", 12, ACCENT, True)])
    add_text(
        s,
        Inches(3.85),
        Inches(1.46),
        Inches(9.0),
        Inches(0.70),
        [
            ("退化数据分析与建模  ·  贝叶斯在线学习", 16, INK, False, 2),
            ("客观贝叶斯方法  ·  寿命数据分析", 16, INK, False),
        ],
    )

    stats = [
        ("60+", "一作 / 通讯 SCI"),
        ("2,478", "Google Scholar 引用"),
        ("29", "h 指数"),
        ("6", "ESI 高被引论文"),
    ]
    for i, (val, lab) in enumerate(stats):
        x = Inches(3.85) + i * Inches(2.28)
        add_box(s, x, Inches(2.28), Inches(2.16), Inches(1.05), fill=WASH, line=RULE)
        add_text(s, x, Inches(2.34), Inches(2.16), Inches(0.48), [(val, 22, NAVY, True)], align=PP_ALIGN.CENTER)
        add_text(s, x, Inches(2.82), Inches(2.16), Inches(0.40), [(lab, 11, MUTED, False)], align=PP_ALIGN.CENTER)

    add_box(s, Inches(3.85), Inches(3.50), Inches(4.40), Inches(3.50), fill=WASH, line=RULE)
    add_text(s, Inches(4.05), Inches(3.62), Inches(4.05), Inches(0.28), [("代表性成果", 14, ACCENT, True)])
    add_text(
        s,
        Inches(4.05),
        Inches(3.96),
        Inches(4.05),
        Inches(2.90),
        [
            ("专著《随机退化过程与统计建模》", 13, NAVY, True, 2),
            ("科学出版社，2025；入选统计与数据科学丛书", 12, MUTED, False, 8),
            ("论文见于 NRL、SJS、JQT、EJOR、", 13, INK, False, 2),
            ("IEEE TR、IISE Transactions 等", 13, INK, False, 8),
            ("主持国自然青年 1 项、面上 3 项", 13, INK, False, 2),
            ("在研面上项目 72571246", 12, MUTED, False, 8),
            ("浙江省自然科学基金重点项目等十余项", 13, INK, False),
        ],
    )

    add_box(s, Inches(8.45), Inches(3.50), Inches(4.40), Inches(3.50), fill=WASH, line=RULE)
    add_text(s, Inches(8.65), Inches(3.62), Inches(4.05), Inches(0.28), [("奖励与学术服务", 14, ACCENT, True)])
    add_text(
        s,
        Inches(8.65),
        Inches(3.96),
        Inches(4.05),
        Inches(2.90),
        [
            ("浙江省自然科学奖", 13, NAVY, True, 2),
            ("福建省自然科学奖、全国统计科技进步奖", 12, MUTED, False, 8),
            ("省高校院士专家结对培养青年英才", 13, INK, False, 2),
            ("省特支计划教育青年人才", 12, MUTED, False, 8),
            ("中国运筹学会可靠性分会副理事长", 13, INK, False, 8),
            ("Statistical Theory and Related Fields", 13, INK, False, 2),
            ("Associate Editor", 12, MUTED, False),
        ],
    )
    add_notes(
        s,
        "开场 1 分钟。先报姓名、单位、职称，再报四个研究方向。"
        "业绩只点三句：六十余篇一作通讯、一本专著、国自然青年加三项面上。"
        "奖项和服务各报一项即可：省自然科学奖、可靠性分会副理事长。不要把格子念完。下一页再讲为什么做这件事。",
    )

    # ------------------------------------------------------------------
    # Slide 2  研究背景与定位
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    header(s, "01  /  背景与定位", "先看研究背景，再落到我们的定位")
    footer(s, 2)

    add_text(s, Inches(0.5), Inches(1.18), Inches(12.3), Inches(0.26), [("研究背景", 13, ACCENT, True)])
    add_box(s, Inches(0.5), Inches(1.48), Inches(12.3), Inches(1.55), fill=WASH, line=RULE)
    add_text(
        s,
        Inches(0.70),
        Inches(1.60),
        Inches(11.95),
        Inches(1.32),
        [
            ("电子器件、机电系统和航空装备的可靠度持续提高。传统寿命试验在有限工期内往往只能拿到大量删失，很难观测到足够失效。", 15, INK, False, 6),
            ("与此同时，产品在试验或服役中会留下连续的性能轨迹：电流漂移、裂纹扩展、光强衰减、制动转矩下降。", 15, INK, False, 6),
            ("退化轨迹比失效时间携带更多过程信息，正在成为高可靠产品评估与预测的主要数据来源。", 15, INK, False),
        ],
    )

    add_text(s, Inches(0.5), Inches(3.16), Inches(12.3), Inches(0.26), [("由此形成的统计困难", 13, ACCENT, True)])
    constraints = [
        ("小样本", "失效稀少，先验一旦定偏，后验会被先验主导"),
        ("多维相依", "多个性能指标联合退化，尾部与波动往往相关"),
        ("个体异质", "随机效应、亚总体、两阶段与双尺度"),
        ("在线流式", "监测陆续到达，不能每次全样本重跑 MCMC"),
    ]
    for i, (t, d) in enumerate(constraints):
        x = Inches(0.5) + i * Inches(3.2)
        add_box(s, x, Inches(3.46), Inches(3.05), Inches(1.28), fill=WHITE, line=RULE)
        add_box(s, x, Inches(3.46), Inches(0.08), Inches(1.28), fill=NAVY)
        add_text(s, x + Inches(0.20), Inches(3.56), Inches(2.72), Inches(0.30), [(t, 15, NAVY, True)])
        add_text(s, x + Inches(0.20), Inches(3.88), Inches(2.72), Inches(0.72), [(d, 12, MUTED, False)])

    add_text(s, Inches(0.5), Inches(4.88), Inches(12.3), Inches(0.26), [("因此，研究定位", 13, ACCENT, True)])
    add_box(s, Inches(0.5), Inches(5.16), Inches(12.3), Inches(1.88), fill=NAVY)
    add_text(
        s,
        Inches(0.72),
        Inches(5.28),
        Inches(11.9),
        Inches(0.70),
        [
            ("用随机过程与贝叶斯方法，从退化监测数据和寿命数据中", 16, WHITE, False, 3),
            ("评估高可靠产品的可靠性，并给出可递归更新的剩余寿命预测。", 16, WHITE, False),
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
        add_text(s, x, Inches(6.08), Inches(2.90), Inches(0.28), [(t, 13, RGBColor(0xF0, 0xC4, 0xB0), True)])
        add_text(s, x, Inches(6.36), Inches(2.90), Inches(0.28), [(d, 12, RGBColor(0xD7, 0xDE, 0xE7), False)])

    add_notes(
        s,
        "这页按三步讲，不要倒过来先报定位。"
        "第一步研究背景：高可靠导致寿命试验失效太少，退化轨迹成为主要信息。"
        "第二步四个困难各举半句现场例子：永磁制动器是小样本，重型机床是多指标，激光器常有个体差异，航空发动机是流式监测。"
        "第三步才读出定位那两句，并点名四条主线。后面三页分别展开过程、推断、评估。",
    )

    # ------------------------------------------------------------------
    # Slide 3  过程建模
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    header(s, "02  /  过程", "随机退化过程：让模型贴合轨迹，且便于推断")
    footer(s, 3)

    add_text(
        s,
        Inches(0.5),
        Inches(1.20),
        Inches(12.3),
        Inches(0.55),
        [
            ("Wiener、逆高斯、Gamma 对应不同机理。我们做的不是再造过程族，而是在可识别、可计算的前提下扩展相依、变点、尺度与尾部。", 15, INK, False),
        ],
    )

    models = [
        ("多元相依", "二元 / 层次贝叶斯 Wiener；退化速率与波动可以相关", "IEEE TR 2018, 2026"),
        ("厚尾相依", "多元 Student-t 过程，刻画尾部加权、指标联合退化", "IISE Trans. 2025"),
        ("两阶段寿命", "重参数化逆高斯 + 变点，给出两阶段 RUL", "EJOR 2024"),
        ("双尺度异质", "统一随机效应逆高斯，兼容两套时间尺度", "IISE Trans. 2026+  Featured"),
    ]
    for i, (t, d, cite) in enumerate(models):
        col = i % 2
        row = i // 2
        x = Inches(0.5) + col * Inches(6.4)
        y = Inches(1.90) + row * Inches(1.85)
        add_box(s, x, y, Inches(6.2), Inches(1.70), fill=WASH, line=RULE)
        add_box(s, x, y, Inches(0.08), Inches(1.70), fill=NAVY)
        add_text(s, x + Inches(0.28), y + Inches(0.16), Inches(5.7), Inches(0.34), [(t, 17, NAVY, True)])
        add_text(s, x + Inches(0.28), y + Inches(0.56), Inches(5.7), Inches(0.60), [(d, 14, INK, False)])
        add_text(s, x + Inches(0.28), y + Inches(1.22), Inches(5.7), Inches(0.30), [(cite, 12, MUTED, False)])

    add_box(s, Inches(0.5), Inches(5.70), Inches(12.3), Inches(1.30), fill=NAVY)
    add_text(s, Inches(0.72), Inches(5.84), Inches(11.9), Inches(0.28), [("系统整理", 12, ACCENT, True)])
    add_text(
        s,
        Inches(0.72),
        Inches(6.14),
        Inches(11.9),
        Inches(0.68),
        [
            ("专著《随机退化过程与统计建模》（徐安察、汤银才、庄亮亮，科学出版社，2025；入选统计与数据科学丛书）", 15, WHITE, False, 3),
            ("在研：面向多维偏态厚尾退化数据的可靠性评估与贝叶斯最优设计  ·  国家自然科学基金面上项目 72571246", 14, RGBColor(0xD7, 0xDE, 0xE7), False),
        ],
    )
    add_notes(
        s,
        "专家若问“和经典过程有何不同”，答：机理仍用 Wiener / IG / Gamma，扩展集中在相依结构、变点、双尺度和尾部，并且重参数化是为了推断稳定。"
        "点两篇即可：Student-t（IISE）说明厚尾多指标，两阶段 rIG（EJOR）说明变点 RUL。"
        "专著放最后一句，作为这条线的收口，不要展开目录。",
    )

    # ------------------------------------------------------------------
    # Slide 4  在线推断
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    header(s, "03  /  推断", "贝叶斯在线学习：递归更新，而不是每次重估")
    footer(s, 4)

    add_text(
        s,
        Inches(0.5),
        Inches(1.20),
        Inches(12.3),
        Inches(0.50),
        [
            ("监测数据流式到达。我们利用共轭或可解析的更新，把后验写成递推，使剩余寿命预测可在线进行。", 15, INK, False),
        ],
    )

    steps = [
        ("共轭结构", "Gamma / 逆高斯在合适参数化下存在共轭或近似共轭先验"),
        ("递归更新", "新观测进入后，后验超参数闭式或近闭式刷新"),
        ("RUL 预测", "由当前后验直接给出剩余寿命分布，不必重跑全样本"),
        ("稳健 / 隐状态", "异常点下的状态识别，避免一次离群拉偏整条轨迹"),
    ]
    for i, (t, d) in enumerate(steps):
        x = Inches(0.5) + i * Inches(3.2)
        add_box(s, x, Inches(1.85), Inches(3.05), Inches(1.70), fill=NAVY if i in (1, 2) else WASH)
        title_c = WHITE if i in (1, 2) else NAVY
        body_c = RGBColor(0xD7, 0xDE, 0xE7) if i in (1, 2) else INK
        tag_c = ACCENT if i not in (1, 2) else RGBColor(0xF0, 0xC4, 0xB0)
        add_text(s, x + Inches(0.16), Inches(1.98), Inches(2.75), Inches(0.24), [(f"0{i+1}", 12, tag_c, True)])
        add_text(s, x + Inches(0.16), Inches(2.26), Inches(2.75), Inches(0.36), [(t, 16, title_c, True)])
        add_text(s, x + Inches(0.16), Inches(2.68), Inches(2.75), Inches(0.70), [(d, 13, body_c, False)])

    papers = [
        ("递归贝叶斯 RUL", "Gamma 过程 + 共轭先验，剩余寿命可递推", "Scand. J. Statist. 2026"),
        ("逆高斯在线估计", "高效在线估计与 RUL，避免全样本重估", "Naval Res. Logist. 2025"),
        ("预后驱动维修", "贝叶斯深度学习把 RUL 接到预测性维修", "RESS 2023  ·  ESI 热点"),
        ("联邦学习 RUL", "数据不出域的航空发动机剩余寿命预测", "Appl. Soft Comput. 2025  ·  ESI 高被引"),
    ]
    for i, (t, d, cite) in enumerate(papers):
        col = i % 2
        row = i // 2
        x = Inches(0.5) + col * Inches(6.4)
        y = Inches(3.80) + row * Inches(1.50)
        add_box(s, x, y, Inches(6.2), Inches(1.36), fill=WASH, line=RULE)
        add_text(s, x + Inches(0.22), y + Inches(0.12), Inches(5.8), Inches(0.30), [(t, 15, NAVY, True)])
        add_text(s, x + Inches(0.22), y + Inches(0.46), Inches(5.8), Inches(0.40), [(d, 13, INK, False)])
        add_text(s, x + Inches(0.22), y + Inches(0.92), Inches(5.8), Inches(0.28), [(cite, 12, MUTED, False)])

    add_notes(
        s,
        "这页的关键句：我们要的是可递归的后验，不是更快的 MCMC。"
        "中间四个格子从左到右讲一遍。代表工作点 SJS 的 Gamma 共轭和 NRL 的 IG 在线估计。"
        "RESS 和联邦学习是应用出口，专家若偏统计可少讲，若偏工业可多讲航空发动机。",
    )

    # ------------------------------------------------------------------
    # Slide 5  小样本、应用、开放问题
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    header(s, "04  /  评估与展望", "小样本评估，以及希望和专家讨论的问题")
    footer(s, 5)

    # three columns
    cols = [
        (
            "客观贝叶斯与小样本",
            [
                "参考先验、无信息先验与后验正常性",
                "屏蔽数据、竞争失效、加速寿命 / 加速退化",
                "Birnbaum–Saunders、Weibull 等寿命模型",
                "代表：IEEE TR、CSDA、JSPI；浙江省自然科学奖",
            ],
        ),
        (
            "接到真实系统上",
            [
                "永磁制动器小样本贝叶斯评估（IEEE TR）",
                "华为：Weibull 核心算法、隐患预警、小子样分析",
                "动态环境下的系统可靠性与竞争失效",
                "加速试验与现场数据联合建模（STARF）",
            ],
        ),
        (
            "希望讨论的开放问题",
            [
                "多维偏态厚尾退化的可识别参数化",
                "在线更新下的校准：覆盖率能否守住",
                "试验信息外推到现场时，偏差如何分解",
                "贝叶斯最优设计如何同时服务评估与预测",
            ],
        ),
    ]
    for i, (title, bullets) in enumerate(cols):
        x = Inches(0.5) + i * Inches(4.25)
        add_box(s, x, Inches(1.25), Inches(4.08), Inches(4.35), fill=WASH, line=RULE)
        add_box(s, x, Inches(1.25), Inches(4.08), Inches(0.08), fill=NAVY if i < 2 else ACCENT)
        add_text(s, x + Inches(0.18), Inches(1.48), Inches(3.72), Inches(0.55), [(title, 16, NAVY, True)])
        lines = [(f"·  {b}", 13, INK, False, 8) for b in bullets]
        add_text(s, x + Inches(0.18), Inches(2.15), Inches(3.72), Inches(3.20), lines)

    add_box(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(1.25), fill=NAVY)
    add_text(
        s,
        Inches(0.72),
        Inches(5.90),
        Inches(8.6),
        Inches(0.95),
        [
            ("后面的工作会沿着偏态厚尾建模、在线校准和试验—现场融合继续做。", 15, WHITE, False, 4),
            ("欢迎批评，也欢迎在具体数据或问题上合作。", 14, RGBColor(0xD7, 0xDE, 0xE7), False),
        ],
    )
    add_text(
        s,
        Inches(9.4),
        Inches(5.95),
        Inches(3.2),
        Inches(0.90),
        [
            ("欢迎批评与合作", 14, RGBColor(0xF0, 0xC4, 0xB0), True, 4),
            ("xuancha@mail.zjgsu.edu.cn", 13, WHITE, False, 2),
            ("www.xu-ancha.com", 13, WHITE, False),
        ],
    )
    add_notes(
        s,
        "这页留给讨论。前两列各举一例：客观贝叶斯用屏蔽数据或加速试验；应用用永磁制动器或华为。"
        "开放问题按听者背景选一两个：理论专家谈偏态厚尾可识别性，应用专家谈现场外推的校准。"
        "业绩已在第 1 页说过，这里不要再报数字。最后停在欢迎批评。",
    )

    out = "/workspace/files/slides/research-intro-experts.pptx"
    prs.save(out)
    print(out)


if __name__ == "__main__":
    build()

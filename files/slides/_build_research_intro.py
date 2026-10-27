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


def build():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # ------------------------------------------------------------------
    # Slide 1  定位
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    add_box(s, Inches(0), Inches(0), Inches(0.18), SLIDE_H, fill=NAVY)
    add_box(s, Inches(0), Inches(0), SLIDE_W, Inches(0.08), fill=NAVY)
    add_text(s, Inches(0.7), Inches(0.45), Inches(12), Inches(0.32), [("研究工作简介  ·  同行专家交流", 14, ACCENT, True)])
    add_text(
        s,
        Inches(0.7),
        Inches(1.00),
        Inches(12),
        Inches(1.5),
        [
            ("随机退化过程与", 36, NAVY, True, 4),
            ("贝叶斯可靠性推断", 36, NAVY, True),
        ],
    )
    add_box(s, Inches(0.7), Inches(2.70), Inches(1.4), Inches(0.05), fill=ACCENT)
    add_text(
        s,
        Inches(0.7),
        Inches(2.95),
        Inches(11.8),
        Inches(0.9),
        [
            ("用随机过程与贝叶斯方法，从退化监测数据和寿命数据中", 18, INK, False, 4),
            ("评估高可靠产品的可靠性，并给出可递归更新的剩余寿命预测。", 18, INK, False),
        ],
    )

    # four chips
    chips = [
        ("01", "退化建模", "Wiener / IG / Gamma\n多元 · 两阶段 · 厚尾"),
        ("02", "在线贝叶斯", "共轭结构与递归更新\nRUL 与隐状态识别"),
        ("03", "客观贝叶斯", "参考先验与后验正常性\n小样本寿命评估"),
        ("04", "试验与现场", "加速试验最优设计\n竞争失效与数据融合"),
    ]
    w = Inches(2.85)
    gap = Inches(0.18)
    x0 = Inches(0.7)
    y0 = Inches(4.15)
    for i, (num, title, body) in enumerate(chips):
        x = x0 + i * (w + gap)
        add_box(s, x, y0, w, Inches(1.85), fill=WASH, line=RULE)
        add_text(s, x + Inches(0.16), y0 + Inches(0.12), w - Inches(0.28), Inches(0.28), [(num, 12, ACCENT, True)])
        add_text(s, x + Inches(0.16), y0 + Inches(0.40), w - Inches(0.28), Inches(0.36), [(title, 16, NAVY, True)])
        add_text(s, x + Inches(0.16), y0 + Inches(0.82), w - Inches(0.28), Inches(0.85), [(body, 13, MUTED, False)])

    add_text(
        s,
        Inches(0.7),
        Inches(6.20),
        Inches(12),
        Inches(0.7),
        [
            ("徐安察  ·  教授、博士生导师", 16, NAVY, True, 2),
            ("浙江工商大学 统计与数据科学学院    xuancha@mail.zjgsu.edu.cn    www.xu-ancha.com", 13, MUTED, False),
        ],
    )
    add_notes(
        s,
        "开场 30 秒。先报身份，再读中间那句研究定位，不要报奖项和论文篇数。"
        "四块只点名：退化建模、在线贝叶斯、客观贝叶斯、试验与现场。"
        "若专家是可靠性同行，可补一句：我们关心的不是再造一个过程，而是让过程可推断、可在线更新。",
    )

    # ------------------------------------------------------------------
    # Slide 2  问题与框架
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    header(s, "01  /  问题", "为什么做退化，而不是只看失效时间")
    footer(s, 2)

    # left problem
    add_box(s, Inches(0.5), Inches(1.25), Inches(6.05), Inches(5.75), fill=WASH, line=RULE)
    add_text(s, Inches(0.72), Inches(1.40), Inches(5.6), Inches(0.32), [("工程事实", 13, ACCENT, True)])
    add_text(
        s,
        Inches(0.72),
        Inches(1.74),
        Inches(5.6),
        Inches(1.55),
        [
            ("高可靠产品在试验期内很少失效。寿命试验给出的多为删失，", 14, INK, False, 4),
            ("信息量不足。电流漂移、裂纹扩展、光强衰减、制动转矩等", 14, INK, False, 4),
            ("退化轨迹是连续观测，比失效时间携带更多过程信息。", 14, INK, False),
        ],
    )
    add_text(s, Inches(0.72), Inches(3.40), Inches(5.6), Inches(0.30), [("统计上要同时处理的四个约束", 13, ACCENT, True)])

    constraints = [
        ("小样本", "失效稀少，先验一旦定偏，后验会被先验主导"),
        ("多维相依", "多个性能指标联合退化，尾部与波动往往相关"),
        ("个体异质", "随机效应、亚总体、两阶段 / 双尺度"),
        ("在线流式", "监测陆续到达，不能每次全样本重跑 MCMC"),
    ]
    for i, (t, d) in enumerate(constraints):
        y = Inches(3.78) + i * Inches(0.72)
        add_box(s, Inches(0.72), y, Inches(5.6), Inches(0.64), fill=WHITE, line=RULE)
        add_box(s, Inches(0.72), y, Inches(0.08), Inches(0.64), fill=NAVY)
        add_text(s, Inches(0.96), y + Inches(0.04), Inches(5.2), Inches(0.26), [(t, 14, NAVY, True)])
        add_text(s, Inches(0.96), y + Inches(0.30), Inches(5.2), Inches(0.28), [(d, 12, MUTED, False)])

    # right framework
    add_text(s, Inches(6.85), Inches(1.25), Inches(5.9), Inches(0.32), [("研究框架：一层对应一个约束", 13, ACCENT, True)])
    layers = [
        ("数据", "退化轨迹  ·  寿命 / 删失  ·  加速试验  ·  现场服役"),
        ("过程", "Wiener / 逆高斯 / Gamma，及其多元、变点、厚尾扩展"),
        ("推断", "客观先验、共轭与递归更新、近似贝叶斯"),
        ("决策", "可靠性评估  ·  RUL  ·  预测性维修  ·  试验设计"),
    ]
    for i, (t, d) in enumerate(layers):
        y = Inches(1.68) + i * Inches(1.18)
        add_box(s, Inches(6.85), y, Inches(5.95), Inches(1.02), fill=NAVY if i % 2 == 0 else NAVY_SOFT)
        add_text(s, Inches(7.08), y + Inches(0.14), Inches(5.5), Inches(0.30), [(t, 16, WHITE, True)])
        add_text(s, Inches(7.08), y + Inches(0.48), Inches(5.5), Inches(0.40), [(d, 13, RGBColor(0xD7, 0xDE, 0xE7), False)])

    add_notes(
        s,
        "这页只讲问题，不报论文。先说高可靠导致寿命试验失效太少，再强调退化轨迹是连续信息。"
        "四个约束各举半句现场例子即可：永磁制动器是小样本，重型机床是多指标，激光器常有个体差异，航空发动机是流式监测。"
        "右边四层从上往下讲一遍，收在：我们后面三页分别对应过程、推断、决策。",
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
            ("一作 / 通讯 SCI 60 余篇，ESI 高被引 6 篇。主持国自然青年 1 项、面上 3 项，以及浙江省自然科学基金重点项目。", 14, WHITE, False, 4),
            ("中国运筹学会可靠性分会副理事长  ·  Statistical Theory and Related Fields 副主编", 13, RGBColor(0xD7, 0xDE, 0xE7), False),
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
        "底部数字只报一句，不要念完。最后停在“欢迎批评”。",
    )

    out = "/workspace/files/slides/research-intro-experts.pptx"
    prs.save(out)
    print(out)


if __name__ == "__main__":
    build()

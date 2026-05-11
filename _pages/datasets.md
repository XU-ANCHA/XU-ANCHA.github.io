---
layout: archive
title: "数据集"
permalink: /datasets/
author_profile: true
---

常用的退化数据与可靠性分析数据集，包含数据说明、数据出处与下载链接。详细介绍见推文： 第[(1)](https://mp.weixin.qq.com/s/DRcW3D7lfKPxWv7I19e0Yg)期，第[(2)](https://mp.weixin.qq.com/s/E09oY6Khr6YFopLGLmOoTQ)期，第[(3)](https://mp.weixin.qq.com/s/fW5x7B6RgHkv_y0z_BE4Rg)期，第[(4)](https://mp.weixin.qq.com/s/JnJayk8Smui8pu9loW7KJA)期。

## 第[一](https://mp.weixin.qq.com/s/DRcW3D7lfKPxWv7I19e0Yg)期

### 1. 激光退化数据

文件名: `gaalaser_SMRD.txt` <a href="/files/datasets/1/gaalaser_SMRD.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集记录了在 80°C 高温条件下测试的 15 个 GaAs（砷化镓）激光器的运行电流随时间增加的百分比变化情况。每隔 250 小时测量一次运行电流的增加量，直至试验终止时间 4000 小时。当电流增加百分比达到 10%（即退化值为 10）时，则认为该器件失效。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 2. 碳膜电阻器退化数据

文件名: `resistor_SMRD.txt` <a href="/files/datasets/1/resistor_SMRD.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集记录了 30 个碳膜电阻器在不同温度条件下电阻随时间的变化情况。试验首先记录了每个电阻器的初始电阻值，随后分别在 452 小时、1030 小时、4341 小时和 8084 小时时，以初始电阻值的百分比形式记录电阻增加情况。该数据集可用于评估不同温度条件下碳膜电阻器的性能退化趋势，帮助研究人员分析温度对电阻器退化速率的影响。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 3. 设备-B / 集成电路退化数据

文件名: `deviceb_SMRD.txt` <a href="/files/datasets/1/deviceb_SMRD.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集记录了名为“器件B”的集成电路器件样品在三种不同温度下的测试数据。其目的是研究该产品在标准工作温度下运行 15 年（约 13 万小时）后的失效比例。工程师将功率输出下降到初始输出以下 0.5 分贝的时间点定义为故障时间，并按固定时间间隔对样品进行测量，直至达到 4000 小时终止。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 4. 金属合金疲劳裂纹扩展试验退化数据

文件名: `alloya_SMRD.txt` <a href="/files/datasets/1/alloya_SMRD.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集是对 21 个未知合金样本进行疲劳裂纹扩展实验获得的。测试之前，在每个样本中切出一条初始裂纹（长度 = 0.9 英寸）作为裂纹成核位点。实验以 10000 次疲劳载荷循环为一个测量单位，记录裂纹长度。当裂纹长度超过 1.6 英寸时，则认为样本失效并终止实验；否则测试在 120 万次循环后结束。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 5. 铝合金裂纹退化数据

文件名: `aluminumalloy_PEM.txt` <a href="/files/datasets/1/aluminumalloy_PEM.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集记录了 30 个抛光处理的 2024-T351 铝合金样本的数据，在室温环境下利用统一测量设备进行测试。实验设计以 10000 次载荷循环为时间单位，测试范围覆盖 1 至 4 单位，步长设定为 0.5 单位。当样本裂纹长度超过 15 毫米时，即判定为失效并终止测试，此时的循环次数记录为样本寿命。

> 数据出处: Wu, W. F., & Ni, C. C. (2003). A study of stochastic fatigue crack growth modeling through experimental data. *Probabilistic Engineering Mechanics, 18*(2), 107-118.

### 6. 列车车轮退化数据

文件名: `wheel_Tech.txt` <a href="/files/datasets/1/wheel_Tech.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集记录了 14 个列车车轮在行驶过程中直径磨损的情况。测试以 50 千公里为间隔，直至累积里程达到 1000 千公里。在每个里程节点，分别测量每个车轮的直径。当直径磨损达到 60 毫米时，即视为车轮失效。

> 数据出处: Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.

### 7. 发光二极管数据

文件名: `LED_Tech.txt` <a href="/files/datasets/1/LED_Tech.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集是发光二极管（LED）相对亮度（相对于初始亮度的比例）的加速退化实验数据。实验分别在 25°C、65°C 和 105°C 下各测试 25 个单元。通常将 LED 失效定义为其相对亮度下降到 0.5，即初始亮度的 50%。

> 数据出处: Hamada, M. S., Wilson, A. G., Reese, C. S., & Martz, H. F. (2008). *Bayesian Reliability*. New York: Springer-Verlag.

### 8. 永磁制动器退化数据

文件名: `PMB_ITR.txt` <a href="/files/datasets/1/PMB_ITR.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来源于对中国浙江省某企业生产的永磁制动器的实验测试。实验分别在 105℃、120℃ 和 140℃ 条件下对 9 个产品进行退化试验，试验过程中监测两个性能关键指标：制动转矩与响应时间。将试样置于 DOS60 型电热恒温干燥箱内，设定相应温度，在为期 30 天的试验周期内每日测量上述性能指标。

> 数据出处: Xu, A., Wang, B., Zhu, D., Pang, J., & Lian, X. (2024). Bayesian reliability assessment of permanent magnet brake under small sample size. *IEEE Transactions on Reliability, 74*(1), 2107-2117.

### 9. 金属膜电阻器退化数据

文件名: `resistance_Tech.txt` <a href="/files/datasets/1/resistance_Tech.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来源于一项评估电阻器寿命信息的实验，其中记录了 200 个测试单元在不同条件下的相对电阻增益与初始电阻之比。

> 数据出处: Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.


## 第[二](https://mp.weixin.qq.com/s/E09oY6Khr6YFopLGLmOoTQ)期


### 1. 发光二极管（LED）数据（二）

文件名: `LED_ITR.txt` <a href="/files/datasets/2/LED_ITR.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集展示的是 12 台 LED 在 40mA 的加速电流下进行测试得到的光强度退化数据。每 50 小时检查一次每个单元的退化水平，直至 250 小时。当光强度到达临界值 50 时，LED 即发生故障。

> 数据出处: Ye, Z. S., Wang, Y., Tsui, K. L., & Pecht, M. (2013). Degradation data analysis using Wiener processes with measurement errors. *IEEE Transactions on Reliability, 62*(4), 772-780.


### 2. 发光二极管（LED）数据（三）

文件名: `Dynamic Environments_Tech.zip` <a href="/files/datasets/2/Dynamic Environments_Tech.zip" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来源于 16 个基于中功率的改造型 LED 灯管的光通量输出测试。数据由两组在不同测试板下的测试结果构成，每组包含 8 个 LED。测试期间，收集每个 LED 的光通量衰减数据，光通量退化定义为当前光通量输出的降低值与初始光通量输出的比值。

> 数据出处: Zhai, Q., & Ye, Z.-S. (2018). Degradation in common dynamic environments. *Technometrics, 60*(4), 461–471.


### 3. 有机发光二极管（OLED）数据

文件名: `OLEDdata.csv` <a href="/files/datasets/2/OLEDdata.csv" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集主要用于评估有机发光二极管在恒定应力水平下的可靠性。数据集包含 6 个用于移动电话显示元件的 OLED 样本单元，在 20 个时间点的光度测量值。测试样本被分配在 4 种加速应力水平下：25 mA、32 mA、40 mA 和 50 mA。

> 数据出处: Bae, S. J., Kim, S. J., Kim, M. S., Lee, B. J., & Kang, C. W. (2008). Degradation analysis of nano-contamination in plasma display panels. *IEEE Transactions on Reliability, 57*(2), 222-229.


### 4. MOS 场效应晶体管退化数据

文件名: `Takeda_device_Tech.txt` <a href="/files/datasets/2/Takeda_device_Tech.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来源于 Takeda 和 Suzuki 以及 Stinebaugh、Harrus 和 Knolle 在 HCI 降解研究中针对 MOS 场效应晶体管（MOSFETs）所进行的退化实验。在整个测试期间，这些样本在相同的漏极电压和电流下进行测试。数据集由 5 个样本构成，每隔 500 秒施加一次应力，并记录相应的退化观测值。

> 数据出处: Takeda, E., & Suzuki, N. (2005). An empirical model for device degradation due to hot-carrier injection. *IEEE Electron Device Letters, 4*(4), 111-113.


### 5. 应力松弛退化数据

文件名: `Stress.csv` <a href="/files/datasets/2/Stress.csv" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集展示了电气连接器在不同温度条件下的应力松弛行为，记录了 18 个电气连接器样本的应力松弛测试结果。这些样本被随机分为三组，每组在指定温度下进行测试，以模拟连接器在实际使用过程中可能遇到的不同环境条件。当应力松弛超过预定义水平时，可认为连接器发生失效。

> 数据出处: Yang, G. (2007). Life Cycle Reliability Engineering. John Wiley & Sons.


### 6. 重型机床退化数据

文件名: `heavy_device_ITR` <a href="/files/datasets/2/heavy_device_ITR.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集是一个多样本、多变量、非等比例采样的重型机床设备性能退化数据集，包含定位精度和输出功率两个性能退化指标，能够较好模拟工业现场中常见的个体差异性、测量随机噪声以及传感器数据缺失等复杂工况。

> 数据出处: Peng, W., Li, Y. F., Yang, Y. J., Zhu, S. P., & Huang, H. Z. (2016). Bivariate analysis of incomplete degradation observations based on inverse Gaussian processes and copulas. *IEEE Transactions on Reliability, 65*(2), 624-639.


### 7. 多种竞争失效模式的电子元器件数据

文件名: `competingRisk_AMM.zip` <a href="/files/datasets/2/competingRisk_AMM.zip" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集由两部分组成：焊接界面断裂数据（灾难性失效或硬失效）和电/光信号亮度降低数据（退化失效或软失效）。数据均在相同测试条件下测得。退化数据定义为当前亮度与初始亮度之间的比率，当该比率降低至 60% 时，产品被认为失效。这两个失效过程相互竞争但彼此独立，适用于研究电子产品的竞争失效可靠性问题。

> 数据出处: Huang, W., & Askin, R. G. (2003). Reliability analysis of electronic devices with multiple competing failure modes involving performance aging degradation. *Quality and Reliability Engineering International, 19*(3), 241-254.


### 8. 抗辐射测试退化数据

文件名: `radiationTest_data.zip` <a href="/files/datasets/2/radiationTest_data.zip" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来自 STM 生产的 N 沟道功率 MOSFET 器件 STRH60N20FSY3 的抗辐射实验数据。总试验样品为 24 个，并设置了对照组。试验过程中记录了样品在辐射、退火及后续老化阶段的电参数变化，可用于研究器件在辐射环境下的性能退化与可靠性评估问题。

> 数据出处: Song, B., Zhou, Z., Ma, C., Jin, G., & Geng, S. (2017). Performance evaluation of anti-radiation based on the gamma degradation process. *Science China Technological Sciences, 60*(4), 501–509.


### 9. NIST 涂层退化数据

文件名: `Lulu_Tech.zip` <a href="/files/datasets/2/Lulu_Tech.zip" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>


该数据集来源于 NIST 开展的聚合物涂层光降解加速试验，用于研究涂层材料在紫外辐射及环境因素共同作用下的退化行为。试验共包含 48 个涂层试样，在不同紫外条件、温度和相对湿度组合下进行暴露测试，其中温度设置为 25°C、35°C 和 45°C，相对湿度设置为 0%、25% 和 50%。试验过程中，研究者利用傅里叶变换红外光谱（FTIR）对样品进行重复测量，并跟踪 1250 cm⁻¹、1510 cm⁻¹ 和 2925 cm⁻¹ 三个波数位置对应的退化特征，以刻画材料在最长 300 天内的多特征退化过程。


> 数据出处: Lu, L., Wang, B., Hong, Y., & Ye, Z. (2021). General path models for degradation data with multiple characteristics and covariates. *Technometrics, 63*(3), 354-369.


## 第[三](https://mp.weixin.qq.com/s/fW5x7B6RgHkv_y0z_BE4Rg)期：电池数据

### 1. 新能源汽车大规模锂离子电池数据

该数据由智能汽车安全技术全国重点实验室（State Key Laboratory of Intelligent Vehicle Safety Technology, IVST）发布。数据来源于运营车辆，共计 300 辆，车辆里程范围为 0 至 50 万公里，运行周期范围为 0.5 至 4 年，涵盖车辆充电、放电、静置等所有行车工况信息。

> 数据出处: Liu, H., Li, C., Hu, X., et al. (2025). Multi-modal framework for battery state of health evaluation using open-source electric vehicle data. *Nature Communications, 16*(1), 1137.

数据集链接: [http://ivstskl.changan.com.cn/?p=2697](http://ivstskl.changan.com.cn/?p=2697)

### 2. Nature Communications 公开锂离子电池 EIS 数据

该数据集由电化学阻抗谱（Electrochemical Impedance Spectroscopy, EIS）方法测量得到，包含在不同健康状态、荷电状态和温度下采集的 20,000 多个商用锂离子电池 EIS 谱。EIS 是一种实时、非侵入性且信息丰富的测量方法，能够通过测量电池对电压扰动的电流响应，获得宽频率范围内的阻抗信息。相比常规电流-电压数据，EIS 包含材料属性、界面现象和电化学反应等丰富信息，与电池内部退化机制密切相关，可用于跟踪电池状态。目前，针对该数据集的研究主要聚焦于利用 EIS 谱预测剩余使用寿命（RUL）及健康状态（SOH）。

> 数据出处: Zhang, Y., Tang, Q., Zhang, Y., et al. (2020). Identifying degradation patterns of lithium ion batteries from impedance spectroscopy using machine learning. *Nature Communications, 11*(1), 1706.

数据集链接: [https://zenodo.org/records/363383](https://zenodo.org/records/363383)

### 3. 西安交通大学（XJTU）电池数据集

该数据集包含 55 块镍钴锰（NCM）锂离子电池。所有电池均在室温环境下，按照常规固定倍率充放电、变周期随机放电、随机行走放电，以及地球同步轨道卫星（GEO）工况充放电等策略循环至失效。数据集共包含 6 种充放电协议，批次 1 至批次 6 分别对应上述不同充放电协议。

> 数据出处: Wang, F., Zhai, Z., Zhao, Z., et al. (2024). Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis. *Nature Communications, 15*(1), 4332.

数据集链接: [https://zenodo.org/records/10963339](https://zenodo.org/records/10963339)

### 4. 麻省理工-斯坦福-丰田研究中心电池数据集

该数据集由麻省理工-斯坦福-丰田研究中心发布，包含 124 个商用锂离子电池，这些电池均在快速充电条件下循环至失效。电池为磷酸铁锂（LFP）/石墨体系，由 A123 Systems 公司生产，型号为 APR18650M1A。实验在设定为 30°C 的强制对流恒温箱内进行，使用 48 通道 Arbin LBT 电化学工作站对水平放置的圆柱形电池进行循环测试。每个电芯的额定容量为 1.1 Ah，额定电压为 3.3 V。整个数据集被划分为三个批次，每个批次包含约 48 个电芯。不同批次之间存在部分实验细节差异，具体说明可参见各批次的独立说明页面。

> 数据出处: Severson, K. A., Attia, P. M., Jin, N., et al. (2019). Data-driven prediction of battery cycle life before capacity degradation. *Nature Energy, 4*(5), 383-391.

数据集链接: [https://data.matr.io/1/projects/5c48dd2bc625d700019f3204](https://data.matr.io/1/projects/5c48dd2bc625d700019f3204)

### 5. Nature 公开快速充电电池数据集

该数据集来源于锂离子磷酸盐（LFP）/石墨电池快速充电实验。研究人员采用不同充电方案对电池进行充电，但使用相同方案进行放电。放电方案为：以 4C 倍率进行恒流-恒压（CC-CV）放电至 2.0 V，截止电流为 C/50。电池采用固定的 10 分钟充电方案，充电电流倍率范围为 3C 至 8C，充电至 80% 荷电状态（SOC）后，再以 1C 倍率进行恒流-恒压充电至 3.6 V，充电截止电流为 C/50。数据集分为 5 个批次，每个批次约包含 48 个电芯。前四批电芯循环 100 至 120 次，最终批次中的电芯被循环至失效，即容量退化至初始容量的 80%。

> 数据出处: Attia, P. M., Grover, A., Jin, N., et al. (2020). Closed-loop optimization of fast-charging protocols for batteries with machine learning. *Nature, 578*(7795), 397-402.

数据集链接: [https://data.matr.io/1/projects/5d80e633f405260001c0b60a](https://data.matr.io/1/projects/5d80e633f405260001c0b60a)

### 6. NASA 锂电池退化数据

该数据集来自 NASA Ames 预后卓越中心（Prognostics Center of Excellence, PCoE）定制电池预报测试平台。锂离子电池在不同温度下通过三种工作模式进行测试，包括充电、放电和电化学阻抗谱测试。放电在不同电流负载水平下进行，直到电池电压降至预设电压阈值。其中部分阈值低于原厂推荐的 2.7 V，以诱发深度放电老化效应。反复充放电循环会导致电池加速老化。当电池达到寿命终止标准，即额定容量衰减 30%（从 2 Ah 降至 1.4 Ah）时，实验终止。

> 数据出处: Saha, B., & Goebel, K. (2007). Battery data set. *NASA Ames Prognostics Data Repository*.

数据集链接: [https://c3.nasa.gov/dashlink/resources/133/](https://c3.nasa.gov/dashlink/resources/133/)

### 7. 马里兰大学 CALCE 电池退化数据

该数据集由马里兰大学 CALCE 电池团队提供，是开放访问的锂离子电池实验测试数据。数据包含 144 块具有三种不同 SOC 水平，即 0% SOC、50% SOC 和 100% SOC 的锂离子电池，这些电池在四种不同温度条件下，即 -40°C、-5°C、25°C 和 50°C，开展储能寿命测试。测试内容包括连续全循环和部分循环、储存、动态驱动曲线、开路电压测量和阻抗测量。电池形制包括圆柱形、袋状和棱柱形，化学体系包括 LCO、LFP 和 NMC。该数据可用于电池状态估计、剩余使用寿命预测、加速退化建模和可靠性分析。

> 数据出处: Pecht, M., & CALCE Battery Group, University of Maryland. (2017). *CALCE battery data*.

数据集链接: [https://calce.umd.edu/data](https://calce.umd.edu/data)

### 8. 同济大学电池数据集

该数据集包含 130 块商用锂离子电池，分别为 NCA 电池、NCM 电池以及 NCM+NCA 混合型电池三类。研究人员在不同工况条件下开展循环测试，该数据可用于验证与评估电池容量估计方法。

> 数据出处: Zhu, J., Wang, Y., Huang, Y., et al. (2022). Data-driven capacity estimation of commercial lithium-ion batteries from voltage relaxation. *Nature Communications, 13*(1), 2261.

数据集链接: [https://zenodo.org/records/6405084](https://zenodo.org/records/6405084)

### 9. 华中科技大学电池数据集

该数据集包含 77 个 LFP/石墨电池，额定容量为 1.1 Ah，额定电压为 3.3 V。实验中，电池采用相同的充电协议，但采用不同的多级放电协议，测试温度恒定为 30°C。

> 数据出处: Ma, G., Xu, S., Jiang, B., et al. (2022). Real-time personalized health status prediction of lithium-ion batteries using deep transfer learning. *Energy & Environmental Science, 15*(10), 4083-4094.

数据集链接: [https://data.mendeley.com/datasets/nsc7hnsg4s/2](https://data.mendeley.com/datasets/nsc7hnsg4s/2)

### 10. RWTH 电池数据集

该数据集包含对 48 个 Sanyo/Panasonic UR18650E 圆柱形锂离子电池单元进行循环老化测试的时间序列数据，包括时间、电流、电压和温度等信息。实验中，48 个同型号电芯在相同条件下进行老化测试。老化前，研究人员通过寿命初始测试（Beginning-of-Life, BOL）确定初始性能；在老化过程中，定期开展参考性能测试（Reference Performance Test, RPT），以确定当前电池性能。

> 数据出处: Li, W., Sengupta, N., Dechent, P., et al. (2021). One-shot battery degradation trajectory prediction with deep learning. *Journal of Power Sources, 506*, 230024.

数据集链接: [https://publications.rwth-aachen.de/record/820366](https://publications.rwth-aachen.de/record/820366)



## 第[四](https://mp.weixin.qq.com/s/JnJayk8Smui8pu9loW7KJA)期：破坏性退化数据

### 1. 粘合剂 A 破坏性退化数据

文件名: `AdhesiveBondA.csv` <a href="/files/datasets/4/AdhesiveBondA.csv" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来自对一种粘合剂 A 的现场服役性能评估。研究人员从已部署 5 至 15 年之间的系统中，按 11 个不同服役年龄组各随机抽取 3 个样品，共获得 33 个破坏性强度测量值。基于这些实测数据，管理方希望估计该粘合剂在服役 20 年及 30 年后强度低于 40 牛顿，即发生失效的样品比例，从而判断其是否满足可靠性要求，并为寿命延长决策提供依据。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 2. 粘合剂 B 加速破坏性退化数据

文件名: `AdhesiveBondB.csv` <a href="/files/datasets/4/AdhesiveBondB.csv" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集展示的是粘合剂随时间变化的加速破坏性强度数据，用于估计在室温条件下使用 260 周后，强度低于 40 牛顿的产品比例。数据集是在三种不同温度条件下进行破坏性试验得到的退化观测，每个试验单元只能记录一次强度值。试验开始时，研究人员首先测量了 8 个未发生退化的基准单元的强度，随后对另外 80 个样品进行了加速退化试验。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 3. 粘合剂 Formulation K 破坏性退化数据

文件名: `AdhesiveFomulationK.csv` <a href="/files/datasets/4/AdhesiveFomulationK.csv" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来自对某种新型粘合剂配方，即 Adhesive Formulation K 的加速破坏性退化试验。数据记录了 120 个样本在三个温度水平下，分别于试验 0、3、6、12、18 和 24 周后进行破坏性测量得到的粘合强度，单位为牛顿。该数据可用于评估粘合强度随时间衰减的趋势，并预测常温条件下使用 2 年和 5 年后强度低于 45 牛顿的样本比例。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 4. 绝缘材料介电强度破坏性退化数据

文件名: `InsulationBreakdown.csv` <a href="/files/datasets/4/InsulationBreakdown.csv" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集展示的是绝缘材料介电强度的加速破坏性退化试验数据。试验在四种不同温度条件下进行，每个温度水平下分别放入 32 个样本。随后在 1、2、4、8、16、32、48 和 64 周时，从每个反应室中取出 4 个样品进行破坏性测量。介电强度通过在短时间内线性增加电压来测量，直到样品发生击穿，此时记录击穿电压，单位为千伏。该绝缘材料设计要求是在正常工作条件下具有 2 kV 的击穿电压。

> 数据出处: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 5. 污染物浓度破坏性降解数据

文件名: `Tech_Sun_MDDT.zip` <a href="/files/datasets/4/Tech_Sun_MDDT.zip" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来自一项关于三种新兴污染物 Saccharin、Acesulfame 和 pCBA 的破坏性降解测试。实验共使用 2 个测试台，每个测试台在 7 个预设时间点，即 0.15 至 1.05，各取出 3 个测试单元。每个测试单元是一管含有三种污染物的溶液，因此总样本量为 126。研究人员测量每种污染物的残留浓度，并通过对数变换得到降解量。基于该数据，可估计降解速率、相关性及区组效应参数，进而用于污染物环境风险评估和水处理时间决策。

> 数据出处: Sun, Q., Ye, Z. S., & Hong, Y. (2020). Statistical modeling of multivariate destructive degradation tests with blocking. *Technometrics, 62*(4), 536-548.

### 6. 电路枝晶尺寸破坏性退化数据

文件名: `Dendrite_size_data.txt` <a href="/files/datasets/4/Dendrite_size_data.txt" download><img src="https://img.shields.io/badge/download-5bc0de?style=flat-square&logo=googledrive&logoColor=white" height="16"></a>

该数据集来源于密封电路中枝晶尺寸的破坏性退化试验。其中，枝晶尺寸定义为树枝状晶体长度占两个导体间距的百分比。失效分析表明，当枝晶在两个平行铜导体之间持续生长并最终导致短路时，电路发生失效。因此，该类数据可以视为导致失效的退化过程的直接物理测量结果。为了估计电路失效时间分布，试验选取了不同寿命阶段的电路样本，并对每个电路中最大枝晶的尺寸进行测量。在部分电路中，未观察到枝晶生长，因此其观测尺寸记为零。

> 数据出处: Nelson, W. B. (2009). Defect initiation, growth, and failure—a general statistical model and data analyses. In *Advances in Degradation Modeling: Applications to Reliability, Survival Analysis, and Finance* (pp. 27-37). Boston, MA: Birkhäuser Boston.










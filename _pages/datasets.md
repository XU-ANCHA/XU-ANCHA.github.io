---
layout: archive
title: "数据集"
permalink: /datasets/
author_profile: true
---


常用的退化数据与可靠性分析数据集，包含数据说明、数据出处与下载链接。详细介绍见推文： 第 [(1)](https://mp.weixin.qq.com/s/DRcW3D7lfKPxWv7I19e0Yg) 期，第 [(2)](https://mp.weixin.qq.com/s/E09oY6Khr6YFopLGLmOoTQ) 期。

## 第一期

### 1. 激光退化数据

文件名：`gaalaser_SMRD.txt`，<a href="/files/datasets/1/gaalaser_SMRD.txt" download>点击下载</a>

该数据集记录了在 80°C 高温条件下测试的 15 个 GaAs（砷化镓）激光器的运行电流随时间增加的百分比变化情况。每隔 250 小时测量一次运行电流的增加量，直至试验终止时间 4000 小时。当电流增加百分比达到 10%（即退化值为 10）时，则认为该器件失效。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 2. 碳膜电阻器退化数据

文件名：`resistor_SMRD.txt`，<a href="/files/datasets/1/resistor_SMRD.txt" download>点击下载</a>

该数据集记录了 30 个碳膜电阻器在不同温度条件下电阻随时间的变化情况。试验首先记录了每个电阻器的初始电阻值，随后分别在 452 小时、1030 小时、4341 小时和 8084 小时时，以初始电阻值的百分比形式记录电阻增加情况。该数据集可用于评估不同温度条件下碳膜电阻器的性能退化趋势，帮助研究人员分析温度对电阻器退化速率的影响。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 3. 设备-B / 集成电路退化数据

文件名：`deviceb_SMRD.txt`，<a href="/files/datasets/1/deviceb_SMRD.txt" download>点击下载</a>

该数据集记录了名为“器件B”的集成电路器件样品在三种不同温度下的测试数据。其目的是研究该产品在标准工作温度下运行 15 年（约 13 万小时）后的失效比例。工程师将功率输出下降到初始输出以下 0.5 分贝的时间点定义为故障时间，并按固定时间间隔对样品进行测量，直至达到 4000 小时终止。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 4. 金属合金疲劳裂纹扩展试验退化数据

文件名：`alloya_SMRD.txt`，<a href="/files/datasets/1/alloya_SMRD.txt" download>点击下载</a>

该数据集是对 21 个未知合金样本进行疲劳裂纹扩展实验获得的。测试之前，在每个样本中切出一条初始裂纹（长度 = 0.9 英寸）作为裂纹成核位点。实验以 10000 次疲劳载荷循环为一个测量单位，记录裂纹长度。当裂纹长度超过 1.6 英寸时，则认为样本失效并终止实验；否则测试在 120 万次循环后结束。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 5. 铝合金裂纹退化数据

文件名：`aluminumalloy_PEM.txt`，<a href="/files/datasets/1/aluminumalloy_PEM.txt" download>点击下载</a>

该数据集记录了 30 个抛光处理的 2024-T351 铝合金样本的数据，在室温环境下利用统一测量设备进行测试。实验设计以 10000 次载荷循环为时间单位，测试范围覆盖 1 至 4 单位，步长设定为 0.5 单位。当样本裂纹长度超过 15 毫米时，即判定为失效并终止测试，此时的循环次数记录为样本寿命。

> 数据出处：Wu, W. F., & Ni, C. C. (2003). A study of stochastic fatigue crack growth modeling through experimental data. *Probabilistic Engineering Mechanics, 18*(2), 107-118.

### 6. 列车车轮退化数据

文件名：`wheel_Tech.txt`，<a href="/files/datasets/1/wheel_Tech.txt" download>点击下载</a>

该数据集记录了 14 个列车车轮在行驶过程中直径磨损的情况。测试以 50 千公里为间隔，直至累积里程达到 1000 千公里。在每个里程节点，分别测量每个车轮的直径。当直径磨损达到 60 毫米时，即视为车轮失效。

> 数据出处：Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.

### 7. 发光二极管数据

文件名：`LED_Tech.txt`，<a href="/files/datasets/1/LED_Tech.txt" download>点击下载</a>

该数据集是发光二极管（LED）相对亮度（相对于初始亮度的比例）的加速退化实验数据。实验分别在 25°C、65°C 和 105°C 下各测试 25 个单元。通常将 LED 失效定义为其相对亮度下降到 0.5，即初始亮度的 50%。

> 数据出处：Hamada, M. S., Wilson, A. G., Reese, C. S., & Martz, H. F. (2008). *Bayesian Reliability*. New York: Springer-Verlag.

### 8. 永磁制动器退化数据

文件名：`PMB_ITR.txt`，<a href="/files/datasets/1/PMB_ITR.txt" download>点击下载</a>

该数据集来源于对中国浙江省某企业生产的永磁制动器的实验测试。实验分别在 105℃、120℃ 和 140℃ 条件下对 9 个产品进行退化试验，试验过程中监测两个性能关键指标：制动转矩与响应时间。将试样置于 DOS60 型电热恒温干燥箱内，设定相应温度，在为期 30 天的试验周期内每日测量上述性能指标。

> 数据出处：Xu, A., Wang, B., Zhu, D., Pang, J., & Lian, X. (2024). Bayesian reliability assessment of permanent magnet brake under small sample size. *IEEE Transactions on Reliability, 74*(1), 2107-2117.

### 9. 金属膜电阻器退化数据

文件名：`resistance_Tech.txt`，<a href="/files/datasets/1/resistance_Tech.txt" download>点击下载</a>

该数据集来源于一项评估电阻器寿命信息的实验，其中记录了 200 个测试单元在不同条件下的相对电阻增益与初始电阻之比。

> 数据出处：Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.


## 第二期


### 1. 发光二极管（LED）数据（二）

文件名：`LED_ITR.txt`，<a href="/files/datasets/2/LED_ITR.txt" download>点击下载</a>

该数据集展示的是 12 台 LED 在 40mA 的加速电流下进行测试得到的光强度退化数据。每 50 小时检查一次每个单元的退化水平，直至 250 小时。当光强度到达临界值 50 时，LED 即发生故障。

> 数据出处：Ye, Z. S., Wang, Y., Tsui, K. L., & Pecht, M. (2013). Degradation data analysis using Wiener processes with measurement errors. *IEEE Transactions on Reliability, 62*(4), 772-780.


### 2. 发光二极管（LED）数据（三）

文件名：`Dynamic Environments_Tech LED_data.mat`，<a href="/files/datasets/2/Dynamic%20Environments_Tech%20LED_data.mat" download>点击下载</a>

该数据集来源于 16 个基于中功率的改造型 LED 灯管的光通量输出测试。数据由两组在不同测试板下的测试结果构成，每组包含 8 个 LED。测试期间，收集每个 LED 的光通量衰减数据，光通量退化定义为当前光通量输出的降低值与初始光通量输出的比值。

> 数据出处：Zhai, Q., & Ye, Z.-S. (2018). Degradation in common dynamic environments. *Technometrics, 60*(4), 461–471.


### 3. 有机发光二极管（OLED）数据

文件名：`OLEDdata.csv`，<a href="/files/datasets/2/OLEDdata.csv" download>点击下载</a>

该数据集主要用于评估有机发光二极管在恒定应力水平下的可靠性。数据集包含 6 个用于移动电话显示元件的 OLED 样本单元，在 20 个时间点的光度测量值。测试样本被分配在 4 种加速应力水平下：25 mA、32 mA、40 mA 和 50 mA。

> 数据出处：Bae, S. J., Kim, S. J., Kim, M. S., Lee, B. J., & Kang, C. W. (2008). Degradation analysis of nano-contamination in plasma display panels. *IEEE Transactions on Reliability, 57*(2), 222-229.


### 4. MOS 场效应晶体管退化数据

文件名：`Takeda_device_Tech.txt`，<a href="/files/datasets/2/Takeda_device_Tech.txt" download>点击下载</a>

该数据集来源于 Takeda 和 Suzuki 以及 Stinebaugh、Harrus 和 Knolle 在 HCI 降解研究中针对 MOS 场效应晶体管（MOSFETs）所进行的退化实验。在整个测试期间，这些样本在相同的漏极电压和电流下进行测试。数据集由 5 个样本构成，每隔 500 秒施加一次应力，并记录相应的退化观测值。

> 数据出处：Takeda, E., & Suzuki, N. (2005). An empirical model for device degradation due to hot-carrier injection. *IEEE Electron Device Letters, 4*(4), 111-113.


### 5. 应力松弛退化数据

文件名：`Stress.csv`，<a href="/files/datasets/2/Stress.csv" download>点击下载</a>

该数据集展示了电气连接器在不同温度条件下的应力松弛行为，记录了 18 个电气连接器样本的应力松弛测试结果。这些样本被随机分为三组，每组在指定温度下进行测试，以模拟连接器在实际使用过程中可能遇到的不同环境条件。当应力松弛超过预定义水平时，可认为连接器发生失效。

> 数据出处：Yang, G. (2007). Life Cycle Reliability Engineering. John Wiley & Sons.


### 6. 重型机床退化数据

文件名：`heavy-device-ITR.txt`，<a href="/files/datasets/2/heavy-device-ITR.txt" download>点击下载</a>

该数据集是一个多样本、多变量、非等比例采样的重型机床设备性能退化数据集，包含定位精度和输出功率两个性能退化指标，能够较好模拟工业现场中常见的个体差异性、测量随机噪声以及传感器数据缺失等复杂工况。

> 数据出处：Peng, W., Li, Y. F., Yang, Y. J., Zhu, S. P., & Huang, H. Z. (2016). Bivariate analysis of incomplete degradation observations based on inverse Gaussian processes and copulas. *IEEE Transactions on Reliability, 65*(2), 624-639.


### 7. 多种竞争失效模式的电子元器件数据

文件名：`competingRisk-AMM.zip`，<a href="/files/datasets/2/competingRisk-AMM.zip" download>点击下载</a>

该数据集由两部分组成：焊接界面断裂数据（灾难性失效或硬失效）和电/光信号亮度降低数据（退化失效或软失效）。数据均在相同测试条件下测得。退化数据定义为当前亮度与初始亮度之间的比率，当该比率降低至 60% 时，产品被认为失效。这两个失效过程相互竞争但彼此独立，适用于研究电子产品的竞争失效可靠性问题。

> 数据出处：Huang, W., & Askin, R. G. (2003). Reliability analysis of electronic devices with multiple competing failure modes involving performance aging degradation. *Quality and Reliability Engineering International, 19*(3), 241-254.


### 8. 抗辐射测试退化数据

文件名：`radiationTest-data`，<a href="/files/datasets/2/radiationTest-data" download>点击下载</a>

该数据集来自 STM 生产的 N 沟道功率 MOSFET 器件 STRH60N20FSY3 的抗辐射实验数据。总试验样品为 24 个，并设置了对照组。试验过程中记录了样品在辐射、退火及后续老化阶段的电参数变化，可用于研究器件在辐射环境下的性能退化与可靠性评估问题。

> 数据出处：Song, B., Zhou, Z., Ma, C., Jin, G., & Geng, S. (2017). Performance evaluation of anti-radiation based on the gamma degradation process. *Science China Technological Sciences, 60*(4), 501–509.


### 9. NIST 涂层退化数据

文件名：`Lulu_Tech.zip`，<a href="/files/datasets/2/Lulu_Tech.zip" download>点击下载</a>

该数据集来源于涂层材料退化研究，适用于分析具有多特征及协变量信息的退化过程。数据可用于建立一般路径模型，并研究多维退化特征随时间和环境因素变化的规律。

> 数据出处：Lu, L., Wang, B., Hong, Y., & Ye, Z. (2021). General path models for degradation data with multiple characteristics and covariates. *Technometrics, 63*(3), 354-369.


### 10. 金属膜电阻器退化数据

文件名：`resistance_Tech.txt`，<a href="/files/datasets/2/resistance_Tech.txt" download>点击下载</a>

该数据集来源于一项评估电阻器寿命信息的实验，其中记录了 200 个测试单元在不同条件下的相对电阻增益与初始电阻之比。

> 数据出处：Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.


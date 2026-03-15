---
layout: archive
title: "数据集"
permalink: /datasets/
author_profile: true
---

本页面整理了课题组常用的退化数据与可靠性分析数据集，包含数据说明、失效判据、数据出处与下载链接。详细介绍见推文[(1)](https://mp.weixin.qq.com/s/DRcW3D7lfKPxWv7I19e0Yg)。

### 1. 激光退化数据

文件名：`gaalaser_SMRD.txt`，[点击下载](/files/datasets/1/gaalaser_SMRD.txt)

该数据集记录了在 80°C 高温条件下测试的 15 个 GaAs（砷化镓）激光器的运行电流随时间增加的百分比变化情况。每隔 250 小时测量一次运行电流的增加量，直至试验终止时间 4000 小时。所有激光器的性能退化过程如图1所示。当电流增加百分比达到 10%（即退化值为10）时，则认为该器件失效。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 2. 碳膜电阻器退化数据

文件名：`resistor_SMRD.txt`，[点击下载](/files/datasets/1/resistor_SMRD.txt)

该数据集记录了 30 个碳膜电阻器在不同温度条件下电阻随时间的变化情况。试验首先记录了每个电阻器的初始电阻值，随后分别在 452 小时、1030 小时、4341 小时和 8084 小时时，以初始电阻值的百分比形式记录电阻增加情况。图2展示了碳膜电阻器的电阻增加百分比退化路径。该数据集可用于评估不同温度条件下碳膜电阻器的性能退化趋势，帮助研究人员分析温度对电阻器退化速率的影响。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 3. 设备-B / 集成电路退化数据

文件名：`deviceb_SMRD.txt`，[点击下载](/files/datasets/1/deviceb_SMRD.txt)

该数据集记录了名为“器件B”的集成电路器件样品在三种不同温度下的测试数据。其目的是研究该产品在标准工作温度下运行 15 年（约 13 万小时）后的失效比例。工程师将功率输出下降到初始输出以下 0.5 分贝的时间点定义为故障时间，并按固定时间间隔对样品进行测量，直至达到 4000 小时终止。三种温度下的退化路径如图3所示。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 4. 金属合金疲劳裂纹扩展试验退化数据

文件名：`alloya_SMRD.txt`，[点击下载](/files/datasets/1/alloya_SMRD.txt)

该数据集是对 21 个未知合金样本进行疲劳裂纹扩展实验获得的。测试之前，在每个样本中切出一条初始裂纹（长度 = 0.9 英寸）作为裂纹成核位点。实验以 10000 次疲劳载荷循环为一个测量单位，记录裂纹长度。当裂纹长度超过 1.6 英寸时，则认为样本失效并终止实验；否则测试在 120 万次循环后结束。相关退化路径如图4所示。

> 数据出处：Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 5. 铝合金裂纹退化数据

文件名：`aluminumalloy_PEM.txt`，[点击下载](/files/datasets/1/aluminumalloy_PEM.txt)

该数据集记录了 30 个抛光处理的 2024-T351 铝合金样本的数据，在室温环境下利用统一测量设备进行测试。实验设计以 10000 次载荷循环为时间单位，测试范围覆盖 1 至 4 单位，步长设定为 0.5 单位。当样本裂纹长度超过 15 毫米时，即判定为失效并终止测试，此时的循环次数记录为样本寿命。具体的数据描述见图5。

> 数据出处：Wu, W. F., & Ni, C. C. (2003). A study of stochastic fatigue crack growth modeling through experimental data. *Probabilistic Engineering Mechanics, 18*(2), 107-118.

### 6. 列车车轮退化数据

文件名：`wheel_Tech.txt`，[点击下载](/files/datasets/1/wheel_Tech.txt)

该数据集记录了 14 个列车车轮在行驶过程中直径磨损的情况。测试以 50 千公里为间隔，直至累积里程达到 1000 千公里。在每个里程节点，分别测量每个车轮的直径。当直径磨损达到 60 毫米时，即视为车轮失效。数据如图6所示。

> 数据出处：Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.

### 7. 发光二极管数据

文件名：`LED_Tech.txt`，[点击下载](/files/datasets/1/LED_Tech.txt)

该数据集是发光二极管（LED）相对亮度（相对于初始亮度的比例）的加速退化实验数据。实验分别在 25°C、65°C 和 105°C 下各测试 25 个单元。通常将 LED 失效定义为其相对亮度下降到 0.5，即初始亮度的 50%。图7展示了该数据集的退化路径。

> 数据出处：Hamada, M. S., Wilson, A. G., Reese, C. S., & Martz, H. F. (2008). *Bayesian Reliability*. New York: Springer-Verlag.

### 8. 永磁制动器退化数据

文件名：`PMB_ITR.txt`，[点击下载](/files/datasets/1/PMB_ITR.txt)

该数据集来源于对中国浙江省某企业生产的永磁制动器的实验测试。实验分别在 105℃、120℃ 和 140℃ 条件下对 9 个产品进行退化试验，试验过程中监测两个性能关键指标：制动转矩与响应时间。将试样置于 DOS60 型电热恒温干燥箱内，设定相应温度，在为期 30 天的试验周期内每日测量上述性能指标。退化路径如图8所示。

> 数据出处：Xu, A., Wang, B., Zhu, D., Pang, J., & Lian, X. (2024). Bayesian reliability assessment of permanent magnet brake under small sample size. *IEEE Transactions on Reliability, 74*(1), 2107-2117.

### 9. 金属膜电阻器退化数据

文件名：`resistance_Tech.txt`，[点击下载](/files/datasets/1/resistance_Tech.txt)

该数据集来源于一项评估电阻器寿命信息的实验，其中记录了 200 个测试单元在不同条件下的相对电阻增益与初始电阻之比。测试单元的相对电阻增益退化路径如图9所示。该数据集可用于电阻器退化建模、寿命评估及可靠性分析研究。

> 数据出处：Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.

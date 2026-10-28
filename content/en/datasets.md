---
title: "Datasets"
slug: "datasets"
---

These pages collect commonly used degradation and reliability datasets, with brief descriptions, sources, and download links. Longer notes are available in Chinese: [Part 1](https://mp.weixin.qq.com/s/DRcW3D7lfKPxWv7I19e0Yg), [Part 2](https://mp.weixin.qq.com/s/E09oY6Khr6YFopLGLmOoTQ), [Part 3](https://mp.weixin.qq.com/s/fW5x7B6RgHkv_y0z_BE4Rg), and [Part 4](https://mp.weixin.qq.com/s/JnJayk8Smui8pu9loW7KJA).

- [Part 1: classic degradation data](#phase-1)
- [Part 2: industrial degradation data](#phase-2)
- [Part 3: battery data](#phase-3)
- [Part 4: destructive degradation data](#phase-4)

## [Part 1](https://mp.weixin.qq.com/s/DRcW3D7lfKPxWv7I19e0Yg) {#phase-1}

### 1. GaAs laser degradation data

File: [`gaalaser_SMRD.txt`](/files/datasets/1/gaalaser_SMRD.txt)

This data set records the percent increase in operating current for 15 GaAs lasers tested at 80°C. Current increase was measured every 250 hours until the test ended at 4000 hours. A unit is regarded as failed when the current increase reaches 10% (degradation value 10).

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 2. Carbon-film resistor degradation data

File: [`resistor_SMRD.txt`](/files/datasets/1/resistor_SMRD.txt)

This data set records resistance change over time for 30 carbon-film resistors under different temperatures. The initial resistance of each unit was recorded first; resistance increase was then recorded as a percentage of the initial value at 452, 1030, 4341, and 8084 hours. The data can be used to study temperature effects on resistor degradation.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 3. Device-B / integrated-circuit degradation data

File: [`deviceb_SMRD.txt`](/files/datasets/1/deviceb_SMRD.txt)

This data set records tests of an integrated-circuit device labeled Device B at three temperatures. The goal is to study the failure proportion after 15 years (about 130,000 hours) at the standard operating temperature. Failure is defined as a 0.5 dB drop in power output relative to the initial output. Units were measured at fixed intervals until 4000 hours.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 4. Metal-alloy fatigue-crack growth data

File: [`alloya_SMRD.txt`](/files/datasets/1/alloya_SMRD.txt)

This data set comes from a fatigue-crack growth experiment on 21 samples of an unknown alloy. An initial crack of 0.9 inches was cut in each sample as a nucleation site. Crack length was recorded every 10,000 load cycles. A sample failed when the crack exceeded 1.6 inches; otherwise the test ended after 1.2 million cycles.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 5. Aluminum-alloy crack growth data

File: [`aluminumalloy_PEM.txt`](/files/datasets/1/aluminumalloy_PEM.txt)

This data set records 30 polished 2024-T351 aluminum-alloy specimens tested at room temperature with a common measurement setup. Time is measured in units of 10,000 load cycles, covering 1 to 4 units in steps of 0.5. A specimen fails when the crack length exceeds 15 mm, and the corresponding cycle count is recorded as lifetime.

> Source: Wu, W. F., & Ni, C. C. (2003). A study of stochastic fatigue crack growth modeling through experimental data. *Probabilistic Engineering Mechanics, 18*(2), 107-118.

### 6. Train-wheel wear data

File: [`wheel_Tech.txt`](/files/datasets/1/wheel_Tech.txt)

This data set records diameter wear for 14 train wheels. Measurements were taken every 50,000 km up to a cumulative 1,000,000 km. A wheel is regarded as failed when diameter wear reaches 60 mm.

> Source: Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.

### 7. LED degradation data

File: [`LED_Tech.txt`](/files/datasets/1/LED_Tech.txt)

This data set contains accelerated degradation measurements of LED relative luminosity (relative to initial luminosity). Twenty-five units were tested at each of 25°C, 65°C, and 105°C. Failure is typically defined as a drop of relative luminosity to 0.5.

> Source: Hamada, M. S., Wilson, A. G., Reese, C. S., & Martz, H. F. (2008). *Bayesian Reliability*. New York: Springer-Verlag.

### 8. Permanent-magnet brake degradation data

File: [`PMB_ITR.txt`](/files/datasets/1/PMB_ITR.txt)

This data set comes from laboratory tests of permanent-magnet brakes produced by a firm in Zhejiang, China. Nine products were tested at 105°C, 120°C, and 140°C, monitoring braking torque and response time. Specimens were placed in a DOS60 electrothermal drying oven and measured daily over a 30-day period.

> Source: Xu, A., Wang, B., Zhu, D., Pang, J., & Lian, X. (2024). Bayesian reliability assessment of permanent magnet brake under small sample size. *IEEE Transactions on Reliability, 74*(1), 2107-2117.

### 9. Metal-film resistor degradation data

File: [`resistance_Tech.txt`](/files/datasets/1/resistance_Tech.txt)

This data set comes from an experiment evaluating resistor lifetime information. It records the ratio of relative resistance gain to initial resistance for 200 test units under different conditions.

> Source: Peng, C. Y., & Cheng, Y. S. (2020). Student-t processes for degradation analysis. *Technometrics, 62*(2), 223-235.

## [Part 2](https://mp.weixin.qq.com/s/E09oY6Khr6YFopLGLmOoTQ) {#phase-2}

### 1. LED data (II)

File: [`LED_ITR.txt`](/files/datasets/2/LED_ITR.txt)

This data set records light-intensity degradation of 12 LEDs tested at an accelerated current of 40 mA. Each unit was inspected every 50 hours until 250 hours. An LED fails when light intensity reaches the critical value 50.

> Source: Ye, Z. S., Wang, Y., Tsui, K. L., & Pecht, M. (2013). Degradation data analysis using Wiener processes with measurement errors. *IEEE Transactions on Reliability, 62*(4), 772-780.

### 2. LED data (III)

File: [`Dynamic Environments_Tech.zip`](/files/datasets/2/Dynamic%20Environments_Tech.zip)

This data set comes from luminous-flux tests of 16 mid-power retrofit LED tubes. The data consist of two groups tested on different boards, with 8 LEDs in each group. Luminous-flux decay is defined as the reduction in current flux output relative to the initial output.

> Source: Zhai, Q., & Ye, Z.-S. (2018). Degradation in common dynamic environments. *Technometrics, 60*(4), 461–471.

### 3. OLED data

File: [`OLEDdata.csv`](/files/datasets/2/OLEDdata.csv)

This data set is used to assess the reliability of organic light-emitting diodes under constant stress. It contains luminosity measurements of 6 OLED units for mobile-phone displays at 20 time points. Units were assigned to four accelerated current levels: 25 mA, 32 mA, 40 mA, and 50 mA.

> Source: Bae, S. J., Kim, S. J., Kim, M. S., Lee, B. J., & Kang, C. W. (2008). Degradation analysis of nano-contamination in plasma display panels. *IEEE Transactions on Reliability, 57*(2), 222-229.

### 4. MOSFET degradation data

File: [`Takeda_device_Tech.txt`](/files/datasets/2/Takeda_device_Tech.txt)

This data set comes from hot-carrier-injection degradation experiments on MOSFETs reported by Takeda and Suzuki and by Stinebaugh, Harrus, and Knolle. Units were tested at the same drain voltage and current. The data consist of 5 samples, with stress applied every 500 seconds and corresponding degradation observations recorded.

> Source: Takeda, E., & Suzuki, N. (2005). An empirical model for device degradation due to hot-carrier injection. *IEEE Electron Device Letters, 4*(4), 111-113.

### 5. Stress-relaxation data

File: [`Stress.csv`](/files/datasets/2/Stress.csv)

This data set records stress-relaxation of electrical connectors at different temperatures. Eighteen connector samples were randomly split into three groups and tested at specified temperatures. A connector may be regarded as failed when stress relaxation exceeds a predefined level.

> Source: Yang, G. (2007). *Life Cycle Reliability Engineering*. John Wiley & Sons.

### 6. Heavy-machine-tool degradation data

File: [`heavy_device_ITR.txt`](/files/datasets/2/heavy_device_ITR.txt)

This is a multi-sample, multivariate, irregularly sampled data set for heavy machine tools, containing positioning accuracy and output power. It captures unit-to-unit variation, measurement noise, and missing sensor readings that are common in industrial settings.

> Source: Peng, W., Li, Y. F., Yang, Y. J., Zhu, S. P., & Huang, H. Z. (2016). Bivariate analysis of incomplete degradation observations based on inverse Gaussian processes and copulas. *IEEE Transactions on Reliability, 65*(2), 624-639.

### 7. Electronic devices with competing failure modes

File: [`competingRisk_AMM.zip`](/files/datasets/2/competingRisk_AMM.zip)

This data set has two parts: solder-interface fracture (catastrophic or hard failure) and electrical/optical brightness reduction (degradation or soft failure), collected under the same test conditions. Degradation is defined as the ratio of current brightness to initial brightness; a product fails when the ratio drops to 60%. The two failure processes compete but are independent, and are useful for studying competing-risks reliability of electronic products.

> Source: Huang, W., & Askin, R. G. (2003). Reliability analysis of electronic devices with multiple competing failure modes involving performance aging degradation. *Quality and Reliability Engineering International, 19*(3), 241-254.

### 8. Radiation-hardness test data

File: [`radiationTest_data.zip`](/files/datasets/2/radiationTest_data.zip)

This data set comes from radiation-hardness experiments on STM N-channel power MOSFETs STRH60N20FSY3. There were 24 samples plus a control group. Electrical parameters were recorded during radiation, annealing, and subsequent aging, and can be used to study performance degradation and reliability under radiation.

> Source: Song, B., Zhou, Z., Ma, C., Jin, G., & Geng, S. (2017). Performance evaluation of anti-radiation based on the gamma degradation process. *Science China Technological Sciences, 60*(4), 501–509.

### 9. NIST coating degradation data

File: [`Lulu_Tech.zip`](/files/datasets/2/Lulu_Tech.zip)

This data set comes from NIST accelerated photodegradation tests of polymer coatings under ultraviolet radiation and environmental factors. Forty-eight coating specimens were exposed under combinations of UV, temperature (25°C, 35°C, 45°C), and relative humidity (0%, 25%, 50%). Repeated FTIR measurements tracked degradation features at 1250, 1510, and 2925 cm⁻¹ for up to 300 days.

> Source: Lu, L., Wang, B., Hong, Y., & Ye, Z. (2021). General path models for degradation data with multiple characteristics and covariates. *Technometrics, 63*(3), 354-369.

## [Part 3: battery data](https://mp.weixin.qq.com/s/fW5x7B6RgHkv_y0z_BE4Rg) {#phase-3}

### 1. Large-scale lithium-ion battery data from new-energy vehicles

Released by the State Key Laboratory of Intelligent Vehicle Safety Technology (IVST). The data come from 300 in-service vehicles with mileage from 0 to 500,000 km and operating periods from 0.5 to 4 years, covering charging, discharging, and rest conditions.

> Source: Liu, H., Li, C., Hu, X., et al. (2025). Multi-modal framework for battery state of health evaluation using open-source electric vehicle data. *Nature Communications, 16*(1), 1137.

Link: [http://ivstskl.changan.com.cn/?p=2697](http://ivstskl.changan.com.cn/?p=2697)

### 2. Nature Communications lithium-ion battery EIS data

This data set contains more than 20,000 commercial lithium-ion battery EIS spectra collected under different states of health, states of charge, and temperatures. EIS is a real-time, noninvasive measurement of the current response to a voltage perturbation over a wide frequency range, and is closely related to internal degradation mechanisms. Existing studies have used these spectra for remaining useful life and state-of-health prediction.

> Source: Zhang, Y., Tang, Q., Zhang, Y., et al. (2020). Identifying degradation patterns of lithium ion batteries from impedance spectroscopy using machine learning. *Nature Communications, 11*(1), 1706.

Link: [https://zenodo.org/records/363383](https://zenodo.org/records/363383)

### 3. XJTU battery data set

This data set contains 55 NCM lithium-ion batteries cycled to failure at room temperature under fixed-rate charge/discharge, variable-period random discharge, random-walk discharge, and GEO satellite charge/discharge protocols. There are six charge/discharge protocols corresponding to batches 1–6.

> Source: Wang, F., Zhai, Z., Zhao, Z., et al. (2024). Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis. *Nature Communications, 15*(1), 4332.

Link: [https://zenodo.org/records/10963339](https://zenodo.org/records/10963339)

### 4. MIT–Stanford–Toyota Research Institute battery data set

This data set contains 124 commercial lithium-ion batteries cycled to failure under fast charging. The cells are LFP/graphite APR18650M1A cells from A123 Systems, tested in a 30°C forced-convection chamber on a 48-channel Arbin LBT cycler. Nominal capacity is 1.1 Ah and nominal voltage is 3.3 V. The data are split into three batches of about 48 cells, with some experimental differences across batches.

> Source: Severson, K. A., Attia, P. M., Jin, N., et al. (2019). Data-driven prediction of battery cycle life before capacity degradation. *Nature Energy, 4*(5), 383-391.

Link: [https://data.matr.io/1/projects/5c48dd2bc625d700019f3204](https://data.matr.io/1/projects/5c48dd2bc625d700019f3204)

### 5. Nature fast-charging battery data set

This data set comes from fast-charging experiments on LFP/graphite cells. Charging protocols vary, while discharge is the same: 4C CC-CV to 2.0 V with a C/50 cutoff. Cells use a fixed 10-minute charging scheme with currents from 3C to 8C to 80% SOC, then 1C CC-CV to 3.6 V with a C/50 cutoff. There are five batches of about 48 cells; the first four were cycled 100–120 times, and the last batch was cycled to failure (80% of initial capacity).

> Source: Attia, P. M., Grover, A., Jin, N., et al. (2020). Closed-loop optimization of fast-charging protocols for batteries with machine learning. *Nature, 578*(7795), 397-402.

Link: [https://data.matr.io/1/projects/5d80e633f405260001c0b60a](https://data.matr.io/1/projects/5d80e633f405260001c0b60a)

### 6. NASA lithium-ion battery degradation data

This data set comes from the NASA Ames Prognostics Center of Excellence battery testbed. Lithium-ion batteries were tested at different temperatures under charge, discharge, and EIS. Discharge used different current loads until voltage reached a preset threshold, some of which were below the manufacturer’s 2.7 V recommendation to induce deep-discharge aging. The experiment ended when capacity faded 30% (from 2 Ah to 1.4 Ah).

> Source: Saha, B., & Goebel, K. (2007). Battery data set. *NASA Ames Prognostics Data Repository*.

Link: [https://c3.nasa.gov/dashlink/resources/133/](https://c3.nasa.gov/dashlink/resources/133/)

### 7. University of Maryland CALCE battery data

This open data set from the CALCE battery group contains 144 lithium-ion cells at 0%, 50%, and 100% SOC, stored at −40°C, −5°C, 25°C, and 50°C. Tests include full and partial cycling, storage, dynamic driving profiles, OCV, and impedance. Form factors include cylindrical, pouch, and prismatic cells; chemistries include LCO, LFP, and NMC.

> Source: Pecht, M., & CALCE Battery Group, University of Maryland. (2017). *CALCE battery data*.

Link: [https://calce.umd.edu/data](https://calce.umd.edu/data)

### 8. Tongji University battery data set

This data set contains 130 commercial lithium-ion batteries of NCA, NCM, and NCM+NCA types, cycled under different operating conditions. It can be used to evaluate capacity-estimation methods.

> Source: Zhu, J., Wang, Y., Huang, Y., et al. (2022). Data-driven capacity estimation of commercial lithium-ion batteries from voltage relaxation. *Nature Communications, 13*(1), 2261.

Link: [https://zenodo.org/records/6405084](https://zenodo.org/records/6405084)

### 9. Huazhong University of Science and Technology battery data set

This data set contains 77 LFP/graphite cells with 1.1 Ah nominal capacity and 3.3 V nominal voltage. Cells used the same charging protocol but different multi-stage discharge protocols at a constant 30°C.

> Source: Ma, G., Xu, S., Jiang, B., et al. (2022). Real-time personalized health status prediction of lithium-ion batteries using deep transfer learning. *Energy & Environmental Science, 15*(10), 4083-4094.

Link: [https://data.mendeley.com/datasets/nsc7hnsg4s/2](https://data.mendeley.com/datasets/nsc7hnsg4s/2)

### 10. RWTH battery data set

This data set contains time-series cycling-aging data (time, current, voltage, and temperature) for 48 Sanyo/Panasonic UR18650E cylindrical cells aged under the same conditions. Beginning-of-life tests determined initial performance, and reference performance tests were run periodically during aging.

> Source: Li, W., Sengupta, N., Dechent, P., et al. (2021). One-shot battery degradation trajectory prediction with deep learning. *Journal of Power Sources, 506*, 230024.

Link: [https://publications.rwth-aachen.de/record/820366](https://publications.rwth-aachen.de/record/820366)

## [Part 4: destructive degradation data](https://mp.weixin.qq.com/s/JnJayk8Smui8pu9loW7KJA) {#phase-4}

### 1. Adhesive A destructive degradation data

File: [`AdhesiveBondA.csv`](/files/datasets/4/AdhesiveBondA.csv)

This data set comes from a field-performance evaluation of adhesive A. Three samples were drawn at random from each of 11 in-service age groups (5 to 15 years), yielding 33 destructive strength measurements. The goal is to estimate the proportion of units whose strength falls below 40 N after 20 and 30 years of service.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 2. Adhesive B accelerated destructive degradation data

File: [`AdhesiveBondB.csv`](/files/datasets/4/AdhesiveBondB.csv)

This data set contains accelerated destructive strength measurements of an adhesive over time, used to estimate the proportion of products whose strength falls below 40 N after 260 weeks at room temperature. Destructive tests were run at three temperatures; each unit contributes one strength value. Eight undegraded baseline units were measured first, followed by 80 accelerated-test samples.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 3. Adhesive Formulation K destructive degradation data

File: [`AdhesiveFormulationK.csv`](/files/datasets/4/AdhesiveFormulationK.csv)

This data set comes from an accelerated destructive degradation test of Adhesive Formulation K. Bond strength (N) was measured destructively for 120 samples at three temperatures after 0, 3, 6, 12, 18, and 24 weeks. The data can be used to assess strength decay and to predict the proportion of samples below 45 N after 2 and 5 years at ambient temperature.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 4. Seal-strength accelerated destructive degradation data

File: [`SealStrength.csv`](/files/datasets/4/SealStrength.csv)

This temperature-accelerated destructive test studies seal strength versus time and temperature. Fifty samples were placed at each of 200°C, 250°C, 300°C, and 350°C; 10 samples were withdrawn every 5 weeks through week 25. Ten baseline samples were measured at the start, for 210 observations in total. Each unit yields one measurement because the test is destructive. Failure is defined as strength below 0.5 N.

> Source: Li, M., & Doganaksoy, N. (2014). Batch variability in accelerated-degradation testing. *Journal of Quality Technology, 46*(2), 171-180.

### 5. Insulation dielectric-strength destructive degradation data

File: [`InsulationBreakdown.csv`](/files/datasets/4/InsulationBreakdown.csv)

This data set records accelerated destructive tests of insulation dielectric strength at four temperatures, with 32 samples at each level. At weeks 1, 2, 4, 8, 16, 32, 48, and 64, four samples were withdrawn from each chamber. Dielectric strength was measured by ramping voltage until breakdown, recorded in kV. The design requirement is a 2 kV breakdown voltage under normal operating conditions.

> Source: Meeker, W. Q., Escobar, L. A., & Pascual, F. G. (2021). *Statistical methods for reliability data*. John Wiley & Sons.

### 6. Contaminant-concentration destructive degradation data

File: [`Tech_Sun_MDDT.zip`](/files/datasets/4/Tech_Sun_MDDT.zip)

This data set comes from destructive degradation tests of three emerging contaminants: saccharin, acesulfame, and pCBA. Two test benches were used; at each of 7 times from 0.15 to 1.05, 3 units were withdrawn from each bench. Each unit is a tube containing the three contaminants, for a total of 126 samples. Residual concentrations were log-transformed to obtain degradation amounts, which can be used to estimate degradation rates, dependence, and block effects.

> Source: Sun, Q., Ye, Z. S., & Hong, Y. (2020). Statistical modeling of multivariate destructive degradation tests with blocking. *Technometrics, 62*(4), 536-548.

### 7. Circuit dendrite-size destructive degradation data

File: [`Dendrite_size_data.txt`](/files/datasets/4/Dendrite_size_data.txt)

This data set comes from destructive tests of dendrite size in sealed circuits. Dendrite size is defined as dendrite length as a percentage of the spacing between two conductors. Failure analysis shows that a circuit fails when a dendrite grows between two parallel copper conductors and causes a short. Samples were taken at different life stages and the size of the largest dendrite in each circuit was measured. In some circuits no dendrite growth was observed, so the recorded size is zero.

> Source: Nelson, W. B. (2009). Defect initiation, growth, and failure—a general statistical model and data analyses. In *Advances in Degradation Modeling: Applications to Reliability, Survival Analysis, and Finance* (pp. 27-37). Boston, MA: Birkhäuser Boston.

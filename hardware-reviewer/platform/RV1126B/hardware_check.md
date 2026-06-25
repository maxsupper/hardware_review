# RV1126B 硬件设计检查规则

> **Source:** RV1126B_Hardware_Design_Guide_V1.0_20250828_CN.pdf
> **Generated:** 2026-06-24
> **Total Pages:** 171
> **Chip:** RV1126B (BGA491, 4×Cortex-A53, 3TOPS NPU)

---

## 1. 系统概述

### 1.1. 概述

RV1126B是一款专为机器视觉应用，尤其是人工智能相关应用设计的高性能视觉处理器芯片。
基于四核ARM Cortex-A53 64位内核架构，集成NEON和FPU，每个内核配备32KB I-cache和32KB D-cache，512KB L2 cache。
内置NPU支持INT8/INT16混合运算，计算能力高达3.0TOPs。
兼容TensorFlow/MXNet/PyTorch/Caffe等框架网络模型转换。

**关键特性:**
- 最大支持1200万像素图像信号处理器(ISP)和后处理器
- HDR、3A、LSC、3DNR、2DNR、锐化、去雾、鱼眼校正、伽马校正、特征点检测等算法加速器
- 最大800万像素AI-ISP
- 两个MIPI CSI（或LVDS/SubLVDS）和一个DVP（BT.601/BT.656/BT.1120）接口
- H.265/H.264视频编码器，支持多码流编码
- H.264/H.265视频解码器最大支持4KP30
- 集成RTC、POR、RMII 100Base-T PHY和双MIC Codec
- 支持DDR3/DDR3L/DDR4/LPDDR3/LPDDR4/LPDDR4X

### 1.2. 芯片差异

| 特性 | RV1126B | RV1126B-P (pin to pin RV1126) | RV1126 (EOL) |
|------|---------|-------------------------------|--------------|
| CPU | 4×A53 | 4×A53 | 4×A7 |
| NPU | 3TOPS | 3TOPS | 2TOPS |
| ISP | 12M30 | 12M30 | 12M20 |
| Encoder | 4K45 H.264&H.265, 8M30 JPEG | 4K45 H.264&H.265, 8M30 JPEG | 4K30 H.264&H.265, 2M30 JPEG |
| USB | USB2.0 DRD+USB3.0 DRD+USB2.0 HOST | USB2.0 DRD+USB2.0 HOST | USB2.0 DRD+USB2.0 HOST |
| PWM | 28 | 28 | 16 |
| SARADC | 24 | 6 | 6 |
| Ethernet | GMAC+FEPHY | GMAC | GMAC |
| Audio Codec | 2×AMIC | N/A | N/A |
| RTC | Built-in | N/A | N/A |
| nPOR | Built-in | Built-in | N/A |
| Package | BGA491 | BGA409 | BGA409 |

---

## 2. 原理图设计建议

### 2.1. 最小系统设计

#### 2.1.1. 系统工作时钟 (24MHz)

**无源晶体电路:**
- OSC_XOUT网络务必串接22Ω电阻，用于限流，防止晶体过驱
- OSC_XOUT和OSC_XIN之间的1MΩ起振电阻不可随意修改

**24MHz晶体参数要求:**
| 参数 | 规范 |
|------|------|
| 频率 | 24.000000 MHz |
| 频率偏差 | ±20 ppm |
| ESR | ≤80 Ω |
| CL值 | 建议不超过12pF |
| 外部电容CL1/CL2 | 需与晶体负载电容匹配，控制常温频率容限在20ppm以内 |
| 电容材质 | 建议COG或NPO |
| 封装 | 建议贴片4Pin晶体，2个GND管脚充分接地，加强抗ESD能力 |

**有源晶体电路:**
| 参数 | 规范 |
|------|------|
| 频率 | 24.000000 MHz |
| 频率偏差 | ±20 ppm |
| 时钟幅度 | 1.35~1.8V |
| 占空比 | 40%~60% |

#### 2.1.2. 系统休眠时钟

**休眠时钟源选择:**
| 时钟源 | 功耗 | 成本 | 说明 |
|--------|------|------|------|
| 外部RTC时钟 | 极低 | 较高 | 需增加RTC芯片及32.768k晶体 |
| 内部RTC时钟 | 较低 | 中等 | 需增加32.768k晶体 |
| 内部RCOSC时钟 | 中等 | 无 | 无需额外电路 |
| 内部24M时钟 | 较大 | 无 | 无需额外电路 |

**休眠注意事项:**
- 休眠时仅支持PMUIO0和PMUIO1电源域IO中断唤醒
- 如果唤醒源和24MHz时钟有关，24MHz时钟不能关掉
- 不关心休眠功耗可删掉RTC电路，使用内部RCOSC时钟
- **AOV产品必须保留RTC时钟电路**

**32.768kHz RTC晶体参数:**
| 参数 | 规范 |
|------|------|
| 频率 | 32.768 kHz |
| 频率偏差 | ±20 ppm |
| ESR | ≤70 kΩ |
| 电容材质 | 建议COG或NPO |

**外部32.768kHz RTC时钟参数:**
| 参数 | 规范 |
|------|------|
| 频率 | 32.768 kHz |
| 频率偏差 | ±30 ppm |
| 时钟幅度 | 2.31~3.3V |
| 占空比 | 45%~55% |
- 输入管脚: GPIO0_A2 (需设置IOMUX为CLK_32K功能)
- 开漏输出RTC芯片不能打开CLK_32K所在GPIO的内部下拉

#### 2.1.3. nPOR复位

**复位流程:**
1. 芯片上电时，内部POR模块输出低电平，进入全局复位状态
2. 模块检测NPOR_DET (Pin AL13) 和 PMUIO0_VCC3V3电压，均达到阈值
3. 内部POR模块解除输出，释放全局复位（脉冲宽度约10ms）

**NPOR模块使用注意事项:**
- 外部复位也通过NPOR_DET (Pin AL13)输入，低电平有效
- NPOR_DET上拉电源必须和PMUIO0_VCC3V3电源保持一致
- NPOR_DET需增加1nF电容和1kΩ上拉电阻，用于消除按键抖动，增强抗干扰能力

#### 2.1.4. WDT/TSADC_SHUT电路

- GPIO0_A1集成了WDT/TSADC_SHUT功能，连接到NPOR_DET
- WDT定时超时，通过TSADC_SHUT输出低电平，对SoC进行硬件复位
- TSADC温度检测超阈值，通过TSADC_SHUT输出低电平进行硬件复位
- 预留硬件看门狗与NPOR_DET相连时，必须选用支持OD输出的看门狗芯片

#### 2.1.5. 电源管理单元 (PMU)
- 用于控制管理芯片内部电源，支持低功耗需求
- 控制内部寄存器以及PMUIO0/PMUIO1电源域的IO
- 支持IO中断输入，实现芯片休眠状态下的中断唤醒

#### 2.1.6. 系统启动引导顺序

**默认Auto模式轮询顺序:**
1. FSPI0 → eMMC → SDMMC0
2. 无固件时进入Maskrom模式，通过USB2.0或UART0下载固件

**引导模式配置 (SARADC0_IN7, Pin 1A20):**
| Item | Rpu | Rpd | Boot Mode |
|------|-----|-----|-----------|
| Config1 | NC | 10K | USB/UART0 (Maskrom Mode) |
| Config2&3 | 100K | 12K | FSPI0→SDMMC0→USB/UART0 |
| Config4&5 | 100K | 51K | FSPI0→EMMC→USB/UART0 |
| Config6 | 100K | 120K | EMMC→USB/UART0 |
| Config7 | 100K | 200K | EMMC→SDMMC0→USB/UART0 |
| Config8&9 | 100K | 330K | SDMMC0→USB/UART0 |
| Config10 | 10K | NC | FSPI0→EMMC→SDMMC0→USB/UART0 (Auto) |

**注意事项:**
- SARADC0_IN7为BOOT配置专用引脚，不可作为其他功能使用
- 调试阶段建议预留测试点或按键，可拉低SARADC0_IN7到地强制进入Maskrom
- 未指定引导模式时，始终保持SARADC0_IN7上拉，默认使用Auto模式

#### 2.1.7. 系统初始化配置信号

- SDMMC0_DET管脚 (Pin AL10) 影响启动配置，需在上电前配置完毕并保持稳定
- 控制SDMMC0/JTAG管脚复用选择
  - 0: 识别为SD卡插入，复用为SDMMC0功能
  - 1: 未识别SD卡插入，复用为JTAG功能 (Default)
- 建议增加1nF电容消除信号抖动

#### 2.1.8. JTAG电路

**JTAG接口信号:**
| 信号名 | 连接方式 | 描述 |
|--------|---------|------|
| JTAG_TCK_M0/M1/M2 | 串联100Ω电阻 | SWD模式时钟输入 |
| JTAG_TMS_M0/M1/M2 | 串联100Ω电阻 | SWD模式数据输入输出 |

**注意事项:**
- 默认JTAG接口为JTAG_M1
- 使用JTAG Debug时，引导阶段需连接仿真器，保证SDMMC0_DETN高电平
- SoC端JTAG接口必须与仿真器IO电平匹配
- 建议预留2.54排针或测试点，串接100Ω电阻不得删减
- 增加TVS管，加强抗静电浪涌能力

#### 2.1.9. UART Debug电路

- 默认调试串口: UART0_M2 (PMUIO0域)，默认波特率1500000bps
- UART0_RX_M2/TX_M2串接510Ω电阻不得删减
- 增加TVS管，加强抗静电浪涌能力
- SoC端UART接口必须与转换芯片IO电平匹配
- 外部USB转UART芯片VCCIO建议从PMUIO0_VCC3V3取电，避免下电时电压倒灌
- 建议预留2.54排针或测试点

#### 2.1.10. DDR电路

**DDR控制器特性:**
- 兼容DDR3/DDR3L/DDR4/LPDDR3/LPDDR4/LPDDR4X
- 32bits数据总线宽度，2个16bits通道，支持2 ranks (2cs)
- 每个rank最大4GB寻址空间，总最大4GB
- 支持Power Down、Self Refresh等模式

**DDR PHY I/O Map:**
- 所有DDR配置模式下CA、CMD信号线顺序不支持对调，必须按参考图分配
- 控制器内置Retention功能，DDR自刷新期间DDR_VDDQ和DDR_VDDQL需保持供电，DDR颗粒端所有电源不能关
- DDR ZQ必须外接120Ω 1%电阻 (DDR3/DDR3L/DDR4/LPDDR3: 下拉到地; LPDDR4/LPDDR4X: 上拉到DDR_VDDQ)

**DDR拓扑规则:**
- DDR3/DDR3L: DQ支持Byte组间整组对调及组内对调; CA顺序不可对调
- DDR4: DQ支持Byte间整组对调及组内对调; CA顺序不可对调
- LPDDR3: DQS0组不支持任何对调; Byte1/2/3支持组间整组对调及组内对调; CA顺序不可对调
- LPDDR4/LPDDR4X: 点对点拓扑，必须按参考图一一对应，不允许调整

**DDR外围电路与VREF设计:**
- DDR3/DDR3L/LPDDR3: ZQ接240Ω 1%下拉到GND; VREFDQ接DDR_VREF_OUT (Pin 2J1); VREFCA用DDR_VDDQ经10k+10k分压
- DDR4: ZQ接240Ω 1%下拉到GND; VREFCA接DDR_VREF_OUT (Pin 2J1)
- LPDDR4/LPDDR4X: ZQ接240Ω 1%上拉到DDR_VDDQ; ODT_CA接DDR_VDDQ

**DDR电源要求:**
| DDR类型 | DDR_VDDQ | DDR_VDDQL | 颗粒VDD1 | 颗粒VDD2 | 颗粒VDDQ |
|---------|----------|-----------|----------|----------|----------|
| DDR3 | 1.5V | 1.5V | 1.5V | 1.5V | 1.5V |
| DDR3L | 1.35V | 1.35V | 1.35V | 1.35V | 1.35V |
| LPDDR3 | 1.2V | 1.2V | 1.8V | 1.2V | 1.2V |
| DDR4 | 1.2V | 1.2V | 1.2V | 1.2V | 1.2V |
| LPDDR4 | 1.1V | 1.1V | 1.8V | 1.1V | 1.1V |
| LPDDR4X | 1.1V | 0.6V | 1.8V | 1.1V | 0.6V |

> 注意: 采用PMIC方案需根据DRAM类型修改PMIC的VFB分压电阻

#### 2.1.11. 外部启动Flash接口电路

**FSPI0接口:**
- FSPI0支持串行NOR及NAND FLASH，SDR模式，1/2/4线模式
- 仅FSPI0支持引导，FSPI1不支持引导
- 支持双片选（双SPI Flash存储），需同型号同容量
- 双Flash共用DATA和CLK，需用T型拓扑，减小Stub分支长度

| 信号 | 内部上下拉 | 连接方式 |
|------|-----------|---------|
| FSPI0_D[3:0] | 上拉 | 直连 |
| FSPI0_CSN0/1 | 上拉 | 直连 |
| FSPI0_CLK | 下拉 | 串联22Ω电阻 |

**eMMC接口:**
- 支持eMMC 4.51，1/4/8-bit数据总线，最高HS200模式
- 属于VCCIO1电源域
- VCC和VCCQ上电无先后要求，但必须在CMD命令发出前稳定
- 颗粒进入睡眠后，可关断VCC电源以降低功耗

| 信号 | 内部上下拉 | 连接方式 |
|------|-----------|---------|
| eMMC_DQ[7:0] | 上拉 | 直连，DQ0需外部上拉 |
| eMMC_CMD | 上拉 | 直连，需外部上拉 |
| eMMC_CLK | 下拉 | 串联22Ω电阻 |

#### 2.1.12. GPIO电路

**GPIO电源域:**
| 电源域 | 电压 | 说明 |
|--------|------|------|
| PMUIO0 | 3.3V only | 固定电平电源域 |
| PMUIO1 | 1.8V/3.3V | 自适应IO电压 |
| VCCIO1~VCCIO7 | 1.8V/3.3V | 自适应IO电压 |

**GPIO设计注意事项:**
- SoC GPIO电源域供电需比外设先上电
- 各电源域供电管脚需就近放置至少1个100nF或1μF去耦电容
- 电源纹波要求在±10%
- 未使用的电源域可以不供电，对应管脚悬空或接地
- GPIO提供23档驱动强度可调

### 2.2. 电源设计

**芯片电源需求汇总:**
| 模块 | 电源管脚 | 冷启动 | 待机 |
|------|---------|--------|------|
| PLL | PLL_AVDD_0V9, PLL_AVDD_1V8 | 必须 | 可关断 |
| RTC | RTC_AVDD | 可不用 | 必须供电 |
| SARADC | SARADC0_AVDD_1V8, TSADC_SARADC1&2_AVDD_1V8 | 必须 | 可关断 |
| OTP | OTP_VCC_1V8 | 必须 | 可关断 |
| LOGIC | VDD_LOGIC | 必须 | 可关断 |
| CPU | VDD_CPU | 必须 | 可关断 |
| NPU | VDD_NPU | 可不用 | 可关断 |
| DDR | DDR_VDDQ, DDR_VDDQL | 必须 | 可关断 |
| PMU LOGIC | PMUIO_VDD0V9/OSC_VDD_0V9 | 必须 | 必须供电 |
| GPIO | PMUIO0, VCCIO1 | 必须 | 可关断 |
| Audio ADC | AUDIO_ADC_AVDD_1V8 | 可不用 | 可关断 |
| USB2.0 PHY | USB_AVDD_0V9_0, USB_AVDD_1V8_0, USB_AVDD_3V3 | 必须 | 可关断 |
| USB3.0 PHY | USB_AVDD_0V9_1, USB_AVDD_1V8_1 | 可不用 | 可关断 |
| MIPI CSI/LVDS RX | MIPI_DPHY_CSI_RX0/1_AVDD_0V9, AVDD_1V8 | 可不用 | 可关断 |
| MIPI DSI/LVDS TX | MIPI_DSI_TX/LVDS_TX_AVDD_0V9, AVDD_1V8 | 可不用 | 可关断 |
| FEPHY | FEPHY_AVDD_0V9, AVDD_1V8, AVDD_3V3 | 可不用 | 可关断 |

#### 上电时序要求
- 同一模块低压先上、高压后上，不同模块相同电压一起上电
- 相同时序内电源无先后要求
- 不同时序间隔 >1ms
- **冷启动总上电时序 <10ms**

**AI-IPC产品时序:** VCC3V3_SYS → VDD_LOGIC & VDD_CPU & VDD_NPU → VCC_DDR & VCC_1V8 → VCC_3V3

**AOV产品时序:** VCC3V3_PMU → VDD_LOGIC & VDD_CPU & VDD_NPU → VCC_DDR & VCC_1V8 → VCC_3V3
- AOV模式下PMUIO0和DDR电源均保持上电状态

**Pre-recording产品时序:** VCC3V3_PMUIO0 & VCC1V8_PMUIO1 → VDD_LOGIC & VDD_CPU & VDD_NPU → VCC_DDR & VCC_1V8 → VCC_3V3

#### 下电时序
- NPOR_DET (RESET) 须先拉低，然后各路电源下电
- GPIO 1.8V与PMUIO0_VCC3V3压差不大于2V
- USB2_OTG_AVDD3V3与USB2_OTG_AVDD1V8压差不大于2V
- 进出AOV/Pre-recording时，下电时间建议>100ms

#### 关键电源参数

| 电源轨 | 峰值电流 | 纹波要求 | 备注 |
|--------|---------|---------|------|
| PLL_AVDD_0V9 | <10mA | <20mV | 建议LDO供电 |
| OSC_PLL_AVDD_1V8 | <30mA | <50mV | 建议LDO供电 |
| RTC_AVDD | <1μA@3.3V | - | 不可直连锂电池，串430kΩ电阻降压 |
| VDD_LOGIC | <2A | ±5% | DC-DC单独供电 |
| VDD_CPU | <2A | ±5% | DC-DC单独供电，支持DVFS |
| VDD_NPU | <3A | ±5% | DC-DC单独供电，支持DVFS |
| DDR_VDDQ | <1A | ±5% | DC-DC独立供电 |
| DDR_VDDQL | <100mA | ±5% | LPDDR4X为0.6V |
| AUDIO_ADC_AVDD_1V8 | <20mA | <50mV | 建议预留0R电阻隔离 |
| USB_AVDD_0V9_0 | <50mA | <20mV | 第一次上电必须供电 |
| USB_AVDD_1V8_0 | <80mA | <50mV | |
| MIPI_AVDD_0V9 | <10~30mA | <20mV | |
| MIPI_AVDD_1V8 | <5~10mA | <50mV | |

**PMU电源:** 支持两种供电方式二选一
- 方案一: PMUIO_3V3输入3.3V，经内部LDO生成0.9V (成本低，效率低)
- 方案二: PMUIO_VDD0V9输入0.9V (效率高，成本高)

**待机模式电源需求:**
- 普通待机: 仅PMUIO_3V3、PMUIO0_VCC3V3供电
- AOV模式: PMUIO_3V3、PMUIO0_VCC3V3、RTC_AVDD、VCC_DDR供电
- Pre-recording: PMUIO_3V3、PMUIO0_VCC3V3、RTC_AVDD、PMUIO1_VCC供电

---

### 2.3. 功能接口设计

#### 2.3.1. FSPI1接口
- FSPI1不支持引导启动
- FSPI1接口匹配: D[3:0]/CSN直连 (内部上拉), CLK串联22Ω (内部下拉)

#### 2.3.2. SPI2AHB接口
- 直连，串联22Ω电阻

#### 2.3.3. SDMMC接口
**SDMMC0:**
- 支持SD3.0，最高SDR104 (208MHz)
- SD3.0模式需VCCIO2=3.3V，VCCIO_SD=1.8V供电切换
- CLK串联22Ω，CMD/DQ[3:0]直连（需外部上拉）
- SD卡座CD/DET管脚需上拉到PMUIO0_VCC3V3（常开卡座）
- DET信号建议加1nF电容

**SDMMC1:**
- 支持SDIO3.0，CLK最高208MHz (SDR104)
- CLK串联22Ω，CMD直连

#### 2.3.4. SARADC接口
- SARADC0: 8通道，IN0~IN7，输入范围0~1.8V
- SARADC0_IN7为BOOT配置专用引脚
- SARADC1/2: 8+8通道，与TSADC共用电源
- 模拟输入建议串接100Ω电阻并加1nF对地电容

#### 2.3.5. USB2/USB3接口
**USB接口汇总:**
- USB2.0 DRD: 支持OTG功能
- USB3.0 DRD: 支持OTG功能
- USB2.0 HOST: 仅支持Host模式

**匹配设计:**
- USB_DP/DM: 预留串接0Ω电阻，预留共模电感位置
- USB_SSTXP/N, SSRXP/N: 串联0.1μF耦合电容 (0201)
- USB_ID: 直连 (内部上拉)
- USB_VBUS: 5V供电检测

**注意事项:**
- USB2.0 DRD/DP/DM建议串接共模电感，提升EMI性能
- USB HOST 5V电源需加限流开关
- ESD器件I/O对地电容不超过0.2pF

#### 2.3.6. 视频输入接口
**MIPI CSI RX:**
- CSI0: 4Lane, 支持MIPI DPHY/LVDS/SubLVDS
- CSI1: 2×2Lane 或 1×4Lane
- 匹配: CLK/DATA串联22Ω，差分对间并联100Ω
- I2C用于sensor配置，MCLK用于提供sensor时钟
- MIPI信号需加上拉电压（1.8V）电源

**DVP (CIF) 接口:**
- 支持BT.601/BT.656/BT.1120
- 最高时钟频率150MHz (DVP模式)，100MHz (BT1120模式)
- 数据线D[15:0]，CLK串联22Ω，控制信号(HSYNC/VSYNC)直连
- PCLK/HSYNC/VSYNC内部下拉

**设计注意事项:**
- 长距离走线建议预留AC耦合电容（串接102电容靠近发送端）
- 接口电平需匹配：Sensor 1.8V / SoC 1.8V

#### 2.3.7. 视频输出接口
**MIPI DSI TX:**
- 支持4Lane，串联22Ω

**LCDC TX接口:**
- 支持RGB/BT1120/BT656/MCU接口
- VCCIO5电源域的IO默认内置上拉，不可配置为下拉
- RGB接口: 时钟与数据时延差≤2ns
- BT1120输出: Y[7:0]/C[7:0]两路8bit数据输出
- 设计时注意RGB/BT656电平（1.8V/3.3V）与VCCIO5保持一致

#### 2.3.8. 音频接口

**SAI数字音频接口:**
- SAI0: 支持1TX+1RX，MCLK/SCLK/LRCK串联22Ω，SDO/SDI直连
- SAI1: 支持1TX+1RX，类似匹配设计
- SAI2: 支持1TX+3RX，可内部连接到Audio DSM/ADC
- 通过连接器板对板连接时，建议串接22~100Ω并预留TVS

**PDM数字音频接口:**
- 1组8通道PDM接口，支持8CH输入
- PDM_CLK与采样率对照: 3.072MHz→48kHz; 2.8224MHz→44.1kHz; 2.048MHz→16kHz
- 提供CLK0和CLK1两个同源同相时钟
- CLK串联22Ω，SDI直连

**DSM音频接口:**
- 两对差分输出（立体声）
- 输出需接RC低通滤波电路，不得删除
- 差分输出不能拆成2路单端使用
- SAI2_SDO内部连接到DSM模块，两者不能同时使用

**AUDIO ADC音频接口:**
- 内置2个AUDIO ADC，支持差分MIC输入
- 差分输入不能拆成两路单端输入
- MIC输入耦合电容推荐1μF或以上，靠近SoC放置
- VCM外接对地2.2μF电容，VREF外接对地2.2μF电容（不得更改）
- 需预留偏置电压RC滤波: 100Ω + 4.7μF

#### 2.3.9. GMAC接口
- 支持10/100/1000Mbps RGMII，10/100Mbps RMII
- GMAC_M0: VCCIO6域; GMAC_M1: VCCIO5域（二选一）
- 建议优先采用1.8V电平
- TXD/TXCLK/TXCTL预留串接0Ω; RXD/RXCLK/RXCTL在PHY端串22Ω
- MDIO需外部上拉1.5~1.8kΩ
- PHY Reset需用GPIO控制，靠近PHY加100nF电容
- **8211F/FI复位只支持3.3V电平

#### 2.3.10. FEPHY接口
- 内置百兆以太网PHY，与GMAC_M0/GMAC_M1三选一
- 差分信号TXP/N和RXP/N间并联110Ω端接电阻（靠近SoC）
- 串联5.1Ω电阻（靠近变压器端）
- 变压器中心抽头1nF电容不得修改
- FEPHY_EXTR串接6.49kΩ 1%精密电阻接地
- 支持TX/RX对调，支持组内P/N对调

#### 2.3.11. IRFPA接口
- 支持热成像传感器，7进14出/3进8出/3进7出模式
- 仅支持1.8V工作电平
- VI_CIF_D[15:0]/HSYNC/VSYNC直连（内部下拉），CLKIN串联22Ω

#### 2.3.12. DSMC接口
- DDR串行内存控制器，用于连接PSRAM或FPGA
- 8/16线串行传输，CLKP/N最高100MHz
- DSMC_RDYN需外部上拉4.7kΩ
- CLKP/N预留串接0Ω
- 属于VCCIO5电源域

#### 2.3.13. UART接口
- 8个UART控制器，最高4Mbps
- UART1~7支持RS485自动收发功能
- UART0默认烧录/打印串口

#### 2.3.14. I2C接口
- 6个I2C控制器，最高1Mbit/s，仅支持主模式
- SCL/SDA需外接上拉电阻（推荐2.2~4.7kΩ）
- 总线设备地址不能冲突，上拉电源与GPIO电源域一致

#### 2.3.15. SPI接口
- 2个通用SPI控制器（除2个FSPI外）
- 支持Master/Slave模式
- SPI1_M1最高CLK 50MHz

#### 2.3.16. CAN接口
- 2个CAN控制器，支持CAN FD
- CAN_TX推荐外部接4.7kΩ上拉

#### 2.3.17. PWM接口
- 28个PWM通道（PWM0 8CH, PWM1 4CH, PWM2 8CH, PWM3 8CH）
- 支持捕获模式、波形发生器、红外输入、双相计数器
- 红外接收头待机唤醒只能选择PWM1_CH0~3
- 红外接收头电源需22~100Ω+10μF RC滤波，输出串22Ω+1nF到SoC

---

## 3. PCB设计建议

### 3.1. 通用高速信号布线建议

| # | 规则 | 要求 |
|---|------|------|
| 1 | 走线长度 | 应包含过孔和封装 |
| 2 | 参考平面 | 走线应有完整且连续的参考层平面 |
| 3 | 表贴焊盘阻抗 | 在表贴焊盘正下方挖去一层参考层 |
| 4 | 同层地铜皮间距 | ≥3倍线宽 |
| 5 | 跨区禁止 | 高速信号距离参考平面边沿≥40mil |
| 6 | 测试点 | 不要在高速信号上放置测试点 |
| 7 | 拐角 | 用135度代替90度 |
| 8 | 串接电阻 | 靠近发送端（400mil以内） |
| 9 | IC地焊盘 | 各打1个地通孔 |
| 10 | 非功能焊盘 | 全部移除 |
| 11 | 差分对内等长 | P/N时延差尽可能小，就近绕线补偿 |
| 12 | 换层回流过孔 | 差分对称放置; 单端信号过孔旁放一个 |
| 13 | 差分对走线 | 应对称 |
| 14 | 连接器地焊盘 | 至少1个地通孔，建议2个 |
| 15 | 包地 | 包地线距信号≥3W，地过孔间隔建议≤500mil |
| 16 | 蛇形绕线 | S≥3W |
| 17 | 残桩 | 尽量为零 |
| 18 | 跨电源平面 | 两个电源层分别加对地电容 |

### 3.2. 接口PCB设计建议

#### Power电路PCB设计

| 电源轨 | DCDC过孔数 | 铜皮宽度 | PDN 100k~1MHz | PDN 1M~30MHz | PDN 30M~100MHz |
|--------|-----------|---------|---------------|---------------|----------------|
| VDD_CPU | ≥4(建议≥6) | W1≥200mil, W2≥40mil | ≤0.06Ω | ≤0.08Ω | ≤0.18Ω |
| VDD_LOGIC | ≥4(建议≥6) | W1≥150mil, W2≥40mil | ≤0.06Ω | ≤0.08Ω | ≤0.17Ω |
| VDD_NPU | ≥6(建议≥8) | W1≥200mil, W2≥60mil | ≤0.06Ω | ≤0.08Ω | ≤0.21Ω |
| VCC_DDR | ≥4(建议≥6) | ≥250mil, W≥40mil | - | - | - |
| VCC0V6_DDR | ≥4(建议≥6) | ≥120mil, W≥40mil | - | - | - |

**通用电源布局:**
- DCDC到芯片直流电阻建议≤10mΩ (VCC0V6_DDR≤15mΩ)
- 每个电源Pad配置一个电源过孔
- 电源过孔40mil范围内至少一个GND过孔
- 去耦电容放芯片背面，GND焊盘至少一个GND过孔
- 顶层走"井"字形交叉连接
- 小容值电容(100nF)距电源过孔≤12mil; 1μF距电源过孔≤50mil

#### DDR PCB设计（按类型）

**DDR3/DDR3L / LPDDR3 / DDR4 / LPDDR4 / LPDDR4X 走线要求:**

**通用规则 (DDR3/DDR3L/LPDDR3):**
| 参数 | DDR3/DDR3L | LPDDR3 |
|------|-------------|--------|
| 单端阻抗 | 50Ω ±10% | 50Ω ±10% |
| 差分阻抗 | 100Ω ±10% | 100Ω ±10% |
| DQ与DQS等长（同Byte） | ≤100ps | ≤100ps |
| DM与DQS等长（同Byte） | ≤100ps | ≤100ps |
| CS/ODT/CKE/地址/控制与CLK | ≤5ps(CS/ODT/CKE) ≤200ps(其他) | ≤5ps(地址/控制) |
| DQS_P/N等长 | ≤2ps | ≤2ps |
| CLK_P/N等长 | ≤2ps | ≤2ps |
| DQS与CLK等长 | ≤250ps | ≤250ps |
| Byte间距 | ≥2W | ≥2W |
| DQ间距 | ≥2W | ≥2W |
| DQ与DQS间距 | ≥3W(建议) | ≥3W(建议) |
| CLK与其他信号间距 | ≥3W(建议) | ≥3W(建议) |

**DDR4:** LPDR4_DQS_P/N等长≤1ps; CLK_P/N等长≤1ps; DQS与CLK等长≤230ps

**LPDDR4 / LPDDR4X:**
- DQ与DQS延时≤50ps; DM与DQS延时≤50ps; 地址/控制线与CLK≤50ps
- DQS_P/N≤1ps; CLK_P/N≤1ps; DQS与CLK≤200ps

#### MIPI TX/RX PCB设计
| 参数 | 要求 |
|------|------|
| 差分阻抗 | 100Ω ±10% |
| 对内时延差 | <2ps |
| 数据与时钟差分对时延差 | <6ps |
| 差分对间距 | ≥3W |
| 走线长度 | <6 inches |
| 过孔数量 | ≤4个 |

#### USB3.0 PCB设计
| 参数 | 要求 |
|------|------|
| 差分阻抗 | 90Ω ±10% |
| 对内时延差 | <1ps |
| 走线长度 | Host<6", Device/OTG<5" |
| 差分对间距 | ≥4倍USB线宽 |
| 过孔数量 | ≤2个 |
| 耦合电容 | 100nF ±20%, 0201封装 |
| ESD电容 | I/O对地≤0.2pF |

#### USB2.0 PCB设计
| 参数 | 要求 |
|------|------|
| 差分阻抗 | 90Ω ±10% |
| 对内时延差 | <3ps |
| 走线长度 | <6 inches |
| 过孔数量 | ≤4个（不超过6个） |
| 与其他信号间距 | 3W |

#### FEPHY PCB设计
| 参数 | 要求 |
|------|------|
| 差分阻抗 | 100Ω ±10% |
| 对内时延差 | <3ps |
| 走线长度 | <24 inches |
| 过孔数量 | <2个 |

#### DSMC PCB设计
- 单端50Ω ±10%，差分100Ω ±10%
- 分支长度: L2<500mil, L3<500mil, L4<1000mil, L5<100mil
- 总长: L1+Lx<5 inches
- CLK_P/N时延差<1ps; CLK与CS时延差<16ps; CLK与DQS时延差<16ps

#### eMMC PCB设计
- 单端50Ω ±10%; 时钟与数据时延差<20ps; 走线<3 inches; 建议过孔≤2个

#### RGMII PCB设计
- 单端50Ω ±10%; TXD/TXEN与TXCLK时延差<20ps; 走线<6 inches; 建议过孔≤2个

#### RMII / SDMMC / FSPI PCB设计
- 单端50Ω ±10%; 时钟与数据时延差<20~33ps
- RMII走线<6 inches; SDMMC走线<4~6 inches; FSPI走线<4 inches
- 建议过孔≤2个

#### LCDC/BT1120/BT656/MCU PCB设计
- 单端50Ω ±10%; 时钟与数据时延差<30ps; 走线<5 inches; 建议过孔≤4个

#### SAI / SPI PCB设计
- 单端50Ω ±10%; 时钟与数据时延差<50ps; 走线<6 inches; 建议过孔≤4个

---

## 4. 热设计建议

**温度控制策略 (Linux Thermal Framework):**
- Power_allocator: PID控制，动态分配功率，转频率限制（默认）
- Step_wise: 逐级限制频率
- Fair share: 频率档位多的优先降频
- Userspace: 不限制频率

**工作状态:**
- 温度上升超阈值: 允许最高频率降低
- 温度下降超阈值: 允许最高频率升高
- 温度低于阈值: 频率为默认值
- 降频后仍过温: 软件触发重启

**PCB板级热设计:**
- 空旷区域增加地过孔（不破坏电源平面完整性）
- 注意LDO输入输出压差，提高电源效率
- 大电流走线/铺铜考虑载流能力
- e-PAD打满过孔
- 合理结构设计，考虑热交换途径

---

## 5. ESD/EMI防护设计建议

**ESD防护:**
- 保证合理模具设计，端口和插接件预留抗ESD器件
- PCB布局做好敏感器件保护隔离
- RV1126B放在PCB中间；不能放中间屏蔽罩离板边≥2mm且可靠接地
- 按功能模块及信号流向布局，敏感部分相互独立
- ESD器件摆在源头（接口处或静电释放处）
- 元件布局远离板边且距插接件一定距离
- PCB表面有良好GND回路，各接插件表层有良好GND连接
- 表层板边不走线且多打地孔
- 多露铜加强静电释放效果

**EMI防护:**
- 处理干扰源和耦合通道
- 常用方法: 滤波、接地、平衡、阻抗控制、端接
- 常用材料: 屏蔽罩、滤波器、电阻、电容、电感、磁珠、共模电感、吸波材料
- 滤波器选择: 高阻抗负载→容性滤波并联; 低阻抗负载→感性滤波串联
- 差分接口一般用共模电感抑制EMI
- 差分线做好等长及紧密耦合，保证对称性
- 带金属壳器件避免耦合干扰信号
- 散热器需考虑EMI要求，预留接地条件

---

## 6. 焊接工艺说明

**焊膏要求:**
- 推荐SAC305锡膏，flux比重10%~11.5%
- 锡膏冷藏温度2~10℃，使用前回温3~4小时
- 推荐Type 4
- 手工搅拌3~5分钟或机械搅拌3分钟

**推荐SMT回流焊曲线:**
| 阶段 | 参数 |
|------|------|
| 预热区温升斜率 | 1~2℃/s |
| 恒温(150~180℃) | 60~90s |
| 回流(220℃以上) | 55~70s |
| 峰值温度 | 245±5℃ |
| 峰值时间 | 15~30s |
| 冷却斜率 | ≤3℃/s |

---

## 7. 包装和存放条件

**存放环境:**
- 真空包装，温度≤40℃，相对湿度<90%，保存期限12个月

**MSL等级: 3 (暴露时间168小时)**
| MSL等级 | 暴露时间 (≤30℃/60%RH) |
|---------|----------------------|
| 1 | 无限 (≤30℃/85%RH) |
| 2 | 1年 |
| 2a | 4周 |
| 3 | 168小时 |
| 4 | 72小时 |
| 5 | 48小时 |
| 5a | 24小时 |

**烘烤要求:**
- 条件: 湿度指示卡>10%变色，或未符合规范
- 125℃烘烤: 超过时效>72h需9h, ≤72h需7h
- 90℃烘烤: 超过时效>72h需33h, ≤72h需23h
- 40℃烘烤: 超过时效>72h需13天, ≤72h需9天
- 优先选择低温烘烤

---

*此文档由RV1126B Hardware Design Guide V1.0 (20250828) 自动生成*
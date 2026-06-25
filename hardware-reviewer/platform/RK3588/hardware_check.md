# RK3588 硬件设计检查规则

> 参考文档：Rockchip RK3588 硬件设计指南 V1.3 (2023-02-13)（瑞芯微官方）
> 章节结构：第2章 原理图设计建议 + 第3章 PCB设计建议 + 第4章 热设计 + 第5章 ESD/EMI + 第6章 焊接 + 第7章 包装
> 本文提取全部关键设计参数供原理图审查使用
>
> ⛔ **引脚电平参考**：接口引脚的 GPIO→VCCIO 域映射以 `pinout.md`（RK3588_PinOut_V1.1_20220922.xlsx 官方表导出）为权威来源。禁止按 GPIO Bank 编号一刀切映射 VCCIO 域，必须查该表逐子 Bank 确认。

> ⛔ **G0 前置依赖**：本文是 RK3588 芯片的规则参考，不替代 G0 手册门禁。对于非 RK3588 的 IC（如 RK806-1 / RK860 / 电平转换器 / DDR 颗粒等），仍需通过 `hardware-reviewer.md` 中定义的 Step 0（G0 手册搜索）获取各自的官方数据手册。本规则中的参数值（如 DDR ZQ 240Ω、eMMC CMD 10kΩ 上拉）虽为官方设计指南参数，但若实际设计中使用不同型号的 DDR 颗粒或 PMIC，必须以其原厂手册为准。

---

## 一、VCCIO 域定义

RK3588 共有 9 个 GPIO/IO 供电域，每个域供电给不同的 GPIO Bank 子集。**VCCIO 编号与 GPIO Bank 编号不是一一对应关系**，必须逐子 Bank 查表。

| 域 | 电压 | 类型 | 承载接口 |
|---|:---:|------|------|
| **PMUIO1** | 1.8V 固定 | PMU IO | GPIO0_A, GPIO0_B[0:4], JTAG/UART Debug (M1), REFCLK_OUT, 32K时钟, NPOR复位 |
| **PMUIO2** | 1.8V/3.3V 自识别 | PMU IO | GPIO0_B[5:7], GPIO0_C, GPIO0_D, PCIe控制信号, AVS信号, UART0_M0 |
| **EMMCIO_1V8** | 1.8V 固定 | eMMC 专用IO | GPIO2_A[0:3], GPIO2_D[0:7], FSPI_M0 (与eMMC复用) |
| **VCCIO1** | 1.8V 固定 | GPIO IO | GPIO1_C, GPIO1_D[0:5] |
| **VCCIO2** | 1.8V/3.3V 自识别 | GPIO IO | GPIO4_D[0:5], SDMMC, JTAG_M1, CAN0_M1 |
| **VCCIO3** | 1.8V 固定 | GPIO IO | GPIO2_A[6:7], GPIO2_B, GPIO2_C[0:5], GPIO4_C[2:6], GMAC0 |
| **VCCIO4** | 1.8V/3.3V 自识别 | GPIO IO | GPIO1_A, GPIO1_B[0:5], GPIO1_D[6:7], PCIe3.0控制信号, MIPI CAM CLK |
| **VCCIO5** | 1.8V/3.3V 自识别 | GPIO IO | GPIO3_A/B/C/D, GMAC1, SDIO_M1, PCIe控制信号, CIF |
| **VCCIO6** | 1.8V/3.3V 自识别 | GPIO IO | GPIO4_A, GPIO4_B[0:5], GPIO4_C[0:1], CIF/BT1120, PCIe控制信号 |

> **供电引脚说明**：可调域（PMUIO2, VCCIO2/4/5/6）均有一对供电引脚 —— `{DOMAIN}` 主供电（1.8V/3.3V）和 `{DOMAIN}_1V8`（1.8V 固定，给内部1.8V电路使用）。二者必须同时上电。

---

## 二、GPIO Bank → VCCIO 域映射表

> **来源：RK3588 官方 PinOut 表 V1.1（2022-09-22），本表为权威来源。**
> 当任何工具或脚本的 `gpio_bank_map` 与本表冲突时，以本表为准。

### 2.1 精确映射表

| GPIO 子 Bank | VCCIO 域 | 电压 | 关键说明 |
|---|---|---|---|
| GPIO0_A[0:7] | PMUIO1 | 1.8V fixed | |
| GPIO0_B[0:4] | PMUIO1 | 1.8V fixed | |
| GPIO0_B[5:7] | PMUIO2 | 1.8V/3.3V | **同Bank跨域分离点** |
| GPIO0_C[0:7] | PMUIO2 | 1.8V/3.3V | |
| GPIO0_D[0:7] | PMUIO2 | 1.8V/3.3V | |
| GPIO1_A[0:7] | **VCCIO4** | 1.8V/3.3V | ⚠️ 不在 VCCIO1 |
| GPIO1_B[0:5] | **VCCIO4** | 1.8V/3.3V | ⚠️ 不在 VCCIO1 |
| GPIO1_C[0:7] | VCCIO1 | 1.8V fixed | |
| GPIO1_D[0:5] | VCCIO1 | 1.8V fixed | |
| GPIO1_D[6:7] | VCCIO4 | 1.8V/3.3V | **同Bank跨域分离点** |
| GPIO2_A[0:3] | **EMMCIO_1V8** | 1.8V fixed | ⚠️ 不在 VCCIO2 |
| GPIO2_A[6:7] | VCCIO3 | 1.8V fixed | **同Bank跨域分离点** |
| GPIO2_B[0:7] | VCCIO3 | 1.8V fixed | |
| GPIO2_C[0:5] | VCCIO3 | 1.8V fixed | |
| GPIO2_D[0:7] | **EMMCIO_1V8** | 1.8V fixed | ⚠️ 不在 VCCIO2 |
| GPIO3_A[0:7] | VCCIO5 | 1.8V/3.3V | |
| GPIO3_B[0:7] | VCCIO5 | 1.8V/3.3V | |
| GPIO3_C[0:7] | VCCIO5 | 1.8V/3.3V | |
| GPIO3_D[0:7] | VCCIO5 | 1.8V/3.3V | |
| GPIO4_A[0:7] | VCCIO6 | 1.8V/3.3V | |
| GPIO4_B[0:5] | VCCIO6 | 1.8V/3.3V | |
| GPIO4_C[0:1] | VCCIO6 | 1.8V/3.3V | |
| GPIO4_C[2:6] | VCCIO3 | 1.8V fixed | **同Bank跨域分离点** |
| GPIO4_D[0:5] | VCCIO2 | 1.8V/3.3V | SDMMC / JTAG 复用 |

### 2.2 关键例外（必须逐子 Bank 匹配）

| 子 Bank | 错误映射（按编号一刀切） | 正确映射（PinOut 表） |
|---|---|---|
| GPIO1_A[0:7], GPIO1_B[0:5] | ❌ VCCIO1 | ✅ **VCCIO4** |
| GPIO2_A[0:3] | ❌ VCCIO2 | ✅ **EMMCIO_1V8** |
| GPIO2_D[0:7] | ❌ VCCIO2 | ✅ **EMMCIO_1V8** |
| GPIO4_D[0:5] | ❌ VCCIO3 | ✅ **VCCIO2** |

### 2.3 域汇总速查

| 域 | 包含 GPIO | 总GPIO数 |
|---|---|---|
| PMUIO1 | GPIO0_A[0:7], GPIO0_B[0:4] | 13 |
| PMUIO2 | GPIO0_B[5:7], GPIO0_C[0:7], GPIO0_D[0:7] | 19 |
| EMMCIO_1V8 | GPIO2_A[0:3], GPIO2_D[0:7] | 12 |
| VCCIO1 | GPIO1_C[0:7], GPIO1_D[0:5] | 14 |
| VCCIO2 | GPIO4_D[0:5] | 6 |
| VCCIO3 | GPIO2_A[6:7], GPIO2_B[0:7], GPIO2_C[0:5], GPIO4_C[2:6] | 21 |
| VCCIO4 | GPIO1_A[0:7], GPIO1_B[0:5], GPIO1_D[6:7] | 17 |
| VCCIO5 | GPIO3_A[0:7], GPIO3_B[0:7], GPIO3_C[0:7], GPIO3_D[0:7] | 32 |
| VCCIO6 | GPIO4_A[0:7], GPIO4_B[0:5], GPIO4_C[0:1] | 16 |

---

## 三、检查规则

### 3.1 反向供电校验（强制）

每分配一个信号到某 VCCIO 域后，必须执行反向校验：

1. **正向分配**：`GPIO{Bank}_{Port}{Pin}` → 查本文件 §2.1 映射表 → 得 `VCCIO_domain` 和预期电压
2. **反向追踪**：查 U6 (RK3588) 该 VCCIO 域的供电引脚（如 `U6.VCCIO4`, `U6.EMMCIO_1V8`）→ 追踪其物理网络名称 → 查电源树得实际电压
3. **交叉比对**：正向分配的域电压 vs 反向追踪的供电引脚实际电压
4. **不一致 → WARNING**，阻止继续
5. 如映射表无匹配 → 标记为 `INFERRED`，电压从供电引脚反向追踪

### 3.2 GPIO 子 Bank 精度规则

- **禁止**按 GPIO Bank 编号一刀切映射 VCCIO 域
- **必须**使用 §2.1 映射表逐子 Bank 匹配
- 同一 Bank 内存在跨域分离（如 GPIO0_B 跨 PMUIO1/PMUIO2, GPIO1_D 跨 VCCIO1/VCCIO4, GPIO2_A 跨 EMMCIO/VCCIO3）
- 对每个 GPIO 引脚，必须匹配到子 Bank 级别（`GPIO{Bank}_{Port}[range]`）

### 3.3 PinOut 表为权威来源

- 当任何 `gpio_bank_map` 脚本或工具与本文件 §2.1 映射表冲突时，以本表（PinOut 表）为准
- 本表数据源：RK3588_PinOut_V1.1_20220922.xlsx，逐Pin解析

### 3.4 信号分配 I/O 方向校验

- 确认信号方向与 GPIO 默认 I/O 方向兼容
- eMMC 域 GPIO 默认上拉（D0-D7/A0）或下拉（A1-A3），见 PinOut 表
- SDMMC 域 GPIO4_D 默认上拉（D0-D2/D3-u/D4）或下拉（D5），见 PinOut 表

---

## 四、时钟电路

- 24MHz 晶体：CL ≤12pF，频偏 ≤20ppm
- XOUT24M 串 22Ω 限流电阻，XOUT/XIN 间 510kΩ 并联电阻不可随意修改
- 负载电容材质 COG/NPO，推荐贴片 4Pin 晶体
- 32.768KHz：频率偏差 ±30ppm，幅度 0.7×VDD~VDD（VDD=PMUIO1），占空比 45%~55%
- IOMUX 必须设为 CLK32K_IN 功能，输入幅度必须满足 PMUIO1 域供电要求
- REFCLK_OUT 可输出时钟（频率可配）
- CLK32K_OUT0/1 可提供给 WIFI/BT/PCIe 等设备当休眠或工作时钟
- MIPI_CAMERA0_CLK~MIPI_CAMERA4_CLK：默认 24MHz 输出
- ETH0/1_REFCLKO_25M：25MHz 时钟输出给 Ethernet PHY
- 时钟 IO 电平必须与外设匹配，否则加电平转换

---

## 五、复位/看门狗

- NPOR (Pin M31) 低有效，最短 4μs（100 个 24MHz 周期），需 100nF 去抖电容
- RESET_L 上拉电源 = PMUIO1_1V8
- TSADC_SHUT 输出硬件复位（芯片内部 7 个 TSADC 模块，超温时输出低电平）
- RK806-1 RESETB 上电完成后释放低电平（开漏输出）
- 看门狗：RK3588 内部集成 Watchdog Timer

---

## 六、系统启动

- 引导源：FSPI0/FSPI1/eMMC/UFS/SDMMC0/USB2.0/USB3.2
- SARADC_IN0_BOOT (Pin AM16) 多种 Config 模式，专用引脚不可他用
- SDMMC_DET (Pin P31)：复用为 SDMMC 卡检测
- 不支持 PCIe BOOT

---

## 七、JTAG / UART Debug

- SWD 两线模式（ARM JTAG）
- JTAG_M1 (PMUIO1, 与 UART2_M1 复用，推荐预留)
- JTAG_M0 (VCCIO2, 与 SDMMC 复用)
- **JTAG_TCK/TMS 串 100Ω + TVS**
- UART2_M0 (PMUIO2) 为 Debug UART
- **UART2_RX/TX 串 100Ω + TVS**
- IO 电平必须匹配

---

## 八、DDR 电路

### 8.1 控制器

RK3588 支持 LPDDR4/LPDDR4X/LPDDR5，2 通道 × 32bit（每通道 2×16bit 子通道），最大 32GB

### 8.2 DDR PHY I/O Map

RK3588 DDR PHY I/O Map 详见设计指南表 2-4。**DQ/CA 顺序全部不支持对调。**点对点拓扑，全部 ODT 终端。

### 8.3 ZQ（每颗必须检查）

| 对象 | 连接 | 电阻 |
|------|------|:---:|
| RK3588 DDR PHY ZQ | → VDDQ_DDR_S0 | 240Ω ±1% |
| LPDDR4/4X/5 颗粒 ZQ | → VDDQ_DDR_S0 | 240Ω ±1% |
| LPDDR4/4X ODT_CA | → VDD2_DDR_S3 | 10kΩ ±5% |

### 8.4 供电电压

#### SOC 端（RK3588 DDR PHY）

| 电源 | LPDDR4/4X | LPDDR5 |
|------|:---:|:---:|
| DDR_CHx_VDD | 0.75V | 0.75V |
| DDR_CHx_VDD_MIF | 0.75V | 0.75V |
| DDR_CHx_VDDQ | 0.6V | 0.5V |
| DDR_CHx_VDDQ_CK | 0.6V | 0.5V |
| DDR_CHx_VDDQ_CKE | 1.1V | 1.05V |
| DDR_CHx_PLL_DVDD | 0.75V~0.85V | 0.75V~0.85V |
| DDR_CHx_PLL_AVDD1V8 | 1.8V | 1.8V |

#### DRAM 颗粒端

| 电源 | LPDDR4 | LPDDR4X | LPDDR5 |
|------|:---:|:---:|:---:|
| VDD1 | 1.8V | 1.8V | 1.8V |
| VDD2 | 1.1V | 1.1V | — |
| VDD2H | — | — | 1.05V |
| VDD2L | — | — | 0.9V |
| VDDQ | 1.1V | **0.6V** | 0.5V |

### 8.5 PMIC 设置

RK806-1 BUCK6/BUCK9 分压电阻必须根据颗粒 VDDQ/VDD2 调整（详见设计指南图 2-16/2-17）

### 8.6 上电时序

SOC 端：DDR_CH_VDD / DDR_VDD_MIF → DDR_CH_VDDQ_CKE → DDR_VDDQ
DRAM 颗粒上电时序请参考各 JEDEC 标准

---

## 九、eMMC 电路

### 9.1 接口设计（设计指南表 2-5）

| 信号 | 外部电路 |
|------|------|
| EMMC_D[7:0] | D0 预留 10kΩ 上拉 |
| EMMC_CLKOUT | RK3588 端串 0Ω；颗粒端预留 10pF→GND (V1.3 修正) |
| EMMC_CMD | **必须**外部 10kΩ 上拉 |
| EMMC_DATA_STROBE | 颗粒端串 0Ω；预留 47kΩ 下拉 |
| EMMC_RSTN | RK3588 端串 0Ω+上拉；颗粒端 100nF→GND |

- 支持 HS400ES/HS400/HS200/DDR50
- **EMMCIO_1V8 域（1.8V 固定）**，与 FSPI0_M0 复用
- GPIO 充足时 RSTN 须接颗粒 RST_n

---

## 十、FSPI Flash 电路

- 与 eMMC 复用 EMMCIO_1V8 域引脚（FSPI_M0）
- FSPI_M1/M2 在其他域（VCCIO3/VCCIO5）
- 接口设计参考设计指南表 2-6

---

## 十一、PCIe 参数

### 11.1 控制器

RK3588 共 5 个 PCIe 控制器 + 5 个 PHY：
- 2× PCIe3.0 PHY（支持 ×4/×2/×1 + ×2/×1/×1）
- 3× PCIe2.0/SATA3.0/USB3.0 Combo PHY

### 11.2 PCIe3.0

| 参数 | 值 |
|------|------|
| AC 耦合电容 | **220nF**（推荐 0201 封装） |
| RESREF | **200Ω ±1%** 到 GND，靠近 RK3588 引脚 |
| PERSTn | 0Ω 串联，标准 PCIe Slot 用 3.3V 电平 |
| NPOR_u 去抖 | ≥100nF 到 GND (Pin M31) |
| RESET_L 上拉 | PMUIO1_1V8 域 |

### 11.3 PCIe2.0

| 参数 | 值 |
|------|------|
| AC 耦合电容 | **100nF**（推荐 0201 封装） |
| PERSTn | 0Ω 串联，3.3V 电平 |

### 11.4 PCIe 控制信号域分布

| 域 | PCIe 控制信号 |
|------|------|
| PMUIO2 | PCIE30X1_0/1_CLKREQN_M0, WAKEN_M0, PERSTN_M0, PCIE30X4_CLKREQN_M0 |
| VCCIO4 | PCIE30X1_0/1_CLKREQN_M2, WAKEN_M2, PERSTN_M2, PCIE30X4_CLKREQN_M3, WAKEN_M3, PERSTN_M3, PCIE30X2_CLKREQN_M3 |
| VCCIO5 | PCIE30X4_CLKREQN_M2, WAKEN_M2, PERSTN_M2, PCIE30X2_CLKREQN_M2, WAKEN_M2, PERSTN_M2, PCIE20X1_2_CLKREQN_M0 |
| VCCIO6 | PCIE30X1_0/1_CLKREQN_M1, WAKEN_M1, PERSTN_M1, PCIE30X2_CLKREQN_M1, WAKEN_M1, PERSTN_M1, PCIE20X1_2_CLKREQN_M1 |

---

## 十二、PMIC 供电

### 12.1 PMIC 型号与架构

| 元件 | 型号 | 用途 |
|------|------|------|
| 主 PMIC | **RK806-1** (单 PMIC 方案) | 大部分电源轨 |
| 外部 DCDC U1 | **RK860-2** (I2C 42H) | NPU 供电 |
| 外部 DCDC U5 | **RK860-3** (I2C 43H) | Big CPU0 供电 |
| 外部 DCDC U13 | **RK860-2** (I2C 42H) | Big CPU1 供电 |

### 12.2 RK860 参数

| 参数 | 值 |
|------|------|
| VIN | 2.7V ~ 5.5V |
| VOUT | 0.5V ~ 1.5V（默认 0.8V，步进 6.25mV） |
| IOUT max | 7A (V1.3) / 6A (V1.2) |
| Fsw | 2.4MHz |
| L | 0.22μH ~ 0.47μH |
| CIN/COUT | >10μF / 44μF ~ 88μF |
| 封装 | WLCSP-20 (1.65mm × 2.05mm, pitch 0.4mm) |

### 12.3 RK806-1 BUCK/LDO 参数

| BUCK | 最大电流 | L | CIN | COUT | Fsw |
|------|:---:|------|------|------|:---:|
| BUCK1 | 6.5A | 0.22μH | 22μF | 66μF | 2MHz |
| BUCK2/3/4 | 5A | 0.22μH | 22μF | 66μF | 2MHz |
| BUCK5/6/7/8/9/10 | 3A | 0.47μH | 10μF | 44μF | 2MHz |

| LDO | 电流 | COUT |
|------|:---:|------|
| PLDO1/4 | 500mA | ≥1μF |
| PLDO 其他 | 300mA | ≥1μF |
| NLDO3/4 | 500mA | ≥2.2μF |
| NLDO 其他 | 300mA | ≥2.2μF |

### 12.4 上电时序

RK806-1 Slot 1-6 上电时序为固化的默认电压和时序，详见设计指南图 2-64/2-65。

整体上电序列：
PMU_0V75 / PLL_DVDD_0V75 → VDD_LOGIC → VDD_BIG0/1 / VDD_GPU / VDD_NPU / VDD_VDENC → VDD_BIG0/1_MEM / VDD_GPU_MEM / VDD_NPU_MEM / VDD_VDENC_MEM → RESETn（最后一路稳定后 ≥1ms）

---

## 十三、通用接口规则

### SDMMC：SDMMC0 (VCCIO2)，支持 SD Card
### SDIO：SDIO_M0 (VCCIO3), SDIO_M1 (VCCIO5)
### SPI：支持 FSPI（Octal），SPI0~SPI4 共 5 组
### I2C：支持 I2C0~I2C8 共 9 组，上拉 2.2k~4.7kΩ；RK3588 支持 I3C 兼容
### UART：支持 UART0~UART9 共 10 组，支持流控和 RS485 自动收发
### CAN：支持 CAN0~CAN2 共 3 组
### GMAC：GMAC0 (RGMII/RMII, VCCIO3), GMAC1 (RGMII/RMII, VCCIO5)
### SATA：3 路 SATA3.0（与 PCIe2.0 Combo PHY 复用）
### USB：2× USB3.0/DP1.4 Combo PHY + 2× USB2.0 HOST + 2× USB2.0 OTG (Type-C)
### HDMI RX：HDMI2.0 RX
### HDMI/eDP TX：2× HDMI2.1/eDP Combo PHY，TX AC 耦合
### DP：DP0/DP1 (与 USB3 Combo PHY)，TX AC 耦合
### MIPI CSI：CSI0/1 (DPHY RX) + D/C-PHY0/1 (Combo RX)
### MIPI DSI：D/C-PHY0/1 (Combo TX)
### Audio：I2S0/1/2/3 + PDM0/1 + SPDIF0/1_TX + DSM PWM Audio

---

## 十四、PCB 设计

- 推荐 10 层 1 阶/2 阶 HDI 或 8 层 PTH 板
- 时钟串阻近源端，TX 串阻近源端，RX 串阻近接收端
- ESD/耦合电容近连接器
- DDR 各电源域独立 PDN + 背面去耦 + 回流地孔
- BGA 焊盘区域挖参考层（8GT/s 及以上信号）
- PCIe3.0 / HDMI2.1 / DP1.4 等 8GT/s+ 信号：避免玻纤编织效应（10° 或 zigzag 走线）
- 各接口独立 PCB 规范（见设计指南第 3.4 节）

---

## 十五、检查优先级

| 优先级 | 检查项 |
|:---:|------|
| **P0** | **VCCIO 域映射**：逐子 Bank 匹配，禁止按编号一刀切 |
| **P0** | **反向供电校验**：正向分配域 vs 反向追踪供电引脚电压 |
| **P0** | DDR PHY I/O Map 引脚分配 |
| **P0** | DDR ZQ 电阻连接 240Ω ±1% |
| **P0** | DDR 电源电压 |
| **P0** | eMMC CMD 上拉 10kΩ |
| **P0** | NPOR 复位 100nF |
| **P0** | SARADC_IN0_BOOT 配置 |
| **P0** | PCIe3.0 RESREF 200Ω ±1% |
| **P1** | DDR CA 顺序不可对调 |
| **P1** | PMIC RK806-1 FB6/FB9 匹配 |
| **P1** | eMMC STRB 下拉 47kΩ |
| **P1** | JTAG/UART 100Ω 串阻 |
| **P1** | GPIO 子 Bank 跨域分离点校验（GPIO0_B, GPIO1_D, GPIO2_A, GPIO4_C） |
| **P2** | 时钟输出电平匹配 |
| **P2** | PCIe AC 耦合电容值（3.0: 220nF, 2.0: 100nF） |
| **P2** | 各接口 PCB Layout |

---

## 附录 A：PinOut 表 GPIO 域总览

| 引脚 | 域 |
|---|---|
| GPIO0_A[0:7], GPIO0_B[0:4] | PMUIO1 (1.8V) |
| GPIO0_B[5:7], GPIO0_C[0:7], GPIO0_D[0:7] | PMUIO2 (1.8V/3.3V) |
| GPIO2_A[0:3], GPIO2_D[0:7] | **EMMCIO_1V8** (1.8V) |
| GPIO1_C[0:7], GPIO1_D[0:5] | VCCIO1 (1.8V) |
| GPIO4_D[0:5] | VCCIO2 (1.8V/3.3V) |
| GPIO2_A[6:7], GPIO2_B[0:7], GPIO2_C[0:5], GPIO4_C[2:6] | VCCIO3 (1.8V) |
| GPIO1_A[0:7], GPIO1_B[0:5], GPIO1_D[6:7] | VCCIO4 (1.8V/3.3V) |
| GPIO3_A/B/C/D (全部) | VCCIO5 (1.8V/3.3V) |
| GPIO4_A[0:7], GPIO4_B[0:5], GPIO4_C[0:1] | VCCIO6 (1.8V/3.3V) |

---

> **数据来源**：RK3588_PinOut_V1.1_20220922.xlsx + Rockchip RK3588 硬件设计指南 V1.3

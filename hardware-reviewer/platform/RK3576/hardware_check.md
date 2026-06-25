# RK3576 硬件设计检查规则

> 参考文档：RK3576_Hardware_Design_Guide_V1.1_20240528_CN.pdf（242页，瑞芯微官方）
> 章节结构：第2章 原理图设计建议 + 第3章 PCB设计建议 + 第4章 热设计 + 第5章 ESD/EMI + 第6章 焊接 + 第7章 包装
> 本文提取全部关键设计参数供原理图审查使用
>
> ⛔ **引脚电平参考**：接口引脚的 GPIO→VCCIO 域映射以 `pinout.md`（RK3576_PinOut_V1.0_20240302.xlsx 官方表导出）为权威来源。禁止按 GPIO Bank 编号一刀切映射 VCCIO 域，必须查该表逐子 Bank 确认。

> ⛔ **G0 前置依赖（2026-06-05 新增）**：本文是 RK3576 芯片的规则参考，不替代 G0 手册门禁。对于非 RK3576 的 IC（如 MP2975 / MPQ7920 / 电平转换器 / DDR 颗粒等），仍需通过 `hardware-reviewer.md` 中定义的 Step 0（G0 手册搜索）获取各自的官方数据手册。本规则中的参数值（如 DDR ZQ 240Ω、eMMC CMD 10kΩ 上拉）虽为官方设计指南参数，但若实际设计中使用不同型号的 DDR 颗粒或 PMIC，必须以其原厂手册为准。

---

## 1. 时钟电路

- 24MHz 有源晶振：电平 1.35~1.8V，占空比 50%，频偏 ≤20ppm
- R1100 影响占空比，需实测调整
- 32.768KHz：频率 32.768kHz ±30ppm，幅度 0.7×VDD~VDD
- IOMUX 必须设为 CLK32K_IN，开漏 RTC 需关 GPIO 下拉
- REF_CLK_OUT 支持 12/24/25/26/27/37.125/74.25/10/20/40/50/58.5/100MHz
- CAM_CLK_OUT 支持 24MHz(默认)+27/37.125/74.25
- 时钟 IO 电平必须与外设匹配，否则加电平转换

## 2. 复位/看门狗

- NPOR (Pin W28) 低有效，最短 4μs，需 100nF 去抖电容
- RESET_L 上拉电源 = PMUIO0_VCC1V8
- TSADC_CTRL_M0 输出硬件复位
- 外部看门狗需开漏输出型
- RK806S-5 RESETB 上电完成后释放低电平

## 3. 系统启动

- 引导源：FSPI0/FSPI1/eMMC/UFS/SDMMC0/USB2.0/USB3.2
- SARADC_IN0_BOOT (Pin A25) 11 种 Config 模式
- SARADC_IN0_BOOT 专用引脚，不可他用
- RK3576 不支持 PCIe BOOT
- SDMMC0_DETN (Pin U21)：高=JTAG、低=SDMMC0，需 1nF 去抖

## 4. JTAG / UART Debug

- SWD 两线模式
- JTAG_M0(VCCIO1, 与 SDMMC0 复用)
- JTAG_M1(PMUIO1, 与 UART0_M0 复用，推荐预留)
- **JTAG_TCK/TMS 串 100Ω + TVS**
- UART0_M0 默认波特率 1500000 bps
- **UART0_RX/TX 串 100Ω + TVS**
- IO 电平必须匹配

## 5. DDR 电路（关键！）

### 5.1 控制器

支持 LPDDR4/LPDDR4X/LPDDR5，32bit=2×16bit，每通道 8GB，总 16GB

### 5.2 DDR PHY I/O Map（表 2-4，必须严格遵循）

| 球位 | LPDDR4 | LPDDR5 |
|------|------|------|
| W1 | LP4_DQ0_A | LP5_DQ0_A |
| ... | ... | ... |
| 1U5 | LP4_RESET | LP5_RESET |

每个 BGA 球位对应 3 种内存类型的信号名不同。**DQ/CA 顺序全部不支持对调。**

### 5.3 ZQ（每颗必须检查）

| 对象 | 连接 | 电阻 |
|------|------|:---:|
| RK3576 DDR PHY ZQ | → DDRPHY_VDDQ_S0 | 240Ω ±1% |
| LPDDR4X/5 颗粒 ZQ | → DDRPHY_VDDQ_S0 | 240Ω ±1% |
| LPDDR4 颗粒 ZQ | → VDD2_DDR_S3 | 240Ω ±1% |
| LPDDR4/4X ODT_CA | → VDD2_DDR_S3 | — |

> ⚠ **ZQ 电阻 cellRef 陷阱**：OrCAD 库中 ZQ 电阻常被命名为 `RESISTOR5_NC`。
> `_NC` = No-Connect **引脚**（封装有未使用的引脚），**不是 DNP（不焊接）**。
> 只要电阻在 EDN 中有 `portRef` 连接且两端分别连到 ZQ 引脚和 VDDQ 轨，即为正确焊接。
> 禁止仅凭 cellRef 中的 `_NC` 后缀判定为"未焊接"（2026-06-15，教训：FL-24-E-MRF1-A-V10 误判）。

### 5.4 供电电压

| 电源 | LPDDR4/4X | LPDDR5 |
|------|:---:|:---:|
| DDRPHY_VDDQ | 0.61V | 0.51V |
| DDRPHY_CK_VDDQ | 0.61V | 0.51V |
| DDRPHY_CKE_VDDQ | 1.1V | 1.05V |
| DDRPHY_PLL_DVDD | 0.75~0.85V | 0.75~0.85V |
| DDRPHY_AVDD1V8 | 1.8V | 1.8V |
| 颗粒 VDD1 | 1.8V | 1.8V |
| 颗粒 VDD2/VDD2H | 1.1V | 1.05V |
| 颗粒 VDDQ | 1.1V/0.61V | 0.51V |

### 5.5 PMIC 设置

RK806S-5 FB6/FB9 分压电阻必须根据颗粒 VDDQ/VDD2 调整

### 5.6 LPDDR5 特殊信号

- WCK 差分数据时钟（CK 频率的 2× 或 4×）
- RDQS 差分读选通
- CA[6:0] DDR 总线
- 点对点拓扑，全部 ODT

## 6. eMMC 电路

### 6.1 接口设计（表 2-5）

| 信号 | 外部电路 |
|------|------|
| eMMC_D[7:0] | D0 预留 10kΩ 上拉 |
| eMMC_CLK | RK3576 端串 0Ω；颗粒端预留 10pF→GND |
| eMMC_CMD | **必须**外部 10kΩ 上拉 |
| eMMC_STRB | 颗粒端串 0Ω；预留 47kΩ 下拉 |
| eMMC_RST | RK3576 端串 0Ω+上拉；颗粒端 100nF→GND |

- 支持 HS400ES/HS400/HS200/DDR50
- VCCIO0_1V8 域，与 FSPI0 复用
- GPIO 充足时 RST 须接颗粒 RST_n

## 7. 通用接口规则

### I2C：上拉 2.2k~4.7kΩ，RK3576 支持 I3C（兼容）
### SPI：支持 FSPI（Octal）
### UART：RS485 自动收发
### CAN：RK3576 新增 CAN 2.0
### MIPI CSI：CSI1/2(DPHY)+CSI3/4(DPHY)+DCPHY(C-PHY)
### HDMI/eDP：Combo PHY，TX AC 耦合，HPD/CEC/DDC 隔离
### DP：DP1.4+USB3 Combo PHY，TX AC 耦合

## 8. PCB 设计

- 推荐 8 层板
- 时钟串阻近源端，TX 串阻近源端，RX 串阻近接收端
- ESD/耦合电容近连接器
- DDR 各电源域独立 PDN + 背面去耦 + 回流地孔
- 各接口独立 PCB 规范

## 9. 检查优先级

| 优先级 | 检查项 |
|:---:|------|
| **P0** | DDR PHY I/O Map 引脚分配 |
| **P0** | DDR ZQ 电阻连接 240Ω ±1% |
| **P0** | DDR 电源电压 |
| **P0** | eMMC CMD 上拉 10kΩ |
| **P0** | NPOR 复位 100nF |
| **P0** | SARADC_IN0_BOOT 配置 |
| **P1** | DDR CA 顺序不可对调 |
| **P1** | PMIC FB6/FB9 匹配 |
| **P1** | eMMC STRB 下拉 47kΩ |
| **P1** | JTAG/UART 100Ω 串阻 |
| **P2** | 时钟输出电平匹配 |
| **P2** | 各接口 PCB Layout |

# IC 型号 → 数据手册索引

> Agent 自动积累，在 G0 Step 0.2b 优先查此表。命中则跳过本地搜索和在线检索，直接读取手册。
> 每次硬件审查完成后，agent 自动追加新发现的 IC。已存在的跳过。
> 无需人工审核。

---

## 状态定义

| 状态 | 含义 |
|---|---|
| `FOUND (本地)` | 手册在本地 {REFBOOK_DIR} 中找到 |
| `FOUND (在线下载)` | 手册从网络下载到本地（记录来源 URL） |
| `FOUND (learn/ic_index)` | 从自学习索引命中，直接使用已记录路径 |
| `TRULY_MISSING` | 本地无 + 在线 3+ 来源均未找到（不写入此表，仅在 G0 Step 0.5 报告中列出） |

---

## 索引表

| IC 型号 | 手册路径 | 来源 | 下载 URL | 首次项目 | 首次日期 | 最后使用 |
|---|---|---|---|---|---|---|
| RK3576 | D:\Refbook\RK3576.pdf | 本地 | — | V10 | 2026-06-11 | 2026-06-16 |
| RK3588 | D:\Refbook\RK3588 Hardware Design Guide-CN-V1.3-20230213.pdf | 本地 | — | V01 | 2026-05-01 | 2026-05-27 |
| RK806S-5 | D:\Refbook\RK3576参考设计资料\6-开发参考资料\数据手册\核心板元器件\OTHERS\RK806S-5.pdf | 本地 | — | V10 | 2026-06-11 | 2026-06-16 |
| ETA3409 | D:\Refbook\ETA3409-1uH.pdf | 本地 | — | V10 | 2026-06-11 | 2026-06-15 |
| MS4553S | D:\Refbook\MS4553S.pdf | 本地 | — | V10 | 2026-06-11 | 2026-06-16 |
| ETA5055 | D:\Refbook\ETA5055.pdf | 本地 | — | V10 | 2026-06-11 | 2026-06-16 |
| BL8079AG | D:\Refbook\BL8079AG_V1.2_en.pdf | 本地 | — | V10 | 2026-06-11 | 2026-06-16 |
| ETA3417S2F | D:\Refbook\Power\ETA3417S2F.pdf | 在线下载 | https://datasheet.lcsc.com/datasheet/pdf/25ca3a3aec3da812ee50f81920f8d618.pdf | V10 | 2026-06-16 | 2026-06-16 |
| TMI3112H | D:\Refbook\Power\TMI3112H.pdf | 在线下载 | https://uploadcdn.oneyac.com/attachments/files/brand_pdf/tmi/75/18/Toll-TMI3112H.pdf | V10 | 2026-06-16 | 2026-06-16 |
| LPDDR4_200P | D:\Refbook\Memory\FORESEE_LPDDR4_200ball.pdf | 在线下载 | https://dl.radxa.com/rockpi4/docs/hw/datasheets/FORESEE_LPDDR4_200ball_NCLD4CXMAXXXM32_10x14.5_VFBGA_Spec_B1_20170802.pdf | V10 | 2026-06-16 | 2026-06-16 |

---

| MP2975GU | D:\Refbook\MPS\MP2975_r1.3_MPS(1).pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MP87000GMJTH | D:\Refbook\MPS\MP87000-M.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MPQ8626GD | D:\Refbook\MPS\MPQ8626GD-Z.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| SN74AHC1G04DBVT | D:\Refbook\SN74AHC1G04.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| TXS0108ERKSR | D:\Refbook\飞腾6678-DSK\FT-M6678 手册及参考资料V2.6（20200723）\FT-M6678 手册及参考资料V2.6\3. FT-M6678 Hardware\2. FT-M6678DSK_datasheet\TXS0108EPWR.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MT62F2G64D8EK | D:\Refbook\MT62F2G64D8EK_LPDDR5x.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MP1603GTF | D:\Refbook\MPS\MP1603_r1.2_mps.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| NB715GL | D:\Refbook\MPS\NB715 Datasheet R0.8.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MAX811TM4 | D:\Refbook\max811-max812.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MP2015AGG | D:\Refbook\MPS\MP2015A.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MP5990GMA | D:\Refbook\MPS\MP5990GMA.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| PCA9306DCUR | D:\Refbook\飞腾6678-DSK\FT-M6678 手册及参考资料V2.6（20200723）\FT-M6678 手册及参考资料V2.6\3. FT-M6678 Hardware\2. FT-M6678DSK_datasheet\PCA9306DCUT.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| SN74AXC1T45DRLR | D:\Refbook\SN74AXC1T45.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| MPQ7920GRM | D:\Refbook\MPS\MPQ7920GRM-AEC1.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| TPS2116DRLR | D:\Refbook\TPS2116.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| CH348Q | D:\Refbook\CH348Q.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| PRTR5V0U2X-ES | D:\Refbook\PRTR5V0U2X-ES.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| STM32L471QGI6 | D:\Refbook\stm32l471qe.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| INA219BIDCNT | D:\Refbook\飞腾6678-DSK\FT-M6678 手册及参考资料V2.6（20200723）\FT-M6678 手册及参考资料V2.6\3. FT-M6678 Hardware\2. FT-M6678DSK_datasheet\INA219BID.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| SN74HC21PWR | D:\Refbook\SN74HC21.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| OT8EL89CJI | D:\Refbook\OT8EL89CJI.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| TMP102AIDRLR | D:\Refbook\TMP102.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| AT24C256C-SSHL | D:\Refbook\Memory\AT24C256C.pdf | 在线下载 | https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT24C128C-AT24C256C-Data-Sheet-DS20006270.pdf | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| GD55LB02GF | D:\workdoc\23_2025项目\原粒\KS1-CCL4-128-P\主要元器件资料\QSPI\DS-01015-GD55LB02GF-Rev1.0.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| HSC32C1-S1V30 | D:\workdoc\23_2025项目\原粒\KS1-CCL4-128-P\主要元器件资料\EEPROM\HSC32C1产品规格书V1.1_20191024.pdf | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| KS-1 | D:\workdoc\23_2025项目\原粒\KS-1_disign_guide_files\ (部分参考) | 本地 | — | FL-25-A-K402 | 2026-06-18 | 2026-06-18 |
| XPL3233 | D:\Refbook\XPL3233.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| IS6608A-0001 | D:\Refbook\IS6608A-0001.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| M0503DLBGP | D:\Refbook\M0503DLBGP.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| FMP100T8 | D:\Refbook\FMP100型SRAM型现场可编程门阵列技术手册_V2.3.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| SCCH900202113B | D:\Refbook\16Mb_MRAM V1.pdf | MRAM 16Mb SPI SOP8, 国产MRAM |

| HR682430E | D:\Refbook\HR682430E.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |

| SGM58031 | ADC | VDD / 接口 / 分辨率 / 通道 / 速率 | 3.0-5.5V / I2C / 16-bit Σ-Δ / 4单端或2差分 / 6.25-960SPS | §Electrical Characteristics |
| XT25F128F | NOR Flash | VCC / 容量 / SPI模式 / 频率 | 2.7-3.6V / 128Mb / Single/Dual/Quad SPI / 104MHz | §Datasheet P1 |
| FEMDRW032G-88A19 | eMMC | VCC(NAND) / VCCQ(Controller) / 容量 / 接口 | 2.7-3.6V / 1.7-1.95V或2.7-3.6V / 32GB / eMMC 5.1 HS400 | §5 Product Specifications |
| XPL51200 | DDR VTT | VIN / VLDOIN / Iout / 功能等效 | 2.375-3.5V / 1.1-3.5V / ±3A / DDR Termination (参考TI TPS51200) | §TPS51200 Datasheet || SGM706B | D:\Refbook\SGM706B.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| TPT9H221L1 | D:\Refbook\TPT9H221L1-SO1R-S.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| NCS23391 | D:\Refbook\NCS23391 Datasheet_V1.2 (1).pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| SGM6505 | D:\Refbook\SGM6505.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| SRV05_4 | D:\Refbook\SRV05-4D.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| EF2L45LG144B | D:\Refbook\Anlogic\EF2L45_Datasheet.pdf | 在线下载 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| LTM4644 | D:\Refbook\LTM4644_4644_1-1551397.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| YT8521SH | D:\Refbook\Motorcomm\YT8521SH.pdf | 在线下载 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| SIT3232EESE | D:\Refbook\SIT3232E-datasheet-V1.16-cn.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| CXDQ3BFAM-WG | D:\Refbook\CXMT\CXDQ3BFAM-CQ-A.pdf | 在线下载 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| RS0102YVS8 | D:\Refbook\RS0102.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| FM25Q128AI3 | D:\Refbook\FM25Q128AI3.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| LSF0108PW | D:\Refbook\Nexperia\LSF0108.pdf | 在线下载 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| AiP74LVC1G14GC | D:\Refbook\AIP74LVC1G14GC.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| M1806LDLFF | D:\Refbook\M1206DLFF.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| E2000Q | 飞腾腾珑E2000数据手册V1.4版本.md | 用户提供 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| SD3068 | https://www.sekorm.com/doc/585739676.html | 在线检索 | https://www.sekorm.com/doc/585739676.html | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |

| SGM58031XMS10G/TR | https://www.sg-micro.com/rect/assets/3ed1796d-7e46-4f32-b06f-a6eae4586cec/SGM58031.pdf | 在线下载 | https://www.sg-micro.com/rect/assets/3ed1796d-7e46-4f32-b06f-a6eae4586cec/SGM58031.pdf | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| XT25F128FSSIGU | https://datasheet.lcsc.com/datasheet/pdf/4b1f574ab5a8ddf1366e3cf66fef5583.pdf | 在线下载 | https://datasheet.lcsc.com/datasheet/pdf/4b1f574ab5a8ddf1366e3cf66fef5583.pdf | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| FEMDRW032G-88A19 | https://atta.szlcsc.com/upload/public/pdf/source/20220901/203DA543FFCCF9FBF8282B71276D9BDD.pdf | 在线下载 | https://atta.szlcsc.com/upload/public/pdf/source/20220901/203DA543FFCCF9FBF8282B71276D9BDD.pdf | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| XPL51200 | https://www.ti.com/lit/ds/symlink/tps51200.pdf | 功能等效 (TI TPS51200) | https://www.ti.com/lit/ds/symlink/tps51200.pdf | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
| DGKYD59212188 | https://www.rj45transformer.com/sale-21922981-dgkyd59212188ab1e1dy1e022-5921-series-network-socket-2x1-port-8p8c-modular-jack-multiport-dgkyd.html | 在线规格页 | https://www.rj45transformer.com/sale-21922981-dgkyd59212188ab1e1dy1e022-5921-series-network-socket-2x1-port-8p8c-modular-jack-multiport-dgkyd.html | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |



## 关键参数速查

> G0 命中后直接使用以下参数，跳过 PDF 解析（加速）。参数均标注手册出处以便追溯。

| IC 型号 | 参数类别 | 参数 | 值 | 手册出处 |
|---|---|---|---|---|
| 参数类别 | 参数 | 值 | 手册出处 |
|---|---|---|---|---|
| RK3576 | VCCIO 域 | PMUIO / PMUIO2 / VCCIO1 / VCCIO2 / VCCIO3 / VCCIO4 | 3.3V / 待查 / 1.8V / 3.3V / 1.8V / 1.8V | §4.3 |
| RK3576 | DDR | ZQ 校准电阻 | 240Ω 1% | §DDR PHY |
| RK3576 | 启动 | 启动配置引脚 | SARADC_IN0_BOOT | §Boot Configuration |
| RK806S-5 | Buck6 | 输出电压 | 0.85V | §Electrical Characteristics |
| RK806S-5 | Buck9 | 输出电压 | 1.1V | §Electrical Characteristics |
| ETA3409 | 开关频率 | 1.5MHz | §Electrical Characteristics |
| MS4553S | VCCA | A 侧供电范围 | 1.65V~5.5V | §Recommended Operating Conditions |
| MS4553S | VCCB | B 侧供电范围 | 1.65V~5.5V | §Recommended Operating Conditions |
| ETA3417S2F | DC-DC | Vin / Vout / Fsw / Ilim | 2.6-7V / 0.6V-Vin / 3MHz / 3A | §Electrical Characteristics |
| TMI3112H | DC-DC | Vin / Vout / Fsw / Iout | 2.7-5.5V / 0.6V-Vin / 2.3MHz / 2A | §Electrical Characteristics |
| LPDDR4_200P | DDR | ZQ / VDD1 / VDD2 / VDDQ | 240Ω / 1.8V / 1.1V / 1.1V | JEDEC Standard |

---
| XPL3233 | LDO | Vref / EN / Iout | 0.5V / EN≥1.1V开 / 3A | §电气特性, 表5 |
| IS6608A | Buck | Vin / Vout / Vref / EN / Fsw | 3.3-16V / 0.5-5.5V / 0.6V / EN≥2.8V / 800kHz默认 | §Electrical Characteristics |
| M0503DLBGP | Buck SoC | Vin / Vout / Vref / EN / Fsw / 电感 | 2.5-5.5V / 0.8V-Vin / 0.8V / EN≥1.21V / 2.5MHz / 内置0.47µH | §Electrical Characteristics, P1 |
| EF2L45LG144B | FPGA | VCCAUX / VCC_CORE / IOBanks | 2.375-3.63V / Internal LDO / 113 I/O | DS400 §3.1.3 |
| TPT9H221L1 | MLVDS | VCC / Type-2偏移 / 速率 | 3.0-3.6V / 100mV / 200Mbps | §Datasheet P1 |
| SGM706B | Supervisor | 复位阈值 | 3.08V (T型号) | §Electrical Characteristics |
| NCS23391 | Clock Gen | 输出 / 抖动 / 输入晶振 | 12路差分 / 125fs RMS / 48-54MHz | §Datasheet P1 |
| M1806LDLFF | DC-DC | 内置电感 / SW浮空 | 磁集成SoC, SW引脚内置 | 参考M1206DLFF系列 |
| FMP100T8 | FPGA | VCCCORE / 配置 / Bank | 1.0V / M[2:0]=MSPI / 多种 | 手册§供电与配置章节 |
| HR682430E | RJ45 MagJack | 千兆 / 变压器集成 | 10/100/1000M, 4对MDI | §Datasheet |

| SGM58031 | ADC | VDD / 接口 / 分辨率 / 通道 / 速率 | 3.0-5.5V / I2C / 16-bit Σ-Δ / 4单端或2差分 / 6.25-960SPS | §Electrical Characteristics |
| XT25F128F | NOR Flash | VCC / 容量 / SPI模式 / 频率 | 2.7-3.6V / 128Mb / Single/Dual/Quad SPI / 104MHz | §Datasheet P1 |
| FEMDRW032G-88A19 | eMMC | VCC(NAND) / VCCQ(Controller) / 容量 / 接口 | 2.7-3.6V / 1.7-1.95V或2.7-3.6V / 32GB / eMMC 5.1 HS400 | §5 Product Specifications |
| XPL51200 | DDR VTT | VIN / VLDOIN / Iout / 功能等效 | 2.375-3.5V / 1.1-3.5V / ±3A / DDR Termination (参考TI TPS51200) | §TPS51200 Datasheet |
---

## 使用规则


1. G0 Step 0.2 优先查此表：型号命中 → 直接使用 `手册路径` 列读取手册，跳过本地搜索
2. 未命中 → 执行 G0 Step 0.1 递归搜索 → 找到后追加到此表
3. 在线检索到的（`https://` 开头）→ 记录 URL，备注"在线"
4. MISSING（3+ 来源均未找到）→ 不写入此表，在 corrections.md 中记录


> ⚠️ U13 SCCH900202113B: Originally misidentified as backplane connector in g0_sources. Actually 16Mb SPI MRAM (SOP-8). Corrected 2026-06-23.

| SCCH900202113B | D:\\Refbook\\16Mb_MRAM V1.pdf | 本地 | — | KQ-BZK2412 | 2026-06-23 | 2026-06-23 |
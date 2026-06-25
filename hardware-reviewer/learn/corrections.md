# 人工修正日志

> Agent 在 G6 闭环中自动记录每次被纠正的内容。用于发现规则盲区和生成新的自学习条目。
> Agent 只写不执行，供人工定期分析和挖掘。

---

## 修正记录

| # | 日期 | 项目 | 原结论 | 修正后 | 根因分类 | 对应自学习条目 |
|---|---|---|---|---|---|---|
| C001 | 2026-06-15 | V10 | DDR ZQ 电阻缺失 🔴CRITICAL | ZQ 已连接，cellRef RESISTOR5_NC 被误判 | EDN 陷阱 | F-K002 |
| C002 | 2026-06-05 | KS-1 | 9 颗 IC 标记 INFERRED（手册均在 D:\Refbook\ 子目录中但未搜索到） | 重新搜索后全部 FOUND | G0 跳过 | F-K001 |
| C003 | 2026-06-04 | KS-1 | NODE0_1-1V8 归因到 U118 | 实际驱动源是 U92，追溯不完整 | 未追溯到驱动端 | F-K003 |
| C004 | 2026-06-11 | V10 | VCCIO 域套用了 RK3588 定义（PMUIO1/2, VCCIO1-6） | 修正为 RK3576 的域定义（PMUIO, VCCIO1-4） | 套错芯片参数 | F-K004 |
| C005 | 2026-06-04 | KS-1 | 多颗 IC 的 INFERRED 结论仅引用规则文档 | 修正为引用 datasheet 原文或降级 UNVERIFIED | 推断无手册引用 | F-K005 |
| C006 | 2026-06-05 | KS-1 | U111 DIR 电阻 R794 的 GND 端被误判为 VDD2H | 两端网络名双向验证，修正为 GND | 双向未验证 | F-K006 |
| C007 | 2026-06-05 | KS-1 | 依靠行号偏移推断网络归属 | 修正为从 EDN 结构声明提取 | 邻近推断 | F-K007 |
| C008 | 2026-06-04 | KS-1 | 多项以"全部OK"概括，未逐项枚举 | 修正为逐芯片/逐总线独立结论 | 枚举先行违反 | F-K008 |

---

## 根因分类统计

| 根因 | 次数 | 严重度 |
|---|---|---|
| EDN 陷阱（cellRef/格式误读） | 1 | 高 |
| G0 跳过（手册未搜全） | 1 | 高 |
| 追溯不完整（未到驱动端） | 1 | 高 |
| 套错参数（芯片混淆） | 1 | 高 |
| 推断无手册引用 | 1 | 中 |
| 双向元件未验证 | 1 | 高 |
| 邻近推断 | 1 | 中 |
| 枚举先行违反 | 1 | 中 |

---

## 使用规则

1. G6 闭环中每次修正 → 追加一行到此表
2. 如该修正对应已有的 `learn/knowledge.md` 条目 → 填写"对应自学习条目"列
3. 如该修正是新类型 → 同时评估是否可泛化为新的 [FIX] 条目
4. 人工定期（每 3 个项目或每月）翻阅此表，发现高频根因后手动升级到规则文件

| C009 | 2026-06-16 | V10 | VCCIO6/VCCIO7 供电域标记为虚警 (supply_net=null) | 确认 EDN 中 VCCIO6_VCC/VCCIO7_VCC 在 U1000 引脚的连接通过电源层实现，EDIF 未体现 | 邻近推断/EDN局限 | — |
| C010 | 2026-06-16 | V10 | U2400 VCC_2V0_PLDO_S3 分压器偏差+4.7% CRITICAL | 需确认设计目标电压是否为2.0V；若为2.1V则OK | 参数验证 | — |
| C011 | 2026-06-16 | V10 | I2C6 上拉=0Ω标记 WARNING | 确认 I2C6/I2C8 共享 R9831/R9832 电阻网络为分时复用设计 | 枚举先行 | — |

| C012 | 2026-06-16 | V10 | VCCIO6/VCCIO7 G4\u95e8\u7981\u5f3a\u5236\u901a\u8fc7 | \u7ecf3\u8f6e\u5ba1\u8ba1\uff0cEDN\u786e\u65e0\u7269\u7406\u8fde\u63a5\uff0c\u201c\u4e0d\u5b58\u5728\u5373\u8bc1\u636e\u201d | EDN\u5c40\u9650/PCB\u7535\u6e90\u5c42 | \u2014 |
| C013 | 2026-06-16 | V10 | G6\u95ed\u73af\u5b8c\u6210 | A\u7c7b\u6e05\u7a7a(0\u9879), B\u7c7b\u6e05\u7a7a(0\u9879), C\u7c7b20\u9879\u5f52\u6863, D\u7c7b6\u9879\u8c03\u8bd5\u65b9\u6848 | G6\u95ed\u73af | \u2014 |
| C014 | 2026-06-16 | V10 | \u7528\u6237\u5f3a\u5236\u901a\u8fc7G4 | G4\u4ec5\u5269VCCIO6/7\u4e24\u9879\u7f3aEDN\u951a\u70b9\uff0c\u4e0d\u5b58\u5728\u5373\u8bc1\u636e | \u5ba1\u8ba1\u95ed\u73af | \u2014 |

## 2026-06-16 V10 G6 Closure

### C-V10-001 VCCIO6/VCCIO7 Supply Missing
- Level: CRITICAL | G6: G6-001, G6-002
- VCCIO6_VCC and VCCIO7_VCC have no supply net traced in EDN
- Resolution: Class C - human confirm if UFS/DP interfaces used

### C-V10-002 U2400 DCDC Divider Deviation
- Level: CRITICAL | G6: G6-003
- VCC_2V0_PLDO_S3 divider 249K/100K = 2.094V vs label 2.0V (+4.7%)
- Resolution: Class C - confirm target voltage

### C-V10-003 Floating Pin False Positive Review
- Level: WARNING | G6: G6-012
- 124 CRITICAL floating pins, mostly OrCAD multi-part naming false positives
- Resolution: Class C - cross-reference ddr_evidence.json; CLK1_32K_OUT is primary concern

### D-V10-004 RK806S-5 OTP Rails
- Level: UNVERIFIED | G6: G6-005, G6-006, G6-011
- BUCK1/2/3/7/10 + NLDO2 OTP-programmed outputs
- Resolution: Class D - measure at bring-up with DMM/I2C


| C015 | 2026-06-17 | V10 | §五外设接口混在5.2下无独立分节(I2C/UART/USB/eMMC/MIPI/PCIe混排) | 修复为独立分节5.1(I2C) 5.2(UART) 5.3(USB) 5.4(eMMC) 5.5(MIPI/PCIe/SPI/JTAG)，每节含独立概述+逐项结论 | 报告格式/章节结构 | T-K001,T-K009 |
| C016 | 2026-06-17 | V10 | §七连接器仅有4行摘要，缺少逐引脚映射表 | 补全8连接器253引脚完整8列映射表(Pin/Net/Signal/Direction/Voltage/Domain/Source/Dest) | 报告格式/逐项结论 | T-K005 |
| C017 | 2026-06-17 | V10 | .docx生成脚本(28042bytes)字符数超限无法单次bash写入 | 改为分段Append-Content写入Python脚本(7段)，再执行生成.docx | 工具限制/脚本工程 | — |


| C018 | 2026-06-17 | V10 | I2C6/I2C8 分时复用误判：之前报告误将 I2C6 和 I2C8 合并为一条总线 | 修正为独立物理总线：I2C6_SCL/SDA 和 I2C8_SCL/SDA 是 4 条独立物理网络，不同 SoC GPIO (GPIO0 vs GPIO3)，各自独立上拉，非分时复用 | 枚举先行/邻近推断 | T-K001 |
| C019 | 2026-06-17 | V10 | §五外设检查漏掉了 SPI 和 JTAG 独立小节 | 新增 5.7 SPI 和 5.8 JTAG 独立 Heading 2，共 8 种外设全量输出 | 外设动态发现不完整 | T-K009 |
| C020 | 2026-06-17 | V10 | 连接器输出仅含 pin count 无逐引脚映射 | 补全 8 连接器 253 引脚完整 8 列表，每个连接器含 Pin/Net/Signal/Direction/Voltage/Domain/Source/Dest | 逐项结论格式 | T-K005 |
| C021 | 2026-06-17 | V10 | .docx 报告由 Python 脚本一次性生成（gen_report.py），413 段落 22 表格 | 通过分段写入 Python 脚本再执行的方式解决大文件 bash 写入问题 | 工具工程 | — |
| C022 | 2026-06-17 | V10 | 本报告为全量重新生成，修复上一版报告的 5 项结构性问题 (I2C Mux/外设类型/连接器引脚/CRITICAL 采样/电平转换 §六合并) | 全部修正已应用到 FINAL 版 | 流程规范执行 | — |



### CORR-2026-0617-001: Schema patches pending for 4 evidence files
- **Date**: 2026-06-17 21:05
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Issue**: peripheral_evidence.json, rk3576_soc_evidence.json, level_shifter_ldo_dcdc_evidence.json, pmic_rk806s5_evidence.json missing 'inputs'/'outputs' root fields
- **Resolution**: report acknowledges, source patches deferred to auditor
- **Related FIX**: None (schema validation catch, not a check error)

### CORR-2026-0617-002: I2C6/I2C8 0-ohm bridge CRITICAL
- **Date**: 2026-06-17 21:05
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Issue**: I2C6 SCL/SDA connected via 0R resistor to I2C8 nets, potential bus conflict
- **Resolution**: Flagged as CRITICAL in report S5.3; pending design intent confirmation
- **Related FIX**: None (new pattern - potential future F-K013)

### CORR-2026-0617-003: VCCIO6/VCCIO7 UNCONNECTED
- **Date**: 2026-06-17 21:05
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Issue**: RK3576 VCCIO6 (8 pins) and VCCIO7 (2 pins) have no supply portRef in prep
- **Resolution**: CRITICAL - these domains may be powered via board-to-board connector; needs confirmation
- **Related FIX**: None

### CORR-2026-0617-004: G0 ALL_PASS (12/12 ICs found)
- **Date**: 2026-06-17 21:05
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Note**: All 12 IC datasheets found through learn/ic_index.md (local + path corrections). No TRULY_MISSING ICs. This run validates the ic_index.md self-learning mechanism.
- **Related TEMPLATE**: T-K009 (peripheral discovery)

### CORR-2026-0617-005: RESISTOR5_NC trap avoided
- **Date**: 2026-06-17 21:05
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Issue**: DDR ZQ resistor R3801 has cellRef=RESISTOR5_NC but is correctly soldered (240ohm to VDDQ). The _NC suffix refers to a NC pin in the package, not to DNP status.
- **Resolution**: F-K002 trap correctly avoided in this review cycle.
- **Related FIX**: F-K002 (hit count increased)

---
## 2026-06-18 FL-24-E-MRF1-A-V10 Final Report Regeneration

### F-K011: J3/J5 I2C4/I2C9 Label Warning
- 触发: J3/J5 连接器 I2C4/I2C9 标签与 SoC 实际外设编号不一致
- 处理: 标记为 WARNING，标注 F-K011
- 影响: 6 条 WARNING 结论 (J3 &1-&2, J5 &1-&2)

### F-K002: RESISTOR5_NC cellRef 陷阱
- 触发: DDR ZQ 电阻 R1200/R1201/R3802/R3804 cellRef 含 _NC 后缀
- 处理: 正确识别为库符号名，非 DNP；4 颗电阻均确认焊接
- 已自修复: [自修复 K-F002]

### VCCIO6/VCCIO7 CRITICAL
- 触发: RK3576 VCCIO6 (8 pins) 和 VCCIO7 (2 pins) 供电网络未连接
- 处理: 标记为 CRITICAL；确认 VCCIO6 对应 USB3/PCIe 未使用，VCCIO7 对应 UFS 未使用
- 建议: 即使未使用也应接电避免浮空导致漏电

### EMMC_CMD 上拉缺失
- 触发: eMMC CMD 外部 10k pull-up 电阻未找到
- 处理: 标记为 CRITICAL；R9810=0R 无法提供上拉
- 建议: 改为 10kΩ 上拉到 VCC_1V8_S3

### CORR-2026-0618-001: Knowledge.md hit counts updated for V10 session
- **Date**: 2026-06-18
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Issue**: All 18 TEMPLATE entries (T-K001~T-K018) and 2 FIX entries (F-K002, F-K004) used in this session need hit count +1
- **Resolution**: Knowledge.md summary table and individual entries updated. T-K006 now hits ≥3 (2→3), qualifies for upgrade suggestion.
- **Related TEMPLATE**: T-K001~T-K018, F-K002, F-K004

### CORR-2026-0618-002: V10 session writeback completion
- **Date**: 2026-06-18
- **Run**: FL-24-E-MRF1-A-V10-20260617-202657
- **Note**: Session-end writeback completed. G6 closure previously PASS (822 findings). Report at report/final_report.docx (54KB). All 12 ICs FOUND via ic_index. No TRULY_MISSING.
- **Related**: G0 ALL_PASS, G6 PASS, delivery_check initially FAIL (fixed after report generation)

---

## 交互门禁违规记录（从 hardware-reviewer.md §交互门禁违规记录 迁移）

> 以下违规记录为永久性警示，不得删除。每次违规加固对应规则，防止复发。
> 迁移来源：hardware-reviewer.md lines 1551-1562 | 迁移日期：2026-06-24

| 编号 | 日期 | 项目 | 违规描述 | 根因 | 规则加固 |
|:---:|:---:|------|------|------|------|
| GATE-VIOL-001 | 2026-06-23 | KQ-BZK2412-A-0430 | 以 `run_in_background=true` 启动 → Agent 问了 4 次 Step 0a 用户从未看到 → 任务卡死取消 | 忽略前台强制规则 | §启动自检 项 1 新增 step_0a.json 有效性门禁 |
| GATE-VIOL-002 | 2026-06-23 | KQ-BZK2412-A-0430 | Agent 在第 4 次 TODO CONTINUATION 后自行推断 `manual_dir=工作目录` / `extra_checks=[]`，生成含 `warnings=["推断"]` 的 step_0a.json | 无推断零容忍规则 | §Step 0a 新增推断零容忍 + `raw_user_response` 有效性门禁 |
| GATE-VIOL-003 | 2026-06-23 | KQ-BZK2412-A-0430 | G0.5 缺失但 Agent 未明确阻断，继续进入后续步骤 | G0.5 阻断规则未列全 | §G0.5 阻断规则新增人机交互阻断点声明 |
| GATE-VIOL-004 | 2026-06-23 | KQ-BZK2412-A-0430 | Agent 在 step_0a.json 不存在时未中止，自行创建文件填入假设值并继续执行 EDN 解析 | 中止是抽象动词，Agent将其解释为修复而非停止 | §会话启动流程 重构为 Phase A/B 两阶段：Phase A 纯只读验证，每项 FAIL 输出精确 BLOCKED 消息格式 + 禁止工具调用声明 |
| GATE-VIOL-005 | 2026-06-05 | FL-25-A-K402 | G0 手册搜索跳过递归搜索，仅平铺列举 PDF，致 9 颗 IC 误标为 NOT_FOUND | G0 跳过/非递归搜索 | §G0 手册搜索 Step 0.1 强制递归搜索（Get-ChildItem -Recurse），禁止平铺 |
| GATE-VIOL-006 | 2026-06-15 | FL-24-E-MRF1-A-V10 | DDR ZQ 电阻 R3801(RESISTOR5_NC) 被误判为不焊接/DNP，实际已焊接（240ohm to VDDQ） | cellRef 后缀 `_NC` 被误解为 DNP | §OrCAD/EDIF 常见陷阱 新增 RESISTOR5_NC/CAP_NC 说明 + 强制自检三步法 |
| GATE-VIOL-007 | 2026-06-04 | KS-1 | NODE0_1-1V8 电压轨被归因到 U118，实际驱动源是 U92，导致时序分析错误 | 未追溯到驱动端物理引脚 | §Common Patterns 新增"强制溯源到驱动端"规则：电压轨追溯至 SW 引脚，信号追溯至 TX/输出引脚 |
| GATE-VIOL-008 | 2026-06-05 | KS-1 | U111 DIR 电阻 R794 的 GND 端因行号漂移被误判为 VDD2H，导致 8 项 CRITICAL 假阳性 | 单侧行号偏移推断，未双向验证 | §Common Patterns 新增"跨元件连接必须双向验证网络名"：两端网络名逐字确认 |
| GATE-VIOL-009 | 2026-06-04 | KS-1 | 电源审查拆分为 4 个并行子任务但未传递手册路径和 G0 门禁约束，子任务凭经验推断 | 子任务 prompt 缺少手册引用和门禁要求 | §并行任务分解约束 P1-P6 新增：规则复读、手册路径传递、G0 独立通过、参数引用举证、芯片级拆分优先 |
| GATE-VIOL-010 | 2026-06-23 | KQ-BZK2412-A-0430 | hardware_review 主控 Agent 自己生成 evidence JSON，未委派给 hw_analyze 子任务，导致上下文耗尽 | 违反委派-only 原则 | §多 Agent 委派架构 新增违例警示：hardware_review 是纯调度层，禁止执行任何分析工作 |
| GATE-VIOL-011 | 2026-06-04 | KS-1 | 审查报告仅 78 段落/8 表格，远低于参考报告（1468 段落/JSON 证据链），交付质量不足 | 规则定义"怎么查"但未定义"查多少、输出什么" | §交付质量标准 Q1-Q9 新增：IC 全量清单、逐项结论、JSON 证据、五级判定等量化标准 |
| GATE-VIOL-012 | 2026-06-09 | 多次交付 | INFERRED/UNVERIFIED 不确定结论未在交付前闭环回溯验证，导致多次交付存在未解决项 | 缺少闭环验证程序 | §G6 报告后自审闭环 新增 A/B/C/D 四类分类闭环流程 + G6 通过标准 |
| GATE-VIOL-013 | 2026-06-04 | KS-1 | 外设检查仅覆盖 I2C/UART/SPI/DDR 等已知类型，漏检 USB/eMMC/JTAG/QSPI/FAN/GPIO | 固定检查清单，无动态发现 | §常见外设检查要点 新增动态发现流程：从 EDN 网表信号名匹配全部协议特征，禁止仅列参考样本类型 |
| GATE-VIOL-014 | 2026-06-23 | KQ-BZK2412-A-0430 | hw_auditor 输出 FAIL 但 hardware_review 未处理，直接声称完成并结束 agent | 无自动修复循环 | §复查不合格闭环 新增自动修复机制(v3.6)：逐项 FAIL 定位环节 → 重跑对应 subagent → 重跑审计，最多 3 轮 |

### 经验教训（从 hardware-reviewer.md 迁移）

1. `hardware_review` 永远不能以 `run_in_background=true` 启动。hardware_review 必须在每次 `task()` 调用前验证。
2. `step_0a.json` 必须包含真实用户原话，任何推断/默认值都是违规。
3. 所有交互门禁（Step 0a, G0.5, 会话结束）必须在 hardware_review 前台完成，不可自行跳过。
4. 门禁关键词必须从抽象动词（中止/阻断/停止）替换为可观测行为约束（输出指定格式的 BLOCKED 消息 + 明确禁止调用 write/bash/task 等工具）。两阶段分离（只读验证 vs 执行）可物理隔离越权操作。


---


## 重构记录


| 日期 | 操作 | 范围 | 原因 |

|---|---|---|---|

| 2026-06-24 | 全面重构 hardware-reviewer.md | §0-§7 + 附录 A-E | 新增加规则分类/审核流程章节；行号索引→锚点导航；历史教训迁移 learn/；Agent prompt 去重；hardware_review 转型纯编排器 |


| 原文件 | 备份路径 |

|---|---|

| hardware-reviewer.md (1578行) | hardware-reviewer.md.bak.20260624-* |

| opencode.json | opencode.json.bak.20260624-* |


**重构内容**：
- 历史教训迁移 (GATE-VIOL-005~014) → corrections.md
- 可泛化 FIX 条目 (F-K026, F-K027) → knowledge.md
- 教训迁移清单 → .sisyphus/temp/lesson_migration.md

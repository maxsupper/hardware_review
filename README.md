# Hardware Reviewer Plugin for OpenCode

硬件原理图设计验证插件，支持 OrCAD EDN/EDIF 原理图的自动化审查。

## 审查范围

| 维度 | 检查内容 |
|------|---------|
| **引脚核对** | 芯片引脚功能复用、VCCIO 电源域电平匹配、SoC GPIO→外设映射 |
| **供电网络** | 电源树追踪（SW→电感→VOUT）、电压分压电阻计算、EN/PG 链路 |
| **DDR 接口** | DQ/DQS/CA/CK 信号完整性、ZQ 校准电阻（240Ω±1%）、VDDQ/VDD1/VDD2 电压 |
| **外设接口** | I2C 上拉、SPI/UART 信号交叉、MIPI D-PHY 极性、GMAC RGMII、USB DP/DM、eMMC/SDMMC |
| **连接器** | 253 引脚逐引脚 8 列完整映射（网络名/信号/方向/电压/VCCIO域/源端/目的端） |
| **BOM 核对** | EDN 网表 ↔ BOM 型号一致性、cellRef 符号复用检测、footprint/封装匹配 |
| **浮空引脚** | SoC/DDR/PMIC 未连接引脚分类（Must-Connect/NC/Reserved/需确认） |
| **上电时序** | PMIC Buck/LDO EN→PG 级联、上电甘特图、与 SoC 时序要求对比 |

## 报告输出

审查完成后生成 `final_report.md`（参考模板：`report-template.md`），含 10 个章节 + 3 个附录：

```
§0  报告概览         — 结论统计、Agent 版本
§1  规则适用度声明    — 触发了哪些检查规则
§2  IC 全量清单       — 型号/位号/封装/手册路径
§3  供电架构分析      — 电源树 + Mermaid 上电时序甘特图
§4  关键发现          — CRITICAL / WARNING / UNVERIFIED 分级
§5  IC 深度分析       — 每颗 IC 逐项检查结论
§6  连接器分析        — 8 连接器 253 引脚 8 列逐引脚表
§7  外设接口分析      — 15 种外设类型逐项检查
§8  BOM 核对报告      — EDN↔BOM 型号一致性评分
§9  设计整改建议      — P0/P1/P2/P3 优先级矩阵
附录A 全量结论汇总表  — CRITICAL+WARNING+UNVERIFIED 含 JSON 证据路径
附录B 连接器引脚全量表 — 253 引脚完整 8 列
附录C 文件路径一览表  — EDN/BOM/手册/evidence 路径
```

所有结论使用五级判定：🔴 CRITICAL / 🟡 WARNING / 🟢 OK / 🔵 INFERRED / ⚫ UNVERIFIED

## 自学习机制

插件通过 `learn/` 目录实现跨项目知识积累，无需人工维护：

### IC 型号索引 (`ic_index.md`)

首次审查新 IC 后，自动记录型号→手册路径的映射。后续项目命中索引时**跳过本地搜索和在线检索**，直接使用已记录路径。

### 知识库 (`knowledge.md`)

每次审查后自动总结错误模式和检查流程，分为两类：

- **[FIX] — 反应式修复**：当 agent 再次犯同样错误时自动纠正
- **[TEMPLATE] — 主动式预防**：当发现特定信号特征时自动加载检查流程

成熟度从 1 到 5 自动升级，命中 3 次建议固化到规则文件，跨 2 个芯片平台验证后自动 +1 成熟度。

## 前置依赖

| 依赖 | 说明 | 安装 |
|------|------|------|
| Python | 3.12+ | — |
| openpyxl | BOM Excel 解析 | `pip install openpyxl` |
| pdfplumber | PDF 手册解析（可选） | `pip install pdfplumber` |
| OpenCode | Agent 运行框架 | — |

## 快速安装

### 1. 复制插件

将 `hardware-reviewer/` 目录复制到 `~/.config/opencode/` 下。

### 2. 设置环境变量

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `HW_REVIEW_DIR` | 插件目录 | `C:\Users\xxx\.config\opencode\hardware-reviewer` |
| `REFBOOK_DIR` | 芯片手册目录 | `D:\Refbook` |
| `REBOOK_MD_DIR` | Markdown 手册目录 | `D:\rebook_md` |

### 3. 合并 Agent 配置

打开 `~/.config/opencode/opencode.json`，将 `agent-config.json` 中的 6 个 agent 定义**合并**到 `"agent"` 字段中。

### 4. 开始审查

将 `.EDN` 原理图和 BOM `.xlsx` 放到工作目录，启动 OpenCode 选择 `hardware_review` agent。

## 审查流程

```
Phase A   → 加载 learn/ 知识库 + IC 索引
Wave 1    → hw_prep: EDN 网表解析（IC/连接器/网络提取）
G0        → hw_search: 手册搜索（本地递归 + 在线 3+ 来源）
G0.5      → 缺失手册确认（人机交互）
Gate 1    → prep 数据完整性验证
Wave 2    → hw_analyze: 深度分析（引脚/VCCIO/DDR/外设/连接器, 并发≤5）
G2.x      → evidence JSON schema 验证 + 连接器填充率 + 接口覆盖率
Wave FINAL → hw_write: 报告合成 → hw_auditor: 审计复核 → G6 闭环
```

## Agent 列表

| Agent | 模型 | 角色 |
|-------|------|------|
| hardware_review | deepseek-v4-pro | 编排器（调度/门禁/闭环） |
| hw_search | deepseek-v4-flash | 手册检索（本地+在线） |
| hw_prep | deepseek-v4-flash | EDN 网表解析 |
| hw_analyze | deepseek-v4-pro | 深度分析（引脚/DDR/外设/连接器） |
| hw_auditor | deepseek-v4-pro | 复核审计（报告↔证据↔EDN 三方对照） |
| hw_write | deepseek-v4-flash | 报告编写 |

## License

MIT

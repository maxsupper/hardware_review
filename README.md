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

## 自学习机制

插件通过 `learn/` 目录实现跨项目知识积累，无需人工维护：

### IC 型号索引 (`ic_index.md`)

首次审查新 IC 后，自动记录型号→手册路径的映射。后续项目命中索引时**跳过本地搜索和在线检索**，直接使用已记录路径。

| 状态 | 含义 |
|------|------|
| `FOUND (本地)` | 手册已在本地，直接读取 |
| `FOUND (在线下载)` | 从网络下载到本地，记录来源 URL |
| `FOUND (ic_index)` | 从自学习索引命中 |

### 知识库 (`knowledge.md`)

每次审查后自动总结错误模式和检查流程，分为两类：

- **[FIX] — 反应式修复**：当 agent 再次犯同样错误时自动纠正（如 cellRef 误判、电源追踪不到物理引脚、连接器表格截断等）
- **[TEMPLATE] — 主动式预防**：当发现特定信号特征时自动加载检查流程（如 I2C 总线→检查上拉电阻；DDR→检查 ZQ 校准；PMIC→追踪 EN/PG 链）

成熟度从 1 到 5 自动升级，命中 3 次建议固化到规则文件，跨 2 个芯片平台验证后自动 +1 成熟度。

### 修正日志 (`corrections.md`)

记录每次审查中的修正项，用于事后追溯和自学习统计。

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

## 目录结构

```
hardware-reviewer/
├── hardware-reviewer.md    # 主规则
├── boot/agent-boot.md      # Agent 启动引导
├── tools/                  # 验证脚本 (Python)
├── platform/               # 芯片平台规则
│   ├── RK3576/
│   ├── RK3588/
│   ├── RV1126B/
│   └── E2000/
├── learn/                  # 自学习知识库
│   ├── ic_index.md          # IC 型号→手册索引（自动积累）
│   ├── knowledge.md          # FIX/TEMPLATE 规则（跨项目复用）
│   └── corrections.md        # 修正日志
└── *.md                    # 规则文件
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

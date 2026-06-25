# Hardware Reviewer Plugin for OpenCode

硬件原理图设计验证插件，支持 OrCAD EDN/EDIF 原理图的自动化审查。

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

```json
{
  "agent": {
    // ← 将 agent-config.json 的全部内容粘贴到这里
    "hardware_review": { ... },
    "hw_prep": { ... },
    "hw_analyze": { ... },
    "hw_auditor": { ... },
    "hw_write": { ... },
    "hw_search": { ... }
  }
}
```

### 4. 开始审查

将 `.EDN` 原理图和 BOM `.xlsx` 放到工作目录，启动 OpenCode 选择 `hardware_review` agent。

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
└── *.md                    # 规则文件
```

## 原理图要求

- 格式：OrCAD EDN/EDIF
- BOM：`.xlsx`，芯片型号以 BOM 为准

## Agent 列表

| Agent | 模型 | 角色 |
|-------|------|------|
| hardware_review | deepseek-v4-pro | 编排器 |
| hw_search | deepseek-v4-flash | 手册检索 |
| hw_prep | deepseek-v4-flash | EDN 解析 |
| hw_analyze | deepseek-v4-pro | 深度分析 |
| hw_auditor | deepseek-v4-pro | 复核审计 |
| hw_write | deepseek-v4-flash | 报告编写 |

## License

MIT

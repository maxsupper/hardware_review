# Hardware Reviewer Plugin - 安装指南

## 前置依赖

- Python 3.12+
- openpyxl (`pip install openpyxl`)
- OpenCode (配置路径：`~/.config/opencode/`)

## 安装步骤

### 1. 复制插件到 OpenCode 配置目录

```powershell
Copy-Item -Recurse hardware-reviewer\ $env:USERPROFILE\.config\opencode\hardware-reviewer\
```

### 2. 配置环境变量

在系统环境变量中设置：

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `HW_REVIEW_DIR` | 插件安装目录 | `C:\Users\xxx\.config\opencode\hardware-reviewer` |
| `REFBOOK_DIR` | 芯片手册存放目录 | `D:\Refbook` |
| `REBOOK_MD_DIR` | Markdown 手册目录 | `D:\rebook_md` |

### 3. 合并 Agent 配置

将 `agent-config.json` 中的 agent 定义合并到 `~/.config/opencode/opencode.json` 的 `"agent"` 字段中。

示例 opencode.json：
```json
{
  "agent": {
    "hardware_review": { ... },
    "hw_prep": { ... },
    "hw_analyze": { ... },
    "hw_auditor": { ... },
    "hw_write": { ... },
    "hw_search": { ... }
  }
}
```

### 4. 提交原理图

将 `.EDN` 和 BOM `.xlsx` 放到工作目录，启动 OpenCode 并选择 `hardware_review` agent 即可。

## 目录结构

```
~/.config/opencode/hardware-reviewer/
├── hardware-reviewer.md    # 主规则
├── boot/agent-boot.md      # Agent 启动引导
├── tools/                  # 验证脚本
├── platform/               # 芯片平台规则 (RK3576/RK3588/RV1126B/E2000)
├── learn/                  # 自学习知识库
└── *.md                    # 规则文件
```

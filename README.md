# Hardware Reviewer Plugin for OpenCode

硬件原理图设计验证插件，支持 OrCAD EDN/EDIF 原理图的自动化审查。

## 目录结构

```
hardware-reviewer/
├── hardware-reviewer.md    # 主规则文件
├── boot/agent-boot.md      # Agent 启动引导
├── tools/                  # 验证脚本
│   ├── hardware_review_cli.py
│   ├── prep_validate.py
│   ├── g2x_validate.py
│   ├── schema_validate.py
│   └── finalize_manifest.py
├── platform/               # 芯片平台规则
│   ├── RK3576/
│   ├── RK3588/
│   ├── RV1126B/
│   └── E2000/
├── learn/                  # 自学习知识库
│   ├── ic_index.md
│   ├── knowledge.md
│   └── corrections.md
├── 引脚核对规则.md
├── 引脚电平检查方案.md
├── 引脚复用关系检查规则.md
├── 接口电路检查规则.md
├── 电源检查.md
├── 报告格式规范.md
└── 证据文件Schema规范.md
```

## 安装

将 `hardware-reviewer/` 目录复制到 `~/.config/opencode/` 下，然后在 `opencode.json` 中添加 agent 配置（见 agent-config.json）。

需要配置的外部目录：
- `D:\Refbook\` — 手册/数据手册存放目录
- `D:\rebook_md\` — Markdown 手册目录

## Agent 列表

| Agent | 模型 | 角色 |
|-------|------|------|
| hardware_review | deepseek-v4-pro | 编排器（裁判） |
| hw_search | deepseek-v4-flash | 手册检索 |
| hw_prep | deepseek-v4-flash | EDN 网表解析 |
| hw_analyze | deepseek-v4-pro | 深度分析 |
| hw_auditor | deepseek-v4-pro | 复核审计 |
| hw_write | deepseek-v4-flash | 报告编写 |

## License

MIT

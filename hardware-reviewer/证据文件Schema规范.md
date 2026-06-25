# 证据文件 JSON Schema 规范

> 所有硬件检查任务产出的 .json 证据文件必须遵循本规范。
> Schema 版本: 2.0 | 生效: 2026-06-15

---

## 一、通用要求

### 1.1 根节点元信息

每个证据 JSON 文件根节点必须包含 `meta` 对象：

```json
{
  "meta": {
    "task_id": "T6",
    "task_name": "连接器逐引脚分析",
    "plan": "FL-24-E-MRF1-A-V10-check",
    "generated_at": "2026-06-15T12:00:00Z",
    "source_file": "parsed_v10.json"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `task_id` | string | ✅ | 任务编号，如 T1~T10, F1~F4 |
| `task_name` | string | ✅ | 任务中文名称 |
| `plan` | string | ✅ | 所属计划文件名 |
| `generated_at` | string | ✅ | ISO 8601 时间戳 |
| `source_file` | string | ✅ | 主要输入文件（EDN/JSON 路径） |

---

## 二、任务输出 Schema

### T1: IC 清单 — `v10_ic_inventory.csv`

CSV 格式，列定义：

| 列名 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| 位号 | string | ✅ | U1000, U2, U5… |
| cellRef | string | ✅ | EDN 符号名 |
| Value(型号) | string | ✅ | 实际芯片型号，EDN 提取 |
| 功能类别 | string | ✅ | SOC / PMIC / LDO / DC-DC / DRAM / LEVEL_SHIFTER |
| datasheet_status | enum | ✅ | FOUND / MISSING / EDN-SOURCED |
| datasheet_path | string | ✅ | 本地绝对路径 或 URL |
| 备注 | string | — | EDN line ref、cellRef 不匹配警告等 |

> ⚠️ `datasheet_status = EDN-SOURCED` 指型号从 EDN property 提取，
> 无 BOM 交叉验证。不可写成 FOUND。

### T1 附加: RK3576 参数 — `v10_rk3576_params.json`

```json
{
  "soc": "RK3576",
  "package": "BGA698",
  "vccio_domains": [
    {"name": "PMUIO0", "typical_voltage": "1.8V", "note": "boot-required"},
    {"name": "VCCIO0", "typical_voltage": "1.8V", "note": "eMMC domain"}
  ],
  "ddr": {
    "type": "LPDDR4/LPDDR4X/LPDDR5",
    "zq_value": "240Ω",
    "zq_tolerance": "±1%",
    "zq_connect_to": "DDRPHY_VDDQ_S0"
  },
  "pmic": {
    "model": "RK806S-5",
    "adjustable_bucks": ["FB6","FB9"],
    "buck_count": 10,
    "nldo_count": 6,
    "pldo_count": 7
  },
  "clock": {
    "frequency": "24MHz",
    "tolerance": "±20ppm",
    "duty_cycle": "50%",
    "xout_series_r": "22Ω",
    "parallel_r": "10KΩ"
  },
  "reset": {
    "npor_pin": "W28",
    "min_pulse_width": "~4.17μs",
    "debounce_cap": "100nF"
  },
  "boot": {
    "saradc_pin": "SARADC_IN0_BOOT (A25)",
    "config_modes": 11,
    "sdmmc0_detn_pin": "U21"
  }
}
```

---

### T4: VCCIO 域映射 — `v10_vccio_map.json`

```json
{
  "vccio_domains": [
    {
      "name": "PMUIO0",
      "voltage": "1.8V",
      "source_rail": "VCC_1V8_S3",
      "source_ic": "U2300",
      "source_pin": "VOUT8_A",
      "gpio_banks": ["GPIO0_A", "GPIO0_D"],
      "pin_count": 15,
      "verified": true
    }
  ],
  "supply_rails": {
    "VCC_1V8_S3": {
      "voltage": "1.8V",
      "pmic_source": "U2300/VOUT8_A",
      "fed_domains": ["PMUIO0", "VCCIO0", "VCCIO3", "VCCIO5"]
    }
  },
  "critical_findings": [
    {
      "level": "CRITICAL",
      "domain": "VCCIO6",
      "description": "VCCIO6 有 9 个 GPIO 引脚但无供电轨连接",
      "affected_pins": 9
    }
  ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `vccio_domains[].name` | string | ✅ | 域名 |
| `vccio_domains[].voltage` | string | ✅ | 带单位，如 "1.8V" |
| `vccio_domains[].source_rail` | string | ✅ | EDN 供电网络名 |
| `vccio_domains[].source_ic` | string | ✅ | 供电 IC 位号 |
| `vccio_domains[].source_pin` | string | — | 供电 IC 输出引脚名 |
| `vccio_domains[].gpio_banks` | string[] | ✅ | GPIO Bank 列表 |
| `vccio_domains[].pin_count` | int | ✅ | 该域引脚总数 |
| `vccio_domains[].verified` | bool | ✅ | 是否从 EDN 追踪到供电 |
| `supply_rails.<net>.fed_domains` | string[] | ✅ | 该供电轨覆盖的域 |
| `critical_findings[].level` | enum | ✅ | CRITICAL / WARNING |

---

### T5: 供电网络 — `v10_power_rails.json`

```json
{
  "rails": [
    {
      "net": "VCC_3V3_S3",
      "voltage": "3.3V",
      "source_ic": "U2300",
      "source_pin": "VOUT4_A",
      "load_count": 12,
      "verified": true,
      "verification_note": "符合设计指南 §5.5 BUCK4 配置"
    }
  ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `rails[].net` | string | ✅ | EDN 网名 |
| `rails[].voltage` | string | ✅ | 带单位 |
| `rails[].source_ic` | string | ✅ | 源端 IC 位号 |
| `rails[].source_pin` | string | ✅ | 源端引脚 |
| `rails[].load_count` | int | ✅ | 负载 IC 数量 |
| `rails[].verified` | bool | ✅ | 电压是否从设计指南验证 |
| `rails[].verification_note` | string | — | 验证依据 |

---

### T6: 连接器 — `v10_connector_pinout.json`

```json
{
  "connectors": {
    "J1": [
      {
        "pin": "&1",
        "net": "GND",
        "signal_type": "GND",
        "signal_detail": "GND",
        "direction": "GND",
        "voltage": "0V",
        "domain": "GND",
        "source": "GND",
        "dest": "GND"
      }
    ]
  },
  "summary": {
    "total_connectors": 8,
    "total_pins": 247
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `pin` | string | ✅ | 连接器引脚号（如 &1, A） |
| `net` | string | ✅ | EDN 网名 |
| `signal_type` | enum | ✅ | GND / POWER / UART / I2C / SPI / MIPI / Ethernet / USB / Storage / Clock / Control / Camera / Other |
| `signal_detail` | string | ✅ | 功能简述 |
| `direction` | enum | ✅ | INPUT / OUTPUT / BIDIR / PWR / GND |
| `voltage` | string | ✅ | 带单位，MIPI 等差分信号标注供电域而非信号摆幅 |
| `domain` | string | ✅ | VCCIO 域或 "GND" / "POWER" |
| `source` | string | ✅ | 驱动端 IC.引脚 |
| `dest` | string | ✅ | 接收端标识 |

> ⚠️ MIPI D-PHY 差分信号的 `voltage` 应标注 PHY 供电域（如 "0.75V (VDDA_0V75_S0)"），
> 不得写 "1.2V"（该值是从信号名推测的 fallback，不是实测值）。

---

### T7: DDR — `v10_ddr_check.json`

```json
{
  "checks": {
    "chip_count": {
      "status": "PASS",
      "finding": "1 颗 LPDDR4 (U3800, BGA200)"
    },
    "zq_calibration": {
      "status": "FAIL",
      "finding": "R1200/R1201/R3802/R3804 全部标记 RESISTOR5_NC",
      "level": "CRITICAL"
    },
    "ck_differential": {
      "status": "PASS",
      "finding": "CK_t/CK_c 极性正确，4 对差分"
    },
    "dqs_differential": {
      "status": "PASS",
      "finding": "DQS_t/DQS_c 极性正确，4 对差分"
    },
    "byte_lanes": {
      "status": "PASS",
      "finding": "4 lane × (8DQ + 1DQS + 1DM) 完整"
    },
    "ca_bus": {
      "status": "PASS",
      "finding": "CA[5:0] 每通道完整"
    },
    "csn_cke_reset": {
      "status": "WARNING",
      "finding": "RESET 仅 LPDDR4 侧可见，SOC 侧未在解析范围"
    },
    "supplies": {
      "status": "PASS",
      "finding": "VDD1=1.8V, VDD2=1.1V, VDDQ=0.61V (LPDDR4X) 全部正确"
    }
  },
  "critical_issues": [
    {
      "id": "CRIT-01",
      "title": "ZQ 电阻全部 NC",
      "description": "SOC ZQ(R1200/R1201) + LPDDR4 ZQ(R3802/R3804) 全部标记 RESISTOR5_NC",
      "impact": "DDR ZQ 校准完全失效，训练将失败"
    },
    {
      "id": "CRIT-02",
      "title": "SOC DDR PHY 信号页缺失",
      "description": "69 条 LPDDR4 信号线仅见颗粒侧，SOC 侧在另一个 SPLIT_INST 页面未纳入解析",
      "impact": "无法验证 SOC↔LPDDR4 物理连接顺序和完整性"
    }
  ],
  "verification_summary": {
    "total_checks": 8,
    "passed": 5,
    "failed": 1,
    "warning": 1,
    "incomplete": 1,
    "overall_verdict": "FAIL"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `checks.<name>.status` | enum | ✅ | PASS / FAIL / WARNING / N/A / INCOMPLETE |
| `checks.<name>.finding` | string | ✅ | 详细发现 |
| `checks.<name>.level` | enum | — | CRITICAL / WARNING ，仅 FAIL 和 WARNING 时填 |
| `critical_issues[].id` | string | ✅ | 编号，如 CRIT-01 |
| `critical_issues[].title` | string | ✅ | 简短标题 |
| `critical_issues[].description` | string | ✅ | 详细描述 |
| `critical_issues[].impact` | string | ✅ | 影响说明 |
| `verification_summary.overall_verdict` | enum | ✅ | PASS / FAIL / INCOMPLETE |

---

### T8: 外设 — `v10_peripheral_check.json`

```json
{
  "i2c_groups": [
    {
      "bus_id": "I2C1",
      "scl_net": "I2C1_SCL_M0_RK806",
      "sda_net": "I2C1_SDA_M0_RK806",
      "pull_up_scl": {"present": true, "value": "2.2K", "to_rail": "VCC_1V8_S3"},
      "pull_up_sda": {"present": true, "value": "2.2K", "to_rail": "VCC_1V8_S3"},
      "verdict": "OK"
    }
  ],
  "uart_groups": [
    {
      "name": "UART5",
      "tx_net": "UART5_TX_M0_3V3",
      "rx_net": "UART5_RX_M0_3V3",
      "crossover_ok": true,
      "verdict": "OK"
    }
  ],
  "spi_groups": [
    {
      "name": "SPI3",
      "signals_present": ["CLK", "MOSI"],
      "signals_missing": ["MISO", "CSN"],
      "verdict": "WARNING"
    }
  ],
  "level_shifter": {
    "designator": "U5",
    "model": "MS4553S",
    "vcca": "3.3V",
    "vccb": "3.3V",
    "oe_state": "HIGH",
    "oe_pull": "4.7KΩ to VCC_3V3",
    "verdict": "OK"
  },
  "emmc": {
    "cmd_pullup_present": false,
    "recommendation": "建议 10KΩ 上拉到 VCCIO0",
    "verdict": "WARNING"
  },
  "usb": {
    "interface": "USB2_OTG0",
    "dp_net": "USB2_OTG0_DP",
    "dm_net": "USB2_OTG0_DM",
    "verdict": "OK"
  },
  "jtag_swd": {
    "routed": false,
    "verdict": "INFERRED"
  }
}
```

---

### T9: 悬空引脚 — `v10_floating_pins.json`

```json
{
  "perChip": {
    "SOC_RK3576": {
      "connected": 86,
      "nc_design": 273,
      "floating": 0
    }
  },
  "clock": {
    "frequency": "24MHz",
    "xout_series": "R1100",
    "parallel": "R1101 (10KΩ)",
    "load_caps": "C1100, C1101",
    "verdict": "OK"
  },
  "reset": {
    "signal": "NPOR_E",
    "net": "RESET_L",
    "pull_up": "R1105 → VCC_1V8_S3",
    "debounce": "C1119 + C2366 → GND",
    "source": "PMIC U2300/RESETB_C (via R9856)",
    "verdict": "OK"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `perChip.<soc>.connected` | int | ✅ | 有源端连接的引脚数 |
| `perChip.<soc>.nc_design` | int | ✅ | 设计预留 NC 引脚数 |
| `perChip.<soc>.floating` | int | ✅ | 异常悬空引脚数，应为 0 |
| `clock.verdict` | enum | ✅ | PASS / FAIL / WARNING |
| `reset.verdict` | enum | ✅ | PASS / FAIL / WARNING |

---

### T10: 芯片专属 — `v10_rk3576_specific.json`

```json
{
  "saradc_in0_boot": {
    "status": "WARNING",
    "finding": "R1102 上拉到 1.8V, R1103 NC, 无分压 — 需查 Fig 2-22 确认启动模式"
  },
  "emmc": {
    "status": "OK",
    "finding": "CMD/CLK/DATA[7:0]/STRB/RST_n 均通过串联电阻连到 J1"
  },
  "jtag_swd": {
    "status": "CRITICAL",
    "finding": "SDMMC0_DETN 拉高选 JTAG 模式，但 TCK/TMS/TDI/TDO 均未路由"
  },
  "fspi": {
    "status": "N/A",
    "finding": "FSPI 未在此设计中使用"
  },
  "sdmmc0_detn": {
    "status": "CRITICAL",
    "finding": "R1121 拉到 VCC_1V8_S3 (HIGH=JTAG) 与 JTAG 未路由冲突"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|:--:|------|
| `<check>.status` | enum | ✅ | CRITICAL / WARNING / OK / N/A |
| `<check>.finding` | string | ✅ | 详细发现和判定依据 |

---

## 三、枚举值定义

| 枚举名 | 允许值 |
|--------|------|
| **检查等级** | `CRITICAL` `WARNING` `OK` `INFERRED` `UNVERIFIED` |
| **检查状态** | `PASS` `FAIL` `WARNING` `N/A` `INCOMPLETE` |
| **信号方向** | `INPUT` `OUTPUT` `BIDIR` `PWR` `GND` |
| **Datasheet 状态** | `FOUND` `MISSING` `EDN-SOURCED` |
| **信号分类** (T6) | `GND` `POWER` `UART` `I2C` `SPI` `MIPI` `Ethernet` `USB` `Storage` `Clock` `Control` `Camera` `Other` |

---

## 四、F2 报告代理的使用规范

> ⛔ **报告生成前，F2 代理必须首先读取本文件。**

1. 按本 Schema 定义的字段名读取 JSON，**严禁猜测字段名**
2. 字段不存在时 **必须报错**，不得静默跳过——空章节不可接受
3. 电压值必须是 `string` 类型（如 `"1.8V"`），不是 `number`
4. 连接器表 **不允许截断**——所有引脚必须全部输出
5. MIPI CSI 差分信号的电压标注为 PHY 供电域（如 `"0.75V (VDDA_0V75_S0)"`），不得写推测值

---

## 五、版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0 | — | 初始（隐式，未成文） |
| 2.0 | 2026-06-15 | 正式成文：新增 meta 元信息、T6 方向枚举、T7 checks 结构统一、MIPI 电压标注规范、F2 字段不存在时必须报错 |

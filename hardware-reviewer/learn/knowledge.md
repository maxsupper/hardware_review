# Unified Self-Learning Knowledge Base

> Auto-generated, auto-read, auto-executed by agents. Categorized as [FIX] (reactive) and [TEMPLATE] (proactive), sharing a maturity tracking system.
> Language: English (to avoid encoding corruption from agent tool chains)

---

## Entry Structure

| Field | Description |
|---|---|
| `ID` | Unique identifier: F = Fix / T = Template |
| `Type` | [FIX] reactive repair / [TEMPLATE] proactive prevention |
| `Trigger` | When agent should match this entry (feature match, not project name match) |
| `Action` | Automatic operation to perform when matched |
| `Source` | Projects that triggered this entry's creation |
| `Hits` | Total times triggered and successfully applied |
| `Maturity` | 1-5, affects execution priority and upgrade decisions |
| `Last Hit` | Most recent project and timestamp |
| `Cross-Project` | Whether validated across >=2 different chip platforms |

### Execution Priority

| Maturity | Behavior |
|:---:|------|
| 1-2 | Reference execution, label `Based on K-{ID} check`, skippable (must state reason) |
| 3-4 | Should execute, label `Based on K-{ID} check`, skip requires recording reason |
| 5 | **Force execute**, label `Mandatory check K-{ID}`, skip forbidden |

### Upgrade Rules

| Hits | Action |
|:---:|------|
| 1-2 | Track counter only |
| 3 | **Proactively ask engineer**: "K-{ID} has hit 3 times (across N projects). Recommend upgrading to hardware-reviewer/ rules file. Reason: [scenario and impact]. Approve?" |
| 3+ (confirmed) | Mark `synced to rules`, keep entry but no repeated suggestions |

### Cross-Project Validation
When an entry has been successfully applied on >= 2 different chip platforms (e.g. RK3588 and RK3576), mark as "cross-project validated", maturity auto +1 (cap 5).

---

## [FIX] Reactive Repair — Auto-correct when matching known errors

---

### F-K001: Gate G0 skipped
- **Type**: [FIX]
- **Trigger**: G1 self-audit discovers missing "Step 0.2 IC model->manual match table" or no trace of Steps 0.1-0.5 execution
- **Action**:
  1. Pause current analysis
  2. Return to G0 Step 0.1, recursively search D:\Refbook\ for all PDFs
  3. Regenerate IC->manual match table
  4. Re-produce g0_ic.msg
  5. Print Step 0 results at output start, label [Self-repair K-F001]
- **Source**: KS-1 (2026-06-05)
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KS-1 / 2026-06-05 | **Cross-Project**: No

### F-K002: cellRef suffix misjudged as DNP
- **Type**: [FIX]
- **Trigger**: Conclusion contains "not soldered"/"DNP" judgment based solely on cellRef suffix (e.g. `_NC`, `RESISTOR5_NC`, `CAP_NC`)
- **Action**:
  1. Extract the component's `(instance ...)` declaration from EDN
  2. Search for the component's `portRef` references across all nets
  3. If portRef is non-empty and has remote instanceRef -> correct to "soldered"
  4. If portRef has only one-end connection -> likely test point/single-end component, annotate reason
  5. Label `[Self-repair K-F002]`
- **Source**: V10 (2026-06-15) — DDR ZQ resistor R3801 cellRef=RESISTOR5_NC misjudged as unsoldered
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: No

### F-K003: Power source not traced to driver physical pin
- **Type**: [FIX]
- **Trigger**: Power rail or signal conclusion attributes source to intermediate net name (e.g. `NODE0_1-1V8`, `VCC_1V8`) rather than tracing to the IC physical pin that generates the voltage/signal (SW node, TX pin, etc.)
- **Action**:
  1. Reverse-trace from target net: net -> two-terminal components (inductor/bead/resistor) -> other side net -> continue
  2. Until finding the SW/LX/output pin of the IC generating the voltage, or TX/output pin generating the signal
  3. Correct source attribution, replace with "Uxx.PIN_name -> via Lxx/Cxx -> net"
  4. Label `[Self-repair K-F003]`
- **Source**: KS-1 (2026-06-04) — NODE0_1-1V8 attributed to U118, actual driver was U92
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KS-1 / 2026-06-04 | **Cross-Project**: No

### F-K004: Wrong chip platform parameters applied
- **Type**: [FIX]
- **Trigger**: Current check results contain SoC-specific parameters inconsistent with current chip model (e.g. RK3576 project uses PMUIO1/2 and VCCIO1-6 from RK3588 domain definitions, or vice versa)
- **Action**:
  1. Confirm main chip model from EDN instance property
  2. Look up correct manual path from learn/ic_index.md
  3. If ic_index has no record, re-search for the manual
  4. Re-extract all parameters from the correct manual
  5. Replace all incorrect references with new parameters
  6. Label `[Self-repair K-F004]`
- **Source**: V10 (2026-06-11) — Initial stage applied RK3588 VCCIO domain definitions
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: No

### F-K005: Inferred conclusion lacks manual citation
- **Type**: [FIX]
- **Trigger**: Conclusion labeled INFERRED but evidence cited is from hardware-reviewer/ rule documents rather than IC datasheet original text (with page/table numbers)
- **Action**:
  1. Execute 3-level manual search for this IC: look_at PDF -> multimodal-looker agent -> websearch/Context7
  2. Found -> cite original manual (page/table), upgrade to OK or WARNING
  3. Not found -> downgrade to UNVERIFIED, record all attempted search paths
  4. Label `[Self-repair K-F005]`
- **Source**: KS-1 (2026-06-04) — Multiple IC INFERRED conclusions cited only rule docs, no manual check
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KS-1 / 2026-06-04 | **Cross-Project**: No

### F-K006: Bidirectional component two-end net names not verified
- **Type**: [FIX]
- **Trigger**: CRITICAL or WARNING level conclusion involves two-terminal components (resistor/capacitor/bead/inductor) but the judgment relies on line-number proximity inference without extracting each end's `(net ...)` declaration from EDN for character-by-character comparison
- **Action**:
  1. Locate the component's `(instance ...)` declaration in EDN
  2. Separately search for the component's two portRefs, extract each connected `(netRef ...)`
  3. Compare both net names character-by-character (not "looks similar" pass)
  4. Mismatch -> correct conclusion; match -> supplement EDN line evidence
  5. Label `[Self-repair K-F006]`
- **Source**: KS-1 (2026-06-05) — U111 DIR resistor R794 GND end misjudged as VDD2H due to line shift
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KS-1 / 2026-06-05 | **Cross-Project**: No

### F-K007: Proximity inference — relying on line offset
- **Type**: [FIX]
- **Trigger**: Conclusion about "which net/instance something belongs to" relies on "search upward for nearest bracket" or line offset calculation (rather than extracting EDN structure declarations for verification)
- **Action**:
  1. Search EDN for the component/net's complete structure declaration: `(net NET_NAME ...)` or `(instance INST_NAME ...)`
  2. Extract exact portRef list and instanceRef from the structure declaration
  3. Replace line-offset inference result with structure declaration result
  4. Label `[Self-repair K-F007]`
- **Source**: KS-1 (2026-06-05)
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KS-1 / 2026-06-05 | **Cross-Project**: No

### F-K008: Enumeration-first principle violated
- **Type**: [FIX]
- **Trigger**: Check results present a category of checks as summary statement (e.g. "all DDR chips OK", "all I2C pull-ups correct") rather than per-item independent conclusions
- **Action**:
  1. Execute full enumeration for this category (e.g. DDR: 8 chips x 5 dimensions = 40+ independent conclusions)
  2. Check each item and generate independent conclusion
  3. Label `[Self-repair K-F008]`
- **Source**: KS-1 (2026-06-04) — Pre-delivery found multiple items summarized as "all OK"
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KS-1 / 2026-06-04 | **Cross-Project**: No

### F-K009: Connector Voltage/Domain fill rate insufficient
- **Type**: [FIX]
- **Trigger**: Any connector in evidence JSON has Voltage or Domain fields with UNKNOWN ratio > 20%
- **Action**:
  1. That connector's hw_analyze task result is invalid, return for re-run
  2. Return prompt must include: specific connector ID, UNKNOWN ratio value, re-run requirement (enable VCCIO domain reverse tracing)
  3. Re-verify fill rate after re-run, max 2 rounds
- **Hits**: 1 | **Maturity**: 1/5
- **Last Hit**: 2026-06-17

### F-K010: Peripheral interface type coverage incomplete
- **Type**: [FIX]
- **Trigger**: Number of H2 subsections per peripheral type in report < number of discovered types in evidence JSON
- **Action**:
  1. Compare peripheral_evidence.json discovered field against report section V H2 list
  2. Find missing types, return hw_write to supplement corresponding subsections
  3. Forbidden: output only partial types claiming "representative sample"
- **Hits**: 1 | **Maturity**: 1/5
- **Last Hit**: 2026-06-17

### F-K011: Connector signal name vs SoC peripheral name confusion
- **Type**: [FIX]
- **Trigger**: Report connector pin signal names contain peripheral numbers (I2Cx/SPIx/UARTx) but EDN trace shows actual connected SoC peripheral number is different
- **Action**:
  1. For each connector pin, annotate both "connector-side label" and "SoC-side actual peripheral" columns
  2. If the two peripheral numbers differ, output WARNING with EDN trace path
  3. Report must explain the principle "connector label != SoC peripheral number"
- **Hits**: 1 | **Maturity**: 1/5
- **Last Hit**: 2026-06-17

### F-K012: Report data structured table truncation
- **Type**: [FIX]
- **Trigger**: Report table row count < corresponding data entry count in evidence JSON (e.g. connector pin table rows < total pin count)
- **Action**:
  1. Post-report self-check: compare each section's table row count against evidence JSON entry count
  2. Mismatched sections, return hw_write for completion
  3. hw_write must output per-row, forbidden to replace actual table with "(N rows total)"
- **Hits**: 1 | **Maturity**: 1/5
- **Last Hit**: 2026-06-17

### F-K026: hardware_review self-generates evidence instead of delegating
- **Type**: [FIX]
- **Trigger**: hardware_review agent produces evidence JSON (e.g. `*_evidence.json` or `*_summary.json`) by calling write/bash directly instead of delegating to a hw_analyze sub-agent via `task(subagent_type="hw_analyze", ...)`
- **Action**:
  1. Stop current evidence generation immediately
  2. Review the analysis scope and decompose into chip-level or dimension-level hw_analyze tasks
  3. Each hw_analyze task prompt must include: IC manual path, P1-P6 constraints, evidence/summary output format
  4. Launch hw_analyze via `task(subagent_type="hw_analyze", run_in_background=true, ...)`
  5. Collect results, verify evidence JSON schema compliance
  6. Label `[Self-repair K-F026]`
- **Source**: KQ-BZK2412-A-0430 (2026-06-23) — hardware_review generated evidence directly, context exhausted
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KQ-BZK2412-A-0430 / 2026-06-23 | **Cross-Project**: No

### F-K027: hw_auditor FAIL bypassed without auto-fix cycle
- **Type**: [FIX]
- **Trigger**: hw_auditor sub-agent output contains `overall_status == "FAIL"` but hardware_review does not initiate re-execution of the failing sub-agent(s); instead proceeds to the next stage or claims completion
- **Action**:
  1. Read the full hw_auditor result immediately (do not wait for manual confirmation)
  2. Parse each FAIL item, locate the failing stage (G0 / hw_prep / hw_analyze / hw_write)
  3. For each failing stage, re-run the corresponding sub-agent via `task(...)` with the original prompt + a note about "Re-run due to hw_auditor FAIL: {FAIL_ID}: {reason}"
  4. After all re-runs complete, re-invoke hw_auditor
  5. Max 3 rounds for the same issue type. Round 3 still FAIL → record in `gates/auto_fix_log.json` and output to report unresolved section
  6. Label `[Self-repair K-F027]`
- **Source**: KQ-BZK2412-A-0430 (2026-06-23) — hw_auditor FAIL not actioned before claiming completion
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KQ-BZK2412-A-0430 / 2026-06-23 | **Cross-Project**: No

---

## [TEMPLATE] Proactive Prevention — Load parameterized check flow when entering known scenario
> Core constraint:
> - Only inherit **check flow and methods**, not values (voltage, resistance, quantity)
> - All values must be extracted from current project's EDN netlist + current chip's datasheet
> - `{...}` denotes placeholder, must be filled from current project data

---

### T-K001: I2C bus pull-up verification
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_SCL` or `*_SDA` (at least one I2C bus exists)
- **Action**:
  1. Enumerate all I2C buses (group by net name: SCL_n + SDA_n as one pair)
  2. Per bus: trace SCL/SDA -> confirm whether through pull-up resistor -> confirm pull-up connected to correct VCCIO voltage rail
  3. Verify resistance range: 2.2kOhm~10kOhm (confirm exact recommended value from current IC datasheet)
  4. Multi-device on same bus: check I2C address conflicts (extract and compare address tables from each datasheet)
  5. Output independent conclusion per bus (OK/WARNING/CRITICAL)
- **Source**: V01 (2026-05), V10 (2026-06), KS-1 (2026-06)
- **Hits**: 6 | **Maturity**: 5/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: Yes (RK3588 / RK3576 / MP2975 three different platforms)
- **Upgrade**: Synced to interface_check_rules.md section 3.1 (2026-06-16)

### T-K002: DDR ZQ calibration resistor
- **Type**: [TEMPLATE]
- **Trigger**: EDN instances contain DDR particles (LPDDR4/DDR4/DDR3), cellRef matches `*DDR*` / `*LPDDR*` / `*SDRAM*`
- **Action**:
  1. Confirm particle model and count (extract from EDN property Value)
  2. Extract ZQ calibration resistor recommended value from {DDR_datasheet} (standard LPDDR4=240Ohm 1%, DDR4=240Ohm 1%)
  3. Trace each particle's ZQ pin -> resistor -> to GND complete path
  4. Verify resistor value = {datasheet recommended value}
  5. cellRef `_NC` trap: do not judge unsoldered from cellRef suffix, use portRef as standard
  6. Independent conclusion per particle
- **Source**: V01 (2026-05): RK3588+2xLPDDR4 | V10 (2026-06): RK3576+1xLPDDR4
- **Hits**: 4 | **Maturity**: 4/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: Yes (RK3588 / RK3576)

### T-K003: Level shifter direction and supply configuration
- **Type**: [TEMPLATE]
- **Trigger**: EDN instance cellRef matches level shifter model features (`MS4553*` / `TXS01*` / `TXB01*` / `PCA9306*` / `SN74LVC*T45*` / `NTS01*` etc.)
- **Action**:
  1. Extract level shifter model, from {datasheet} check VCCA/VCCB allowed range and direction control method
  2. Trace VCCA supply source -> confirm voltage within manual range, corresponds to A-side signal VCCIO domain
  3. Trace VCCB supply source -> same, corresponds to B-side
  4. Check DIR/OE pins:
     - Fixed direction type: trace DIR pin pull-up/pull-down -> confirm direction matches signal flow (TX->RX)
     - Auto-direction type: check pull-up resistor configuration
     - OE enable: confirm OE active level matches supply
  5. Check A/B side signals all within respective VCCIO domain voltage range
- **Source**: V10 (2026-06): MS4553S VCCA=1.8V/VCCB=3.3V | KS-1 (2026-06): TXS0108
- **Hits**: 4 | **Maturity**: 4/5
- **Last Hit**: KS-1 / 2026-06 | **Cross-Project**: Yes (RK3576 / standalone FPGA platform)

### T-K004: PMIC power sequencing and EN chain
- **Type**: [TEMPLATE]
- **Trigger**: EDN contains PMIC instances, cellRef matches `*PMIC*` / `*PMU*` / `*RK80*` / `*MP29*` / `*MPQ*` etc.
- **Action**:
  1. From {PMIC_datasheet} extract per-rail EN threshold, PG polarity, soft-start time
  2. Per-rail trace EN pin source (previous rail PG, external GPIO, or fixed enable)
  3. Draw EN->PG cascade diagram, verify power-up sequence
  4. Cross-check multi-rail Power Sequencing constraints from {SoC_datasheet}
  5. Verify divider resistors: Vout = Vref x (1 + R1/R2), compare against EDN actual resistor values
  6. Non-programmable PMIC: confirm hardware strap matches target voltage
  7. Output independent conclusion per power rail
- **Source**: V01 (2026-05): RK806 | V10 (2026-06): RK806S-5 | KS-1 (2026-06): MP2975+MPQ7920
- **Hits**: 5 | **Maturity**: 4/5
- **Last Hit**: KS-1 / 2026-06 | **Cross-Project**: Yes (Rockchip / MPS two completely different PMIC series)
- **Upgrade**: Synced to power_check.md section 1 (2026-06-16)

### T-K005: Connector per-pin complete tracing
- **Type**: [TEMPLATE]
- **Trigger**: EDN contains connector instances (matches `*CON*` / `*HEADER*` / `*DF40*` / `*J*` with >2 pins)
- **Action**:
  1. Enumerate all connectors
  2. Per connector, per pin:
     - Extract portRef from EDN -> net -> remote instanceRef -> signal function
     - Annotate: Pin number / Net name / Signal definition / Direction(IN/OUT/BIDIR/PWR/GND/NC) / Voltage level / Source IC / Function notes
  3. Board-to-board connectors: if remote function cannot be determined, mark "inter-board, awaiting remote function confirmation"
  4. Direction judgment: from signal driver perspective (SoC TX -> connector = OUTPUT)
  5. NC/unconnected pins MUST be listed per-row, NOT summarized as ranges
- **Source**: V01 (2026-05): 7 connectors 198pin | V10 (2026-06): 8 connectors 253pin | KS-1 (2026-06): 5 connectors 120pin
- **Hits**: 6 | **Maturity**: 5/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: Yes
- **Upgrade**: Synced to pin_check_rules.md connector output format (2026-06-16)

### T-K006: Floating pins vs design reserved classification
- **Type**: [TEMPLATE]
- **Trigger**: SoC/DDR/PMIC or other critical IC has pins with no net connection in EDN
- **Action**:
  1. Full enumeration of target IC's all pins -> compare against EDN portRef -> list unconnected pins
  2. From {SoC_datasheet} extract "Must-Connect" pin checklist -> per-pin verify -> missed connection = CRITICAL
  3. From {SoC_datasheet} extract "NC/Reserved" (internal not connected/test reserved) pin checklist -> not connected = OK
  4. Pins not in above two categories -> WARNING (requires manual design intent confirmation)
  5. Forbidden: mark all unconnected pins as "floating" without checking manual
- **Source**: V10 (2026-06): RK3576, ~20 floating, 0 Must-Connect missed
- **Hits**: 3 | **Maturity**: 3/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: No

### T-K007: Boot configuration resistor verification
- **Type**: [TEMPLATE]
- **Trigger**: {SoC_datasheet} contains "Boot Configuration" chapter describing power-up sampling of specific GPIO levels to determine boot mode
- **Action**:
  1. From {SoC_datasheet} extract boot config pin checklist + level-to-mode mapping table
  2. Trace each config pin's pull-up/pull-down resistor in EDN
  3. Verify resistor values (pull-up typical 10kOhm, pull-down typical 1kOhm~10kOhm)
  4. Verify multi-pin combination values match expected boot mode
- **Source**: V10 (2026-06): RK3576 SARADC_IN0_BOOT
- **Hits**: 4 | **Maturity**: 3/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: No

### T-K008: PCIe differential pair and AC coupling
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_PET*` / `*_PER*` / `*_PCIE*_TX*` / `*_PCIE*_RX*` / `*_REFCLK*`
- **Action**:
  1. Identify each PCIe lane TX/RX differential pair (P/N polarity)
  2. TX(P) should connect to remote RX(P), TX(N) to RX(N), no crossing
  3. AC coupling capacitor: TX path per lane (PCIe Gen3+: 100nF~220nF), RX path typically no capacitor
  4. REFCLK differential pair polarity check (if reference clock present)
  5. PERST# / WAKE# / CLKREQ# etc. sideband signal checks
- **Source**: V01 (2026-05): RK3588 PCIe x4 | KS-1 (2026-06): FPGA->PCIe Switch
- **Hits**: 4 | **Maturity**: 4/5
- **Last Hit**: KS-1 / 2026-06 | **Cross-Project**: Yes (RK3588 / FPGA)

### T-K009: Peripheral interface dynamic discovery
- **Type**: [TEMPLATE]
- **Trigger**: EDN parsing complete, net list available
- **Action**:
  1. From all net names match by protocol features, discover all peripheral types:
     - `*_SCL/*_SDA` -> I2C
     - `*_TX/*_RX` / `*_TXD/*_RXD` -> UART
     - `*_MOSI/*_MISO/*_SCK/*_CS` -> SPI
     - `*_CK*/*_DQS*/*_DQ*/*_DM*` -> DDR
     - `*_DP/*_DM` / `*_USB*` / `*_VBUS` -> USB
     - `*_TDI/*_TDO/*_TMS/*_TCK` -> JTAG
     - `*_PER*/*_PET*/*_REFCLK*` -> PCIe
     - `*_CLK*/*_DAT*/*_CMD*` / `*_EMMC*` / `*_SD*` -> eMMC/SD
     - `*_PWM*/*_TACH*` / `*_FAN*` -> FAN
     - `*_MIPI*` / `*_CSI*` / `*_DSI*` -> MIPI
     - `*_HDMI*` / `*_TMDS*` / `*_DDC*` -> HDMI
     - `*_RS232*` / `*_RS485*` / `*_RS422*` -> Serial
     - Unmatched -> "Other", mark for manual confirmation
  2. Coverage confirmation: output must include ALL discovered peripheral types, no pre-defined checklist-only
  3. For each discovered peripheral type, load corresponding [TEMPLATE] entry (if exists)
- **Source**: V10 (2026-06), KS-1 (2026-06)
- **Hits**: 5 | **Maturity**: 4/5
- **Last Hit**: V10 / 2026-06-17 | **Cross-Project**: Yes

### T-K010: GMAC/RGMII Ethernet PHY check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net name match `*_MDC` / `*_MDIO` / `*GMAC*` / `*RGMII*` / `*ETH*`, or cellRef matches PHY features
- **Action**:
  1. MDC/MDIO: check pull-up resistor (1.5k-4.7kOhm), confirm PHY address pins don't conflict
  2. Clock source: confirm 25MHz/50MHz/125MHz provided by SoC or PHY
  3. RGMII Delay: 2ns data setup/hold, via PHY register/SoC config/PCB routing
  4. PHY reset: RESET to SoC GPIO, proper pull-down/-up
  5. Transformer center tap: voltage-drive to VCC, current-drive to cap-to-GND; Bob Smith circuit check
  6. LED current-limit resistors
- **Source**: V10 (2026-06-17) — RK3576 + GMAC RGMII
- **Hits**: 2 | **Maturity**: 5/5
- **Upgrade**: Force check (2026-06-18 confirmed)

### T-K011: CIF parallel camera interface check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `CIF_*` (parallel CMOS image sensor, 8/10/12/16bit data bus)
- **Action**:
  1. I2C/CCI control bus: check camera config bus correctly connected with pull-ups
  2. MCLK and PCLK: series resistors near source
  3. Data bit width alignment: confirm camera output width matches SoC CIF controller (8/10/12-bit)
  4. Sync signals: PCLK/HSYNC/VSYNC level domain consistency
  5. PWDN/RESET control: verify polarity per sensor datasheet
  6. Power rails: CAM supply voltages match datasheet
- **Source**: V10 (2026-06-17) — RK3576 + CIF 8-bit Parallel
- **Hits**: 2 | **Maturity**: 5/5
- **Upgrade**: Force check (2026-06-18 confirmed)

### T-K012: SENSOR control signal check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `SENSOR_*`
- **Action**: Enumerate all SENSOR_* signals, group by function (RSTN/CLK/HS/VS/PWDN). Check RSTN polarity, RC delay matching sensor datasheet reset window. Verify SENSOR_CLK frequency. Check HS/VS voltage domain vs SoC receiver VCCIO.
- **Source**: V10 (2026-06-17) — RK3576 + 3ch SENSOR
- **Hits**: 2 | **Maturity**: 5/5 | **Upgrade**: Force check

### T-K013: UART check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_TXD` / `*_RXD` / `*_TX` / `*_RX` (exclude MIPI/PCIe TX/RX)
- **Action**: Confirm TX/RX cross-connect. Level match between SoC IO and peripheral. Backfeed prevention (series 22-100Ohm). Idle TX default HIGH. Debug UART: near connector, ESD protection.
- **Source**: V10 (2026-06-17) — RK3576 multi-UART
- **Hits**: 2 | **Maturity**: 5/5 | **Upgrade**: Force check

### T-K014: SPI bus check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_MOSI` / `*_MISO` / `*_SCK` / `*_SCLK` / `*_SPI_CS*` / `*_SPI_CLK`
- **Action**: Signal integrity (series 22-33Ohm near TX). CS pull-up (4.7k-10kOhm to VCC) per slave. Multi-slave: independent CS or decoder. Long-distance: buffer driver. Master/slave mode config. One-to-one CLK/MOSI/MISO.
- **Source**: V10 (2026-06-17) — RK3576 SPI
- **Hits**: 2 | **Maturity**: 5/5 | **Upgrade**: Force check

### T-K015: USB interface check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_USB*` / `*_OTG*` / `*_VBUS` / `*_DM` / `*_DP`
- **Action**: USB2.0 DM/DP polarity check. USB3.0 TX->RX cross and AC coupling (TX only). VBUS 5V source and over-current. OTG_ID config. ESD protection near connector.
- **Source**: V10 (2026-06-17) — RK3576 USB2 OTG
- **Hits**: 2 | **Maturity**: 5/5 | **Upgrade**: Force check

### T-K016: MIPI D-PHY/C-PHY check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_MIPI*` / `*_DPHY*` / `*_CPHY*` (MIPI CSI/DSI)
- **Action**: AC coupling (if required by spec). P->P, N->N polarity; Lane Swap support. Data/Clock lane pairing. ESD protection: TVS parasitic cap <0.5pF ideal <0.2pF. Peripheral multi-rail power (AVDD/DVDD/IOVDD). No arbitrary pull-up/cap on signal lines.
- **Source**: V10 (2026-06-17) — RK3576 MIPI D-PHY 4-Lane CSI
- **Hits**: 2 | **Maturity**: 5/5 | **Upgrade**: Force check

### T-K017: HDMI/DisplayPort check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_HDMI*` / `*_TMDS*` / `*_DDC*` / `*_CEC*` / `*_HPD*` / `*DP_*`
- **Action**: TMDS polarity. DDC (I2C) pull-up cross-ref T-K001. HPD direction + ESD. CEC pull-up 3.3V + ESD. VDDA_HDMI decoupling. Level shifter cross-ref T-K003.
- **Source**: V10 (2026-06-17) — RK3576 HDMI
- **Hits**: 2 | **Maturity**: 1/5

### T-K018: SARADC/TSADC analog input check
- **Type**: [TEMPLATE]
- **Trigger**: EDN net names match `*_SARADC*` / `*_TSADC*`
- **Action**: Enumerate all ADC input channels. Per-channel: verify divider ratio within ADC range, check decoupling cap (100nF). KEY detection: verify voltage spacing >200mV. HW_ID/voltage detection: verify divider 1% accuracy.
- **Source**: V10 (2026-06-17) — RK3576 SARADC KEY/RECOVERY/HW_ID
- **Hits**: 2 | **Maturity**: 1/5

---

## Restored Entries (2026-06-23 - recovered after agent encoding corruption)

> These entries were lost when an agent corrupted knowledge.md. Now restored.
> Check logic also integrated into hw_analyze mandatory parameter checklist (#13) — triggers without template match.

### F-K020: BOM NC x Netlist cross-validation
- **Type**: [FIX]
- **Trigger**: IC status=NOT_FOUND and notes contain "NC"/"not soldered"
- **Action**: Query all pin->net connections in nets.json for this IC. If functional pins are connected -> [CRITICAL]
- **Source**: KQ-BZK2412-A-0430 U15 SGM58031
- **Hits**: 1 | **Maturity**: 2/5

### F-K021: Net name x topology source verification
- **Type**: [FIX]
- **Trigger**: Net name contains "FPGA_"/"CPU_"/"CPLD_"/"SOC_" prefix
- **Action**: Check if net node contains matching IC pins. If not -> [WARNING] MISLABELED
- **Source**: KQ-BZK2412-A-0430 FPGA_EN_VCORE
- **Hits**: 1 | **Maturity**: 2/5

### F-K022: Manual power domain x Netlist voltage comparison
- **Type**: [FIX]
- **Trigger**: Any IC power domain check
- **Action**: net -> bead -> LDO/DC-DC VOUT -> manual parameter comparison. Forbidden: claim "no net" when net exists.
- **Source**: KQ-BZK2412-A-0430 ADCVCC 3.3V != required 1.8V
- **⛔ Integrated into hw_analyze mandatory parameter checklist. Triggers without template match.**
- **Hits**: 1 | **Maturity**: 3/5

### F-K023: PGOOD signal x receiver threshold matching
- **Type**: [FIX]
- **Trigger**: Any PG signal trace. Must trace to final receiving IC pin.
- **Source**: KQ-BZK2412-A-0430 VCORE_PG
- **Hits**: 1 | **Maturity**: 2/5

### F-K024: Series resistor multi-hop tracing
- **Type**: [FIX]
- **Trigger**: Signal passes through R/C/L/FB to another net. Minimum 2 hops: IC_A.pin -> R_X.1 -> net_A -> R_X.2 -> net_B -> IC_B.pin.
- **Source**: KQ-BZK2412-A-0430 U15.AIN0<-R272<-VCC5V
- **Hits**: 1 | **Maturity**: 2/5


### F-K025: Net-to-net bridging via two-terminal components not checked
- **Type**: [FIX]
- **Trigger**: A finding concludes "net X does not connect to expected load Y" based solely on tracing net X's connection list, WITHOUT checking whether any two-terminal component (0Ω resistor, ferrite bead, inductor) on net X bridges to a differently-named net that DOES contain load Y.
- **Action**:
  1. For every two-terminal component (R/FB/L with pins &1 and &2) on the traced net, extract the OTHER pin's net from nets.json.
  2. Check if the bridged net contains the expected loads.
  3. Pay special attention to 0Ω resistors — they are intentional jumpers that create net name boundaries while maintaining electrical connection.
  4. Also check ferrite beads: FB.pinA → net_A, FB.pinB → net_B → load may be on net_B.
  5. If bridge found → correct the finding to "OK, connected via {component}" and note the net name boundary.
  6. Label `[Self-repair K-F025]`
- **Source**: KQ-BZK2412-A-0430 (2026-06-23) — DDR4-F002 falsely reported as "VTT not routed to DDR4" because only VTT_L net was traced; R202 (0Ω) bridges VTT_L ↔ VTT net which contains RN1-RN6. Finding retracted after re-trace.
- **Hits**: 1 | **Maturity**: 2/5
- **Last Hit**: KQ-BZK2412-A-0430 / 2026-06-23 | **Cross-Project**: No

### T-K019: FMP100 VCCADC specific check
- **Type**: [TEMPLATE]
- **Trigger**: FMP100 series FPGA
- **Action**: Extract VCCADC from manual (section 7.1.5: 1.8V +/-5%). Find net "ADCVCC"/"VCCADC"/"F0_VCCADC*". Trace through FB/RC filter. Compare source voltage — common mistake: incorrectly connected to VCC3V3.
- **⛔ Also covered by hw_analyze mandatory parameter checklist "Recommended Operating Conditions"**
- **Source**: KQ-BZK2412-A-0430
- **Hits**: 1 | **Maturity**: 3/5

### T-K020: E2000Q power domain check
- **Type**: [TEMPLATE]
- **Trigger**: Platform = Phytium E2000
- **Action**: Extract all power domains from manual. Search nets.json for each. Reverse-trace each to DC-DC/LDO. Compare voltages.
- **Source**: KQ-BZK2412-A-0430
- **Hits**: 1 | **Maturity**: 3/5

---

## Auto-Discovery Flow — How new entries are generated

After session (G6 closure passed):

1. Scan learn/corrections.md for new correction records
   - Does this correction match existing F-K0XX entry? → YES: Hits +1
   - NO: continue
   - Is this a "generalizable error pattern"? (Remove project-specific values, still describable as trigger -> action)
     - YES: Generate new [FIX] entry (maturity=1, hits=1)
     - NO: Record only in corrections.md, no FIX generated

2. Scan check flows successfully applied this session
   - Has this flow appeared in previous projects? (Same signal features, same check dimension = possible pattern)
     - YES: Extract common check actions, remove project-specific values
     - Is the common flow complete and executable?
       - YES: Generate candidate [TEMPLATE] entry (maturity=1, hits=1)
       - NO: Abandon (too project-specific, cannot generalize)

3. Cross-project validation: New entry applied on >=2 different chip platforms → maturity +1, mark "Cross-Project: Yes"

4. Upgrade suggestion: Hits >=3 or maturity = 5 → write to learn/suggestions.md → proactively ask engineer

---

## Anti-Contamination Constraints

> Agent using this knowledge base must obey:

| # | Constraint | Description |
|---|-----------|------|
| C1 | Inherit flow only, not values | "Check I2C per T-K001 flow" NOT "V01 pull-up 4.7kOhm so here too" |
| C2 | Verified through current project data | Template tells agent "what to check", conclusions must come from current EDN + current chip manual |
| C3 | Example values are reference ranges only | "Typical 240Ohm" is hint to look at ZQ, actual value per current datasheet |
| C4 | {placeholder} must be filled | Before executing template, must extract data from current project to fill all placeholders |
| C5 | No cross-platform inference | RK3576 VCCIO domains != RK3588 VCCIO domains. Each project independently extracts chip parameters from its manual |

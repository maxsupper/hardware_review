# RK3588 PinOut List

> Source: RK3588_PinOut_V1.1_20220922.xlsx
> 1088 pins, 149 GPIO

## GPIO -> Domain

| Domain | Pins | Count |
|--------|------|-------|
| EMMCIO_1V8 | GPIO2_A0, GPIO2_A1, GPIO2_A2, GPIO2_A3, GPIO2_D0, GPIO2_D1, GPIO2_D2, GPIO2_D3, GPIO2_D4, GPIO2_D5, GPIO2_D6, GPIO2_D7 | 12 |
| PMUIO1 | GPIO0_A0, GPIO0_A1, GPIO0_A2, GPIO0_A3, GPIO0_A4, GPIO0_A5, GPIO0_A6, GPIO0_A7, GPIO0_B0, GPIO0_B1, GPIO0_B2, GPIO0_B3 | 12 |
| PMUIO2 | GPIO0_B5, GPIO0_B6, GPIO0_B7, GPIO0_C0, GPIO0_C1, GPIO0_C2, GPIO0_C3, GPIO0_C4, GPIO0_C5, GPIO0_C6, GPIO0_C7, GPIO0_D0, GPIO0_D1, GPIO0_D2, ... (+4) | 18 |
| VCCIO1 | GPIO1_C0, GPIO1_C1, GPIO1_C2, GPIO1_C3, GPIO1_C4, GPIO1_C5, GPIO1_C6, GPIO1_C7, GPIO1_D0, GPIO1_D1, GPIO1_D2, GPIO1_D3, GPIO1_D4, GPIO1_D5 | 14 |
| VCCIO2 | GPIO4_D0, GPIO4_D1, GPIO4_D2, GPIO4_D3, GPIO4_D4, GPIO4_D5 | 6 |
| VCCIO3 | GPIO2_A6, GPIO2_A7, GPIO2_B0, GPIO2_B1, GPIO2_B2, GPIO2_B3, GPIO2_B4, GPIO2_B5, GPIO2_B6, GPIO2_B7, GPIO2_C0, GPIO2_C1, GPIO2_C2, GPIO2_C3, ... (+7) | 21 |
| VCCIO4 | GPIO1_A0, GPIO1_A1, GPIO1_A2, GPIO1_A3, GPIO1_A4, GPIO1_A5, GPIO1_A6, GPIO1_A7, GPIO1_B0, GPIO1_B1, GPIO1_B2, GPIO1_B3, GPIO1_B4, GPIO1_B5, ... (+4) | 18 |
| VCCIO5 | GPIO3_A0, GPIO3_A1, GPIO3_A2, GPIO3_A3, GPIO3_A4, GPIO3_A5, GPIO3_A6, GPIO3_A7, GPIO3_B0, GPIO3_B1, GPIO3_B2, GPIO3_B3, GPIO3_B4, GPIO3_B5, ... (+16) | 30 |
| VCCIO6 | GPIO4_A0, GPIO4_A1, GPIO4_A2, GPIO4_A3, GPIO4_A4, GPIO4_A5, GPIO4_A6, GPIO4_A7, GPIO4_B0, GPIO4_B1, GPIO4_B2, GPIO4_B3, GPIO4_B4, GPIO4_B5, ... (+4) | 18 |

## Full Table


### DDR_CH0 (98p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| U1 | DDR_CH0_DQ0_A | - | I/O | - |
| T2 | DDR_CH0_DQ1_A | - | I/O | - |
| T1 | DDR_CH0_DQ2_A | - | I/O | - |
| R2 | DDR_CH0_DQ3_A | - | I/O | - |
| W1 | DDR_CH0_DQ4_A | - | I/O | - |
| V2 | DDR_CH0_DQ5_A | - | I/O | - |
| V1 | DDR_CH0_DQ6_A | - | I/O | - |
| U2 | DDR_CH0_DQ7_A | - | I/O | - |
| AB2 | DDR_CH0_DQ8_A | - | I/O | - |
| AB1 | DDR_CH0_DQ9_A | - | I/O | - |
| AC1 | DDR_CH0_DQ10_A | - | I/O | - |
| AC2 | DDR_CH0_DQ11_A | - | I/O | - |
| Y1 | DDR_CH0_DQ12_A | - | I/O | - |
| Y2 | DDR_CH0_DQ13_A | - | I/O | - |
| AA1 | DDR_CH0_DQ14_A | - | I/O | - |
| AA2 | DDR_CH0_DQ15_A | - | I/O | - |
| V7 | DDR_CH0_WCK0P_A | - | O | - |
| V6 | DDR_CH0_WCK0N_A | - | O | - |
| W4 | DDR_CH0_WCK1P_A | - | O | - |
| W5 | DDR_CH0_WCK1N_A | - | O | - |
| U5 | DDR_CH0_DQS0P_A | - | I/O | - |
| U4 | DDR_CH0_DQS0N_A | - | I/O | - |
| AA5 | DDR_CH0_DQS1P_A | - | I/O | - |
| AA4 | DDR_CH0_DQS1N_A | - | I/O | - |
| Y4 | DDR_CH0_DM0_A | - | I/O | - |
| AB4 | DDR_CH0_DM1_A | - | I/O | - |
| T7 | DDR_CH0_A0_A | - | O | - |
| T8 | DDR_CH0_A1_A | - | O | - |
| P4 | DDR_CH0_A2_A | - | O | - |
| P5 | DDR_CH0_A3_A | - | O | - |
| R1 | DDR_CH0_A4_A | - | O | - |
| P2 | DDR_CH0_A5_A | - | O | - |
| T5 | DDR_CH0_A6_A | - | O | - |
| N2 | DDR_CH0_CK_A | - | O | - |
| N1 | DDR_CH0_CKB_A | - | O | - |
| R6 | DDR_CH0_LP4/4X_CS0_A | - | O | - |
| R7 | DDR_CH0_LP4/4X_CS1_A | - | O | - |
| P7 | DDR_CH0_LP4/4X_CKE0/LP5_CS0_A | - | O | - |
| N7 | DDR_CH0_LP4/4X_CKE1/LP5_CS1_A | - | O | - |
| W8 | DDR_CH0_ZQ_A | - | AI | - |
| T4 | DDR_CH0_RESET_A | - | O | - |
| H1 | DDR_CH0_DQ0_B | - | I/O | - |
| J2 | DDR_CH0_DQ1_B | - | I/O | - |
| J1 | DDR_CH0_DQ2_B | - | I/O | - |
| K2 | DDR_CH0_DQ3_B | - | I/O | - |
| F1 | DDR_CH0_DQ4_B | - | I/O | - |
| G2 | DDR_CH0_DQ5_B | - | I/O | - |
| G1 | DDR_CH0_DQ6_B | - | I/O | - |
| H2 | DDR_CH0_DQ7_B | - | I/O | - |
| D2 | DDR_CH0_DQ8_B | - | I/O | - |
| C1 | DDR_CH0_DQ9_B | - | I/O | - |
| C2 | DDR_CH0_DQ10_B | - | I/O | - |
| B1 | DDR_CH0_DQ11_B | - | I/O | - |
| F2 | DDR_CH0_DQ12_B | - | I/O | - |
| E1 | DDR_CH0_DQ13_B | - | I/O | - |
| E2 | DDR_CH0_DQ14_B | - | I/O | - |
| D1 | DDR_CH0_DQ15_B | - | I/O | - |
| K5 | DDR_CH0_WCK0P_B | - | O | - |
| K4 | DDR_CH0_WCK0N_B | - | O | - |
| H4 | DDR_CH0_WCK1P_B | - | O | - |
| H5 | DDR_CH0_WCK1N_B | - | O | - |
| J8 | DDR_CH0_DQS0P_B | - | I/O | - |
| J7 | DDR_CH0_DQS0N_B | - | I/O | - |
| F5 | DDR_CH0_DQS1P_B | - | I/O | - |
| F4 | DDR_CH0_DQS1N_B | - | I/O | - |
| G4 | DDR_CH0_DM0_B | - | I/O | - |
| E4 | DDR_CH0_DM1_B | - | I/O | - |
| M8 | DDR_CH0_A0_B | - | O | - |
| M5 | DDR_CH0_A1_B | - | O | - |
| N5 | DDR_CH0_A2_B | - | O | - |
| N4 | DDR_CH0_A3_B | - | O | - |
| K1 | DDR_CH0_A4_B | - | O | - |
| L2 | DDR_CH0_A5_B | - | O | - |
| M7 | DDR_CH0_A6_B | - | O | - |
| M2 | DDR_CH0_CK_B | - | O | - |
| M1 | DDR_CH0_CKB_B | - | O | - |
| L7 | DDR_CH0_LP4/4X_CS0_B | - | O | - |
| L8 | DDR_CH0_LP4/4X_CS1_B | - | O | - |
| L5 | DDR_CH0_LP4/4X_CKE0/LP5_CS0_B | - | O | - |
| L4 | DDR_CH0_LP4/4X_CKE1/LP5_CS1_B | - | O | - |
| H7 | DDR_CH0_ZQ_B | - | AI | - |
| K7 | DDR_CH0_RESET_B | - | O | - |
| U11 | DDR_CH0_VDD_0 | 0.75V-0.85V | PI | - |
| T12 | DDR_CH0_VDD_1 | - | PI | - |
| R12 | DDR_CH0_VDD_2 | - | PI | - |
| P12 | DDR_CH0_VDD_3 | - | PI | - |
| M10 | DDR_CH0_VDDQ_0 | 0.6V/0.5V | PI | - |
| N10 | DDR_CH0_VDDQ_1 | - | PI | - |
| P10 | DDR_CH0_VDDQ_2 | - | PI | - |
| R10 | DDR_CH0_VDDQ_3 | - | PI | - |
| T10 | DDR_CH0_VDDQ_4 | - | PI | - |
| L10 | DDR_CH0_VDDQ_CK | 0.6V/0.5V | PI | - |
| N8 | DDR_CH0_VDDQ_CKE | 1.1V/1.05V | PI | - |
| N13 | DDR_CH0_VDD_MIF_0 | 0.75V-0.85V | PI | - |
| P13 | DDR_CH0_VDD_MIF_1 | - | PI | - |
| N12 | DDR_CH0_PLL_DVDD | 0.75V-0.85V | PI | - |
| M12 | DDR_CH0_PLL_AVDD1V8 | 1.8V | API | - |
| M11 | DDR_CH0_PLL_AVSS | - | G | - |

### DDR_CH1 (98p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| A8 | DDR_CH1_DQ0_C | - | I/O | - |
| B9 | DDR_CH1_DQ1_C | - | I/O | - |
| A9 | DDR_CH1_DQ2_C | - | I/O | - |
| B10 | DDR_CH1_DQ3_C | - | I/O | - |
| A6 | DDR_CH1_DQ4_C | - | I/O | - |
| B7 | DDR_CH1_DQ5_C | - | I/O | - |
| A7 | DDR_CH1_DQ6_C | - | I/O | - |
| B8 | DDR_CH1_DQ7_C | - | I/O | - |
| A3 | DDR_CH1_DQ8_C | - | I/O | - |
| B3 | DDR_CH1_DQ9_C | - | I/O | - |
| A2 | DDR_CH1_DQ10_C | - | I/O | - |
| B2 | DDR_CH1_DQ11_C | - | I/O | - |
| A5 | DDR_CH1_DQ12_C | - | I/O | - |
| B5 | DDR_CH1_DQ13_C | - | I/O | - |
| A4 | DDR_CH1_DQ14_C | - | I/O | - |
| B4 | DDR_CH1_DQ15_C | - | I/O | - |
| G9 | DDR_CH1_WCK0P_C | - | O | - |
| H9 | DDR_CH1_WCK0N_C | - | O | - |
| D7 | DDR_CH1_WCK1P_C | - | O | - |
| E7 | DDR_CH1_WCK1N_C | - | O | - |
| E9 | DDR_CH1_DQS0P_C | - | I/O | - |
| D9 | DDR_CH1_DQS0N_C | - | I/O | - |
| E5 | DDR_CH1_DQS1P_C | - | I/O | - |
| D5 | DDR_CH1_DQS1N_C | - | I/O | - |
| F8 | DDR_CH1_DM0_C | - | I/O | - |
| D4 | DDR_CH1_DM1_C | - | I/O | - |
| G12 | DDR_CH1_A0_C | - | O | - |
| F12 | DDR_CH1_A1_C | - | O | - |
| E13 | DDR_CH1_A2_C | - | O | - |
| D13 | DDR_CH1_A3_C | - | O | - |
| A10 | DDR_CH1_A4_C | - | O | - |
| B11 | DDR_CH1_A5_C | - | O | - |
| D10 | DDR_CH1_A6_C | - | O | - |
| B12 | DDR_CH1_CK_C | - | O | - |
| A12 | DDR_CH1_CKB_C | - | O | - |
| G11 | DDR_CH1_LP4/4X_CS0_C | - | O | - |
| H11 | DDR_CH1_LP4/4X_CS1_C | - | O | - |
| D11 | DDR_CH1_LP4/4X_CKE0/LP5_CS0_C | - | O | - |
| E11 | DDR_CH1_LP4/4X_CKE1/LP5_CS1_C | - | O | - |
| G8 | DDR_CH1_ZQ_C | - | AI | - |
| E10 | DDR_CH1_RESET_C | - | O | - |
| A17 | DDR_CH1_DQ0_D | - | I/O | - |
| B16 | DDR_CH1_DQ1_D | - | I/O | - |
| A16 | DDR_CH1_DQ2_D | - | I/O | - |
| B15 | DDR_CH1_DQ3_D | - | I/O | - |
| A19 | DDR_CH1_DQ4_D | - | I/O | - |
| B18 | DDR_CH1_DQ5_D | - | I/O | - |
| A18 | DDR_CH1_DQ6_D | - | I/O | - |
| B17 | DDR_CH1_DQ7_D | - | I/O | - |
| A22 | DDR_CH1_DQ8_D | - | I/O | - |
| B22 | DDR_CH1_DQ9_D | - | I/O | - |
| A23 | DDR_CH1_DQ10_D | - | I/O | - |
| B23 | DDR_CH1_DQ11_D | - | I/O | - |
| A20 | DDR_CH1_DQ12_D | - | I/O | - |
| B20 | DDR_CH1_DQ13_D | - | I/O | - |
| A21 | DDR_CH1_DQ14_D | - | I/O | - |
| B21 | DDR_CH1_DQ15_D | - | I/O | - |
| E17 | DDR_CH1_WCK0P_D | - | O | - |
| D17 | DDR_CH1_WCK0N_D | - | O | - |
| H18 | DDR_CH1_WCK1P_D | - | O | - |
| G18 | DDR_CH1_WCK1N_D | - | O | - |
| H16 | DDR_CH1_DQS0P_D | - | I/O | - |
| G16 | DDR_CH1_DQS0N_D | - | I/O | - |
| D21 | DDR_CH1_DQS1P_D | - | I/O | - |
| E21 | DDR_CH1_DQS1N_D | - | I/O | - |
| D20 | DDR_CH1_DM0_D | - | I/O | - |
| D22 | DDR_CH1_DM1_D | - | I/O | - |
| H15 | DDR_CH1_A0_D | - | O | - |
| G14 | DDR_CH1_A1_D | - | O | - |
| G13 | DDR_CH1_A2_D | - | O | - |
| E14 | DDR_CH1_A3_D | - | O | - |
| A15 | DDR_CH1_A4_D | - | O | - |
| B14 | DDR_CH1_A5_D | - | O | - |
| D14 | DDR_CH1_A6_D | - | O | - |
| B13 | DDR_CH1_CK_D | - | O | - |
| A13 | DDR_CH1_CKB_D | - | O | - |
| E19 | DDR_CH1_LP4/4X_CS0_D | - | O | - |
| D19 | DDR_CH1_LP4/4X_CS1_D | - | O | - |
| D16 | DDR_CH1_LP4/4X_CKE0/LP5_CS0_D | - | O | - |
| E16 | DDR_CH1_LP4/4X_CKE1/LP5_CS1_D | - | O | - |
| F18 | DDR_CH1_ZQ_D | - | AI | - |
| C19 | DDR_CH1_RESET_D | - | O | - |
| L11 | DDR_CH1_VDD_0 | 0.75V-0.85V | PI | - |
| L12 | DDR_CH1_VDD_1 | - | PI | - |
| L13 | DDR_CH1_VDD_2 | - | PI | - |
| L14 | DDR_CH1_VDD_3 | - | PI | - |
| K11 | DDR_CH1_VDDQ_0 | 0.6V/0.5V | PI | - |
| K12 | DDR_CH1_VDDQ_1 | - | PI | - |
| K13 | DDR_CH1_VDDQ_2 | - | PI | - |
| K14 | DDR_CH1_VDDQ_3 | - | PI | - |
| K15 | DDR_CH1_VDDQ_4 | - | PI | - |
| M13 | DDR_CH1_VDDQ_CK | 0.6V/0.5V | PI | - |
| H13 | DDR_CH1_VDDQ_CKE | 1.1V/1.05V | PI | - |
| L17 | DDR_CH1_VDD_MIF_0 | 0.75V-0.85V | PI | - |
| L18 | DDR_CH1_VDD_MIF_1 | - | PI | - |
| L15 | DDR_CH1_PLL_DVDD | 0.75V-0.85V | PI | - |
| K16 | DDR_CH1_PLL_AVDD1V8 | 1.8V | API | - |
| L16 | DDR_CH1_PLL_AVSS | - | G | - |

### EMMCIO_1V8 (13p, 12 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| Y33 | EMMC_D0/FSPI_D0_M0/GPIO2_D0_u | - | I/O | up |
| W33 | EMMC_D1/FSPI_D1_M0/GPIO2_D1_u | - | I/O | up |
| V32 | EMMC_D2/FSPI_D2_M0/GPIO2_D2_u | - | I/O | up |
| AA33 | EMMC_D3/FSPI_D3_M0/GPIO2_D3_u | - | I/O | up |
| Y32 | EMMC_D4/I2C1_SCL_M3/UART5_RX_M2/GPIO2_D4_u | - | I/O | up |
| AA32 | EMMC_D5/I2C1_SDA_M3/UART5_TX_M2/GPIO2_D5_u | - | I/O | up |
| W32 | EMMC_D6/FSPI_CS0N_M0/GPIO2_D6_u | - | I/O | up |
| V33 | EMMC_D7/FSPI_CS1N_M0/GPIO2_D7_u | - | I/O | up |
| W34 | EMMC_CMD/FSPI_CLK_M0/GPIO2_A0_u | - | I/O | up |
| V34 | EMMC_CLKOUT/GPIO2_A1_d | - | I/O | down |
| Y34 | EMMC_DATA_STROBE/I2C2_SDA_M2/UART5_CTSN_M1/GPIO2_A2_d | - | I/O | down |
| AA34 | EMMC_RSTN/I2C2_SCL_M2/UART5_RTSN_M1/GPIO2_A3_d | - | I/O | down |
| V26 | EMMCIO_1V8 | 1.8V | PI | - |

### VCCIO2 (8p, 6 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AD2 | SDMMC_D0/PDM1_SDI3_M0/JTAG_TCK_M1/I2C3_SCL_M4/UART2_TX_M1/PWM8_M1/GPIO4_D0_u | - | I/O | up |
| AD1 | SDMMC_D1/PDM1_SDI2_M0/JTAG_TMS_M1/I2C3_SDA_M4/UART2_RX_M1/PWM9_M1/GPIO4_D1_u | - | I/O | up |
| AF2 | SDMMC_D2/PDM1_SDI1_M0/JTAG_TCK_M0/I2C8_SCL_M0/UART5_CTSN_M0/GPIO4_D2_u | - | I/O | up |
| AF1 | SDMMC_D3/PDM1_SDI0_M0/JTAG_TMS_M0/I2C8_SDA_M0/UART5_RTSN_M0/PWM10_M1/GPIO4_D3_u | - | I/O | up |
| AE2 | SDMMC_CMD/PDM1_CLK1_M0/MCU_JTAG_TCK_M0/CAN0_TX_M1/UART5_RX_M0/PWM7_IR_M1/GPIO4_D | - | I/O | up |
| AE1 | SDMMC_CLK/PDM1_CLK0_M0/TEST_CLKOUT_M0/MCU_JTAG_TMS_M0/CAN0_RX_M1/UART5_TX_M0/GPI | - | I/O | down |
| Y7 | VCCIO2 | 1.8V/3.3V | PI | - |
| AA7 | VCCIO2_1V8 | 1.8V | PI | - |

### PMUIO1 (22p, 12 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| P33 | REFCLK_OUT/GPIO0_A0_d | - | I/O | down |
| P32 | TSADC_SHUT_ORG/TSADC_SHUT/GPIO0_A1_z | - | I/O | high-z |
| R32 | PMIC_SLEEP1/GPIO0_A2_d | - | I/O | down |
| R31 | PMIC_SLEEP2/GPIO0_A3_d | - | I/O | down |
| P31 | SDMMC_DET/GPIO0_A4_u | - | I/O | up |
| N31 | SPI2_CLK_M2/SDMMC_PWREN/PMU_DEBUG/GPIO0_A5_d | - | I/O | down |
| N30 | SPI2_MOSI_M2/I2C0_SDA_M0/GPIO0_A6_z | - | I/O | high-z |
| M30 | PMIC_INT_L/GPIO0_A7_u | - | I/O | up |
| L30 | SPI2_CS1_M2/I2C1_SCL_M1/UART0_RX_M1/GPIO0_B0_z | - | I/O | high-z |
| K30 | SPI2_CS0_M2/I2C1_SDA_M1/PWM5_M0/UART0_TX_M1/GPIO0_B1_z | - | I/O | high-z |
| K29 | CLK32K_IN/CLK32K_OUT0/GPIO0_B2__u | - | I/O | up |
| L29 | SPI2_MISO_M2/I2C0_SCL_M0/GPIO0_B3_z | - | I/O | high-z |
| M31 | NPOR | - | AI | up |
| M29 | TVSS | - | - | down |
| R34 | XIN_24M | - | AI | - |
| T34 | XOUT_24M | - | AO | - |
| N27 | OSC_1V8 | 1.8V | PI | - |
| P27 | PMU_0V75 | 0.75V | PI | - |
| N28 | PMUIO1_1V8 | 1.8V | PI | - |
| V20 | PLL_DVDD0V75 | 0.75V | PI | - |
| U18 | PLL_AVDD1V8 | 1.8V | API | - |
| U19 | PLL_AVSS | - | G | - |

### PMUIO2 (20p, 18 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| P29 | I2S1_MCLK_M1/JTAG_TCK_M2/I2C1_SCL_M0/UART2_TX_M0/PCIE30X1_1_CLKREQN_M0/GPIO0_B5_ | - | I/O | down |
| R29 | I2S1_SCLK_M1/JTAG_TMS_M2/I2C1_SDA_M0/UART2_RX_M0/PCIE30X1_1_WAKEN_M0/GPIO0_B6_d | - | I/O | down |
| T28 | I2S1_LRCK_M1/PWM0_M0/I2C2_SCL_M0/CAN0_TX_M0/SPI0_CS1_M0/PCIE30X1_1_PERSTN_M0/GPI | - | I/O | down |
| T31 | PDM0_CLK0_M1/PWM1_M0/I2C2_SDA_M0/CAN0_RX_M0/SPI0_MOSI_M0/PCIE30X1_0_CLKREQN_M0/G | - | I/O | down |
| U32 | PMIC_SLEEP3/GPIO0_C1_d | - | I/O | down |
| T32 | PMIC_SLEEP4/GPIO0_C2_d | - | I/O | down |
| T30 | PMIC_SLEEP5/GPIO0_C3_d | - | I/O | down |
| R30 | PDM0_CLK1_M1/PWM2_M0/UART0_RX_M0/I2C4_SDA_M2/DP0_HPDIN_M1/PCIE30X1_0_WAKEN_M0/GP | - | I/O | down |
| P30 | I2S1_SDI0_M1/GPU_AVS/UART0_TX_M0/I2C4_SCL_M2/DP1_HPDIN_M1/PWM4_M0/PCIE30X1_0_PER | - | I/O | up |
| T29 | I2S1_SDI1_M1/NPU_AVS/UART0_RTSN/PWM5_M1/SPI0_CLK_M0/PCIE30X4_CLKREQN_M0/SATA_CP_ | - | I/O | up |
| V31 | I2S1_SDI2_M1/PDM0_SDI0_M1/I2C6_SDA_M0/UART1_RTSN_M2/PWM6_M0/SPI0_MISO_M0/PCIE30X | - | I/O | down |
| W31 | I2S1_SDI3_M1/PDM0_SDI1_M1/I2C6_SCL_M0/UART1_CTSN_M2/PWM7_IR_M0/SPI3_MISO_M2/PCIE | - | I/O | down |
| W30 | I2S1_SDO0_M1/CPU_BIG0_AVS/I2C0_SCL_M2/UART0_CTSN/UART1_TX_M2/HDMI_RX_SDA_M0/SPI0 | - | I/O | up |
| W29 | I2S1_SDO1_M1/I2C0_SDA_M2/UART1_RX_M2/HDMI_RX_SCL_M0/SPI3_MOSI_M2/PCIE30X2_WAKEN_ | - | I/O | up |
| U33 | LITCPU_AVS/SPI3_CLK_M2/GPIO0_D3_u | - | I/O | up |
| V29 | I2S1_SDO2_M1/PDM0_SDI2_M1/PWM3_IR_M0/I2C1_SCL_M2/CAN2_RX_M1/HDMI_TX0_SDA_M1/SPI3 | - | I/O | up |
| V28 | I2S1_SDO3_M1/CPU_BIG1_AVS/I2C1_SDA_M2/CAN2_TX_M1/HDMI_TX0_SCL_M1/SPI3_CS1_M2/SAT | - | I/O | up |
| W28 | PMIC_SLEEP6/PDM0_SDI3_M1/GPIO0_D6_d | - | I/O | down |
| P28 | PMUIO2 | 1.8V/3.3V | PI | - |
| R27 | PMUIO2_1V8 | 1.8V | PI | - |

### VCCIO1 (15p, 14 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| G29 | I2C3_SDA_M0/UART3_RX_M0/SPI4_MISO_M0/GPIO1_C0_z | - | I/O | high-z |
| G27 | I2C3_SCL_M0/UART3_TX_M0/SPI4_MOSI_M0/GPIO1_C1_z | - | I/O | high-z |
| F30 | I2S0_MCLK/I2C6_SDA_M1/UART3_RTSN/PWM3_IR_M2/SPI4_CLK_M0/GPIO1_C2_d | - | I/O | down |
| E31 | I2S0_SCLK/I2C6_SCL_M1/UART3_CTSN/PWM7_IR_M2/SPI4_CS0_M0/GPIO1_C3_d | - | I/O | down |
| E30 | PDM0_CLK1_M0/I2C2_SDA_M3/PWM11_IR_M2/SPI4_CS1_M0/GPIO1_C4_d | - | I/O | down |
| D30 | I2S0_LRCK/I2C2_SCL_M3/UART4_RTSN/GPIO1_C5_d | - | I/O | down |
| D29 | PDM0_CLK0_M0/I2C4_SDA_M4/PWM15_IR_M2/GPIO1_C6_d | - | I/O | down |
| E29 | I2S0_SDO0/I2C4_SCL_M4/UART4_CTSN/GPIO1_C7_d | - | I/O | down |
| F26 | I2S0_SDO1/I2C7_SCL_M0/UART6_TX_M2/SPI1_MISO_M2/GPIO1_D0_d | - | I/O | down |
| F27 | I2S0_SDO2/I2S0_SDI3/PDM0_SDI1_M0/I2C7_SDA_M0/UART6_RX_M2/SPI1_MOSI_M2/GPIO1_D1_d | - | I/O | down |
| F28 | I2S0_SDO3/I2S0_SDI2/PDM0_SDI2_M0/I2C1_SCL_M4/UART4_TX_M0/PWM0_M1/SPI1_CLK_M2/GPI | - | I/O | down |
| E28 | I2S0_SDI1/PDM0_SDI3_M0/I2C1_SDA_M4/UART4_RX_M0/PWM1_M1/SPI1_CS0_M2/GPIO1_D3_d | - | I/O | down |
| D28 | I2S0_SDI0/GPIO1_D4_d | - | I/O | down |
| G26 | PDM0_SDI0_M0/SPI1_CS1_M2/GPIO1_D5_d | - | I/O | down |
| G20 | VCCIO1_1V8 | 1.8V | PI | - |

### VCCIO3 (22p, 21 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AC32 | GMAC0_RXD2/SDIO_D0_M0/FSPI_D0_M1/UART6_RX_M0/GPIO2_A6_u | - | I/O | up |
| AC31 | GMAC0_RXD3/SDIO_D1_M0/FSPI_D1_M1/UART6_TX_M0/GPIO2_A7_u | - | I/O | up |
| AE32 | GMAC0_RXCLK/SDIO_D2_M0/FSPI_D2_M1/I2C8_SCL_M1/UART6_RTSN_M0/GPIO2_B0_u | - | I/O | up |
| AC33 | GMAC0_TXD2/SDIO_D3_M0/FSPI_D3_M1/I2C8_SDA_M1/UART6_CTSN_M0/GPIO2_B1_u | - | I/O | up |
| AC34 | GMAC0_TXD3/SDIO_CMD_M0/I2C3_SCL_M3/GPIO2_B2_u | - | I/O | up |
| AE33 | GMAC0_TXCLK/SDIO_CLK_M0/FSPI_CLK_M1/I2C3_SDA_M3/GPIO2_B3_d | - | I/O | down |
| AB31 | GMAC0_PTP_REFCLK/FSPI_CS0N_M1/HDMI_TX1_SDA_M0/I2C4_SDA_M1/UART7_RX_M0/GPIO2_B4_u | - | I/O | up |
| AB30 | GMAC0_PPSTRIG/FSPI_CS1N_M1/HDMI_TX1_SCL_M0/I2C4_SCL_M1/UART7_TX_M0/GPIO2_B5_u | - | I/O | up |
| AD33 | GMAC0_TXD0/I2S2_MCLK_M0/I2C5_SCL_M4/UART1_RX_M0/GPIO2_B6_d | - | I/O | down |
| AD34 | GMAC0_TXD1/I2S2_SCLK_M0/I2C5_SDA_M4/UART1_TX_M0/GPIO2_B7_d | - | I/O | down |
| AE34 | GMAC0_TXEN/I2S2_LRCK_M0/I2C2_SDA_M1/UART1_RTSN_M0/SPI1_CLK_M0/GPIO2_C0_d | - | I/O | down |
| AD32 | GMAC0_RXD0/I2C2_SCL_M1/UART1_CTSN_M0/SPI1_MISO_M0/GPIO2_C1_d | - | I/O | down |
| AD31 | GMAC0_RXD1/I2C6_SDA_M2/UART9_TX_M0/SPI1_MOSI_M0/GPIO2_C2_d | - | I/O | down |
| AD30 | ETH0_REFCLKO_25M/I2S2_SDI_M0/I2C6_SCL_M2/SPI1_CS0_M0/GPIO2_C3_d | - | I/O | down |
| AC30 | GMAC0_PPSCLK/TEST_CLKOUT_M1/HDMI_TX1_CEC_M0/UART9_RX_M0/SPI1_CS1_M0/GPIO2_C4_d | - | I/O | down |
| AE30 | CLK32K_OUT1/GPIO2_C5_d | - | I/O | down |
| AE31 | GMAC0_RXDV_CRS/UART7_RTSN_M0/PWM2_M2/SPI3_CS0_M0/GPIO4_C2_d | - | I/O | down |
| AF34 | GMAC0_MCLKINOUT/I2S2_SDO_M0/I2C7_SCL_M1/PWM4_M1/SPI3_CS1_M0/GPIO4_C3_d | - | I/O | down |
| AB34 | GMAC0_MDC/I2C7_SDA_M1/UART9_RTSN_M0/PWM5_M2/SPI3_MISO_M0/GPIO4_C4_d | - | I/O | down |
| AB33 | GMAC0_MDIO/I2C0_SCL_M1/UART9_CTSN_M0/PWM6_M2/SPI3_MOSI_M0/GPIO4_C5_d | - | I/O | down |
| AF33 | GMAC0_TXER/I2C0_SDA_M1/UART7_CTSN_M0/PWM7_IR_M3/SPI3_CLK_M0/GPIO4_C6_d | - | I/O | down |
| Y26 | VCCIO3_1V8 | 1.8V | PI | - |

### VCCIO4 (20p, 18 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| A24 | PCIE30X1_1_CLKREQN_M2/DP0_HPDIN_M2/I2C2_SDA_M4/UART6_RX_M1/SPI4_MISO_M2/GPIO1_A0 | - | I/O | down |
| A25 | PCIE30X1_1_WAKEN_M2/DP1_HPDIN_M2/SATA1_ACT_LED_M1/I2C2_SCL_M4/UART6_TX_M1/SPI4_M | - | I/O | down |
| A26 | VOP_POST_EMPTY/I2C4_SDA_M3/UART6_RTSN_M1/PWM0_M2/SPI4_CLK_M2/GPIO1_A2_d | - | I/O | down |
| A27 | HDMI_TX1_SDA_M2/I2C4_SCL_M3/UART6_CTSN_M1/PWM1_M2/SPI4_CS0_M2/GPIO1_A3_d | - | I/O | down |
| B25 | HDMI_TX1_SCL_M2/SPI2_MISO_M0/GPIO1_A4_d | - | I/O | down |
| B26 | HDMI_TX0_HPD_M0/SPI2_MOSI_M0/GPIO1_A5_d | - | I/O | down |
| C24 | HDMI_TX1_HPD_M0/SPI2_CLK_M0/GPIO1_A6_d | - | I/O | down |
| C25 | PDM1_SDI0_M1/PCIE30X1_1_PERSTN_M2/PWM3_IR_M3/SPI2_CS0_M0/GPIO1_A7_u | - | I/O | up |
| C27 | PDM1_SDI1_M1/PCIE30X4_CLKREQN_M3/SPI2_CS1_M0/GPIO1_B0_u | - | I/O | up |
| D25 | PDM1_SDI2_M1/PCIE30X4_WAKEN_M3/SPI0_MISO_M2/GPIO1_B1_d | - | I/O | down |
| D26 | PDM1_SDI3_M1/PCIE30X4_PERSTN_M3/UART4_RX_M2/SPI0_MOSI_M2/GPIO1_B2_d | - | I/O | down |
| D27 | PDM1_CLK1_M1/PCIE30X1_0_WAKEN_M2/SATA0_ACT_LED_M1/UART4_TX_M2/SPI0_CLK_M2/GPIO1_ | - | I/O | down |
| E24 | PDM1_CLK0_M1/PCIE30X1_0_PERSTN_M2/UART7_RX_M2/SPI0_CS0_M2/GPIO1_B4_u | - | I/O | up |
| E25 | PCIE30X1_0_CLKREQN_M2/UART7_TX_M2/SPI0_CS1_M2/GPIO1_B5_u | - | I/O | up |
| E26 | MIPI_CAMERA1_CLK_M0/SPDIF0_TX_M0/PCIE30X2_WAKEN_M3/HDMI_RX_HPDOUT_M2/I2C5_SCL_M3 | - | I/O | up |
| E27 | MIPI_CAMERA2_CLK_M0/SPDIF1_TX_M0/PCIE30X2_PERSTN_M3/HDMI_RX_CEC_M2/SATA2_ACT_LED | - | I/O | up |
| F24 | MIPI_CAMERA3_CLK_M0/HDMI_RX_SCL_M2/I2C8_SCL_M2/UART1_RTSN_M1/PWM14_M2/GPIO1_D6_u | - | I/O | up |
| F25 | MIPI_CAMERA4_CLK_M0/PCIE30X2_CLKREQN_M3/HDMI_RX_SDA_M2/I2C8_SDA_M2/UART1_CTSN_M1 | - | I/O | up |
| H21 | VCCIO4 | 1.8V/3.3V | PI | - |
| H20 | VCCIO4_1V8 | 1.8V | PI | - |

### VCCIO5 (32p, 30 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AA29 | GMAC1_TXD2/SDIO_D0_M1/I2S3_MCLK/FSPI_D0_M2/I2C6_SDA_M4/PWM10_M0/SPI4_MISO_M1/GPI | - | I/O | up |
| AA30 | GMAC1_TXD3/SDIO_D1_M1/I2S3_SCLK/AUDDSM_LN/FSPI_D1_M2/I2C6_SCL_M4/PWM11_IR_M0/SPI | - | I/O | up |
| AD27 | GMAC1_RXD2/SDIO_D2_M1/I2S3_LRCK/AUDDSM_LP/FSPI_D2_M2/UART8_TX_M1/SPI4_CLK_M1/GPI | - | I/O | up |
| AE27 | GMAC1_RXD3/SDIO_D3_M1/I2S3_SDO/AUDDSM_RN/FSPI_D3_M2/UART8_RX_M1/SPI4_CS0_M1/GPIO | - | I/O | up |
| AD28 | GMAC1_TXCLK/SDIO_CMD_M1/I2S3_SDI/AUDDSM_RP/UART8_RTSN_M1/SPI4_CS1_M1/GPIO3_A4_d | - | I/O | down |
| AH30 | GMAC1_RXCLK/SDIO_CLK_M1/MIPI_CAMERA0_CLK_M1/FSPI_CLK_M2/I2C4_SDA_M0/UART8_CTSN_M | - | I/O | down |
| AH27 | ETH1_REFCLKO_25M/MIPI_CAMERA1_CLK_M1/I2C4_SCL_M0/GPIO3_A6_d | - | I/O | down |
| AG29 | GMAC1_RXD0/MIPI_CAMERA2_CLK_M1/PWM8_M0/GPIO3_A7_u | - | I/O | up |
| AG28 | GMAC1_RXD1/MIPI_CAMERA3_CLK_M1/PWM9_M0/GPIO3_B0_u | - | I/O | up |
| AH29 | GMAC1_RXDV_CRS/MIPI_CAMERA4_CLK_M1/UART2_TX_M2/PWM2_M1/GPIO3_B1_d | - | I/O | down |
| AE28 | GMAC1_TXER/I2S2_SDI_M1/UART2_RX_M2/PWM3_IR_M1/GPIO3_B2_d | - | I/O | down |
| AC28 | GMAC1_TXD0/I2S2_SDO_M1/UART2_RTSN/GPIO3_B3_u | - | I/O | up |
| AC29 | GMAC1_TXD1/I2S2_MCLK_M1/UART2_CTSN/GPIO3_B4_u | - | I/O | up |
| AD29 | GMAC1_TXEN/I2S2_SCLK_M1/CAN1_RX_M0/UART3_TX_M1/PWM12_M0/GPIO3_B5_u | - | I/O | up |
| AE29 | GMAC1_MCLKINOUT/I2S2_LRCK_M1/CAN1_TX_M0/UART3_RX_M1/PWM13_M0/GPIO3_B6_d | - | I/O | down |
| AA28 | GMAC1_PTP_REF_CLK/HDMI_TX1_HPD_M1/I2C3_SCL_M1/SPI1_MOSI_M1/GPIO3_B7_d | - | I/O | down |
| Y29 | GMAC1_PPSTRIG/I2C3_SDA_M1/UART7_TX_M1/SPI1_MISO_M1/GPIO3_C0_d | - | I/O | down |
| Y27 | GMAC1_PPSCLK/PCIE30X2_BUTTON_RSTN/UART7_RX_M1/SPI1_CLK_M1/GPIO3_C1_d | - | I/O | down |
| Y31 | GMAC1_MDC/MIPI_TE0/I2C8_SCL_M4/UART7_RTSN_M1/PWM14_M0/SPI1_CS0_M1/GPIO3_C2_d | - | I/O | down |
| Y30 | GMAC1_MDIO/MIPI_TE1/I2C8_SDA_M4/UART7_CTSN_M1/PWM15_IR_M0/SPI1_CS1_M1/GPIO3_C3_d | - | I/O | down |
| AH26 | CIF_D8/FSPI_CS0N_M2/PCIE30X4_CLKREQN_M2/HDMI_TX1_CEC_M2/CAN2_RX_M0/UART5_TX_M1/S | - | I/O | up |
| AH25 | CIF_D9/FSPI_CS1N_M2/PCIE30X4_WAKEN_M2/HDMI_TX1_SDA_M1/CAN2_TX_M0/UART5_RX_M1/SPI | - | I/O | up |
| AG26 | CIF_D10/PCIE30X4_PERSTN_M2/HDMI_TX1_SCL_M1/SPI3_MISO_M3/GPIO3_C6_u | - | I/O | up |
| AJ24 | CIF_D11/PCIE20X1_2_CLKREQN_M0/HDMI_TX0_SCL_M2/I2C5_SCL_M0/SPI3_MOSI_M3/GPIO3_C7_ | - | I/O | up |
| AH24 | CIF_D12/PCIE20X1_2_WAKEN_M0/HDMI_TX0_SDA_M2/I2C5_SDA_M0/UART4_RX_M1/PWM8_M2/SPI3 | - | I/O | up |
| AG23 | CIF_D13/PCIE20X1_2_PERSTN_M0/HDMI_RX_CEC_M1/UART4_TX_M1/PWM9_M2/SPI0_MISO_M3/GPI | - | I/O | down |
| AG25 | CIF_D14/PCIE30X2_CLKREQN_M2/HDMI_RX_SCL_M1/I2C7_SCL_M2/UART9_RTSN_M2/SPI0_MOSI_M | - | I/O | down |
| AG24 | CIF_D15/PCIE30X2_WAKEN_M2/HDMI_RX_SDA_M1/I2C7_SDA_M2/UART9_CTSN_M2/PWM10_M2/SPI0 | - | I/O | down |
| AA27 | HDMI_TX0_HPD_M1/PCIE30X2_PERSTN_M2/HDMI_RX_HPDOUT_M1/MCU_JTAG_TCK_M1/UART9_RX_M2 | - | I/O | down |
| AB28 | PCIE30X4_BUTTON_RSTN/DP1_HPDIN_M0/MCU_JTAG_TMS_M1/UART9_TX_M2/PWM11_IR_M3/SPI0_C | - | I/O | down |
| W26 | VCCIO5 | 1.8V/3.3V | PI | - |
| W25 | VCCIO5_1V8 | 1.8V | PI | - |

### VCCIO6 (20p, 18 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AK30 | CIF_D0/BT1120_D0/I2S1_MCLK_M0/PCIE30X1_1_CLKREQN_M1/UART9_RTSN_M1/SPI0_MISO_M1/G | - | I/O | down |
| AL30 | CIF_D1/BT1120_D1/I2S1_SCLK_M0/PCIE30X1_1_WAKEN_M1/UART9_CTSN_M1/SPI0_MOSI_M1/GPI | - | I/O | down |
| AM29 | CIF_D2/BT1120_D2/I2S1_LRCK_M0/PCIE30X1_1_PERSTN_M1/SPI0_CLK_M1/GPIO4_A2_d | - | I/O | down |
| AL29 | CIF_D3/BT1120_D3/PCIE30X1_0_CLKREQN_M1/UART0_TX_M2/GPIO4_A3_d | - | I/O | down |
| AL28 | CIF_D4/BT1120_D4/PCIE30X1_0_WAKEN_M1/I2C3_SCL_M2/UART0_RX_M2/SPI2_MISO_M1/GPIO4_ | - | I/O | down |
| AK27 | CIF_D5/BT1120_D5/I2S1_SDI0_M0/PCIE30X1_0_PERSTN_M1/I2C3_SDA_M2/UART3_TX_M2/SPI2_ | - | I/O | down |
| AL27 | CIF_D6/BT1120_D6/I2S1_SDI1_M0/PCIE30X2_CLKREQN_M1/I2C5_SCL_M2/UART3_RX_M2/SPI2_C | - | I/O | down |
| AM27 | CIF_D7/BT1120_D7/I2S1_SDI2_M0/PCIE30X2_WAKEN_M1/I2C5_SDA_M2/SPI2_CS0_M1/GPIO4_A7 | - | I/O | down |
| AK26 | CIF_CLKIN/BT1120_CLKOUT/I2S1_SDI3_M0/PCIE30X2_PERSTN_M1/I2C6_SDA_M3/UART8_TX_M0/ | - | I/O | down |
| AL24 | MIPI_CAMERA0_CLK_M0/SPDIF1_TX_M1/I2S1_SDO0_M0/PCIE30X1_0_BUTTON_RSTN/SATA2_ACT_L | - | I/O | up |
| AK25 | CIF_HREF/BT1120_D8/I2S1_SDO1_M0/PCIE30X1_1_BUTTON_RSTN/I2C7_SCL_M3/UART8_RTSN_M0 | - | I/O | up |
| AM25 | CIF_VSYNC/BT1120_D9/I2S1_SDO2_M0/PCIE20X1_2_BUTTON_RSTN/I2C7_SDA_M3/UART8_CTSN_M | - | I/O | up |
| AL26 | CIF_CLKOUT/BT1120_D10/I2S1_SDO3_M0/PCIE30X4_CLKREQN_M1/DP0_HPDIN_M0/SPDIF0_TX_M1 | - | I/O | up |
| AJ26 | BT1120_D11/PCIE30X4_WAKEN_M1/HDMI_RX_CEC_M0/SATA1_ACT_LED_M0/UART9_RX_M1/PWM12_M | - | I/O | down |
| AJ27 | BT1120_D12/PCIE30X4_PERSTN_M1/HDMI_RX_HPDOUT_M0/SATA0_ACT_LED_M0/I2C5_SCL_M1/PWM | - | I/O | down |
| AJ28 | BT1120_D13/PCIE20X1_2_CLKREQN_M1/HDMI_TX0_SCL_M0/I2C5_SDA_M1/SPI3_CLK_M1/GPIO4_B | - | I/O | up |
| AJ25 | BT1120_D14/PCIE20X1_2_WAKEN_M1/HDMI_TX0_SDA_M0/I2C8_SCL_M3/SPI3_CS0_M1/GPIO4_C0_ | - | I/O | up |
| AK24 | BT1120_D15/SPDIF1_TX_M2/PCIE20X1_2_PERSTN_M1/HDMI_TX0_CEC_M0/I2C8_SDA_M3/PWM6_M1 | - | I/O | down |
| AC26 | VCCIO6 | 1.8V/3.3V | PI | - |
| AC25 | VCCIO6_1V8 | 1.8V | PI | - |

### USB2.0 (19p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AK6 | USB20_HOST0_DP | - | AI/O | - |
| AL6 | USB20_HOST0_DM | - | AI/O | - |
| AG9 | USB20_HOST0_REXT | - | AI | - |
| AL7 | USB20_HOST1_DP | - | AI/O | - |
| AM7 | USB20_HOST1_DM | - | AI/O | - |
| AH9 | USB20_HOST1_REXT | - | AI | - |
| AL12 | TYPEC0_USB20_OTG_DP | - | AI/O | - |
| AM12 | TYPEC0_USB20_OTG_DM | - | AI/O | - |
| AL14 | TYPEC0_USB20_OTG_ID | - | I | - |
| AM14 | TYPEC0_USB20_VBUSDET | - | I | - |
| AP12 | TYPEC0_USB20_OTG0_REXT | - | AI | - |
| AK9 | TYPEC1_USB20_OTG_DP | - | AI/O | - |
| AL9 | TYPEC1_USB20_OTG_DM | - | AI/O | - |
| AK8 | TYPEC1_USB20_OTG_ID | - | I | - |
| AL8 | TYPEC1_USB20_VBUSDET | - | I | - |
| AP7 | TYPEC1_USB20_OTG1_REXT | - | AI | - |
| AH10 | USB20_DVDD_0V75 | 0.75V | PI | - |
| AG11 | USB20_AVDD_1V8 | 1.8V | API | - |
| AJ10 | USB20_AVDD_3V3 | 3.3V | API | - |

### TYPEC 0/1 (28p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AN13 | TYPEC0_SSRX1P/DP0_TX0P | - | AI/O | - |
| AP13 | TYPEC0_SSRX1N/DP0_TX0N | - | AI/O | - |
| AP14 | TYPEC0_SSTX1P/DP0_TX1P | - | AO | - |
| AN14 | TYPEC0_SSTX1N/DP0_TX1N | - | AO | - |
| AN15 | TYPEC0_SSRX2P/DP0_TX2P | - | AI/O | - |
| AP15 | TYPEC0_SSRX2N/DP0_TX2N | - | AI/O | - |
| AP16 | TYPEC0_SSTX2P/DP0_TX3P | - | AO | - |
| AN16 | TYPEC0_SSTX2N/DP0_TX3N | - | AO | - |
| AL15 | TYPEC0_SBU1/DP0_AUXP | - | AI/O | - |
| AM15 | TYPEC0_SBU2/DP0_AUXN | - | AI/O | - |
| AH16 | TYPEC0_DP0_REXT | - | AI | - |
| AJ14 | TYPEC0_DP0_VDD_0V85 | 0.85V | PI | - |
| AH14 | TYPEC0_DP0_VDDA_0V85 | 0.85V | API | - |
| AG14 | TYPEC0_DP0_VDDH_1V8 | 1.8V | PI | - |
| AN8 | TYPEC1_SSRX1P/DP1_TX0P | - | AI/O | - |
| AP8 | TYPEC1_SSRX1N/DP1_TX0N | - | AI/O | - |
| AP9 | TYPEC1_SSTX1P/DP1_TX1P | - | AO | - |
| AN9 | TYPEC1_SSTX1N/DP1_TX1N | - | AO | - |
| AN10 | TYPEC1_SSRX2P/DP1_TX2P | - | AI/O | - |
| AP10 | TYPEC1_SSRX2N/DP1_TX2N | - | AI/O | - |
| AP11 | TYPEC1_SSTX2P/DP1_TX3P | - | AO | - |
| AN11 | TYPEC1_SSTX2N/DP1_TX3N | - | AO | - |
| AL10 | TYPEC1_SBU1/DP1_AUXP | - | AI/O | - |
| AM10 | TYPEC1_SBU2/DP1_AUXN | - | AI/O | - |
| AG16 | TYPEC1_DP1_REXT | - | AI | - |
| AH13 | TYPEC1_DP1_VDD_0V85 | 0.85V | PI | - |
| AJ13 | TYPEC1_DP1_VDDA_0V85 | 0.85V | API | - |
| AG13 | TYPEC1_DP1_VDDH_1V8 | 1.8V | PI | - |

### PCIE20/SATA30/USB30 (24p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| M34 | PCIE20_0_TXP/SATA30_0_TXP | - | AO | - |
| M33 | PCIE20_0_TXN/SATA30_0_TXN | - | AO | - |
| N33 | PCIE20_0_RXP/SATA30_0_RXP | - | AI | - |
| N34 | PCIE20_0_RXN/SATA30_0_RXN | - | AI | - |
| L32 | PCIE20_0_REFCLKP | - | AI/O | - |
| L33 | PCIE20_0_REFCLKN | - | AI/O | - |
| M27 | PCIE20_SATA30_0_AVDD_1V8 | 1.8V | API | - |
| M28 | PCIE20_SATA30_0_AVDD_0V85 | 0.85V | API | - |
| K33 | PCIE20_1_TXP/SATA30_1_TXP | - | AO | - |
| K34 | PCIE20_1_TXN/SATA30_1_TXN | - | AO | - |
| J33 | PCIE20_1_RXP/SATA30_1_RXP | - | AI | - |
| J34 | PCIE20_1_RXN/SATA30_1_RXN | - | AI | - |
| H32 | PCIE20_1_REFCLKP | - | AI/O | - |
| H33 | PCIE20_1_REFCLKN | - | AI/O | - |
| L27 | PCIE20_SATA30_1_AVDD_1V8 | 1.8V | API | - |
| L28 | PCIE20_SATA30_1_AVDD_0V85 | 0.85V | API | - |
| H30 | PCIE20_2_TXP/SATA30_2_TXP/USB30_2_SSTXP | - | AO | - |
| H29 | PCIE20_2_TXN/SATA30_2_TXN/USB30_2_SSTXN | - | AO | - |
| J31 | PCIE20_2_RXP/SATA30_2_RXP/USB30_2_SSRXP | - | AI | - |
| J30 | PCIE20_2_RXN/SATA30_2_RXN/USB30_2_SSRXN | - | AI | - |
| G31 | PCIE20_2_REFCLKP | - | AI/O | - |
| G30 | PCIE20_2_REFCLKN | - | AI/O | - |
| K27 | PCIE20_SATA30_USB30_2_AVDD_1V8 | 1.8V | API | - |
| K28 | PCIE20_SATA30_USB30_2_AVDD_0V85 | 0.85V | API | - |

### PCIE30 (26p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| D32 | PCIE30_PORT0_TX0P | - | AO | - |
| D33 | PCIE30_PORT0_TX0N | - | AO | - |
| G33 | PCIE30_PORT0_RX0P | - | AI | - |
| G34 | PCIE30_PORT0_RX0N | - | AI | - |
| C33 | PCIE30_PORT0_TX1P | - | AO | - |
| C34 | PCIE30_PORT0_TX1N | - | AO | - |
| F32 | PCIE30_PORT0_RX1P | - | AI | - |
| F33 | PCIE30_PORT0_RX1N | - | AI | - |
| E33 | PCIE30_PORT0_REF_CLKP | - | AI | - |
| E34 | PCIE30_PORT0_REF_CLKN | - | AI | - |
| B34 | PCIE30_PORT0_RESREF | - | AI | - |
| G23 | PCIE30_PORT0_AVDD1V8 | 1.8V | API | - |
| G24 | PCIE30_PORT0_AVDD0V75 | 0.75V | API | - |
| B30 | PCIE30_PORT1_TX0P | - | AO | - |
| A30 | PCIE30_PORT1_TX0N | - | AO | - |
| B32 | PCIE30_PORT1_RX0P | - | AI | - |
| A32 | PCIE30_PORT1_RX0N | - | AI | - |
| C29 | PCIE30_PORT1_TX1P | - | AO | - |
| B29 | PCIE30_PORT1_TX1N | - | AO | - |
| C31 | PCIE30_PORT1_RX1P | - | AI | - |
| B31 | PCIE30_PORT1_RX1N | - | AI | - |
| A28 | PCIE30_PORT1_REF_CLKP | - | AI | - |
| B28 | PCIE30_PORT1_REF_CLKN | - | AI | - |
| A33 | PCIE30_PORT1_RESREF | - | AI | - |
| H23 | PCIE30_PORT1_AVDD1V8 | 1.8V | API | - |
| H24 | PCIE30_PORT1_AVDD0V75 | 0.75V | API | - |

### MIPI CSI (28p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AG33 | MIPI_CSI0_D0P | - | AI | - |
| AG34 | MIPI_CSI0_D0N | - | AI | - |
| AH33 | MIPI_CSI0_D1P | - | AI | - |
| AH34 | MIPI_CSI0_D1N | - | AI | - |
| AK33 | MIPI_CSI0_D2P | - | AI | - |
| AK34 | MIPI_CSI0_D2N | - | AI | - |
| AL33 | MIPI_CSI0_D3P | - | AI | - |
| AL34 | MIPI_CSI0_D3N | - | AI | - |
| AJ33 | MIPI_CSI0_CLK0P | - | AI | - |
| AJ34 | MIPI_CSI0_CLK0N | - | AI | - |
| AM33 | MIPI_CSI0_CLK1P | - | AI | - |
| AM34 | MIPI_CSI0_CLK1N | - | AI | - |
| AB25 | MIPI_CSI0_AVCC0V75 | 0.75V | API | - |
| AB26 | MIPI_CSI0_AVCC1V8 | 1.8V | API | - |
| AG31 | MIPI_CSI1_D0P | - | AI | - |
| AG32 | MIPI_CSI1_D0N | - | AI | - |
| AH31 | MIPI_CSI1_D1P | - | AI | - |
| AH32 | MIPI_CSI1_D1N | - | AI | - |
| AK31 | MIPI_CSI1_D2P | - | AI | - |
| AK32 | MIPI_CSI1_D2N | - | AI | - |
| AL31 | MIPI_CSI1_D3P | - | AI | - |
| AL32 | MIPI_CSI1_D3N | - | AI | - |
| AJ31 | MIPI_CSI1_CLK0P | - | AI | - |
| AJ32 | MIPI_CSI1_CLK0N | - | AI | - |
| AM31 | MIPI_CSI1_CLK1P | - | AI | - |
| AM32 | MIPI_CSI1_CLK1N | - | AI | - |
| AA25 | MIPI_CSI1_AVCC0V75 | 0.75V | API | - |
| AA26 | MIPI_CSI1_AVCC1V8 | 1.8V | API | - |

### MIPI D/C-PHY0 (24p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AN24 | MIPI_DPHY0_TX_D0P/MIPI_CPHY0_TX_TRIO0_B | - | AO | - |
| AP24 | MIPI_DPHY0_TX_D0N/MIPI_CPHY0_TX_TRIO0_A | - | AO | - |
| AN25 | MIPI_DPHY0_TX_D1P/MIPI_CPHY0_TX_TRIO1_A | - | AO | - |
| AP25 | MIPI_DPHY0_TX_D1N/MIPI_CPHY0_TX_TRIO0_C | - | AO | - |
| AN27 | MIPI_DPHY0_TX_D2P/MIPI_CPHY0_TX_TRIO2_B | - | AO | - |
| AP27 | MIPI_DPHY0_TX_D2N/MIPI_CPHY0_TX_TRIO2_A | - | AO | - |
| AN28 | MIPI_DPHY0_TX_D3P/NO_USE | - | AO | - |
| AP28 | MIPI_DPHY0_TX_D3N/MIPI_CPHY0_TX_TRIO2_C | - | AO | - |
| AN26 | MIPI_DPHY0_TX_CLKP/MIPI_CPHY0_TX_TRIO1_C | - | AO | - |
| AP26 | MIPI_DPHY0_TX_CLKN/MIPI_CPHY0_TX_TRIO1_B | - | AO | - |
| AN29 | MIPI_DPHY0_RX_D0P/MIPI_CPHY0_RX_TRIO0_B | - | AI | - |
| AP29 | MIPI_DPHY0_RX_D0N/MIPI_CPHY0_RX_TRIO0_A | - | AI | - |
| AN30 | MIPI_DPHY0_RX_D1P/MIPI_CPHY0_RX_TRIO1_A | - | AI | - |
| AP30 | MIPI_DPHY0_RX_D1N/MIPI_CPHY0_RX_TRIO0_C | - | AI | - |
| AN33 | MIPI_DPHY0_RX_D2P/MIPI_CPHY0_RX_TRIO2_B | - | AI | - |
| AP32 | MIPI_DPHY0_RX_D2N/MIPI_CPHY0_RX_Trio2_A | - | AI | - |
| AN34 | MIPI_DPHY0_RX_D3P/NO_USE | - | AI | - |
| AP33 | MIPI_DPHY0_RX_D3N/MIPI_CPHY0_RX_TRIO2_C | - | AI | - |
| AN32 | MIPI_DPHY0_RX_CLKP/MIPI_CPHY0_RX_TRIO1_C | - | AI | - |
| AP31 | MIPI_DPHY0_RX_CLKN/MIPI_CPHY0_RX_TRIO1_B | - | AI | - |
| AF20 | MIPI_D/C_PHY0_VREG | - | AI | - |
| AG20 | MIPI_D/C_PHY0_VDD | 0.75V/0.85V | API | - |
| AH20 | MIPI_D/C_PHY0_VDD_1V2 | 1.2V | API | - |
| AJ20 | MIPI_D/C_PHY0_VDD_1V8 | 1.8V | PI | - |

### DMIPI D/C-PHY1 (24p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AN18 | MIPI_DPHY1_TX_D0P/MIPI_CPHY1_TX_TRIO0_B | - | AO | - |
| AP18 | MIPI_DPHY1_TX_D0N/MIPI_CPHY1_TX_TRIO0_A | - | AO | - |
| AN19 | MIPI_DPHY1_TX_D1P/MIPI_CPHY1_TX_TRIO1_A | - | AO | - |
| AP19 | MIPI_DPHY1_TX_D1N/MIPI_CPHY1_TX_TRIO0_C | - | AO | - |
| AN21 | MIPI_DPHY1_TX_D2P/MIPI_CPHY1_TX_TRIO2_B | - | AO | - |
| AP21 | MIPI_DPHY1_TX_D2N/MIPI_CPHY1_TX_TRIO2_A | - | AO | - |
| AN22 | MIPI_DPHY1_TX_D3P/NO_USE | - | AO | - |
| AP22 | MIPI_DPHY1_TX_D3N/MIPI_CPHY1_TX_TRIO2_C | - | AO | - |
| AN20 | MIPI_DPHY1_TX_CLKP/MIPI_CPHY1_TX_TRIO1_C | - | AO | - |
| AP20 | MIPI_DPHY1_TX_CLKN/MIPI_CPHY1_TX_TRIO1_B | - | AO | - |
| AK18 | MIPI_DPHY1_RX_D0P/MIPI_CPHY1_RX_TRIO0_B | - | AI | - |
| AL18 | MIPI_DPHY1_RX_D0N/MIPI_CPHY1_RX_TRIO0_A | - | AI | - |
| AK19 | MIPI_DPHY1_RX_D1P/MIPI_CPHY1_RX_TRIO1_A | - | AI | - |
| AL19 | MIPI_DPHY1_RX_D1N/MIPI_CPHY1_RX_TRIO0_C | - | AI | - |
| AK21 | MIPI_DPHY1_RX_D2P/MIPI_CPHY1_RX_TRIO2_B | - | AI | - |
| AL21 | MIPI_DPHY1_RX_D2N/MIPI_CPHY1_RX_TRIO2_A | - | AI | - |
| AK22 | MIPI_DPHY1_RX_D3P/NO_USE | - | AI | - |
| AL22 | MIPI_DPHY1_RX_D3N/MIPI_CPHY1_RX_TRIO2_C | - | AI | - |
| AK20 | MIPI_DPHY1_RX_CLKP/MIPI_CPHY1_RX_TRIO1_C | - | AI | - |
| AL20 | MIPI_DPHY1_RX_CLKN/MIPI_CPHY1_RX_TRIO1_B | - | AI | - |
| AF19 | MIPI_D/C_PHY1_VREG | - | AI | - |
| AG19 | MIPI_D/C_PHY1_VDD | 0.75V/0.85V | API | - |
| AH19 | MIPI_D/C_PHY1_VDD_1V2 | 1.2V | API | - |
| AJ19 | MIPI_D/C_PHY1_VDD_1V8 | 1.8V | PI | - |

### HDMI/eDP_TX_0/1 (30p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AJ1 | HDMI_TX0_D0N/EDP_TX0_D0N | - | AO | - |
| AJ2 | HDMI_TX0_D0P/EDP_TX0_D0P | - | AO | - |
| AK2 | HDMI_TX0_D1N/EDP_TX0_D1N | - | AO | - |
| AK3 | HDMI_TX0_D1P/EDP_TX0_D1P | - | AO | - |
| AL1 | HDMI_TX0_D2N/EDP_TX0_D2N | - | AO | - |
| AL2 | HDMI_TX0_D2P/EDP_TX0_D2P | - | AO | - |
| AH2 | HDMI_TX0_D3N/EDP_TX0_D3N | - | AO | - |
| AH3 | HDMI_TX0_D3P/EDP_TX0_D3P | - | AO | - |
| AG1 | HDMI_TX0_SBDN/EDP_TX0_AUXN | - | AI/O | - |
| AG2 | HDMI_TX0_SBDP/EDP_TX0_AUXP | - | AI/O | - |
| AM2 | HDMI/eDP_TX0_REXT | - | AI | - |
| AA9 | HDMI/eDP_TX0_VDD_0V75 | 0.8375V | PI | - |
| AB9 | HDMI/eDP_TX0_AVDD_0V75 | 0.8375V | API | - |
| AC7 | HDMI/eDP_TX0_VDD_IO_1V8 | 1.8V | PI | - |
| AC6 | HDMI/eDP_TX0_VDD_CMN_1V8 | 1.8V | PI | - |
| AP4 | HDMI_TX1_D0N/EDP_TX1_D0N | - | AO | - |
| AN4 | HDMI_TX1_D0P/EDP_TX1_D0P | - | AO | - |
| AN5 | HDMI_TX1_D1N/EDP_TX1_D1N | - | AO | - |
| AM5 | HDMI_TX1_D1P/EDP_TX1_D1P | - | AO | - |
| AP6 | HDMI_TX1_D2N/EDP_TX1_D2N | - | AO | - |
| AN6 | HDMI_TX1_D2P/EDP_TX1_D2P | - | AO | - |
| AN3 | HDMI_TX1_D3N/EDP_TX1_D3N | - | AO | - |
| AM3 | HDMI_TX1_D3P/EDP_TX1_D3P | - | AO | - |
| AP2 | HDMI_TX1_SBDN/EDP_TX1_AUXN | - | AI/O | - |
| AN2 | HDMI_TX1_SBDP/EDP_TX1_AUXP | - | AI/O | - |
| AN1 | HDMI/eDP_TX1_REXT | - | AI | - |
| AD9 | HDMI/eDP_TX1_VDD_0V75 | 0.8375V | PI | - |
| AC9 | HDMI/eDP_TX1_AVDD_0V75 | 0.8375V | API | - |
| AD7 | HDMI/eDP_TX1_VDD_IO_1V8 | 1.8V | PI | - |
| AD6 | HDMI/eDP_TX1_VDD_CMN_1V8 | 1.8V | PI | - |

### HDMI RX (12p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AG4 | HDMI_RX_D0N | - | AI | - |
| AG5 | HDMI_RX_D0P | - | AI | - |
| AH5 | HDMI_RX_D1N | - | AI | - |
| AH6 | HDMI_RX_D1P | - | AI | - |
| AJ4 | HDMI_RX_D2N | - | AI | - |
| AJ5 | HDMI_RX_D2P | - | AI | - |
| AF5 | HDMI_RX_CLKN | - | AI | - |
| AF6 | HDMI_RX_CLKP | - | AI | - |
| AF3 | HDMI_RX_REXT | - | AI | - |
| AE4 | HDMI_RX_VPH3V3 | 3.3V | PI | - |
| AE5 | HDMI_RX_DVDD3V3 | 3.3V | PI | - |
| AE8 | HDMI_RX_AVDD0V75 | 0.75V | API | - |

### SARADC/OTP/TSADC (12p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AM16 | SARADC_IN0_BOOT | - | AI | - |
| AL16 | SARADC_IN1 | - | AI | - |
| AK16 | SARADC_IN2 | - | AI | - |
| AN17 | SARADC_IN3 | - | AI | - |
| AM17 | SARADC_IN4 | - | AI | - |
| AK15 | SARADC_IN5 | - | AI | - |
| AL17 | SARADC_IN6 | - | AI | - |
| AK17 | SARADC_IN7 | - | AI | - |
| AH18 | SARADC_AVDD_1V8 | 1.8V | API | - |
| AF18 | TSADC_TEST_OUT_TS | - | API | - |
| AD4 | NC | - | PI | - |
| AD3 | OTP_VDDOTP_0V75 | 0.75V | PI | - |

### POWER (75p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| M16 | VDD_CPU_BIG0_0 | 0.55V-0.95V            Default:0.75V | PI | - |
| N16 | VDD_CPU_BIG0_1 | - | PI | - |
| P16 | VDD_CPU_BIG0_2 | - | PI | - |
| R16 | VDD_CPU_BIG0_3 | - | PI | - |
| T16 | VDD_CPU_BIG0_4 | - | PI | - |
| T17 | VDD_CPU_BIG0_5 | - | PI | - |
| R17 | VDD_CPU_BIG0_6 | - | PI | - |
| P17 | VDD_CPU_BIG0_7 | - | PI | - |
| N17 | VDD_CPU_BIG0_8 | - | PI | - |
| M17 | VDD_CPU_BIG0_9 | - | PI | - |
| M19 | VDD_CPU_BIG0_MEM_0 | 0.75V-0.95V  Default:0.75V | PI | - |
| N19 | VDD_CPU_BIG0_MEM_1 | - | PI | - |
| K24 | VDD_CPU_BIG1_0 | 0.55V-0.95V            Default:0.75V | PI | - |
| L24 | VDD_CPU_BIG1_1 | - | PI | - |
| M24 | VDD_CPU_BIG1_2 | - | PI | - |
| N24 | VDD_CPU_BIG1_3 | - | PI | - |
| P24 | VDD_CPU_BIG1_4 | - | PI | - |
| P23 | VDD_CPU_BIG1_5 | - | PI | - |
| N23 | VDD_CPU_BIG1_6 | - | PI | - |
| M23 | VDD_CPU_BIG1_7 | - | PI | - |
| L23 | VDD_CPU_BIG1_8 | - | PI | - |
| K23 | VDD_CPU_BIG1_9 | - | PI | - |
| M21 | VDD_CPU_BIG1_MEM_0 | 0.75V-0.95V   Default:0.75V | PI | - |
| N21 | VDD_CPU_BIG1_MEM_1 | - | PI | - |
| U22 | VDD_CPU_LIT_0 | 0.55V-0.95V            Default:0.75V | PI | - |
| V22 | VDD_CPU_LIT_1 | - | PI | - |
| W22 | VDD_CPU_LIT_2 | - | PI | - |
| Y22 | VDD_CPU_LIT_3 | - | PI | - |
| Y21 | VDD_CPU_LIT_4 | - | PI | - |
| W21 | VDD_CPU_LIT_5 | - | PI | - |
| V21 | VDD_CPU_LIT_6 | - | PI | - |
| U21 | VDD_CPU_LIT_7 | - | PI | - |
| T22 | VDD_CPU_LIT_MEM_0 | 0.75V-0.95V   Default:0.75V | PI | - |
| T21 | VDD_CPU_LIT_MEM_1 | - | PI | - |
| R14 | VDD_VDENC_0 | 0.65V-0.85V            Default:0.75V | PI | - |
| T14 | VDD_VDENC_1 | - | PI | - |
| U14 | VDD_VDENC_2 | - | PI | - |
| V14 | VDD_VDENC_3 | - | PI | - |
| W14 | VDD_VDENC_4 | - | PI | - |
| W13 | VDD_VDENC_5 | - | PI | - |
| V12 | VDD_VDENC_MEM_0 | 0.75V-0.85V   Default:0.75V | PI | - |
| V13 | VDD_VDENC_MEM_1 | - | PI | - |
| AA13 | VDD_GPU_0 | 0.55V-0.95V            Default:0.75V | PI | - |
| AB13 | VDD_GPU_1 | - | PI | - |
| AC13 | VDD_GPU_2 | - | PI | - |
| AD13 | VDD_GPU_3 | - | PI | - |
| AD14 | VDD_GPU_4 | - | PI | - |
| AC14 | VDD_GPU_5 | - | PI | - |
| AB14 | VDD_GPU_6 | - | PI | - |
| AA14 | VDD_GPU_7 | - | PI | - |
| AD15 | VDD_GPU_8 | - | PI | - |
| AC15 | VDD_GPU_9 | - | PI | - |
| AB15 | VDD_GPU_10 | - | PI | - |
| AA15 | VDD_GPU_11 | - | PI | - |
| AA12 | VDD_GPU_MEM_0 | 0.75V-0.95V   Default:0.75V | PI | - |
| AB12 | VDD_GPU_MEM_1 | - | PI | - |
| AD23 | VDD_NPU_0 | 0.55V-0.95V            Default:0.75V | PI | - |
| AC23 | VDD_NPU_1 | - | PI | - |
| AB23 | VDD_NPU_2 | - | PI | - |
| AD22 | VDD_NPU_3 | - | PI | - |
| AC22 | VDD_NPU_4 | - | PI | - |
| AB22 | VDD_NPU_5 | - | PI | - |
| AB21 | VDD_NPU_6 | - | PI | - |
| AE22 | VDD_NPU_MEM_0 | 0.75V-0.95V  Default:0.75V | PI | - |
| AE23 | VDD_NPU_MEM_1 | - | PI | - |
| AD17 | VDD_LOGIC_0 | 0.75V | PI | - |
| AD18 | VDD_LOGIC_1 | - | PI | - |
| AD19 | VDD_LOGIC_2 | - | PI | - |
| AC19 | VDD_LOGIC_3 | - | PI | - |
| AC18 | VDD_LOGIC_4 | - | PI | - |
| AC17 | VDD_LOGIC_5 | - | PI | - |
| V16 | VDD_LOGIC_6 | - | PI | - |
| V17 | VDD_LOGIC_7 | - | PI | - |
| K19 | VDD_LOGIC_8 | - | PI | - |
| K20 | VDD_LOGIC_9 | - | PI | - |

### VSS (317p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| A1 | VSS_1 | - | - | - |
| A11 | VSS_2 | - | - | - |
| A14 | VSS_3 | - | - | - |
| A34 | VSS_4 | - | - | - |
| B6 | VSS_5 | - | - | - |
| B19 | VSS_6 | - | - | - |
| B24 | VSS_7 | - | - | - |
| B27 | VSS_8 | - | - | - |
| B33 | VSS_9 | - | - | - |
| C3 | VSS_10 | - | - | - |
| C4 | VSS_11 | - | - | - |
| C5 | VSS_12 | - | - | - |
| C6 | VSS_13 | - | - | - |
| C7 | VSS_14 | - | - | - |
| C8 | VSS_15 | - | - | - |
| C9 | VSS_16 | - | - | - |
| C10 | VSS_17 | - | - | - |
| C11 | VSS_18 | - | - | - |
| C12 | VSS_19 | - | - | - |
| C13 | VSS_20 | - | - | - |
| C14 | VSS_21 | - | - | - |
| C15 | VSS_22 | - | - | - |
| C16 | VSS_23 | - | - | - |
| C17 | VSS_24 | - | - | - |
| C18 | VSS_25 | - | - | - |
| C20 | VSS_26 | - | - | - |
| C21 | VSS_27 | - | - | - |
| C22 | VSS_28 | - | - | - |
| C23 | VSS_29 | - | - | - |
| C26 | VSS_30 | - | - | - |
| C28 | VSS_31 | - | - | - |
| C30 | VSS_32 | - | - | - |
| C32 | VSS_33 | - | - | - |
| D3 | VSS_34 | - | - | - |
| D23 | VSS_35 | - | - | - |
| D24 | VSS_36 | - | - | - |
| D31 | VSS_37 | - | - | - |
| E3 | VSS_38 | - | - | - |
| E6 | VSS_39 | - | - | - |
| E8 | VSS_40 | - | - | - |
| E12 | VSS_41 | - | - | - |
| E18 | VSS_42 | - | - | - |
| E20 | VSS_43 | - | - | - |
| E22 | VSS_44 | - | - | - |
| E23 | VSS_45 | - | - | - |
| E32 | VSS_46 | - | - | - |
| F3 | VSS_47 | - | - | - |
| F7 | VSS_48 | - | - | - |
| F9 | VSS_49 | - | - | - |
| F10 | VSS_50 | - | - | - |
| F11 | VSS_51 | - | - | - |
| F13 | VSS_52 | - | - | - |
| F14 | VSS_53 | - | - | - |
| F15 | VSS_54 | - | - | - |
| F16 | VSS_55 | - | - | - |
| F19 | VSS_56 | - | - | - |
| F20 | VSS_57 | - | - | - |
| F21 | VSS_58 | - | - | - |
| F22 | VSS_59 | - | - | - |
| F23 | VSS_60 | - | - | - |
| F31 | VSS_61 | - | - | - |
| G3 | VSS_62 | - | - | - |
| G6 | VSS_63 | - | - | - |
| G10 | VSS_64 | - | - | - |
| G15 | VSS_65 | - | - | - |
| G19 | VSS_66 | - | - | - |
| G21 | VSS_67 | - | - | - |
| G22 | VSS_68 | - | - | - |
| G25 | VSS_69 | - | - | - |
| G32 | VSS_70 | - | - | - |
| H3 | VSS_71 | - | - | - |
| H6 | VSS_72 | - | - | - |
| H10 | VSS_73 | - | - | - |
| H12 | VSS_74 | - | - | - |
| H14 | VSS_75 | - | - | - |
| H19 | VSS_76 | - | - | - |
| H22 | VSS_77 | - | - | - |
| H25 | VSS_78 | - | - | - |
| H26 | VSS_79 | - | - | - |
| J3 | VSS_80 | - | - | - |
| J4 | VSS_81 | - | - | - |
| J5 | VSS_82 | - | - | - |
| J6 | VSS_83 | - | - | - |
| J10 | VSS_84 | - | - | - |
| J11 | VSS_85 | - | - | - |
| J12 | VSS_86 | - | - | - |
| J13 | VSS_87 | - | - | - |
| J14 | VSS_88 | - | - | - |
| J15 | VSS_89 | - | - | - |
| J16 | VSS_90 | - | - | - |
| J18 | VSS_91 | - | - | - |
| J19 | VSS_92 | - | - | - |
| J20 | VSS_93 | - | - | - |
| J21 | VSS_94 | - | - | - |
| J22 | VSS_95 | - | - | - |
| J23 | VSS_96 | - | - | - |
| J24 | VSS_97 | - | - | - |
| J25 | VSS_98 | - | - | - |
| K3 | VSS_99 | - | - | - |
| K6 | VSS_100 | - | - | - |
| K8 | VSS_101 | - | - | - |
| K9 | VSS_102 | - | - | - |
| K18 | VSS_103 | - | - | - |
| K21 | VSS_104 | - | - | - |
| K22 | VSS_105 | - | - | - |
| L1 | VSS_106 | - | - | - |
| L3 | VSS_107 | - | - | - |
| L6 | VSS_108 | - | - | - |
| L9 | VSS_109 | - | - | - |
| L19 | VSS_110 | - | - | - |
| L20 | VSS_111 | - | - | - |
| L21 | VSS_112 | - | - | - |
| L22 | VSS_113 | - | - | - |
| L25 | VSS_114 | - | - | - |
| M3 | VSS_115 | - | - | - |
| M6 | VSS_116 | - | - | - |
| M9 | VSS_117 | - | - | - |
| M14 | VSS_118 | - | - | - |
| M15 | VSS_119 | - | - | - |
| M18 | VSS_120 | - | - | - |
| M20 | VSS_121 | - | - | - |
| M22 | VSS_122 | - | - | - |
| M25 | VSS_123 | - | - | - |
| N3 | VSS_124 | - | - | - |
| N6 | VSS_125 | - | - | - |
| N9 | VSS_126 | - | - | - |
| N11 | VSS_127 | - | - | - |
| N14 | VSS_128 | - | - | - |
| N15 | VSS_129 | - | - | - |
| N18 | VSS_130 | - | - | - |
| N20 | VSS_131 | - | - | - |
| N22 | VSS_132 | - | - | - |
| N25 | VSS_133 | - | - | - |
| N26 | VSS_134 | - | - | - |
| N29 | VSS_135 | - | - | - |
| P1 | VSS_136 | - | - | - |
| P3 | VSS_137 | - | - | - |
| P6 | VSS_138 | - | - | - |
| P8 | VSS_139 | - | - | - |
| P9 | VSS_140 | - | - | - |
| P11 | VSS_141 | - | - | - |
| P14 | VSS_142 | - | - | - |
| P15 | VSS_143 | - | - | - |
| P18 | VSS_144 | - | - | - |
| P19 | VSS_145 | - | - | - |
| P20 | VSS_146 | - | - | - |
| P21 | VSS_147 | - | - | - |
| P22 | VSS_148 | - | - | - |
| P25 | VSS_149 | - | - | - |
| P26 | VSS_150 | - | - | - |
| P34 | VSS_151 | - | - | - |
| R3 | VSS_152 | - | - | - |
| R5 | VSS_153 | - | - | - |
| R8 | VSS_154 | - | - | - |
| R9 | VSS_155 | - | - | - |
| R11 | VSS_156 | - | - | - |
| R13 | VSS_157 | - | - | - |
| R15 | VSS_158 | - | - | - |
| R18 | VSS_159 | - | - | - |
| R19 | VSS_160 | - | - | - |
| R20 | VSS_161 | - | - | - |
| R21 | VSS_162 | - | - | - |
| R22 | VSS_163 | - | - | - |
| R23 | VSS_164 | - | - | - |
| R24 | VSS_165 | - | - | - |
| R25 | VSS_166 | - | - | - |
| R26 | VSS_167 | - | - | - |
| R28 | VSS_168 | - | - | - |
| R33 | VSS_169 | - | - | - |
| T3 | VSS_170 | - | - | - |
| T6 | VSS_171 | - | - | - |
| T9 | VSS_172 | - | - | - |
| T11 | VSS_173 | - | - | - |
| T13 | VSS_174 | - | - | - |
| T15 | VSS_175 | - | - | - |
| T18 | VSS_176 | - | - | - |
| T19 | VSS_177 | - | - | - |
| T20 | VSS_178 | - | - | - |
| T23 | VSS_179 | - | - | - |
| T24 | VSS_180 | - | - | - |
| T25 | VSS_181 | - | - | - |
| T26 | VSS_182 | - | - | - |
| T27 | VSS_183 | - | - | - |
| T33 | VSS_184 | - | - | - |
| U3 | VSS_185 | - | - | - |
| U12 | VSS_186 | - | - | - |
| U13 | VSS_187 | - | - | - |
| U15 | VSS_188 | - | - | - |
| U16 | VSS_189 | - | - | - |
| U17 | VSS_190 | - | - | - |
| U20 | VSS_191 | - | - | - |
| U23 | VSS_192 | - | - | - |
| U24 | VSS_193 | - | - | - |
| U30 | VSS_194 | - | - | - |
| U31 | VSS_195 | - | - | - |
| U34 | VSS_196 | - | - | - |
| V3 | VSS_197 | - | - | - |
| V4 | VSS_198 | - | - | - |
| V5 | VSS_199 | - | - | - |
| V8 | VSS_200 | - | - | - |
| V9 | VSS_201 | - | - | - |
| V10 | VSS_202 | - | - | - |
| V11 | VSS_203 | - | - | - |
| V15 | VSS_204 | - | - | - |
| V18 | VSS_205 | - | - | - |
| V19 | VSS_206 | - | - | - |
| V23 | VSS_207 | - | - | - |
| V24 | VSS_208 | - | - | - |
| V25 | VSS_209 | - | - | - |
| V27 | VSS_210 | - | - | - |
| V30 | VSS_211 | - | - | - |
| W2 | VSS_212 | - | - | - |
| W3 | VSS_213 | - | - | - |
| W6 | VSS_214 | - | - | - |
| W7 | VSS_215 | - | - | - |
| W9 | VSS_216 | - | - | - |
| W10 | VSS_217 | - | - | - |
| W11 | VSS_218 | - | - | - |
| W12 | VSS_219 | - | - | - |
| W15 | VSS_220 | - | - | - |
| W16 | VSS_221 | - | - | - |
| W17 | VSS_222 | - | - | - |
| W18 | VSS_223 | - | - | - |
| W19 | VSS_224 | - | - | - |
| W20 | VSS_225 | - | - | - |
| W23 | VSS_226 | - | - | - |
| W24 | VSS_227 | - | - | - |
| W27 | VSS_228 | - | - | - |
| Y3 | VSS_229 | - | - | - |
| Y5 | VSS_230 | - | - | - |
| Y6 | VSS_231 | - | - | - |
| Y8 | VSS_232 | - | - | - |
| Y9 | VSS_233 | - | - | - |
| Y10 | VSS_234 | - | - | - |
| Y11 | VSS_235 | - | - | - |
| Y12 | VSS_236 | - | - | - |
| Y13 | VSS_237 | - | - | - |
| Y14 | VSS_238 | - | - | - |
| Y15 | VSS_239 | - | - | - |
| Y16 | VSS_240 | - | - | - |
| Y17 | VSS_241 | - | - | - |
| Y18 | VSS_242 | - | - | - |
| Y19 | VSS_243 | - | - | - |
| Y20 | VSS_244 | - | - | - |
| Y23 | VSS_245 | - | - | - |
| Y24 | VSS_246 | - | - | - |
| Y28 | VSS_247 | - | - | - |
| AA3 | VSS_248 | - | - | - |
| AA6 | VSS_249 | - | - | - |
| AA11 | VSS_250 | - | - | - |
| AA16 | VSS_251 | - | - | - |
| AA17 | VSS_252 | - | - | - |
| AA18 | VSS_253 | - | - | - |
| AA19 | VSS_254 | - | - | - |
| AA20 | VSS_255 | - | - | - |
| AA21 | VSS_256 | - | - | - |
| AA22 | VSS_257 | - | - | - |
| AA23 | VSS_258 | - | - | - |
| AA24 | VSS_259 | - | - | - |
| AA31 | VSS_260 | - | - | - |
| AB3 | VSS_261 | - | - | - |
| AB5 | VSS_262 | - | - | - |
| AB11 | VSS_263 | - | - | - |
| AB16 | VSS_264 | - | - | - |
| AB17 | VSS_265 | - | - | - |
| AB18 | VSS_266 | - | - | - |
| AB19 | VSS_267 | - | - | - |
| AB20 | VSS_268 | - | - | - |
| AB24 | VSS_269 | - | - | - |
| AB27 | VSS_270 | - | - | - |
| AB29 | VSS_271 | - | - | - |
| AB32 | VSS_272 | - | - | - |
| AC3 | VSS_273 | - | - | - |
| AC4 | VSS_274 | - | - | - |
| AC11 | VSS_275 | - | - | - |
| AC12 | VSS_276 | - | - | - |
| AC16 | VSS_277 | - | - | - |
| AC20 | VSS_278 | - | - | - |
| AC21 | VSS_279 | - | - | - |
| AC24 | VSS_280 | - | - | - |
| AC27 | VSS_281 | - | - | - |
| AD11 | VSS_282 | - | - | - |
| AD12 | VSS_283 | - | - | - |
| AD16 | VSS_284 | - | - | - |
| AD20 | VSS_285 | - | - | - |
| AD21 | VSS_286 | - | - | - |
| AD24 | VSS_287 | - | - | - |
| AD25 | VSS_288 | - | - | - |
| AD26 | VSS_289 | - | - | - |
| AE3 | VSS_290 | - | - | - |
| AE11 | VSS_291 | - | - | - |
| AE12 | VSS_292 | - | - | - |
| AE13 | VSS_293 | - | - | - |
| AE14 | VSS_294 | - | - | - |
| AE15 | VSS_295 | - | - | - |
| AE16 | VSS_296 | - | - | - |
| AE18 | VSS_297 | - | - | - |
| AE19 | VSS_298 | - | - | - |
| AE20 | VSS_299 | - | - | - |
| AE21 | VSS_300 | - | - | - |
| AE24 | VSS_301 | - | - | - |
| AE26 | VSS_302 | - | - | - |
| AF22 | VSS_303 | - | - | - |
| AF24 | VSS_304 | - | - | - |
| AF25 | VSS_305 | - | - | - |
| AF27 | VSS_306 | - | - | - |
| AF28 | VSS_307 | - | - | - |
| AF29 | VSS_308 | - | - | - |
| AF30 | VSS_309 | - | - | - |
| AF31 | VSS_310 | - | - | - |
| AF32 | VSS_311 | - | - | - |
| AG30 | VSS_312 | - | - | - |
| AJ30 | VSS_313 | - | - | - |
| AK28 | VSS_314 | - | - | - |
| AK29 | VSS_315 | - | - | - |
| AL25 | VSS_316 | - | - | - |
| AM30 | VSS_317 | - | - | - |

### AVSS (101p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| H28 | AVSS_1 | - | - | - |
| H31 | AVSS_2 | - | - | - |
| J27 | AVSS_3 | - | - | - |
| J28 | AVSS_4 | - | - | - |
| J29 | AVSS_5 | - | - | - |
| J32 | AVSS_6 | - | - | - |
| K26 | AVSS_7 | - | - | - |
| K31 | AVSS_8 | - | - | - |
| K32 | AVSS_9 | - | - | - |
| L26 | AVSS_10 | - | - | - |
| L31 | AVSS_11 | - | - | - |
| M26 | AVSS_12 | - | - | - |
| M32 | AVSS_13 | - | - | - |
| N32 | AVSS_14 | - | - | - |
| AA8 | AVSS_15 | - | - | - |
| AA10 | AVSS_16 | - | - | - |
| AB6 | AVSS_17 | - | - | - |
| AB7 | AVSS_18 | - | - | - |
| AB8 | AVSS_19 | - | - | - |
| AB10 | AVSS_20 | - | - | - |
| AC5 | AVSS_21 | - | - | - |
| AC8 | AVSS_22 | - | - | - |
| AC10 | AVSS_23 | - | - | - |
| AD5 | AVSS_24 | - | - | - |
| AD8 | AVSS_25 | - | - | - |
| AD10 | AVSS_26 | - | - | - |
| AE6 | AVSS_27 | - | - | - |
| AE7 | AVSS_28 | - | - | - |
| AE9 | AVSS_29 | - | - | - |
| AF4 | AVSS_30 | - | - | - |
| AF7 | AVSS_31 | - | - | - |
| AF8 | AVSS_32 | - | - | - |
| AF11 | AVSS_33 | - | - | - |
| AF12 | AVSS_34 | - | - | - |
| AF13 | AVSS_35 | - | - | - |
| AF14 | AVSS_36 | - | - | - |
| AF15 | AVSS_37 | - | - | - |
| AF16 | AVSS_38 | - | - | - |
| AF21 | AVSS_39 | - | - | - |
| AG3 | AVSS_40 | - | - | - |
| AG6 | AVSS_41 | - | - | - |
| AG7 | AVSS_42 | - | - | - |
| AG10 | AVSS_43 | - | - | - |
| AG12 | AVSS_44 | - | - | - |
| AG15 | AVSS_45 | - | - | - |
| AG18 | AVSS_46 | - | - | - |
| AG21 | AVSS_47 | - | - | - |
| AG22 | AVSS_48 | - | - | - |
| AH4 | AVSS_49 | - | - | - |
| AH8 | AVSS_50 | - | - | - |
| AH11 | AVSS_51 | - | - | - |
| AH12 | AVSS_52 | - | - | - |
| AH15 | AVSS_53 | - | - | - |
| AH21 | AVSS_54 | - | - | - |
| AH22 | AVSS_55 | - | - | - |
| AH23 | AVSS_56 | - | - | - |
| AJ3 | AVSS_57 | - | - | - |
| AJ7 | AVSS_58 | - | - | - |
| AJ8 | AVSS_59 | - | - | - |
| AJ9 | AVSS_60 | - | - | - |
| AJ11 | AVSS_61 | - | - | - |
| AJ12 | AVSS_62 | - | - | - |
| AJ15 | AVSS_63 | - | - | - |
| AJ16 | AVSS_64 | - | - | - |
| AJ18 | AVSS_65 | - | - | - |
| AJ21 | AVSS_66 | - | - | - |
| AJ22 | AVSS_67 | - | - | - |
| AJ23 | AVSS_68 | - | - | - |
| AK4 | AVSS_69 | - | - | - |
| AK5 | AVSS_70 | - | - | - |
| AK7 | AVSS_71 | - | - | - |
| AK10 | AVSS_72 | - | - | - |
| AK11 | AVSS_73 | - | - | - |
| AK12 | AVSS_74 | - | - | - |
| AK13 | AVSS_75 | - | - | - |
| AK14 | AVSS_76 | - | - | - |
| AK23 | AVSS_77 | - | - | - |
| AL3 | AVSS_78 | - | - | - |
| AL4 | AVSS_79 | - | - | - |
| AL5 | AVSS_80 | - | - | - |
| AL11 | AVSS_81 | - | - | - |
| AL13 | AVSS_82 | - | - | - |
| AL23 | AVSS_83 | - | - | - |
| AM4 | AVSS_84 | - | - | - |
| AM8 | AVSS_85 | - | - | - |
| AM9 | AVSS_86 | - | - | - |
| AM18 | AVSS_87 | - | - | - |
| AM20 | AVSS_88 | - | - | - |
| AM22 | AVSS_89 | - | - | - |
| AM23 | AVSS_90 | - | - | - |
| AM24 | AVSS_91 | - | - | - |
| AM26 | AVSS_92 | - | - | - |
| AM28 | AVSS_93 | - | - | - |
| AN7 | AVSS_94 | - | - | - |
| AN12 | AVSS_95 | - | - | - |
| AN23 | AVSS_96 | - | - | - |
| AN31 | AVSS_97 | - | - | - |
| AP1 | AVSS_98 | - | - | - |
| AP17 | AVSS_99 | - | - | - |
| AP23 | AVSS_100 | - | - | - |
| AP34 | AVSS_101 | - | - | - |

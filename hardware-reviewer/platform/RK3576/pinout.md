# RK3576 PinOut List

> Source: RK3576_PinOut_V1.0_20240302.xlsx
> 698 pins, 148 GPIO

## GPIO -> Domain

| Domain | Pins | Count |
|--------|------|-------|
| PMUIO0 | GPIO0_A0, GPIO0_A1, GPIO0_A2, GPIO0_A3, GPIO0_A4, GPIO0_A5, GPIO0_A6, GPIO0_A7, GPIO0_B0, GPIO0_B1, GPIO0_B2, GPIO0_B3 | 12 |
| PMUIO1 | GPIO0_B4, GPIO0_B5, GPIO0_B6, GPIO0_B7, GPIO0_C0, GPIO0_C1, GPIO0_C2, GPIO0_C3, GPIO0_C4, GPIO0_C5, GPIO0_C6, GPIO0_C7, GPIO0_D0, GPIO0_D1, ... (+4) | 18 |
| VCCIO0 | GPIO1_A0, GPIO1_A1, GPIO1_A2, GPIO1_A3, GPIO1_A4, GPIO1_A5, GPIO1_A6, GPIO1_A7, GPIO1_B0, GPIO1_B1, GPIO1_B2, GPIO1_B3 | 12 |
| VCCIO1 | GPIO2_A0, GPIO2_A1, GPIO2_A2, GPIO2_A3, GPIO2_A4, GPIO2_A5 | 6 |
| VCCIO2 | GPIO4_A2, GPIO4_A3, GPIO4_A4, GPIO4_A5, GPIO4_A6, GPIO4_A7, GPIO4_B0, GPIO4_B1, GPIO4_B2, GPIO4_B3, GPIO4_B4, GPIO4_B5 | 12 |
| VCCIO3 | GPIO1_B4, GPIO1_B5, GPIO1_B6, GPIO1_B7, GPIO1_C0, GPIO1_C1, GPIO1_C2, GPIO1_C3, GPIO1_C4, GPIO1_C5, GPIO1_C6, GPIO1_C7, GPIO1_D0, GPIO1_D1, ... (+4) | 18 |
| VCCIO4 | GPIO2_A6, GPIO2_A7, GPIO2_B0, GPIO2_B1, GPIO2_B2, GPIO2_B3, GPIO2_B4, GPIO2_B5, GPIO2_B6, GPIO2_B7, GPIO2_C0, GPIO2_C1, GPIO2_C2, GPIO2_C3, ... (+16) | 30 |
| VCCIO5_VCC | GPIO3_A4, GPIO3_A5, GPIO3_A6, GPIO3_A7, GPIO3_B0, GPIO3_B1, GPIO3_B2, GPIO3_B3, GPIO3_B4, GPIO3_B5, GPIO3_B6, GPIO3_B7, GPIO3_C0, GPIO3_C1, ... (+16) | 30 |
| VCCIO6 | GPIO4_C0, GPIO4_C1, GPIO4_C2, GPIO4_C3, GPIO4_C4, GPIO4_C5, GPIO4_C6, GPIO4_C7 | 8 |
| VCCIO7 | GPIO4_D0, GPIO4_D1 | 2 |

## Full Table


### DDR (97p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| W1 | LP4_DQ0_A/LP4X_DQ0_A/LP5_DQ0_A | - | I/O | - |
| 1T1 | LP4_DQ1_A/LP4X_DQ1_A/LP5_DQ1_A | - | I/O | - |
| 1P1 | LP4_DQ2_A/LP4X_DQ2_A/LP5_DQ2_A | - | I/O | - |
| U1 | LP4_DQ3_A/LP4X_DQ3_A/LP5_DQ3_A | - | I/O | - |
| 1V3 | LP4_DQ4_A/LP4X_DQ4_A/LP5_DQ4_A | - | I/O | - |
| 1W4 | LP4_DQ5_A/LP4X_DQ5_A/LP5_DQ5_A | - | I/O | - |
| AC1 | LP4_DQ6_A/LP4X_DQ6_A/LP5_DQ6_A | - | I/O | - |
| AB1 | LP4_DQ7_A/LP4X_DQ7_A/LP5_DQ7_A | - | I/O | - |
| 1V1 | LP4_DMI0_A/LP4X_DMI0_A/LP5_DMI0_A | - | I/O | - |
| 1U1 | LP4_DQS0P_A/LP4X_DQS0P_A/LP5_RDQS0P_A | - | I/O | - |
| Y1 | LP4_DQS0N_A/LP4X_DQS0N_A/LP5_RDQS0N_A | - | I/O | - |
| 1V5 | LP5_WCK0P_A | - | O | - |
| 1V4 | LP5_WCK0N_A | - | O | - |
| AF1 | LP4_DQ8_A/LP4X_DQ8_A/LP5_DQ8_A | - | I/O | - |
| 1AB1 | LP4_DQ9_A/LP4X_DQ9_A/LP5_DQ9_A | - | I/O | - |
| 1AD1 | LP4_DQ10_A/LP4X_DQ10_A/LP5_DQ10_A | - | I/O | - |
| AH1 | LP4_DQ11_A/LP4X_DQ11_A/LP5_DQ11_A | - | I/O | - |
| 1Y1 | LP4_DQ12_A/LP4X_DQ12_A/LP5_DQ12_A | - | I/O | - |
| 1W2 | LP4_DQ13_A/LP4X_DQ13_A/LP5_DQ13_A | - | I/O | - |
| 1AA3 | LP4_DQ14_A/LP4X_DQ14_A/LP5_DQ14_A | - | I/O | - |
| 1AA1 | LP4_DQ15_A/LP4X_DQ15_A/LP5_DQ15_A | - | I/O | - |
| AE1 | LP4_DMI1_A/LP4X_DMI1_A/LP5_DMI1_A | - | I/O | - |
| 1AB4 | LP4_DQS1P_A/LP4X_DQS1P_A/LP5_RDQS1P_A | - | I/O | - |
| 1AB3 | LP4_DQS1N_A/LP4X_DQS1N_A/LP5_RDQS1N_A | - | I/O | - |
| 1AA6 | LP5_WCK1P_A | - | O | - |
| 1AA5 | LP5_WCK1N_A | - | O | - |
| T1 | LP4_A0_A/LP4X_A0_A/LP5_A0_A | - | O | - |
| 1N1 | LP4_A1_A/LP4X_A1_A/LP5_A1_A | - | O | - |
| 1R3 | LP4_A2_A/LP4X_A2_A/LP5_A2_A | - | O | - |
| 1T2 | LP4_A3_A/LP4X_A3_A/LP5_A3_A | - | O | - |
| 1M5 | LP4_A4_A/LP4X_A4_A/LP5_A4_A | - | O | - |
| 1P5 | LP4_A5_A/LP4X_A5_A/LP5_A5_A | - | O | - |
| 1R5 | LP5_A6_A | - | O | - |
| 1L1 | LP4_CLKP_A/LP4X_CLKP_A/LP5_CLKP_A | - | O | - |
| P1 | LP4_CLKN_A/LP4X_CLKN_A/LP5_CLKN_A | - | O | - |
| 1R4 | LP4_CSN0_A/LP4X_CSN0_A | - | O | - |
| 1T4 | LP4_CSN1_A/LP4X_CSN1_A | - | O | - |
| 1N3 | LP4_CKE0_A/LP4X_CKE0_A/LP5_CSN0_A | - | O | - |
| 1N5 | LP4_CKE1_A/LP4X_CKE1_A/LP5_CSN1_A | - | O | - |
| 1R6 | ZQ_A | - | A | - |
| 1D2 | LP4_DQ0_B/LP4X_DQ0_B/LP5_DQ0_B | - | I/O | - |
| 1F2 | LP4_DQ1_B/LP4X_DQ1_B/LP5_DQ1_B | - | I/O | - |
| 1G1 | LP4_DQ2_B/LP4X_DQ2_B/LP5_DQ2_B | - | I/O | - |
| K1 | LP4_DQ3_B/LP4X_DQ3_B/LP5_DQ3_B | - | I/O | - |
| 1C3 | LP4_DQ4_B/LP4X_DQ4_B/LP5_DQ4_B | - | I/O | - |
| 1B3 | LP4_DQ5_B/LP4X_DQ5_B/LP5_DQ5_B | - | I/O | - |
| A5 | LP4_DQ6_B/LP4X_DQ6_B/LP5_DQ6_B | - | I/O | - |
| G1 | LP4_DQ7_B/LP4X_DQ7_B/LP5_DQ7_B | - | I/O | - |
| B4 | LP4_DMI0_B/LP4X_DMI0_B/LP5_DMI0_B | - | I/O | - |
| H1 | LP4_DQS0P_B/LP4X_DQS0P_B/LP5_RDQS0P_B | - | I/O | - |
| 1F1 | LP4_DQS0N_B/LP4X_DQS0N_B/LP5_RDQS0N_B | - | I/O | - |
| 1G5 | LP5_WCK0P_B | - | O | - |
| 1G4 | LP5_WCK0N_B | - | O | - |
| 1A1 | LP4_DQ8_B/LP4X_DQ8_B/LP5_DQ8_B | - | I/O | - |
| B1 | LP4_DQ9_B/LP4X_DQ9_B/LP5_DQ9_B | - | I/O | - |
| B2 | LP4_DQ10_B/LP4X_DQ10_B/LP5_DQ10_B | - | I/O | - |
| A2 | LP4_DQ11_B/LP4X_DQ11_B/LP5_DQ11_B | - | I/O | - |
| 1E1 | LP4_DQ12_B/LP4X_DQ12_B/LP5_DQ12_B | - | I/O | - |
| 1C1 | LP4_DQ13_B/LP4X_DQ13_B/LP5_DQ13_B | - | I/O | - |
| E1 | LP4_DQ14_B/LP4X_DQ14_B/LP5_DQ14_B | - | I/O | - |
| D1 | LP4_DQ15_B/LP4X_DQ15_B/LP5_DQ15_B | - | I/O | - |
| 1B1 | LP4_DMI1_B/LP4X_DMI1_B/LP5_DMI1_B | - | I/O | - |
| A3 | LP4_DQS1P_B/LP4X_DQS1P_B/LP5_RDQS1P_B | - | I/O | - |
| B3 | LP4_DQS1N_B/LP4X_DQS1N_B/LP5_RDQS1N_B | - | I/O | - |
| 1D4 | LP5_WCK1P_B | - | O | - |
| 1E4 | LP5_WCK1N_B | - | O | - |
| L1 | LP4_A0_B/LP4X_A0_B/LP5_A0_B | - | O | - |
| 1J1 | LP4_A1_B/LP4X_A1_B/LP5_A1_B | - | O | - |
| 1J3 | LP4_A2_B/LP4X_A2_B/LP5_A2_B | - | O | - |
| 1G2 | LP4_A3_B/LP4X_A3_B/LP5_A3_B | - | O | - |
| 1F4 | LP4_A4_B/LP4X_A4_B/LP5_A4_B | - | O | - |
| 1K5 | LP4_A5_B/LP4X_A5_B/LP5_A5_B | - | O | - |
| 1H5 | LP5_A6_B | - | O | - |
| 1K1 | LP4_CLKP_B/LP4X_CLKP_B/LP5_CLKP_B | - | O | - |
| N1 | LP4_CLKN_B/LP4X_CLKN_B/LP5_CLKN_B | - | O | - |
| 1J5 | LP4_CSN0_B/LP4X_CSN0_B | - | O | - |
| 1K4 | LP4_CSN1_B/LP4X_CSN1_B | - | O | - |
| 1K2 | LP4_CKE0_B/LP4X_CKE0_B/LP5_CSN0_B | - | O | - |
| 1M3 | LP4_CKE1_B/LP4X_CKE1_B/LP5_CSN1_B | - | O | - |
| 1U5 | LP4_RESET/LP4X_RESET/LP5_RESET | - | O | - |
| 1J6 | ZQ_B | - | A | - |
| 2C3 | DDRPHY_PLL_DVDD | TBD | PI | - |
| 2D2 | DDRPHY_PLL_AVDD1V8 | 1.8V | API | - |
| 2C2 | DDRPHY_PLL_AVSS | - | G | - |
| 2E2 | DDRPHY_DVDD_0 | TBD | PI | - |
| 2F3 | DDRPHY_DVDD_1 | - | PI | - |
| 2G2 | DDRPHY_DVDD_2 | - | PI | - |
| 2G3 | DDRPHY_DVDD_3 | - | PI | - |
| 2H2 | DDRPHY_DVDD_4 | - | PI | - |
| 2B2 | DDRPHY_CKE_VDDQ | 1.1V/1.05V | PI | - |
| 2D1 | DDRPHY_CK_VDDQ | 0.6V/0.5V | PI | - |
| 2E1 | DDRPHY_VDDQ_0 | 0.6V/0.5V | PI | - |
| 2F1 | DDRPHY_VDDQ_1 | - | PI | - |
| 2F2 | DDRPHY_VDDQ_2 | - | PI | - |
| 2G1 | DDRPHY_VDDQ_3 | - | PI | - |
| 2H1 | DDRPHY_VDDQ_4 | - | PI | - |
| 2J2 | DDRPHY_VDDQ_5 | - | PI | - |

### UFS (11p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 1AD6 | UFS_TX_D0P | - | AO | - |
| 1AC6 | UFS_TX_D0N | - | AO | - |
| 1AD4 | UFS_TX_D1P | - | AO | - |
| 1AD5 | UFS_TX_D1N | - | AO | - |
| AK8 | UFS_RX_D0P | - | AI | - |
| AL7 | UFS_RX_D0N | - | AI | - |
| AK7 | UFS_RX_D1P | - | AI | - |
| AL6 | UFS_RX_D1N | - | AI | - |
| 2R2 | UFS_TX_REXT | - | A | - |
| 2N2 | UFS_AVDD0V85 | 0.85V | API | - |
| 2P2 | UFS_AVDD1V8 | 1.8V | API | - |

### VCCIO0 (13p, 12 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| E28 | EMMC_D0/FSPI0_D0/SAI0_SCLK_M2/UART7_RTSN_M1/I2C2_SCL_M1/GPIO1_A0_u | - | I/O | up |
| E29 | EMMC_D1/FSPI0_D1/SAI0_LRCK_M2/UART7_CTSN_M1/I2C2_SDA_M1/GPIO1_A1_u | - | I/O | up |
| 1C24 | EMMC_D2/FSPI0_D2/SAI0_SDO1_M2/SAI0_SDI3_M2/PDM0_SDI3_M1/UART7_TX_M1/UART6_RTSN_M | - | I/O | up |
| F28 | EMMC_D3/FSPI0_D3/SAI0_SDO2_M2/SAI0_SDI2_M2/PDM0_SDI1_M1/UART7_RX_M1/UART6_CTSN_M | - | I/O | up |
| 1D24 | EMMC_D4/SAI0_MCLK_M2/SAI3_MCLK_M0/SPI0_CSN0_M2/GPIO1_A4_u | - | I/O | up |
| G28 | EMMC_D5/SAI3_SCLK_M0/PDM0_SDI2_M1/SPI0_MOSI_M2/I2C9_SCL_M0/GPIO1_A5_u | - | I/O | up |
| D28 | EMMC_D6/SAI3_LRCK_M0/PDM0_CLK1_M1/SPI0_MISO_M2/I2C9_SDA_M0/GPIO1_A6_u | - | I/O | up |
| 1B24 | EMMC_D7/SAI0_SDO0_M2/SAI3_SDI_M0/SPI0_CLK_M2/GPIO1_A7_u | - | I/O | up |
| 1F22 | EMMC_CMD/FSPI0_RSTN/FSPI0_CSN1/UART6_TX_M2/I2C7_SCL_M0/GPIO1_B0_u | - | I/O | up |
| 1G23 | EMMC_CLK/FSPI0_CLK/SAI0_SDO3_M2/SAI0_SDI1_M2/PDM0_CLK0_M1/PWM2_CH7_M1/GPIO1_B1_d | - | I/O | down |
| 1F23 | EMMC_STRB/SAI0_SDI0_M2/SAI3_SDO_M0/PDM0_SDI0_M1/SPI0_CSN1_M2/GPIO1_B2_d | - | I/O | down |
| 1D23 | EMMC_RSTN/FSPI0_CSN0/UART6_RX_M2/I2C7_SDA_M0/MIPI_TE_M3/PWM2_CH1_M0/GPIO1_B3_u | - | I/O | up |
| 1J20 | VCCIO0_VCC1V8 | 1.8V | PI | - |

### VCCIO1 (7p, 6 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| B24 | SDMMC0_D0/FSPI1_D0_M0/DSM_AUD_LP_M0/UART0_RX_M1/UART7_RX_M2/I2C8_SCL_M0/SPI0_MOS | - | I/O | down |
| B25 | SDMMC0_D1/FSPI1_D1_M0/DSM_AUD_LN_M0/SAI3_MCLK_M3/UART0_TX_M1/UART7_TX_M2/I2C8_SD | - | I/O | down |
| A23 | SDMMC0_D2/FSPI1_D2_M0/DSM_AUD_RP_M0/SAI3_LRCK_M3/JTAG_TCK_M0/UART5_RTSN_M2/SPI0_ | - | I/O | down |
| B23 | SDMMC0_D3/FSPI1_D3_M0/DSM_AUD_RN_M0/SAI3_SDI_M3/JTAG_TMS_M0/UART5_CTSN_M2/CAN1_T | - | I/O | down |
| 1A21 | SDMMC0_CMD/FSPI1_CSN0_M0/SAI3_SDO_M3/UART5_RX_M2/I2C5_SDA_M0/SPI0_CSN0_M1/PWM2_C | - | I/O | down |
| 1B21 | SDMMC0_CLK/FSPI1_CLK_M0/SAI3_SCLK_M3/TEST_CLK_OUT/UART5_TX_M2/I2C5_SCL_M0/SPI0_C | - | I/O | down |
| 2A8 | VCCIO1_VCC | 1.8V/3.3V | PI | - |

### OSC (3p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| U29 | OSC_XOUT | - | AO | - |
| U28 | OSC_XIN | - | AI | - |
| 2J10 | OSC_AVDD1V8 | 1.8V | API | - |

### PLL (3p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2G11 | PLL_DVDD0V75 | 0.75V | PI | - |
| 2H12 | PLL_AVDD1V8 | 1.8V | API | - |
| 2G12 | PLL_AVSS | - | G | - |

### PMUIO0 (15p, 12 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| W28 | NPOR | - | I | up |
| 2H10 | TVSS | - | G | - |
| V29 | REF_CLK0_OUT/AUPLL_CLK_IN_M0/GPIO0_A0_d | - | I/O | down |
| 1R24 | TSADC_CTRL_M0/TSADC_CTRL_ORG/GPIO0_A1_z | - | I/O | high-z |
| 1U23 | CLK_32K_IN/CLK0_32K_OUT/I2C6_SCL_M0/GPIO0_A2_d | - | I/O | down |
| Y28 | PWR_CTRL1/TSADC_CTRL_M1/GPIO0_A3_d | - | I/O | down |
| 1T24 | PWR_CTRL2/GPIO0_A4_d | - | I/O | down |
| Y29 | PWR_CTRL3/I2C6_SDA_M0/GPIO0_A5_d | - | I/O | down |
| 1T21 | PMIC_INT/GPIO0_A6_u | - | I/O | up |
| 1U21 | SDMMC0_DETN/SPI2_CSN1_M0/GPIO0_A7_u | - | I/O | up |
| 1U22 | AUPLL_CLK_IN_M1/SPI2_CSN0_M0/I2C0_SCL_M0/GPIO0_B0_z | - | I/O | high-z |
| 1P23 | SPI2_MISO_M0/I2C0_SDA_M0/GPIO0_B1_z | - | I/O | high-z |
| 1T22 | SPI2_CLK_M0/I2C1_SCL_M0/GPIO0_B2_z | - | I/O | high-z |
| 1T23 | SPI2_MOSI_M0/I2C1_SDA_M0/GPIO0_B3_z | - | I/O | high-z |
| 2K11 | PMUIO0_VCC1V8 | 1.8V | PI | - |

### PMUIO1 (19p, 18 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AD28 | REF_CLK1_OUT/I2C1_SCL_M1/UART4_TX_M2/PWM1_CH0_M0/GPIO0_B4_d | - | I/O | down |
| AD29 | REF_CLK2_OUT/I2C1_SDA_M1/UART4_RX_M2/PWM1_CH1_M0/GPIO0_B5_d | - | I/O | down |
| 1Y24 | SDMMC0_PWREN/SDMMC1_DETN_M2/HDMI_TX_HPDIN_M1/EDP_TX_HPDIN_M1/PWM1_CH2_M0/GPIO0_B | - | I/O | down |
| 1W24 | I2C2_SCL_M0/UART1_TX_M0/NPU_AVS/PWM1_CH4_M0/GPIO0_B7_d | - | I/O | down |
| AB29 | I2C2_SDA_M0/UART1_RX_M0/CPULIT_AVS/PWM1_CH3_M0/GPIO0_C0_d | - | I/O | down |
| AB28 | I2C0_SCL_M1/UART8_TX_M2/I3C0_SCL_M0/GPIO0_C1_d | - | I/O | down |
| 1V24 | I2C0_SDA_M1/UART8_RX_M2/I3C0_SDA_M0/GPIO0_C2_d | - | I/O | down |
| 1W21 | PDM0_CLK1_M0/HDMI_TX_CEC_M1/SPI0_CSN1_M0/PWM0_CH1_M0/GPIO0_C3_d | - | I/O | down |
| 1W22 | SAI0_MCLK_M1/PDM0_CLK0_M0/UART10_TX_M2/PWM0_CH0_M0/GPIO0_C4_d | - | I/O | down |
| 1AA22 | SAI0_SDO0_M1/DP_HPDIN_M1/UART10_RX_M2/I3C0_SDA_PU_M0/GPIO0_C5_d | - | I/O | down |
| 1Y21 | SAI0_SCLK_M1/I2C3_SCL_M1/SPI0_CSN0_M0/GPIO0_C6_d | - | I/O | down |
| 1Y23 | SAI0_LRCK_M1/I2C3_SDA_M1/SPI0_CLK_M0/GPIO0_C7_d | - | I/O | down |
| 1W23 | SAI0_SDI0_M1/PDM0_SDI0_M0/SPI0_MOSI_M0/GPIO0_D0_d | - | I/O | down |
| AC28 | SAI0_SDI1_M1/SAI0_SDO3_M1/PDM0_SDI1_M0/SPI0_MISO_M0/GPIO0_D1_d | - | I/O | down |
| 1Y22 | SAI0_SDI2_M1/SAI0_SDO2_M1/PDM0_SDI2_M0/I2C4_SCL_M0/CPUBIG_AVS/PWM1_CH5_M0/UART1_ | - | I/O | down |
| 1AA23 | SAI0_SDI3_M1/SAI0_SDO1_M1/PDM0_SDI3_M0/I2C4_SDA_M0/GPU_AVS/PWM2_CH0_M0/UART1_RTS | - | I/O | down |
| 1U24 | UART0_TX_M0/JTAG_TCK_M1/GPIO0_D4_u | - | I/O | up |
| AA28 | UART0_RX_M0/JTAG_TMS_M1/GPIO0_D5_u | - | I/O | up |
| 1U20 | PMUIO1_VCC | 1.8V/3.3V | PI | - |

### PMU_LOGIC (2p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2L2 | PMU_LOGIC_DVDD0V75_0 | 0.75V | PI | - |
| 2L10 | PMU_LOGIC_DVDD0V75_1 | 0.75V | PI | - |

### VCCIO2 (13p, 12 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 1D6 | SAI1_MCLK_M0/SAI4_MCLK_M0/AUPLL_CLK_IN_M2/PWM2_CH5_M0/GPIO4_A2_d | - | I/O | down |
| 1C6 | SAI1_SCLK_M0/FLEXBUS1_CSN_M4/SPI3_CSN0_M2/UART5_RTSN_M1/I2C2_SCL_M2/PWM2_CH4_M1/ | - | I/O | down |
| 1C5 | SAI4_SCLK_M0/PDM1_SDI3_M1/FLEXBUS0_D13_M1/SPI3_MOSI_M2/UART6_TX_M0/I2C4_SCL_M1/C | - | I/O | down |
| 1B6 | SAI1_LRCK_M0/FLEXBUS1_D12_M1/SPI4_CSN1_M2/UART5_CTSN_M1/I2C2_SDA_M2/PCIE1_CLKREQ | - | I/O | down |
| 1B5 | SAI4_LRCK_M0/PDM1_CLK0_M1/FLEXBUS0_D14_M1/SPI3_MISO_M2/UART6_RX_M0/I2C4_SDA_M1/C | - | I/O | down |
| A7 | SAI1_SDO0_M0/SAI4_SDI_M0/SPI3_CLK_M2/PWM2_CH6_M0/GPIO4_A7_d | - | I/O | down |
| 1A5 | SAI1_SDO1_M0/SAI1_SDI3_M0/PDM1_CLK1_M1/FLEXBUS1_D13_M1/SPI4_CLK_M2/UART5_TX_M1/U | - | I/O | down |
| B7 | SAI1_SDO2_M0/SAI1_SDI2_M0/PDM1_SDI2_M1/FLEXBUS1_D14_M1/SPI4_MOSI_M2/UART5_RX_M1/ | - | I/O | down |
| B6 | SAI1_SDO3_M0/SAI1_SDI1_M0/PDM1_SDI1_M1/FLEXBUS1_D15_M1/SPI4_MISO_M2/MIPI_TE_M0/G | - | I/O | down |
| 1A6 | SAI1_SDI0_M0/SAI4_SDO_M0/PDM1_SDI0_M1/SPI4_CSN0_M2/SPI3_CSN1_M2/PWM2_CH7_M0/GPIO | - | I/O | down |
| B8 | SPDIF_RX0_M0/FLEXBUS0_CSN_M4/UART2_RX_M1/I2C3_SDA_M0/CAN1_RX_M2/GPIO4_B4_d | - | I/O | down |
| 1A4 | SPDIF_TX0_M0/FLEXBUS0_D15_M1/UART2_TX_M1/I2C3_SCL_M0/PCIE0_CLKREQN_M2/CAN1_TX_M2 | - | I/O | down |
| 2A2 | VCCIO2_VCC | 1.8V/3.3V | PI | - |

### VCCIO3 (19p, 18 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| A28 | ETH1_RXD2_M1/SDMMC1_D0_M0/SAI3_SCLK_M1/I2C9_SDA_M1/SPI1_CLK_M0/PCIE1_CLKREQN_M1/ | - | I/O | down |
| B27 | ETH1_RXD3_M1/SDMMC1_D1_M0/SAI3_LRCK_M1/I2C9_SCL_M1/SPI1_MOSI_M0/PWM1_CH1_M1/GPIO | - | I/O | down |
| 1A23 | ETH1_RXCLK_M1/SDMMC1_D2_M0/SAI3_SDO_M1/UART3_CTSN_M2/SPI1_MISO_M0/PCIE0_CLKREQN_ | - | I/O | down |
| A27 | ETH1_TXD2_M1/SDMMC1_D3_M0/SAI3_SDI_M1/UART3_RTSN_M2/SPI1_CSN0_M0/GPIO1_B7_d | - | I/O | down |
| B26 | ETH1_TXD3_M1/SDMMC1_CMD_M0/PDM0_SDI2_M2/UART3_TX_M2/SPI1_CSN1_M0/PWM0_CH0_M1/GPI | - | I/O | down |
| 1B22 | ETH1_TXCLK_M1/SDMMC1_CLK_M0/SAI3_MCLK_M1/PDM0_CLK0_M2/UART3_RX_M2/GPIO1_C1_d | - | I/O | down |
| B29 | ETH1_PPSCLK_M1/SDMMC1_PWREN_M0/FSPI1_RSTN_M1/FSPI1_CSN1_M1/UART4_RTSN_M1/I2C6_SC | - | I/O | up |
| 1C23 | ETH1_PPSTRIG_M1/SDMMC1_DETN_M0/FSPI1_CSN0_M1/UART4_CTSN_M1/I2C6_SDA_M1/SPI2_CSN0 | - | I/O | up |
| 1B23 | ETH1_TXD0_M1/FSPI1_D0_M1/UART4_TX_M1/UART2_RTSN_M0/SPI2_MOSI_M1/PCIE0_BUTTONRSTN | - | I/O | down |
| B28 | ETH1_TXD1_M1/FSPI1_D1_M1/UART4_RX_M1/UART2_CTSN_M0/SPI2_MISO_M1/PCIE1_BUTTONRSTN | - | I/O | down |
| A26 | ETH1_TXCTL_M1/FSPI1_D2_M1/PDM0_SDI0_M2/UART2_TX_M0/I2C8_SCL_M1/SATA_CPPOD/GPIO1_ | - | I/O | down |
| 1C22 | ETH1_RXD0_M1/FSPI1_D3_M1/PDM0_SDI1_M2/UART2_RX_M0/I2C8_SDA_M1/SATA_CPDET/GPIO1_C | - | I/O | down |
| C29 | ETH1_RXD1_M1/SAI2_SDO_M0/UART10_TX_M1/GPIO1_D0_d | - | I/O | down |
| 1D22 | ETH1_RXCTL_M1/SAI2_SCLK_M0/UART10_RX_M1/I3C0_SDA_PU_M1/GPIO1_D1_d | - | I/O | down |
| 1A24 | ETH1_MDC_M1/SAI2_LRCK_M0/I3C0_SCL_M1/PWM1_CH3_M1/GPIO1_D2_d | - | I/O | down |
| C28 | ETH1_MDIO_M1/SAI2_SDI_M0/I3C0_SDA_M1/PWM1_CH4_M1/GPIO1_D3_d | - | I/O | down |
| 1E21 | ETH1_MCLK_M1/SAI2_MCLK_M0/PDM0_SDI3_M2/SPDIF_RX1_M2/UART10_RTSN_M1/I2C5_SCL_M1/G | - | I/O | down |
| 1E22 | ETH_CLK1_25M_OUT_M1/FSPI1_CLK_M1/PDM0_CLK1_M2/SPDIF_TX1_M2/UART10_CTSN_M1/I2C5_S | - | I/O | down |
| 2B10 | VCCIO3_VCC | 1.8V/3.3V | PI | - |

### VCCIO4 (31p, 30 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| B22 | VI_CIF_D15/SDMMC1_D0_M1/ETH0_RXD0_M1/SAI0_SDO0_M0/UART8_TX_M1/SPI4_CSN1_M3/I2C4_ | - | I/O | down |
| B20 | VI_CIF_D14/SDMMC1_D1_M1/ETH0_TXCTL_M1/SAI0_SDO1_M0/UART8_RX_M1/I2C4_SDA_M2/GPIO2 | - | I/O | down |
| B19 | VI_CIF_D13/SDMMC1_D2_M1/ETH0_TXD1_M1/SAI0_SDI0_M0/PDM0_SDI3_M3/UART1_TX_M1/GPIO2 | - | I/O | down |
| 1A18 | VI_CIF_D12/SDMMC1_D3_M1/ETH0_TXD0_M1/SAI0_SDI1_M0/PDM0_SDI2_M3/UART1_RX_M1/GPIO2 | - | I/O | down |
| 1A17 | VI_CIF_D11/SDMMC1_CMD_M1/ETH0_TXD3_M1/SAI0_SDI2_M0/PDM0_SDI1_M3/UART1_CTSN_M1/SP | - | I/O | down |
| 1B16 | VI_CIF_D10/SDMMC1_CLK_M1/ETH0_TXCLK_M1/SAI0_SDO2_M0/PDM0_CLK1_M3/UART1_RTSN_M1/S | - | I/O | down |
| A19 | VI_CIF_D9/SDMMC1_PWREN_M1/ETH0_TXD2_M1/SAI0_SDI3_M0/PDM0_SDI0_M3/UART7_CTSN_M0/S | - | I/O | down |
| 1C18 | VI_CIF_D8/SDMMC1_DETN_M1/ETH0_RXCLK_M1/SAI0_MCLK_M0/PDM0_CLK0_M3/UART7_RTSN_M0/S | - | I/O | down |
| A21 | VI_CIF_D7/ETH1_PTP_REFCLK_M1/ETH0_RXD3_M1/SAI0_SCLK_M0/UART7_TX_M0/UART8_RTSN_M1 | - | I/O | down |
| B21 | VI_CIF_D6/ETH0_RXD2_M1/SAI0_LRCK_M0/UART7_RX_M0/UART8_CTSN_M1/I2C8_SDA_M2/GPIO2_ | - | I/O | down |
| A17 | VI_CIF_D5/ETH1_RXD2_M0/ETH0_PTP_REFCLK_M1/PDM1_SDI1_M0/UART9_RX_M0/PWM1_CH0_M2/G | - | I/O | down |
| 1A15 | VI_CIF_D4/ETH1_RXD3_M0/ETH0_PPSCLK_M1/SAI2_MCLK_M1/PDM1_CLK1_M0/UART9_TX_M0/SPI1 | - | I/O | down |
| 1D15 | VI_CIF_D3/ETH1_RXCLK_M0/ETH0_PPSTRIG_M1/SAI2_SCLK_M1/PDM1_SDI2_M0/UART11_CTSN_M1 | - | I/O | down |
| A15 | VI_CIF_D2/ETH1_TXD2_M0/SAI2_LRCK_M1/PDM1_SDI3_M0/UART11_RTSN_M1/SPI1_MISO_M1/PWM | - | I/O | down |
| 1A13 | VI_CIF_D1/ETH1_TXD3_M0/SAI2_SDO_M1/PDM1_SDI0_M0/UART11_TX_M1/SPI1_CSN0_M1/PWM1_C | - | I/O | down |
| 1C15 | VI_CIF_D0/ETH1_TXCLK_M0/SAI2_SDI_M1/PDM1_CLK0_M0/UART11_RX_M1/SPI1_CLK_M1/PWM1_C | - | I/O | down |
| 1A14 | ETH1_TXD0_M0/SAI4_SCLK_M3/UART4_CTSN_M0/I2C5_SCL_M2/PWM1_CH5_M2/GPIO2_C6_d | - | I/O | down |
| B15 | ETH1_TXD1_M0/SAI4_LRCK_M3/UART4_RTSN_M0/I2C5_SDA_M2/PWM0_CH1_M2/GPIO2_C7_d | - | I/O | down |
| B16 | ETH1_TXCTL_M0/SAI4_SDI_M3/UART4_TX_M0/I2C6_SCL_M2/PWM2_CH0_M2/GPIO2_D0_d | - | I/O | down |
| 1A16 | ETH1_RXD0_M0/SAI4_SDO_M3/UART4_RX_M0/I2C6_SDA_M2/PWM2_CH1_M2/GPIO2_D1_d | - | I/O | down |
| B17 | CAM_CLK0_OUT_M1/ETH1_RXD1_M0/SAI4_MCLK_M3/UART6_TX_M1/I3C1_SCL_M0/PWM2_CH2_M2/GP | - | I/O | down |
| B18 | ETH1_RXCTL_M0/UART6_RX_M1/I3C1_SDA_M0/PWM2_CH3_M2/GPIO2_D3_d | - | I/O | down |
| 1B13 | ISP_PRELIGHT_TRIG_M0/ETH1_MDC_M0/UART6_RTSN_M1/I2C9_SDA_M2/PWM2_CH4_M2/GPIO2_D4_ | - | I/O | down |
| 1B15 | ISP_FLASH_TRIGOUT_M0/ETH1_MDIO_M0/UART6_CTSN_M1/I2C9_SCL_M2/PWM2_CH5_M2/GPIO2_D5 | - | I/O | down |
| 1D18 | CAM_CLK1_OUT_M1/ETH_CLK1_25M_OUT_M0/ETH0_MCLK_M1/SAI3_MCLK_M2/SPDIF_RX0_M2/UART9 | - | I/O | down |
| 1E15 | CAM_CLK2_OUT_M1/ETH1_MCLK_M0/ETH_CLK0_25M_OUT_M1/SAI0_SDO3_M0/SPDIF_TX0_M2/UART9 | - | I/O | down |
| 1D16 | VI_CIF_HREF/ETH0_MDIO_M1/SAI3_SCLK_M2/UART3_TX_M0/SPI3_CLK_M0/I2C7_SCL_M1/GPIO3_ | - | I/O | down |
| 1B18 | VI_CIF_VSYNC/ETH1_PPSTRIG_M0/ETH0_MDC_M1/SAI3_LRCK_M2/UART3_RX_M0/SPI3_MOSI_M0/I | - | I/O | down |
| 1A20 | VI_CIF_CLKO/ETH1_PPSCLK_M0/ETH0_RXCTL_M1/SAI3_SDO_M2/SPDIF_RX1_M1/UART3_CTSN_M0/ | - | I/O | down |
| 1A19 | VI_CIF_CLKI/ETH1_PTP_REFCLK_M0/ETH0_RXD1_M1/SAI3_SDI_M2/SPDIF_TX1_M1/UART3_RTSN_ | - | I/O | down |
| 2A7 | VCCIO4_VCC | 1.8V/3.3V | PI | - |

### VCCIO5_VCC (32p, 30 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 1D13 | VO_LCDC_D23/VO_EBC_SDSHR/ETH_CLK0_25M_OUT_M0/SAI4_SDI_M1/DSMC_RDYN/FLEXBUS1_D11/ | - | I/O | down |
| A9 | VO_LCDC_D22/VO_EBC_GDSP/ETH0_MDIO_M0/PDM1_SDI3_M2/DSMC_DATA15/FLEXBUS0_D7/UART1_ | - | I/O | down |
| 1A7 | VO_LCDC_D21/VO_EBC_GDOE/ETH0_MDC_M0/PDM1_SDI2_M2/DSMC_DATA14/FLEXBUS0_D6/UART1_R | - | I/O | down |
| B13 | VO_LCDC_D20/VO_EBC_VCOM/ETH0_RXCTL_M0/PDM1_CLK1_M2/DSMC_DATA13/FLEXBUS0_D5/UART1 | - | I/O | down |
| B14 | VO_LCDC_D19/VO_EBC_SDCE3/ETH0_MCLK_M0/SAI4_MCLK_M1/DSMC_CSN1/FLEXBUS0_D8/UART10_ | - | I/O | down |
| 1A11 | VO_LCDC_D18/VO_EBC_SDCE2/ETH0_RXD1_M0/PDM1_CLK0_M2/DSMC_DATA12/FLEXBUS0_D4/UART1 | - | I/O | down |
| A13 | VO_LCDC_D17/VO_EBC_SDCE1/ETH0_RXD0_M0/PDM1_SDI1_M2/DSMC_DATA11/FLEXBUS0_D3/UART9 | - | I/O | down |
| A11 | VO_LCDC_D16/VO_EBC_SDCE0/ETH0_TXCTL_M0/PDM1_SDI0_M2/DSMC_DATA10/FLEXBUS0_D2/UART | - | I/O | down |
| B10 | VO_LCDC_D15/VO_EBC_SDDO15/ETH0_TXD1_M0/SPDIF_RX1_M0/DSMC_DATA9/FLEXBUS0_D1/UART9 | - | I/O | down |
| 1A9 | VO_LCDC_D14/VO_EBC_SDDO14/ETH0_TXD0_M0/SPDIF_TX1_M0/DSMC_DATA8/FLEXBUS0_D0/UART9 | - | I/O | down |
| B11 | VO_LCDC_D13/VO_EBC_SDDO13/ETH0_TXCLK_M0/DSMC_DQS1/FLEXBUS0_CLK/SPI3_CSN0_M1/PWM0 | - | I/O | down |
| 1D12 | VO_LCDC_D12/VO_EBC_SDDO12/ETH0_PPSTRIG_M0/SAI1_SDI0_M1/DSMC_DQS0/FLEXBUS1_D10/FL | - | I/O | down |
| 1E9 | VO_LCDC_D11/VO_EBC_SDDO11/ETH0_PPSCLK_M0/SAI1_SDO3_M1/DSMC_DATA7/FLEXBUS1_D9/UAR | - | I/O | down |
| 1B10 | VO_LCDC_D10/VO_EBC_SDDO10/ETH0_PTP_REFCLK_M0/SAI1_SDO2_M1/DSMC_DATA6/FLEXBUS1_D8 | - | I/O | down |
| B9 | VO_LCDC_D9/VO_EBC_SDDO9/ETH0_TXD3_M0/SAI2_SCLK_M2/DSMC_INT1/FLEXBUS0_D9/UART11_R | - | I/O | down |
| 1A8 | VO_LCDC_D8/VO_EBC_SDDO8/ETH0_TXD2_M0/SAI2_LRCK_M2/DSMC_INT3/FLEXBUS0_D10/FLEXBUS | - | I/O | down |
| 1D9 | VO_LCDC_D7/VO_EBC_SDDO7/SAI1_SDO1_M1/DSMC_DATA5/FLEXBUS1_D7/UART11_TX_M0/SPI2_CS | - | I/O | down |
| 1B9 | VO_LCDC_D6/VO_EBC_SDDO6/SAI1_SDO0_M1/DSMC_DATA4/FLEXBUS1_D6/UART8_RX_M0/SPI1_MIS | - | I/O | down |
| 1D7 | VO_LCDC_D5/VO_EBC_SDDO5/SAI1_LRCK_M1/DSMC_DATA3/FLEXBUS1_D5/UART8_TX_M0/SPI1_MOS | - | I/O | down |
| 1C7 | VO_LCDC_D4/VO_EBC_SDDO4/SAI1_SCLK_M1/DSMC_DATA2/FLEXBUS1_D4/UART8_RTSN_M0/SPI1_C | - | I/O | down |
| 1C12 | VO_LCDC_D3/VO_EBC_SDDO3/SAI1_MCLK_M1/DSMC_DATA1/FLEXBUS1_D3/UART8_CTSN_M0/SPI1_C | - | I/O | down |
| 1A12 | VO_LCDC_D2/VO_EBC_SDDO2/ETH0_RXCLK_M0/SAI2_MCLK_M2/DSMC_CSN2/FLEXBUS0_D11/FLEXBU | - | I/O | down |
| 1A10 | VO_LCDC_D1/VO_EBC_SDDO1/ETH0_RXD3_M0/SAI2_SDI_M2/DSMC_CSN3/FLEXBUS0_D12/FLEXBUS1 | - | I/O | down |
| B12 | VO_LCDC_D0/VO_EBC_SDDO0/ETH0_RXD2_M0/SAI2_SDO_M2/DSMC_CSN0/FLEXBUS1_D2/UART2_CTS | - | I/O | down |
| 1E12 | VO_LCDC_DEN/VO_EBC_SDLE/SAI1_SDI1_M1/DSMC_DATA0/FLEXBUS1_D1/UART5_RX_M0/SPI3_CLK | - | I/O | down |
| 1D10 | VO_LCDC_HSYNC/VO_EBC_GDCLK/SAI1_SDI2_M1/DSMC_CLKP/FLEXBUS1_D0/UART5_TX_M0/SPI3_M | - | I/O | down |
| 1C10 | VO_LCDC_VSYNC/VO_EBC_SDCLK/SAI1_SDI3_M1/DSMC_CLKN/FLEXBUS1_CLK/UART5_CTSN_M0/SPI | - | I/O | down |
| 1E7 | VO_LCDC_CLK/VO_EBC_SDOE/CAM_CLK0_OUT_M0/SAI4_SCLK_M1/DSMC_RESETN/FLEXBUS0_D15_M0 | - | I/O | down |
| 1B12 | SPDIF_RX0_M1/CAM_CLK1_OUT_M0/SAI4_LRCK_M1/DSMC_INT0/FLEXBUS0_D13_M0/FLEXBUS1_D14 | - | I/O | down |
| 1B7 | VO_POST_EMPTY/SPDIF_TX0_M1/CAM_CLK2_OUT_M0/SAI4_SDO_M1/DSMC_INT2/FLEXBUS0_D14_M0 | - | I/O | down |
| 2A4 | VCCIO5_VCC_0 | 1.8V/3.3V | PI | - |
| 2A5 | VCCIO5_VCC_1 | 1.8V/3.3V | PI | - |

### VCCIO6 (9p, 8 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AK3 | DSM_AUD_LP_M1/SAI4_MCLK_M2/HDMI_TX_CEC_M0/I2C7_SCL_M3/SPI4_CSN1_M0/UART11_TX_M2/ | - | I/O | down |
| AK2 | DSM_AUD_LN_M1/HDMI_TX_HPDIN_M0/PCIE1_CLKREQN_M3/I2C7_SDA_M3/EDP_TX_HPDIN_M0/UART | - | I/O | down |
| AL2 | DSM_AUD_RP_M1/HDMI_TX_SCL/I2C2_SCL_M3/CAN0_TX_M1/UART9_TX_M2/PWM2_CH0_M1/GPIO4_C | - | I/O | down |
| 1AE2 | DSM_AUD_RN_M1/HDMI_TX_SDA/I2C2_SDA_M3/CAN0_RX_M1/UART9_RX_M2/PWM2_CH1_M1/GPIO4_C | - | I/O | down |
| AL3 | ISP_PRELIGHT_TRIG_M1/SAI4_LRCK_M2/DP_HPDIN_M0/I2C3_SCL_M3/SPI4_CSN0_M0/UART6_TX_ | - | I/O | down |
| AK1 | ISP_FLASH_TRIGOUT_M1/SAI4_SDO_M2/VP0_SYNC_OUT/SATA1_ACTLED_M1/I2C3_SDA_M3/SPI4_M | - | I/O | down |
| 1AE1 | SAI4_SDI_M2/VP1_SYNC_OUT/PCIE0_CLKREQN_M3/SATA0_ACTLED_M1/I2C6_SCL_M3/SPI4_MISO_ | - | I/O | down |
| AJ1 | SAI4_SCLK_M2/VP2_SYNC_OUT/I2C6_SDA_M3/SPI4_CLK_M0/CAN1_RX_M1/PWM2_CH3_M1/GPIO4_C | - | I/O | down |
| 2N3 | VCCIO6_VCC | 1.8V/3.3V | PI | - |

### VCCIO7 (3p, 2 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 1AD2 | UFS_RSTN/GPIO4_D0_d | - | I/O | down |
| AK4 | UFS_REFCLK/GPIO4_D1_d | - | I/O | down |
| 2M3 | VCCIO7_VCC | 1.2V/1.8V | PI | - |

### OSC_UFS (3p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AL5 | OSC_UFS_XOUT | - | AO | - |
| AK5 | OSC_UFS_XIN | - | AI | - |
| 2M2 | OSC_UFS_AVDD | 1.2V/1.8V | API | - |

### USB3_OTG0/DP_TX (14p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2T2 | DP_TX_AUXP | - | AI/O | - |
| 2T3 | DP_TX_AUXN | - | AI/O | - |
| AK10 | USB3_OTG0_SSRX1P/DP_TX_D0P | - | AI/O | - |
| AL10 | USB3_OTG0_SSRX1N/DP_TX_D0N | - | AI/O | - |
| AL11 | USB3_OTG0_SSTX1P/DP_TX_D1P | - | AO | - |
| AK11 | USB3_OTG0_SSTX1N/DP_TX_D1N | - | AO | - |
| AK12 | USB3_OTG0_SSRX2P/DP_TX_D2P | - | AI/O | - |
| AL12 | USB3_OTG0_SSRX2N/DP_TX_D2N | - | AI/O | - |
| AL13 | USB3_OTG0_SSTX2P/DP_TX_D3P | - | AO | - |
| AK13 | USB3_OTG0_SSTX2N/DP_TX_D3N | - | AO | - |
| 2T7 | USB3_OTG0_REXT/DP_TX_REXT | - | A | - |
| 2M5 | USB3_OTG0_DP_TX_AVDD0V85 | 0.85V | API | - |
| 2N5 | USB3_OTG0_DP_TX_DVDD0V85 | 0.85V | PI | - |
| 2N4 | USB3_OTG0_DP_TX_AVDD1V8 | 1.8V | API | - |

### USB2_OTG0 (5p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AK9 | USB2_OTG0_DP | - | AI/O | - |
| AL9 | USB2_OTG0_DM | - | AI/O | - |
| 2R6 | USB2_OTG0_ID | - | I | - |
| 2P3 | USB2_OTG0_VBUSDET | - | I | - |
| 2R3 | USB2_OTG0_REXT | - | A | - |

### USB2_OTG1 (5p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2T4 | USB2_OTG1_DP | - | AI/O | - |
| 2T5 | USB2_OTG1_DM | - | AI/O | - |
| 2T9 | USB2_OTG1_ID | - | I | - |
| 2T10 | USB2_OTG1_VBUSDET | - | I | - |
| 2U8 | USB2_OTG1_REXT | - | A | - |

### USB2_OTG_DVDD0V75 (1p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2P5 | USB2_OTG_DVDD0V75 | 0.75V | PI | - |

### USB2_OTG_AVDD1V8 (1p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2P4 | USB2_OTG_AVDD1V8 | 1.8V | API | - |

### USB2_OTG_AVDD3V3 (1p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2P7 | USB2_OTG_AVDD3V3 | 3.3V | API | - |

### PCIE0/SATA0 (8p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 1N22 | PCIE0_REFCLKP | - | AI/O | - |
| 1N23 | PCIE0_REFCLKN | - | AI/O | - |
| P29 | PCIE0_TXP/SATA0_TXP | - | AO | - |
| P28 | PCIE0_TXN/SATA0_TXN | - | AO | - |
| R28 | PCIE0_RXP/SATA0_RXP | - | AI | - |
| R29 | PCIE0_RXN/SATA0_RXN | - | AI | - |
| 2F11 | PCIE0_SATA0_AVDD0V85 | 0.85V | API | - |
| 2F12 | PCIE0_SATA0_AVDD1V8 | 1.8V | API | - |

### PCIE1/SATA1/USB3_OTG1 (8p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 1L23 | PCIE1_REFCLKP | - | AI/O | - |
| 1M23 | PCIE1_REFCLKN | - | AI/O | - |
| N28 | PCIE1_TXP/SATA1_TXP/USB3_OTG1_SSTXP | - | AO | - |
| N29 | PCIE1_TXN/SATA1_TXN/USB3_OTG1_SSTXN | - | AO | - |
| M28 | PCIE1_RXP/SATA1_RXP/USB3_OTG1_SSRXP | - | AI | - |
| M29 | PCIE1_RXN/SATA1_RXN/USB3_OTG1_SSRXN | - | AI | - |
| 2E11 | PCIE1_SATA1_USB3_OTG1_AVDD0V85 | 0.85V | API | - |
| 2E12 | PCIE1_SATA1_USB3_OTG1_AVDD1V8 | 1.8V | API | - |

### MIPI_DCPHY (24p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AK15 | MIPI_DPHY_DSI_TX_D0N/MIPI_CPHY_DSI_TX_TRIO0_A | - | AO | - |
| AL15 | MIPI_DPHY_DSI_TX_D0P/MIPI_CPHY_DSI_TX_TRIO0_B | - | AO | - |
| AK16 | MIPI_DPHY_DSI_TX_D1N/MIPI_CPHY_DSI_TX_TRIO0_C | - | AO | - |
| AL16 | MIPI_DPHY_DSI_TX_D1P/MIPI_CPHY_DSI_TX_TRIO1_A | - | AO | - |
| AK17 | MIPI_DPHY_DSI_TX_CLKN/MIPI_CPHY_DSI_TX_TRIO1_B | - | AO | - |
| AL17 | MIPI_DPHY_DSI_TX_CLKP/MIPI_CPHY_DSI_TX_TRIO1_C | - | AO | - |
| AK18 | MIPI_DPHY_DSI_TX_D2N/MIPI_CPHY_DSI_TX_TRIO2_A | - | AO | - |
| AL18 | MIPI_DPHY_DSI_TX_D2P/MIPI_CPHY_DSI_TX_TRIO2_B | - | AO | - |
| AK19 | MIPI_DPHY_DSI_TX_D3N/MIPI_CPHY_DSI_TX_TRIO2_C | - | AO | - |
| AL19 | MIPI_DPHY_DSI_TX_D3P/NO_USE | - | AO | - |
| AL20 | MIPI_DPHY_CSI0_RX_D0N/MIPI_CPHY_CSI_RX_TRIO0_A | - | AI | - |
| AK20 | MIPI_DPHY_CSI0_RX_D0P/MIPI_CPHY_CSI_RX_TRIO0_B | - | AI | - |
| AL21 | MIPI_DPHY_CSI0_RX_D1N/MIPI_CPHY_CSI_RX_TRIO0_C | - | AI | - |
| AK21 | MIPI_DPHY_CSI0_RX_D1P/MIPI_CPHY_CSI_RX_TRIO1_A | - | AI | - |
| AL22 | MIPI_DPHY_CSI0_RX_CLKN/MIPI_CPHY_CSI_RX_TRIO1_B | - | AI | - |
| AK22 | MIPI_DPHY_CSI0_RX_CLKP/MIPI_CPHY_CSI_RX_TRIO1_C | - | AI | - |
| AL23 | MIPI_DPHY_CSI0_RX_D2N/MIPI_CPHY_CSI_RX_TRIO2_A | - | AI | - |
| AK23 | MIPI_DPHY_CSI0_RX_D2P/MIPI_CPHY_CSI_RX_TRIO2_B | - | AI | - |
| AL24 | MIPI_DPHY_CSI0_RX_D3N/MIPI_CPHY_CSI_RX_TRIO2_C | - | AI | - |
| AK24 | MIPI_DPHY_CSI0_RX_D3P/NO_USE | - | AI | - |
| 2N7 | MIPI_DCPHY_VREG | - | A | - |
| 2M7 | MIPI_DCPHY_AVDD | 0.75V/0.85V | API | - |
| 2M8 | MIPI_DCPHY_AVDD1V2 | 1.2V | API | - |
| 2P8 | MIPI_DCPHY_AVDD1V8 | 1.8V | API | - |

### MIPI_DPHY_CSI1/
MIPI_DPHY_CSI2 (14p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AE28 | MIPI_DPHY_CSI1_RX_D0N | - | AI | - |
| AE29 | MIPI_DPHY_CSI1_RX_D0P | - | AI | - |
| AF28 | MIPI_DPHY_CSI1_RX_D1N | - | AI | - |
| AF29 | MIPI_DPHY_CSI1_RX_D1P | - | AI | - |
| 1AC23 | MIPI_DPHY_CSI1_RX_CLKN | - | AI | - |
| 1AC22 | MIPI_DPHY_CSI1_RX_CLKP | - | AI | - |
| AG28 | MIPI_DPHY_CSI1_RX_D2N/MIPI_DPHY_CSI2_RX_D0N | - | AI | - |
| AG29 | MIPI_DPHY_CSI1_RX_D2P/MIPI_DPHY_CSI2_RX_D0P | - | AI | - |
| AH28 | MIPI_DPHY_CSI1_RX_D3N/MIPI_DPHY_CSI2_RX_D1N | - | AI | - |
| AH29 | MIPI_DPHY_CSI1_RX_D3P/MIPI_DPHY_CSI2_RX_D1P | - | AI | - |
| 1AD22 | MIPI_DPHY_CSI2_RX_CLKN | - | AI | - |
| 1AD21 | MIPI_DPHY_CSI2_RX_CLKP | - | AI | - |
| 2L11 | MIPI_DPHY_CSI1/2_RX_AVDD0V75 | 0.75V | API | - |
| 1W20 | MIPI_DPHY_CSI1/2_RX_AVDD1V8 | 1.8V | API | - |

### MIPI_DPHY_CSI3/
MIPI_DPHY_CSI4 (14p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| H29 | MIPI_DPHY_CSI3_RX_D0N | - | AI | - |
| H28 | MIPI_DPHY_CSI3_RX_D0P | - | AI | - |
| J29 | MIPI_DPHY_CSI3_RX_D1N | - | AI | - |
| J28 | MIPI_DPHY_CSI3_RX_D1P | - | AI | - |
| 1H23 | MIPI_DPHY_CSI3_RX_CLKN | - | AI | - |
| 1H22 | MIPI_DPHY_CSI3_RX_CLKP | - | AI | - |
| K29 | MIPI_DPHY_CSI3_RX_D2N/MIPI_DPHY_CSI4_RX_D0N | - | AI | - |
| K28 | MIPI_DPHY_CSI3_RX_D2P/MIPI_DPHY_CSI4_RX_D0P | - | AI | - |
| L29 | MIPI_DPHY_CSI3_RX_D3N/MIPI_DPHY_CSI4_RX_D1N | - | AI | - |
| L28 | MIPI_DPHY_CSI3_RX_D3P/MIPI_DPHY_CSI4_RX_D1P | - | AI | - |
| 1K23 | MIPI_DPHY_CSI4_RX_CLKN | - | AI | - |
| 1K22 | MIPI_DPHY_CSI4_RX_CLKP | - | AI | - |
| 2D11 | MIPI_DPHY_CSI3/4_RX_AVDD0V75 | 0.75V | API | - |
| 2D12 | MIPI_DPHY_CSI3/4_RX_AVDD1V8 | 1.8V | API | - |

### HDMI_TX/EDP_TX (15p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2T12 | HDMI_TX_SBDP/EDP_TX_AUXP | - | AI/O | - |
| 2U12 | HDMI_TX_SBDN/EDP_TX_AUXN | - | AI/O | - |
| 1AE24 | HDMI_TX_D0P/EDP_TX_D0P | - | AO | - |
| AK27 | HDMI_TX_D0N/EDP_TX_D0N | - | AO | - |
| AK28 | HDMI_TX_D1P/EDP_TX_D1P | - | AO | - |
| AL28 | HDMI_TX_D1N/EDP_TX_D1N | - | AO | - |
| AJ28 | HDMI_TX_D2P/EDP_TX_D2P | - | AO | - |
| AK29 | HDMI_TX_D2N/EDP_TX_D2N | - | AO | - |
| AL26 | HDMI_TX_D3P/EDP_TX_D3P | - | AO | - |
| AK26 | HDMI_TX_D3N/EDP_TX_D3N | - | AO | - |
| 1AA20 | HDMI_TX_REXT/EDP_TX_REXT | - | A | - |
| 2N11 | HDMI_TX_EDP_TX_AVDDD0V75 | 0.75V | API | - |
| 2P11 | HDMI_TX_EDP_TX_AVDDC0V75 | 0.75V | API | - |
| 2N10 | HDMI_TX_EDP_TX_AVDDIO1V8 | 1.8V | API | - |
| 2P10 | HDMI_TX_EDP_TX_AVDDCMN1V8 | 1.8V | API | - |

### SARADC (9p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| A25 | SARADC_IN0_BOOT | - | AI | - |
| 1A22 | SARADC_IN1 | - | AI | - |
| 1B19 | SARADC_IN2 | - | AI | - |
| 1C19 | SARADC_IN3 | - | AI | - |
| 1E18 | SARADC_IN4 | - | AI | - |
| 1D19 | SARADC_IN5 | - | AI | - |
| 1D21 | SARADC_IN6 | - | AI | - |
| 1E19 | SARADC_IN7 | - | AI | - |
| 2A10 | SARADC_AVDD1V8 | 1.8V | API | - |

### TSADC_TEST (1p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2F10 | TSADC_TEST_OUT_TS | - | - | - |

### OTP_DVDD0V75 (1p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2H11 | OTP_DVDD0V75 | 0.75V | PI | - |

### CPU_BIG_DVDD (8p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2G5 | CPU_BIG_DVDD_0 | TBD | PI | - |
| 2G6 | CPU_BIG_DVDD_1 | - | PI | - |
| 2H6 | CPU_BIG_DVDD_2 | - | PI | - |
| 2H7 | CPU_BIG_DVDD_3 | - | PI | - |
| 2J6 | CPU_BIG_DVDD_4 | - | PI | - |
| 2J7 | CPU_BIG_DVDD_5 | - | PI | - |
| 2K6 | CPU_BIG_DVDD_6 | - | PI | - |
| 2K7 | CPU_BIG_DVDD_7 | - | PI | - |

### CPU_LIT_DVDD (5p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2H4 | CPU_LIT_DVDD_0 | TBD | PI | - |
| 2J3 | CPU_LIT_DVDD_1 | - | PI | - |
| 2J4 | CPU_LIT_DVDD_2 | - | PI | - |
| 2K3 | CPU_LIT_DVDD_3 | - | PI | - |
| 2K4 | CPU_LIT_DVDD_4 | - | PI | - |

### LOGIC_DVDD (7p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2E7 | LOGIC_DVDD_0 | TBD | PI | - |
| 2F8 | LOGIC_DVDD_1 | - | PI | - |
| 2F9 | LOGIC_DVDD_2 | - | PI | - |
| 2G8 | LOGIC_DVDD_3 | - | PI | - |
| 2G9 | LOGIC_DVDD_4 | - | PI | - |
| 2H8 | LOGIC_DVDD_5 | - | PI | - |
| 2H9 | LOGIC_DVDD_6 | - | PI | - |

### LOGIC_MEM_DVDD (2p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2F7 | LOGIC_MEM_DVDD_0 | TBD | PI | - |
| 2J9 | LOGIC_MEM_DVDD_1 | - | PI | - |

### GPU_DVDD (5p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2C4 | GPU_DVDD_0 | TBD | PI | - |
| 2C5 | GPU_DVDD_1 | - | PI | - |
| 2D4 | GPU_DVDD_2 | - | PI | - |
| 2D5 | GPU_DVDD_3 | - | PI | - |
| 2E4 | GPU_DVDD_4 | - | PI | - |

### NPU_DVDD (5p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| 2C7 | NPU_DVDD_0 | TBD | PI | - |
| 2C8 | NPU_DVDD_1 | - | PI | - |
| 2C9 | NPU_DVDD_2 | - | PI | - |
| 2D7 | NPU_DVDD_3 | - | PI | - |
| 2D8 | NPU_DVDD_4 | - | PI | - |

### VSS (163p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| A1 | VSS_0 | - | G | - |
| A4 | VSS_1 | - | G | - |
| A29 | VSS_2 | - | G | - |
| B5 | VSS_3 | - | G | - |
| C1 | VSS_4 | - | G | - |
| V28 | VSS_5 | - | G | - |
| AL1 | VSS_6 | - | G | - |
| 1A2 | VSS_7 | - | G | - |
| 1A3 | VSS_8 | - | G | - |
| 1B2 | VSS_9 | - | G | - |
| 1C2 | VSS_10 | - | G | - |
| 1C4 | VSS_11 | - | G | - |
| 1C9 | VSS_12 | - | G | - |
| 1C13 | VSS_13 | - | G | - |
| 1C16 | VSS_14 | - | G | - |
| 1C21 | VSS_15 | - | G | - |
| 1D1 | VSS_16 | - | G | - |
| 1D3 | VSS_17 | - | G | - |
| 1D5 | VSS_18 | - | G | - |
| 1E2 | VSS_19 | - | G | - |
| 1E3 | VSS_20 | - | G | - |
| 1E5 | VSS_21 | - | G | - |
| 1E6 | VSS_22 | - | G | - |
| 1E10 | VSS_23 | - | G | - |
| 1E13 | VSS_24 | - | G | - |
| 1E16 | VSS_25 | - | G | - |
| 1E23 | VSS_26 | - | G | - |
| 1E24 | VSS_27 | - | G | - |
| 1F3 | VSS_28 | - | G | - |
| 1F5 | VSS_29 | - | G | - |
| 1F6 | VSS_30 | - | G | - |
| 1F20 | VSS_31 | - | G | - |
| 1F21 | VSS_32 | - | G | - |
| 1F24 | VSS_33 | - | G | - |
| 1G3 | VSS_34 | - | G | - |
| 1G6 | VSS_35 | - | G | - |
| 1G20 | VSS_36 | - | G | - |
| 1G21 | VSS_37 | - | G | - |
| 1G22 | VSS_38 | - | G | - |
| 1G24 | VSS_39 | - | G | - |
| 1H1 | VSS_40 | - | G | - |
| 1H2 | VSS_41 | - | G | - |
| 1H3 | VSS_42 | - | G | - |
| 1H4 | VSS_43 | - | G | - |
| 1H6 | VSS_44 | - | G | - |
| 1H20 | VSS_45 | - | G | - |
| 1J2 | VSS_46 | - | G | - |
| 1J4 | VSS_47 | - | G | - |
| 1K3 | VSS_48 | - | G | - |
| 1K6 | VSS_49 | - | G | - |
| 1L2 | VSS_50 | - | G | - |
| 1L3 | VSS_51 | - | G | - |
| 1L4 | VSS_52 | - | G | - |
| 1L5 | VSS_53 | - | G | - |
| 1L6 | VSS_54 | - | G | - |
| 1M1 | VSS_55 | - | G | - |
| 1M2 | VSS_56 | - | G | - |
| 1M4 | VSS_57 | - | G | - |
| 1M6 | VSS_58 | - | G | - |
| 1N2 | VSS_59 | - | G | - |
| 1N4 | VSS_60 | - | G | - |
| 1N6 | VSS_61 | - | G | - |
| 1P2 | VSS_62 | - | G | - |
| 1P3 | VSS_63 | - | G | - |
| 1P4 | VSS_64 | - | G | - |
| 1P6 | VSS_65 | - | G | - |
| 1P20 | VSS_66 | - | G | - |
| 1P21 | VSS_67 | - | G | - |
| 1P22 | VSS_68 | - | G | - |
| 1P24 | VSS_69 | - | G | - |
| 1R1 | VSS_70 | - | G | - |
| 1R2 | VSS_71 | - | G | - |
| 1T3 | VSS_72 | - | G | - |
| 1T5 | VSS_73 | - | G | - |
| 1T6 | VSS_74 | - | G | - |
| 1T20 | VSS_75 | - | G | - |
| 1U2 | VSS_76 | - | G | - |
| 1U3 | VSS_77 | - | G | - |
| 1U4 | VSS_78 | - | G | - |
| 1U6 | VSS_79 | - | G | - |
| 1V2 | VSS_80 | - | G | - |
| 1V6 | VSS_81 | - | G | - |
| 1W1 | VSS_82 | - | G | - |
| 1W3 | VSS_83 | - | G | - |
| 1W5 | VSS_84 | - | G | - |
| 1W6 | VSS_85 | - | G | - |
| 1Y2 | VSS_86 | - | G | - |
| 1Y3 | VSS_87 | - | G | - |
| 1Y4 | VSS_88 | - | G | - |
| 1Y5 | VSS_89 | - | G | - |
| 1Y6 | VSS_90 | - | G | - |
| 1AA2 | VSS_91 | - | G | - |
| 1AA4 | VSS_92 | - | G | - |
| 1AA21 | VSS_93 | - | G | - |
| 1AA24 | VSS_94 | - | G | - |
| 1AB2 | VSS_95 | - | G | - |
| 1AB5 | VSS_96 | - | G | - |
| 1AB6 | VSS_97 | - | G | - |
| 1AC1 | VSS_98 | - | G | - |
| 1AC2 | VSS_99 | - | G | - |
| 1AC3 | VSS_100 | - | G | - |
| 1AC4 | VSS_101 | - | G | - |
| 1AC5 | VSS_102 | - | G | - |
| 1AD3 | VSS_103 | - | G | - |
| 1AE3 | VSS_104 | - | G | - |
| 2A1 | VSS_105 | - | G | - |
| 2A3 | VSS_106 | - | G | - |
| 2A6 | VSS_107 | - | G | - |
| 2A9 | VSS_108 | - | G | - |
| 2A11 | VSS_109 | - | G | - |
| 2A12 | VSS_110 | - | G | - |
| 2B1 | VSS_111 | - | G | - |
| 2B3 | VSS_112 | - | G | - |
| 2B4 | VSS_113 | - | G | - |
| 2B5 | VSS_114 | - | G | - |
| 2B6 | VSS_115 | - | G | - |
| 2B7 | VSS_116 | - | G | - |
| 2B8 | VSS_117 | - | G | - |
| 2B9 | VSS_118 | - | G | - |
| 2B11 | VSS_119 | - | G | - |
| 2B12 | VSS_120 | - | G | - |
| 2C1 | VSS_121 | - | G | - |
| 2C6 | VSS_122 | - | G | - |
| 2C10 | VSS_123 | - | G | - |
| 2C11 | VSS_124 | - | G | - |
| 2C12 | VSS_125 | - | G | - |
| 2D3 | VSS_126 | - | G | - |
| 2D6 | VSS_127 | - | G | - |
| 2D9 | VSS_128 | - | G | - |
| 2E3 | VSS_129 | - | G | - |
| 2E5 | VSS_130 | - | G | - |
| 2E6 | VSS_131 | - | G | - |
| 2E8 | VSS_132 | - | G | - |
| 2E9 | VSS_133 | - | G | - |
| 2F4 | VSS_134 | - | G | - |
| 2F5 | VSS_135 | - | G | - |
| 2F6 | VSS_136 | - | G | - |
| 2G4 | VSS_137 | - | G | - |
| 2G7 | VSS_138 | - | G | - |
| 2G10 | VSS_139 | - | G | - |
| 2H3 | VSS_140 | - | G | - |
| 2H5 | VSS_141 | - | G | - |
| 2J1 | VSS_142 | - | G | - |
| 2J5 | VSS_143 | - | G | - |
| 2J8 | VSS_144 | - | G | - |
| 2J11 | VSS_145 | - | G | - |
| 2J12 | VSS_146 | - | G | - |
| 2K1 | VSS_147 | - | G | - |
| 2K2 | VSS_148 | - | G | - |
| 2K5 | VSS_149 | - | G | - |
| 2K8 | VSS_150 | - | G | - |
| 2K9 | VSS_151 | - | G | - |
| 2K10 | VSS_152 | - | G | - |
| 2K12 | VSS_153 | - | G | - |
| 2L1 | VSS_154 | - | G | - |
| 2L3 | VSS_155 | - | G | - |
| 2L4 | VSS_156 | - | G | - |
| 2L5 | VSS_157 | - | G | - |
| 2L6 | VSS_158 | - | G | - |
| 2L7 | VSS_159 | - | G | - |
| 2L8 | VSS_160 | - | G | - |
| 2L9 | VSS_161 | - | G | - |
| 2L12 | VSS_162 | - | G | - |

### AVSS (102p, 0 GPIO)

| Pin# | Name | V | Type | Pull |
|------|------|---|---|------|
| AJ29 | AVSS_0 | - | AG | - |
| AK6 | AVSS_1 | - | AG | - |
| AK14 | AVSS_2 | - | AG | - |
| AK25 | AVSS_3 | - | AG | - |
| AL4 | AVSS_4 | - | AG | - |
| AL8 | AVSS_5 | - | AG | - |
| AL14 | AVSS_6 | - | AG | - |
| AL25 | AVSS_7 | - | AG | - |
| AL29 | AVSS_8 | - | AG | - |
| 1Y20 | AVSS_9 | - | AG | - |
| 1AB20 | AVSS_10 | - | AG | - |
| 1AB21 | AVSS_11 | - | AG | - |
| 1AB22 | AVSS_12 | - | AG | - |
| 1AB23 | AVSS_13 | - | AG | - |
| 1AB24 | AVSS_14 | - | AG | - |
| 1AC20 | AVSS_15 | - | AG | - |
| 1AC21 | AVSS_16 | - | AG | - |
| 1AC24 | AVSS_17 | - | AG | - |
| 1AD20 | AVSS_18 | - | AG | - |
| 1AD23 | AVSS_19 | - | AG | - |
| 1AD24 | AVSS_20 | - | AG | - |
| 1AE4 | AVSS_21 | - | AG | - |
| 1AE6 | AVSS_22 | - | AG | - |
| 1AE20 | AVSS_23 | - | AG | - |
| 1AE21 | AVSS_24 | - | AG | - |
| 1AE23 | AVSS_25 | - | AG | - |
| 2M1 | AVSS_26 | - | AG | - |
| 2M4 | AVSS_27 | - | AG | - |
| 2M6 | AVSS_28 | - | AG | - |
| 2M9 | AVSS_29 | - | AG | - |
| 2M10 | AVSS_30 | - | AG | - |
| 2M11 | AVSS_31 | - | AG | - |
| 2M12 | AVSS_32 | - | AG | - |
| 2N1 | AVSS_33 | - | AG | - |
| 2N6 | AVSS_34 | - | AG | - |
| 2N8 | AVSS_35 | - | AG | - |
| 2N9 | AVSS_36 | - | AG | - |
| 2N12 | AVSS_37 | - | AG | - |
| 2P1 | AVSS_38 | - | AG | - |
| 2P6 | AVSS_39 | - | AG | - |
| 2P9 | AVSS_40 | - | AG | - |
| 2P12 | AVSS_41 | - | AG | - |
| 2R1 | AVSS_42 | - | AG | - |
| 2R4 | AVSS_43 | - | AG | - |
| 2R5 | AVSS_44 | - | AG | - |
| 2R7 | AVSS_45 | - | AG | - |
| 2R8 | AVSS_46 | - | AG | - |
| 2R9 | AVSS_47 | - | AG | - |
| 2R10 | AVSS_48 | - | AG | - |
| 2R11 | AVSS_49 | - | AG | - |
| 2R12 | AVSS_50 | - | AG | - |
| 2T1 | AVSS_51 | - | AG | - |
| 2T6 | AVSS_52 | - | AG | - |
| 2T8 | AVSS_53 | - | AG | - |
| 2T11 | AVSS_54 | - | AG | - |
| 2U1 | AVSS_55 | - | AG | - |
| 2U2 | AVSS_56 | - | AG | - |
| 2U3 | AVSS_57 | - | AG | - |
| 2U4 | AVSS_58 | - | AG | - |
| 2U5 | AVSS_59 | - | AG | - |
| 2U6 | AVSS_60 | - | AG | - |
| 2U7 | AVSS_61 | - | AG | - |
| 2U9 | AVSS_62 | - | AG | - |
| 2U10 | AVSS_63 | - | AG | - |
| 2U11 | AVSS_64 | - | AG | - |
| 2V1 | AVSS_65 | - | AG | - |
| 2V2 | AVSS_66 | - | AG | - |
| 2V3 | AVSS_67 | - | AG | - |
| 2V4 | AVSS_68 | - | AG | - |
| 2V5 | AVSS_69 | - | AG | - |
| 2V6 | AVSS_70 | - | AG | - |
| 2V7 | AVSS_71 | - | AG | - |
| 2V8 | AVSS_72 | - | AG | - |
| 2V9 | AVSS_73 | - | AG | - |
| 2V10 | AVSS_74 | - | AG | - |
| 2V11 | AVSS_75 | - | AG | - |
| 2V12 | AVSS_76 | - | AG | - |
| G29 | AVSS1_0 | - | AG | - |
| T28 | AVSS1_1 | - | AG | - |
| T29 | AVSS1_2 | - | AG | - |
| 1H21 | AVSS1_3 | - | AG | - |
| 1H24 | AVSS1_4 | - | AG | - |
| 1J21 | AVSS1_5 | - | AG | - |
| 1J22 | AVSS1_6 | - | AG | - |
| 1J23 | AVSS1_7 | - | AG | - |
| 1J24 | AVSS1_8 | - | AG | - |
| 1K20 | AVSS1_9 | - | AG | - |
| 1K21 | AVSS1_10 | - | AG | - |
| 1K24 | AVSS1_11 | - | AG | - |
| 1L20 | AVSS1_12 | - | AG | - |
| 1L21 | AVSS1_13 | - | AG | - |
| 1L22 | AVSS1_14 | - | AG | - |
| 1L24 | AVSS1_15 | - | AG | - |
| 1M20 | AVSS1_16 | - | AG | - |
| 1M21 | AVSS1_17 | - | AG | - |
| 1M22 | AVSS1_18 | - | AG | - |
| 1M24 | AVSS1_19 | - | AG | - |
| 1N20 | AVSS1_20 | - | AG | - |
| 1N21 | AVSS1_21 | - | AG | - |
| 1N24 | AVSS1_22 | - | AG | - |
| 2D10 | AVSS1_23 | - | AG | - |
| 2E10 | AVSS1_24 | - | AG | - |

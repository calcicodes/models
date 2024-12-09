# Box model of trace elements

## Parameters

- $z$ height of calcifying fluid, in m
- $\rho$ density of seawater, in kg/m³
- $T$ temperature, in °C
- $S$ salinity, in PSU
- $K$ seawater exchange rate, in 1/s
- $R$ calcification rate, in mol/m²/s
- $F_{H}$ Alkalinity pumping, in mol H⁺/m²/s
- $p_{H-Ca}$ Ca/TA ratio of alkalinity pumping, in mol Ca²⁺/mol H⁺
- $F_{Ca}$ Ca pumping, in mol Ca²⁺/m²/s
- $F_{HCO3}$ HCO3 pumping, in mol HCO3⁻/m²/s
- $D_{CO2}$ CO2 diffusion rate, in m²/s
- $x$ thickness of the tissue, in m
- $k_{rate}$, $n_{rate}$ precipitation rate constants, in mol/m²/s and dimensionless

## Equations - Calcifying Fluid

$$
\frac{d[Ca]_{cf}}{dt} = K (Ca_{sw} - [Ca]_{cf}) + \frac{F_{Ca}}{z \rho} + \frac{p_{TA-Ca} F_{TA}}{z \rho} - \frac{R}{z \rho} 
$$

$$
\frac{dDIC_{cf}}{dt} = K (DIC_{sw} - DIC_{cf}) + \frac{F_{HCO3}}{z \rho} + D_{CO2} \frac{([CO_2]_{sw} - [CO2]_{cf})}{x z} - \frac{R}{z \rho}
$$

$$
\frac{dTA_{cf}}{dt} = K (TA_{sw} - TA_{cf}) + \frac{F_{H}}{z \rho} + \frac{F_{HCO3}}{z \rho} - \frac{2R}{z \rho}
$$


## Equations - macropinocytosis

Initial composition = calcifying fluid composition

$$
\frac{d[Ca]_v}{dt} = - \frac{R}{v \rho}
$$

$$
\frac{dDIC_v}{dt} = D_{CO2} ([CO_2]_{cell} - [CO2]_{v}) + \frac{F^v_{HCO3}}{z \rho} - \frac{R}{v \rho}
$$

$$
\frac{dTA_v}{dt} = \frac{F^v_{H}}{z \rho} + \frac{F^v_{HCO3}}{z \rho} - \frac{2R}{v \rho}
$$

## Precipitation Rate

$$
R = k_{rate} (\Omega - 1)^{n _{rate}}
$$

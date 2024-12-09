def calc_D_TE(R):
    return 1e-3 - 10 * R

def biomin_box(t, state, z, rho, K, F_H, F_Ca, F_HCO3, D_CO2, x_CO2, p_H_Ca, k_rate, n_rate, Ca_sw, DIC_sw, TA_sw, TE_sw, CO2_sw): 
    Ca, DIC, TA, TE = state

    cs = cb.Csys(TA=TA*1e6, DIC=DIC*1e6)  # could swap this out for a more efficient version
    CO3 = cs.CO3[0] * 1e-6
    CO2 = cs.CO2[0] * 1e-6
        
    Omega = CO3 * Ca / KspA
    
    R = max(0, k_rate * (Omega - 1)**n_rate)
    
    dCa = K * (Ca_sw - Ca) + (F_Ca + p_H_Ca * F_H - R) / z / rho # - pinocytosis?
    dDIC = K * (DIC_sw - DIC) + (F_HCO3 - R) / z / rho + D_CO2 * (CO2_sw - CO2) / 100e-6 / z # - pinocytosis?
    dTA = K * (TA_sw - TA) + (F_H + F_HCO3 - 2 * R) / z / rho # - pinocytosis?
    
    # for each trace element...
    D_TE = calc_D_TE(R)
    dTE = K * (TE_sw - TE) - R * D_TE * (TE / Ca) / z / rho   # - pinocytosis?
    # + other processes for TE?
    
    return [dCa, dDIC, dTA, dTE]


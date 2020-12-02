"""
Trans-Membrane Transport 'mixing' model (Mewes et al, 2015, http://dx.doi.org/10.5194/bg-12-2153-2015) 
"""
import numpy as np

def TMT(Rsw, frac, x):
    """
    'Mixing Model' of foram geochemistry from Mewes et al (2015).
    http://dx.doi.org/10.5194/bg-12-2153-2015

    Parameters
    ----------
    Rsw : array-like
        The ratio of the trace element to Ca (TE/Ca) in seawater.
    frac : float
        Parameter describing the specificity of pumping, where:
        R_TMT = Rsw * frac and R_PT = Rsw
    x : float
        The fraction of cations that are transported by passive transport (PT)

    Returns
    -------
    TE/Ca of foram calcite.
    """
    return Rsw * ((frac * (1 - x) + x + frac * Rsw) /
                  (1 + (1 - x + frac * x) * Rsw))
"""
Rayleigh Fractionation Model (Elderfield et al, 1996)
"""

def Rayleigh_KD(f, alpha):
    """
    Calculate partitioning of trace element (TE) as a function of Rayleigh fractionation.

    Parameters
    ----------
    f : array-like
        Fraction of Ca remaining in the biomineralisation reservoir.
    alpha : array-like
        Partition coefficient for extraction of TE from the reservoir.
    
    Returns
    -------
    KD : array-like
        Partitioning of TE into mineral.
    """
    return (1 - f**alpha) / (1 - f)
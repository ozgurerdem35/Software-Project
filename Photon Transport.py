# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:45:54 2026

@author: Erdem
"""

import numpy as np
from numpy import log as ln

def total_interaction_coef(mu_a,mu_s):
    """
    This function calculates total interaction coefficient
    
    Parameters: 
        mu_a : Absorption coefficient
        mu_s : Scattering coefficient
        
    Return : 
        mu_t : Total interaction coefficient
    """
    
    mu_t = mu_a + mu_s
    return mu_t


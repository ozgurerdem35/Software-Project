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

def step_size(mu_t):
    """
      This function determines the distance that photons will 
      travel in the environment before its next interaction.
      
      Parameters: 
          mu_t : Total interaction coefficient
          
      Return:
          s : step size 
    """
    xi = 1 - np.random.random()
    s = - (np.ln(xi) / mu_t)
    
    return s 
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:45:54 2026

@author: Erdem
"""

import numpy as np

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
    s = - (np.log(xi) / mu_t)
    
    return s 

def photon_absorption(W,mu_a,mu_t):
    """
    This function calculates the amount of energy deposited in the medium 
    and the remaining weight of the photon
        
    Parameters:
        mu_a: absorption coefficient of the medium.
        mu_t: total interaction coefficient (mu_a + mu_s) of the medium.
        W: current statistical weight of the photon packet
            
    Returns:
        The deposited energy (delta_W) and the updated weight (new_W) of the 
        photon
    """
    
    
    delta_W = W * (mu_a / mu_t)
    new_W = W - delta_W
    
    return delta_W, new_W
    

def calculate_scatter_angles(g):
    """
    This function calculates the polar angle cosine and the azimuthal angle
    for photon scattering using the Henyey-Greenstein phase function
        
    Parameters:
        g: anisotropy factor of the medium
            
    Returns:
        The cosine of the polar angle and the azimuthal angle
    """
    
    xi_1 = np.random.random()
    
    if g == 0.0:
        cos_theta = 2.0 * xi_1 - 1.0
    else:
        temp = (1.0 - g**2) / (1.0 - g + 2.0 * g * xi_1)
        cos_theta = (1.0 / (2.0 * g)) * (1.0 + g**2 - temp**2)
        
    xi_2 = np.random.random()
    phi = 2.0 * np.pi * xi_2
    
    return cos_theta, phi


def update_directions(u_x, u_y, u_z, cos_theta, phi):
    
    """
    This function updates the direction cosines of the photon after scattering 
        
    Parameters:
        u_x: current direction cosine in the x-axis
        u_y: current direction cosine in the y-axis
        u_z: current direction cosine in the z-axis
        cos_theta: cosine of the polar scattering angle
        phi: azimuthal scattering angle
            
    Returns:
        The updated direction cosines of the photon
    """
    
    sin_theta = np.sqrt(max(0.0, 1.0 - cos_theta**2))
    
    if u_z > 0.99999 :
        
        new_u_x = sin_theta * np.cos(phi)
        new_u_y = sin_theta * np.sin(phi)
        new_u_z = cos_theta
        
    elif u_z < -0.99999 : 
        
        new_u_x = sin_theta * np.cos(phi)
        new_u_y = -sin_theta * np.sin(phi)
        new_u_z = -cos_theta 
        
    else:
        temp = np.sqrt(1.0 - u_z**2)
        
        new_u_x = sin_theta/temp * (u_x * u_z * np.cos(phi) 
                - u_y * np.sin(phi)) + u_x * cos_theta
        
        new_u_y = sin_theta/temp * (u_z * u_y * np.cos(phi) 
                + u_x * np.sin(phi)) + u_y * cos_theta
        
        new_u_z = - temp * sin_theta * np.cos(phi) + u_z * cos_theta
        
    return new_u_x , new_u_y , new_u_z

def photon_movement(x, y, z, u_x, u_y, u_z, s):
    
    """
    This function calculates the new spatial coordinates of the photon 
    after taking a step
        
    Parameters:
        x: current spatial coordinate in the x-axis
        y: current spatial coordinate in the y-axis
        z: current spatial coordinate in the z-axis
        u_x: current direction cosine in the x-axis
        u_y: current direction cosine in the y-axis
        u_z: current direction cosine in the z-axis
        s: calculated step size for the photon's movement
            
    Returns:
        The updated spatial coordinates of the photon
    """
    
    new_x = x + u_x * s
    new_y = y + u_y * s
    new_z = z + u_z * s
    
    return new_x , new_y , new_z

def photon_termination(W, m, threshold):
    
    if W <= threshold:
        survival_probability = 1.0 / m
        
        if np.random.random() < survival_probability:
            return W * m, True
        
        else:
            return 0.0, False
            
    return W, True

def normalize_direction(u_x, u_y, u_z):
    """
    This function renormalizes the direction cosines to unit length
 
    Parameters:
        u_x, u_y, u_z : direction cosines of the photon
 
    Returns:
        The normalized direction cosines
    """
    norm = np.sqrt(u_x**2 + u_y**2 + u_z**2)

    return u_x / norm, u_y / norm, u_z / norm


def calculate_specular_reflectance(n1, n2):
    """
    This function calculates the specular reflectance for a photon beam entering
    Medium 2 from Medium 1 at normal incidence

    Parameters:
        n1: refractive index of Medium 1
        n2: refractive index of Medium 2

    Returns:
        The specular reflectance fraction
    """
    return np.abs(((n1 - n2) / (n1 + n2))**2)
    

def calculate_fresnel_reflectance(u_z, n1, n2):
    """
    This function calculates the Fresnel reflection probability for a photon hitting 
    the boundary between Medium 2 and Medium 1 from inside Medium 2.

    Parameters:
        u_z: current direction cosine in the z-axis
        n1: refractive index of Medium 1
        n2: refractive index of Medium 2

    Returns:
        The Fresnel reflectance probability
    """
    cos_theta_i = abs(u_z)

    if cos_theta_i > 0.99999:
        return ((n2 - n1) / (n1 + n2))**2

    sin_theta_i = np.sqrt(max(0.0, 1.0 - cos_theta_i**2))
    sin_theta_t = (n2 / n1) * sin_theta_i

    if sin_theta_t >= 1.0:
        return 1.0

    cos_theta_t = np.sqrt(max(0.0, 1.0 - sin_theta_t**2))

    r_s = (n2*cos_theta_i - n1*cos_theta_t) / (n2*cos_theta_i + n1*cos_theta_t)
    
    r_p = (n1*cos_theta_i - n2*cos_theta_t) / (n1*cos_theta_i + n2*cos_theta_t)

    return 0.5 * (r_s**2 + r_p**2)



        
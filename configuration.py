# -*- coding: utf-8 -*-

# --- Photon energies -----------------
ENERGIES_EV = [1.16, 1.49]

N_PHOTONS = 24000          # photon packets launched per run
SEED = 42                  # random seed
ROULETTE_M = 10
ROULETTE_THRESHOLD = 1e-4

TABLE_ENERGY_EV = [1.16, 1.27, 1.32, 1.46, 1.49] # eV [1]

N1 = 1.0                  # refractive index outside (medium 1, air) [2]

# --- Optical properties of inside (medium 2, native liver tissue) ----------

TABLE_MU_A =    [0.018, 0.064, 0.057, 0.071, 0.073]   # 1/cm [1]
TABLE_MU_S = [4.34, 4.72, 4.89, 5.39, 5.5]   # 1/cm [1]
TABLE_G = [0.93, 0.93, 0.93, 0.93, 0.93] # [1]
TABLE_N = [1.3658839, 1.3670865, 1.3677217, 1.3694429, 1.3698909] # [3]


GRID_X_HALF_WIDTH = 1.2   # cm, x from -value to +value
GRID_Z_DEPTH = 1.6        # cm, z from 0 to value
GRID_BINS_X = 240
GRID_BINS_Z = 160

OUTPUT_DIR = "output"


"""
[1] Ritz, Joerg‐P., et al. "Optical properties of native and coagulated porcine 
liver tissue between 400 and 2400 nm." Lasers in Surgery and Medicine: 
    The Official Journal of the American Society for Laser Medicine and 
    Surgery 29.3 (2001): 205-212.

[2] Ciddor, Philip E. "Refractive index of air: new equations for the visible 
and near infrared." Applied optics 35.9 (1996): 1566-1573.

[3] Giannios, Panagiotis, et al. "Visible to near-infrared refractive 
properties of freshly-excised human-liver tissues: marking hepatic 
malignancies." Scientific reports 6.1 (2016): 27910. 
"""

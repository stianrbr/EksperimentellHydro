import numpy as np


sampling_freq = 200
g = 9.80665
rho = 1000  # kg/m^3
nu = 0.000001 # m/s**2

path = "Group5\\"
results = "Results\\"
calibration_results = results+"Calibration\\"
towing_results = results+"Towing\\"
comparison = results+"Comparison\\"

show_plots = False

"""
Model dimensions
"""

# Model scale

L_wl_m = 2.377  # m
B_m = 0.387  # m
T_m = 0.126  # m
Trim_m = 0  # deg
S_m = 1.107  # m^2
Vol_m = 0.076  # m^3
C_b_m = 0.656  # -

# Full scale

L_wl_f = 178.3  # m
B_f = 29.0  # m
T_f = 9.45  # m
Trim_f = 0  # deg
S_f = 6227.8  # m^2
Vol_f = 32049.8  # m^3
C_b_f = 0.656  # -

planned_speeds_repeated = np.array([0.6, 0.7, 0.8, 0.9, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4])
planned_speeds = np.array([0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4])  #  m/s
planned_speeds_refined = np.linspace(0.5, 1.5, 100)


given_froude = np.array([0.172, 0.185, 0.197, 0.209, 0.221, 0.234, 0.246, 0.258, 0.271, 0.283, 0.295, 0.308])

given_holtrop = np.array([0.000115, 0.000186, 0.000283, 0.000407, 0.000564, 0.000745, 0.000937,
                          0.001169, 0.00149, 0.001886, 0.002261, 0.002515])

given_hollenbach = np.array([0.000829, 0.000873, 0.000938, 0.001025, 0.001133, 0.001262, 0.001413, 0.001585,
                             0.001845, 0.002169, 0.002551, 0.002999])
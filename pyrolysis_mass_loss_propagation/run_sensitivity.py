import model_mass_loss

import numpy as np
import pybitup
import matplotlib.pyplot as plt

# Sensitivity analysis with kernel method
input_file_name = "input_SA.json"
case_name = "mass_loss"
case_name = "one_reaction_pyrolysis"

post_dist = pybitup.sensitivity_analysis.SensitivityAnalysis(input_file_name, case_name)

pybitup.post_process.post_process_data(input_file_name)


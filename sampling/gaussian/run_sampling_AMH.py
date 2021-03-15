import pybitup
import json
from jsmin import jsmin
import numpy as np 

#input_file_name = "sampling_gaussian.json"
input_file_name = "sampling_multivariate_gaussian_AMH.json"

post_dist = pybitup.solve_problem.Sampling(input_file_name)
post_dist.sample()
post_dist.__del__()

pybitup.post_process.post_process_data(input_file_name)



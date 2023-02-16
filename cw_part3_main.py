from parametric_simulation2 import run_two_parameter_parametric
from energy_plus_two_parameters import EnergyPlusParameter
# from post_processor import plot_1D_results
# csv module makes it easy to process delimited text files
import csv


def get_indoor_temp_mean(filename):
    # Open the file and create a csv reader
    f = open(filename, 'r')
    reader = csv.reader(f)

    # indoor air temperature list with this parameter
    inside_temp = []
    # Reader automatically iterates through the lines in the file
    for i, line in enumerate(reader):
        if i > 0:
            inside_temp.append(float(line[8]))

    mean_temp = 0.0 if len(inside_temp) == 0 else sum(inside_temp) / len(inside_temp)
    return mean_temp


eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'

parameter_key_of_window_u = ['WindowMaterial:SimpleGlazingSystem',
                 'SimpleWindow:DOUBLE PANE WINDOW',
                 'solar_heat_gain_coefficient']

parameter_vals_of_window_u = [i / 100 for i in range(25, 75, 5)]


parameter_key_of_window_SHGC = ['WindowMaterial:SimpleGlazingSystem',
                 'SimpleWindow:DOUBLE PANE WINDOW',
                 'u_factor']

parameter_vals_of_window_SHGC = [i / 100 for i in range(100, 250, 10)]

energy_plus_parameter = EnergyPlusParameter()

# set window_u_parameter and return result
set_window_u_parameter_result = energy_plus_parameter.set_window_u_key_and_values(
    parameter_key_of_window_u, parameter_vals_of_window_u, val_range=(0.25, 0.75))

# set window_SHGC_parameter and return result
set_window_SHGC_parameter_result = energy_plus_parameter.set_window_SHGC_key_and_values(
    parameter_key_of_window_SHGC, parameter_vals_of_window_SHGC, val_range=(1.0, 2.5))

if set_window_SHGC_parameter_result and set_window_SHGC_parameter_result:
    output_dir = 'param_window'
    window_u_key_vals = energy_plus_parameter.get_window_u_key_and_values()
    window_SHGC_key_vals = energy_plus_parameter.get_window_SHGC_key_and_values()

    # run simulation for two parameters
    output_paths, all_vals = run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                                window_u_key_vals[0], window_u_key_vals[1],
                                                window_SHGC_key_vals[0], window_SHGC_key_vals[1])

    print("output_paths:", output_paths)
    max_indoor_mean_temp = 0.0
    for val_as_key, val_truple in zip(output_paths.keys(), all_vals):
        this_mean = get_indoor_temp_mean('./' + output_paths[val_as_key])
        if this_mean > max_indoor_mean_temp:
            max_indoor_mean_temp = this_mean
            max_val = val_truple

    print('The parameter values that leads to the highest indoor air temperature of window U:',
          max_val[0], ', window SHGC:', max_val[1])



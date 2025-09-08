import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlsxwriter

from amplification.layer import Layer
from amplification.open_file import open_file_selection
from amplification.simulator import SimYoon
from amplification.stack import Stack


if __name__ == '__main__':

    def find_data_file(filename):
        if getattr(sys, "frozen", False):
            # The application is frozen
            datadir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            datadir = os.path.dirname(__file__)
        return os.path.join(datadir, filename)


    # excel_filepath = open_file_selection()
    excel_filepath = "input_MODEL.xlsx"
    df = pd.read_excel(find_data_file(excel_filepath))

    excitation_col = df["Excitation wavelength [nm]"]
    excitation = excitation_col[0]
    raman_shift_col = df["Raman shift [cm-1]"]
    raman_shift = raman_shift_col[0]
    simu_mode_col = df["Simulation mode"]
    # print(simu_mode_col)
    simu_mode = simu_mode_col[0]

    layer_col = df["Layer"]
    mat_col = df["Mat. Name"]
    label_col = df["Label"]
    LOI_col = df["Layer of Interest"]
    VAR_col = df["Variable Layer"]
    Thick_col = df["Thickness [nm]"]

    index_int = [i for i in range(len(LOI_col)) if LOI_col[i] == True][0]
    index_var = [i for i in range(len(VAR_col)) if VAR_col[i] == True][0]

    thickness_stack = [0] * len(layer_col)

    for i in range(len(layer_col)):
        thickness = Thick_col[i]
        thickness_stack[i] = thickness
    # print(type(thickness_stack[0]))

    N = 100
    thickness_var = np.linspace(start=0, stop=Thick_col[index_var], num=N)
    thickness_stack[index_var] = thickness_var

    raman_stack = Stack()

    for i in range(len(thickness_stack)):
        mat = mat_col[i]
        label = label_col[i]
        thickness = thickness_stack[i]
        layer = Layer(mat, label, thickness)
        raman_stack.append(layer)

    # creation of layer of interest
    layer_interest = raman_stack[index_int]
    ylabel = layer_interest.label

    # creation of variable layer
    layer_var = raman_stack[index_var]
    xlabel = layer_var.label

    # simulator creation
    sim = SimYoon(raman_stack, layer_interest,
                  layer_var)  # Yoon et al. model

    if simu_mode == 'amplification_LOI':
        intensity = sim.amplification_layer_of_interest(wavelength=excitation,
                                       shift=raman_shift)
    elif simu_mode == 'amplification_OTHER':
        intensity = sim.amplification_other_layer(wavelength=excitation,
                                         shift=raman_shift)

    # Write data to new xlsx file
    workbook = xlsxwriter.Workbook('output_MODEL.xlsx')
    worksheet = workbook.add_worksheet('enhancement_results')
    thickness_var_list = thickness_var.tolist()
    intensity_list = intensity.tolist()

    worksheet.write('A1', str(xlabel) + ' thickness [nm]')
    worksheet.write('B1', str(xlabel) + ' intensity [a.u.]')
    worksheet.write_column(1, 0, thickness_var_list)
    worksheet.write_column(1, 1, intensity_list)

    chart = workbook.add_chart({'type': 'scatter'})
    chart.add_series({'name': '=enhancement_results!$B$1',
                      'categories': '=enhancement_results!$A$2:$A$' + str(N),
                      'values': '=enhancement_results!$B$2:$B$' + str(N)})
    chart.set_title({'name': str(xlabel) + '-dependent Raman signal'})
    chart.set_x_axis({'name': str(xlabel) + ' thickness [nm]'})
    chart.set_y_axis({'name': str(ylabel) + ' intensity [a.u.]'})
    chart.set_style(2)
    chart.set_legend({'delete_series': [0]})

    worksheet.insert_chart('E6', chart)

    workbook.close()

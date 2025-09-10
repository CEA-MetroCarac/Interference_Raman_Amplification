"""
Impact of the variation of a layer's thickness on the Raman amplification of
the layer of interest.
"""
import matplotlib.pyplot as plt
import numpy as np

from raman_ampli.layer import Layer
from raman_ampli.stack import Stack
from raman_ampli.simulator import SimYoon


def otherlayer_amplification(make_plots=True):
    # layers definition
    d_0 = 0
    d_1 = 0.34
    d_11 = 10
    d_2 = np.linspace(start=0, stop=300, num=100)

    excitation = 532
    raman_shift = 1586

    # stack creation / graphene
    sup = Layer('INFO_Air', 'Sup')
    layer_0 = Layer('INFO_SiO2', 'Surf. Oxide', d_0)
    layer_1 = Layer('INFO_Graphene', 'Graphene', d_1)
    layer_11 = Layer('INFO_Si', 'SOI', d_11)
    layer_2 = Layer('INFO_SiO2', 'BOX', d_2)
    sub = Layer('INFO_Si', 'Sub')

    # stack creation (including air = superstrate)
    raman_stack = Stack()
    raman_stack.append(sup)
    # raman_stack.append(layer_0)
    raman_stack.append(layer_1)
    # raman_stack.append(layer_11)
    raman_stack.append(layer_2)
    raman_stack.append(sub)

    # creation of layer of interest
    layer_interest = raman_stack[1]

    # creation of variable layer
    layer_var = raman_stack[2]
    xlabel = layer_var.label

    # simulator creation
    sim = SimYoon(raman_stack, layer_interest,
                  layer_var)  # Yoon et al. model

    intensity = sim.amplification_other_layer(wavelength=excitation,
                                              shift=raman_shift)
    if make_plots:
        plt.figure('Thickness study')
        plt.title(str(xlabel) + '-dependent Raman signal')
        plt.plot(d_2, intensity)
        plt.xlabel(str(xlabel) + ' thickness [nm]')
        plt.ylabel('Raman intensity [a.u.]')
        plt.show()
    else:
        return d_2, intensity


if __name__ == '__main__':
    otherlayer_amplification(make_plots=True)

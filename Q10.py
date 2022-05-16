import networkx as nx
import numpy as np
from seirsplus.models import *
from seirsplus.networks import *

# Network Definition
network_size = 5500000
scaling = 0.001
g = nx.erdos_renyi_graph(int(network_size * scaling), 0.001)

sigma_values = np.linspace(1052767/5500000, 0.1915, 1)   # 0.11 / np.linspace(0.07, 0.08, 2)   rate of progression
gamma_values = np.linspace(46/5500, 0.0084, 1)    # 0.1 / np.linspace(0.11, 0.12, 2)   rate of recovery
r0_values = np.linspace(2.5, 4, 3)        # 3.6 / 3.6, 3.7, 2      basic rate reproduction

iteration = 0
for SIGMA in sigma_values:
    for GAMMA in gamma_values:
        for R0 in r0_values:
            iteration += 1
            print("Iteration {}/{}".format(iteration, len(sigma_values) * len(gamma_values) * len(r0_values)))

            BETA   = 1/(1/GAMMA) * R0
            model = SEIRSNetworkModel(G       = g,
                                      beta    = BETA,
                                      sigma   = SIGMA,
                                      gamma   = GAMMA,
                                      initI   = network_size * 0.00015) #0.000005
            # Simulation
            model.run(T=120) #120

            # Visualization
            model.figure_infections(plot_percentages=False, plot_E=False, title=f"Sigma: {round(SIGMA, 3)}, Gamma: {round(GAMMA, 5)}, R0: {R0}")
            #model.figure_basic(plot_percentages=False, plot_E=False, plot_S=False, title=f"Sigma: {round(SIGMA, 3)}, Gamma: {round(GAMMA, 5)}, R0: {R0}")
import networkx as nx
import numpy as np
from seirsplus.models import *
from seirsplus.networks import *

# Network Definition
network_size = 5500000
scaling = 0.001
g = nx.erdos_renyi_graph(int(network_size * scaling), 0.001)

sigma_values = np.linspace(0.15, 0.25, 3)   # 0.15
gamma_values = np.linspace(0.08, 0.1, 3)    # 0.09
r0_values = np.linspace(1.75, 1.85, 3)        # 1.85

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
                                      initI   = network_size * 0.000005)
            # Simulation
            model.run(T=120)

            # Visualization
            model.figure_infections(plot_percentages=False, plot_E=False, title=f"Sigma: {round(SIGMA, 2)}, Gamma: {round(GAMMA, 2)}, R0: {R0}")

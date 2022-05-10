import networkx as nx
from seirsplus.models import *
from seirsplus.networks import *

# Network Definition
network_size = 5500000
scaling = 0.001
g = nx.erdos_renyi_graph(int(network_size * scaling), 0.001)

# Initial model parameter values
SIGMA  = 1/5.2
GAMMA  = 1/10
R0     = 2.5
BETA   = 1/(1/GAMMA) * R0
model = SEIRSNetworkModel(G       = g,
                          beta    = BETA,
                          sigma   = SIGMA,
                          gamma   = GAMMA,
                          initI   = network_size*0.000005)

# Simulation
model.run(T=120)

# Visualization
model.figure_infections(plot_percentages=False, plot_E=False, title=f"Sigma: {round(SIGMA, 2)}, Gamma: {GAMMA}, R0: {R0}")

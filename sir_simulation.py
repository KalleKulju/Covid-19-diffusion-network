import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from matplotlib import pyplot as plt

if __name__ == "__main__":

    iterations_amount = 120
    node_amount = 5500
    iterations = []

    # Create graph with "node_amount" amount of nodes
    g = nx.fast_gnp_random_graph(int(node_amount), 0.001)

    # Set SIR model parameters
    model = ep.SIRModel(g)
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.012)
    cfg.add_model_parameter('gamma', 0.06)
    cfg.add_model_parameter("fraction_infected", 0.04)
    model.set_initial_status(cfg)

    # Simulate for "iterations_amount" iterations
    for i in range(int(iterations_amount / 4)):
        iter = model.iteration()
        iterations.append(iter)

    recovered_so_far = iterations[-1]["node_count"][2]
    node_amount -= recovered_so_far
    new_fraction = iterations[-1]["node_count"][1] / node_amount
    g = nx.fast_gnp_random_graph(int(node_amount), 0.001)
    model = ep.SIRModel(g)
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.015)
    cfg.add_model_parameter('gamma', 0.06)
    cfg.add_model_parameter("fraction_infected", new_fraction)
    model.set_initial_status(cfg)

    for i in range(int(iterations_amount / 4)):
        iter = model.iteration()
        iterations.append(iter)
    
    recovered_so_far += iterations[-1]["node_count"][2]
    node_amount -= iterations[-1]["node_count"][2]
    new_fraction = iterations[-1]["node_count"][1] / node_amount
    g = nx.fast_gnp_random_graph(int(node_amount), 0.001)
    model = ep.SIRModel(g)
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.025)
    cfg.add_model_parameter('gamma', 0.06)
    cfg.add_model_parameter("fraction_infected", new_fraction)
    model.set_initial_status(cfg)

    for i in range(int(iterations_amount / 4)):
        iter = model.iteration()
        iterations.append(iter)
    
    recovered_so_far += iterations[-1]["node_count"][2]
    node_amount -= iterations[-1]["node_count"][2]
    new_fraction = iterations[-1]["node_count"][1] / node_amount
    g = nx.fast_gnp_random_graph(int(node_amount), 0.001)
    model = ep.SIRModel(g)
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.3)
    cfg.add_model_parameter('gamma', 0.1)
    cfg.add_model_parameter("fraction_infected", new_fraction)
    model.set_initial_status(cfg)

    for i in range(int(iterations_amount / 4)):
        iter = model.iteration()
        iterations.append(iter)

    # Get number of infected and recovered nodes for each iteration
    infected = []
    for iter in iterations:
        infected.append(iter["node_count"][1])

    recovered = []
    for iter in iterations:
        recovered.append(iter["status_delta"][2])
    
    plt.plot(infected, label="Infected")
    plt.plot(recovered, label="Recovered")
    #plt.plot(recovered, label="Recovered")
    plt.legend()
    plt.show()

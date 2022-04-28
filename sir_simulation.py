import time
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from matplotlib import pyplot as plt

if __name__ == "__main__":

    iterations_amount = 100
    node_amount = 150000

    # Create graph with "node_amount" amount of nodes
    start_time = time.time()
    print("Creating graph with {} nodes...".format(str(node_amount)))
    g = nx.fast_gnp_random_graph(node_amount, 0.001)
    stop_time = time.time() - start_time
    print("Graph creation time: {} seconds.\n".format(str(round(stop_time, 2))))

    # Set SIR model parameters
    model = ep.SIRModel(g)
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.01)
    cfg.add_model_parameter('gamma', 0.04)
    cfg.add_model_parameter("fraction_infected", 0.15)
    model.set_initial_status(cfg)

    # Simulate for "iterations_amount" iterations
    start_time = time.time()
    iterations = model.iteration_bunch(iterations_amount)
    stop_time = time.time() - start_time
    print("Simulating for {} iterations...".format(str(iterations_amount)))
    print("Time for 200 iterations: {} seconds.".format(str(round(stop_time, 2))))

    # Get number of infected and recovered nodes for each iteration
    infected = []
    for iter in iterations:
        infected.append(iter["node_count"][1])

    recovered = []
    for iter in iterations:
        recovered.append(iter["node_count"][2])

    # Plotters gonna plot
    plt.plot(infected)
    plt.plot(recovered)
    plt.show()


import networkx as nx
import ndlib.models.CompositeModel as gc
import ndlib.models.ModelConfig as mc
import ndlib.models.compartments as cpm
#from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
from bokeh.io import output_notebook, show
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
from ndlib.viz.bokeh.MultiPlot import MultiPlot
import numpy as np

# Network Definition
g = nx.erdos_renyi_graph(5500, 0.001)

infection_rates = np.linspace(0.001, 0.01, 3)
death_rates = np.linspace(0.0001, 0.001, 3)

vm = MultiPlot()
iteration = 0
# Change infection rate
for p in infection_rates:
    # Change death rate
    for q in death_rates:
        iteration += 1
        print("Iteration {}/{}".format(iteration, len(infection_rates) * len(death_rates)))

        # Model Selection
        model = gc.CompositeModel(g)

        # Model statuses
        model.add_status('Susceptible')
        model.add_status('Infected')
        model.add_status('Dead')

        # Compartment definition
        c1 = cpm.NodeStochastic(p, triggering_status="Infected")
        c2 = cpm.NodeStochastic(q)

        # Rule definition
        model.add_rule("Susceptible", "Infected", c1)
        model.add_rule("Infected", "Dead", c2)

        # Model initial status configuration
        config = mc.Configuration()
        config.add_model_parameter('fraction_infected', 0.005)
        config.add_model_parameter('p', p)
        config.add_model_parameter('q', q)
        model.set_initial_status(config)

        # Simulation
        iterations = model.iteration_bunch(120)
        trends = model.build_trends(iterations)

        # Create plot
        viz = DiffusionTrend(model, trends)
        pl = viz.plot()
        vm.add_plot(pl)

m = vm.plot()
show(m)

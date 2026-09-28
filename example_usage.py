from client import PushRelabelMaxFlow

solver = PushRelabelMaxFlow(4)
solver.add_edge(0, 1, 15)
solver.add_edge(0, 2, 10)
solver.add_edge(1, 2, 5)
solver.add_edge(1, 3, 10)
solver.add_edge(2, 3, 10)

flow = solver.compute_max_flow(0, 3)
print(f"Push-Relabel Max Flow: {flow}")

"""Push-Relabel Maximum Flow Engine.
100% Python Standard Library.
"""

import collections

class PushRelabelMaxFlow:
    """Goldberg-Tarjan Push-Relabel algorithm with excess flows and height relabeling."""
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.cap = collections.defaultdict(int)
        self.flow = collections.defaultdict(int)
        self.excess = [0] * num_nodes
        self.height = [0] * num_nodes

    def add_edge(self, u, v, capacity):
        self.cap[(u, v)] = capacity

    def compute_max_flow(self, s, t):
        self.height[s] = self.n
        self.excess[s] = float("inf")
        for v in range(self.n):
            if self.cap[(s, v)] > 0:
                c = self.cap[(s, v)]
                self.flow[(s, v)] += c
                self.flow[(v, s)] -= c
                self.excess[v] += c
                self.excess[s] -= c

        queue = collections.deque([v for v in range(self.n) if v != s and v != t and self.excess[v] > 0])

        while queue:
            u = queue.popleft()
            pushed = False
            for v in range(self.n):
                res_cap = self.cap[(u, v)] - self.flow[(u, v)]
                if res_cap > 0 and self.height[u] == self.height[v] + 1:
                    delta = min(self.excess[u], res_cap)
                    self.flow[(u, v)] += delta
                    self.flow[(v, u)] -= delta
                    self.excess[u] -= delta
                    self.excess[v] += delta
                    if v != s and v != t and v not in queue and self.excess[v] > 0:
                        queue.append(v)
                    pushed = True
                    if self.excess[u] == 0:
                        break
            if self.excess[u] > 0:
                min_h = float("inf")
                for v in range(self.n):
                    if self.cap[(u, v)] - self.flow[(u, v)] > 0:
                        min_h = min(min_h, self.height[v])
                if min_h < float("inf"):
                    self.height[u] = min_h + 1
                queue.append(u)

        return self.excess[t]

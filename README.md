# Push-Relabel Max Flow Algorithm Skill

Robust, zero-dependency Python implementation of the **Goldberg-Tarjan Push-Relabel Algorithm** for asymptotic \(O(V^3)\) maximum flow computation.

## Features
- **Preflow-Push Dynamics**: Operates locally by pushing excess flow across downhill residual edges.
- **Height Function Relabeling**: Maintains valid labeling bounds ensuring no augmenting path exists when excess dissipates.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    NodeU["Vertex u with Excess Flow e(u) > 0"] --> CheckHeight{"Height h(u) == h(v) + 1?"}
    CheckHeight -- Yes --> Push["Push delta = min(e(u), c_f(u, v))"]
    CheckHeight -- No --> Relabel["Relabel: h(u) = 1 + min h(v)"]
```

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topo_sort(nodes, edges):
            grid, inp = {k: [] for k in nodes}, Counter({k: 0 for k in nodes})
            [grid[a].append(b) or inp.update({b: 1}) for a, b in edges if a in nodes and b in nodes]

            topo = [k for k, v in inp.items() if v <= 0]
            [inp.update({kid: -1}) or inp[kid] == 0 and topo.append(kid) for node in topo for kid in grid[node]]
            return topo if len(topo) == len(grid) else []

        group = [m + idx if grp == -1 else grp for idx, grp in enumerate(group)]

        edges_grp = set((group[before], grp) for grp, befores in zip(group, beforeItems) for before in befores if group[before] != grp)
        if len(topo1 := topo_sort(set(group), edges_grp)) != len(set(group)):
            return []

        edges_node = set((before, idx) for idx, befores in enumerate(beforeItems) for before in befores)
        if len(topo2 := topo_sort(set(range(n)), edges_node)) != n:
            return []

        a, b = {x: i for i, x in enumerate(topo1)}, {x: i for i, x in enumerate(topo2)}
        return sorted(range(n), key=lambda x: (a[group[x]], b[x]))
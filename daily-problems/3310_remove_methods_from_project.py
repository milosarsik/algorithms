"""
3310. Remove Methods From Project
"""

# Description:
# You have n methods numbered from 0 to n - 1. Each pair [a, b] means method a
# invokes method b. Method k is buggy, so k and everything reachable from k are
# suspicious. The suspicious group can be removed only if no method outside the
# group invokes a method inside the group. If that outside-to-inside dependency
# exists, return every method unchanged.
#
# Intuition:
# Think of the bug as spreading through directed method calls. First, color every
# method reachable from k as suspicious. Then ask one safety question:
# "Does any safe method depend on this suspicious group?"
#
# If yes, removing the suspicious group would break safe code, so remove
# nothing. If no, the suspicious group is isolated and can be removed.
#
# Recognition cue:
# This is a directed graph reachability problem. The phrase "directly or
# indirectly invoked by k" points to DFS/BFS from k. The phrase "no method
# outside the group invokes any methods within it" means you must check boundary
# edges from non-suspicious nodes into suspicious nodes.

# Algorithm in English:
# 1. Treat methods as a directed graph.
#    i. If invocations has [a, b], method a calls method b.
#    ii. That means the directed edge is a -> b.
# 2. Starting from the buggy method k, run DFS and mark every reachable method
#    as suspicious.
# 3. Check every invocation again.
#    i. If a non-suspicious method calls a suspicious method, then the
#       suspicious group cannot be safely removed.
#    ii. In that case, return every method because none should be removed.
# 4. If no outside method calls into the suspicious group, return all methods
#    that were not marked suspicious.


# Time Complexity: O(n + m), where m is len(invocations).
# Space Complexity: O(n + m), for the graph, stack, and suspicious array.
def remaining_methods(n, k, invocations):
    graph = [[] for _ in range(n)]

    for method, invoked_method in invocations:
        graph[method].append(invoked_method)

    suspicious = [False] * n
    stack = [k]
    suspicious[k] = True

    while stack:
        method = stack.pop()

        for invoked_method in graph[method]:
            if not suspicious[invoked_method]:
                suspicious[invoked_method] = True
                stack.append(invoked_method)

    for method, invoked_method in invocations:
        if not suspicious[method] and suspicious[invoked_method]:
            return list(range(n))

    return [method for method in range(n) if not suspicious[method]]


# AlgoMonster-style two-traversal solution:
# 1. Build a directed graph to find everything reachable from k.
# 2. Build an undirected graph to explore the full connected area attached to
#    every non-suspicious method.
# 3. If a non-suspicious component touches suspicious methods, those suspicious
#    methods cannot be removed, so mark them back as not suspicious.
#
# Time Complexity: O(n + m), where m is len(invocations).
# Space Complexity: O(n + m), for both graphs, stacks, and marker arrays.
def remaining_methods_two_graphs(n, k, invocations):
    directed_graph = [[] for _ in range(n)]
    undirected_graph = [[] for _ in range(n)]

    for method, invoked_method in invocations:
        directed_graph[method].append(invoked_method)
        undirected_graph[method].append(invoked_method)
        undirected_graph[invoked_method].append(method)

    suspicious = [False] * n
    stack = [k]
    suspicious[k] = True

    while stack:
        method = stack.pop()

        for invoked_method in directed_graph[method]:
            if not suspicious[invoked_method]:
                suspicious[invoked_method] = True
                stack.append(invoked_method)

    visited = [False] * n

    for method in range(n):
        if suspicious[method] or visited[method]:
            continue

        stack = [method]
        visited[method] = True

        while stack:
            current_method = stack.pop()
            suspicious[current_method] = False

            for connected_method in undirected_graph[current_method]:
                if not visited[connected_method]:
                    visited[connected_method] = True
                    stack.append(connected_method)

    return [method for method in range(n) if not suspicious[method]]


print(remaining_methods(4, 1, [[1, 2], [0, 1], [3, 2]]))  # [0, 1, 2, 3]
print(remaining_methods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))  # [3, 4]
print(remaining_methods(3, 2, [[1, 2], [0, 1], [2, 0]]))  # []

print(remaining_methods_two_graphs(4, 1, [[1, 2], [0, 1], [3, 2]]))  # [0, 1, 2, 3]
print(remaining_methods_two_graphs(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))  # [3, 4]
print(remaining_methods_two_graphs(3, 2, [[1, 2], [0, 1], [2, 0]]))  # []

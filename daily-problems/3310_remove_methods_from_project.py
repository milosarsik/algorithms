"""
3310. Remove Methods From Project
"""

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


print(remaining_methods(4, 1, [[1, 2], [0, 1], [3, 2]]))  # [0, 1, 2, 3]
print(remaining_methods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))  # [3, 4]
print(remaining_methods(3, 2, [[1, 2], [0, 1], [2, 0]]))  # []

input =  [line.rstrip().split(')') for line in open("day6/input.txt").readlines()]

import sys, collections

class Node:
    def __init__(self, code):
        self.code = code
        self.root = True
        self.children = []

def build_orbit_graph(orbit_map):
    orbit_graph = {}
    for left, right in orbit_map:
        if left not in orbit_graph:
            orbit_graph[left] = Node(left)
        if right not in orbit_graph:
            orbit_graph[right] = Node(right)
        orbit_graph[right].root = False
        orbit_graph[left].children.append(orbit_graph[right])
        orbit_graph[right].children.append(orbit_graph[left])
    return orbit_graph

def count_checksums(graph):
    seen = set()
    def _traverse(node, depth=0):
        if node.code in seen:
            return 0
        seen.add(node.code)
        return depth + sum(_traverse(child, depth+1) for child in node.children)
    return sum(_traverse(node) for node in graph.values() if node.root)

def minimum_transfers(graph, source, destination):
    queue = collections.deque([(graph[source], 0)])
    seen = {source: 0}
    while destination not in seen:
        node, depth = queue.pop()
        for child in node.children:
            if child.code not in seen:
                seen[child.code] = depth+1
                queue.appendleft((child, depth+1))
    return seen[destination]-2

orbit_graph = build_orbit_graph(input)
print("Part 1: "+str(count_checksums(orbit_graph)))
print("Part 1: "+str(minimum_transfers(orbit_graph, 'YOU', 'SAN')))
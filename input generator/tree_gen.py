"""
It is mainly for generating tree inputs.
"""

from random import randint

def show(node_count:int, graph:list[tuple]):
  edge_count = len(graph)

  print(node_count, edge_count if edge_count != node_count-1 else '')
  for u, v in graph:
    print(u, v)


def tree_gen(node_count:int,
             min_nodes:int=None,
             edge_count:int=None,
             start_index:int=1) -> tuple[int, list]:
  """Returns tree size, and tree structure."""
  if not min_nodes: min_nodes = node_count
  tree_size: int = randint(min_nodes, node_count)
  if not edge_count: edge_count = tree_size - 1

  tree: list = []
  existence: set[frozenset] = set()

  i: int = 0
  while i < edge_count:
    edge: frozenset = frozenset((randint(0, tree_size-1) + start_index, randint(0, tree_size-1) + start_index))
    if len(edge)==1: continue
    if edge in existence: continue

    tree.append(tuple(edge))
    existence.add(edge)
    i += 1
  return tree_size, tree

if __name__ == '__main__':
  # print(tree_gen(5, edge_count=8))
  show(*tree_gen(6, edge_count=4))
"""
gen.py - Competitive Programming Random Generators

Includes:
- Trees, forests, graphs
- Arrays, permutations, strings
- Printing helpers
"""

from random import randint, shuffle, random

Edge = tuple[int, int]
WEdge = tuple[int, int, int]   # (u, v, w)
DEdge = tuple[int, int]        # directed edge


# =========================================================
# OUTPUT HELPERS
# =========================================================

def show(n: int, edges) -> None:
  m = len(edges)

  print(n, "" if m == n - 1 else m)

  for e in edges:
    if len(e) == 2:
      u, v = e
      print(u, v)
    else:
      u, v, w = e
      print(u, v, w)


def show_array(a: list[int]) -> None:
    print(*a)


def show_matrix(mat: list[list[int]]) -> None:
    for row in mat:
        print(*row)


# =========================================================
# BASIC HELPERS
# =========================================================

def coin() -> bool:
    return randint(0, 1) == 1


def random_size(mx: int, mn: int | None = None) -> int:
    if mn is None:
        mn = mx
    return randint(mn, mx)


def random_edge(n: int, start: int = 1) -> Edge:
    u = randint(start, start + n - 1)
    v = randint(start, start + n - 1)
    while u == v:
        v = randint(start, start + n - 1)
    return u, v


def randomize_edges(edges: list[Edge]) -> None:
    for i, (u, v) in enumerate(edges):
        if coin():
            edges[i] = (v, u)
    shuffle(edges)


# =========================================================
# ARRAYS
# =========================================================

def array_gen(mx_n: int, mn_n: int | None = None,
              lo: int = 1, hi: int = 10) -> list[int]:
    n = random_size(mx_n, mn_n)
    return [randint(lo, hi) for _ in range(n)]


def distinct_array(mx_n: int, lo: int = 1, hi: int = 10**9) -> list[int]:
    n = random_size(mx_n)
    return shuffle_and_take(list(range(lo, hi)), n)


def permutation(n: int) -> list[int]:
    p = list(range(1, n + 1))
    shuffle(p)
    return p


def shuffle_and_take(arr: list[int], k: int) -> list[int]:
    shuffle(arr)
    return arr[:k]


# =========================================================
# STRINGS
# =========================================================

def string_gen(mx_n: int, mn_n: int | None = None,
               alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    n = random_size(mx_n, mn_n)
    return "".join(alphabet[randint(0, len(alphabet) - 1)] for _ in range(n))


# =========================================================
# TREES
# =========================================================

def tree_gen(mx_n: int, mn_n: int | None = None,
             start: int = 1) -> tuple[int, list[Edge]]:
    n = random_size(mx_n, mn_n)
    edges: list[Edge] = []

    for v in range(2, n + 1):
        u = randint(1, v - 1)
        edges.append((u + start - 1, v + start - 1))

    randomize_edges(edges)
    return n, edges


def weighted_tree_gen(mx_n: int, mn_n: int | None = None,
                      start: int = 1,
                      lo: int = 1, hi: int = 10) -> tuple[int, list[WEdge]]:
  """
  Random weighted tree
  """

  n = random_size(mx_n, mn_n)
  edges: list[WEdge] = []

  for v in range(2, n + 1):
    u = randint(1, v - 1)
    w = randint(lo, hi)
    edges.append((u + start - 1, v + start - 1, w))

  shuffle(edges)
  return n, edges

# =========================================================
# FORESTS
# =========================================================

def forest_gen(mx_n: int, edge_cnt: int | None = None,
               mn_n: int | None = None,
               start: int = 1) -> tuple[int, list[Edge]]:
    n = random_size(mx_n, mn_n)

    if edge_cnt is None:
        edge_cnt = randint(0, n - 1)

    if not (0 <= edge_cnt <= n - 1):
        raise ValueError("Forest must have <= n-1 edges")

    n, edges = tree_gen(n, n, start)

    shuffle(edges)
    edges = edges[:edge_cnt]

    randomize_edges(edges)
    return n, edges


# =========================================================
# GRAPHS
# =========================================================

def graph_gen(mx_n: int, edge_cnt: int | None = None,
              mn_n: int | None = None,
              start: int = 1) -> tuple[int, list[Edge]]:
    n = random_size(mx_n, mn_n)

    max_edges = n * (n - 1) // 2
    if edge_cnt is None:
        edge_cnt = randint(0, max_edges)

    if not (0 <= edge_cnt <= max_edges):
        raise ValueError("Too many edges")

    used = set()
    edges: list[Edge] = []

    while len(edges) < edge_cnt:
        u, v = random_edge(n, start)
        if u > v:
            u, v = v, u
        if (u, v) in used:
            continue
        used.add((u, v))
        edges.append((u, v))

    shuffle(edges)
    return n, edges


def weighted_graph_gen(mx_n: int, edge_cnt: int | None = None,
                       mn_n: int | None = None,
                       start: int = 1,
                       lo: int = 1, hi: int = 10) -> tuple[int, list[WEdge]]:
  """
  Random weighted undirected graph
  """

  n = random_size(mx_n, mn_n)

  max_edges = n * (n - 1) // 2
  if edge_cnt is None:
    edge_cnt = randint(0, max_edges)

  if not (0 <= edge_cnt <= max_edges):
    raise ValueError("Too many edges")

  used = set()
  edges: list[WEdge] = []

  while len(edges) < edge_cnt:
    u, v = random_edge(n, start)

    if u > v:
      u, v = v, u

    if (u, v) in used:
      continue

    used.add((u, v))
    w = randint(lo, hi)
    edges.append((u, v, w))

  shuffle(edges)
  return n, edges


def digraph_gen(mx_n: int, edge_cnt: int | None = None,
                  mn_n: int | None = None,
                  start: int = 1) -> tuple[int, list[DEdge]]:
    """
    Random directed graph (can have cycles)
    """

    n = random_size(mx_n, mn_n)

    max_edges = n * (n - 1)
    if edge_cnt is None:
      edge_cnt = randint(0, max_edges)

    if not (0 <= edge_cnt <= max_edges):
      raise ValueError("Too many edges")

    edges: list[DEdge] = []
    used = set()

    while len(edges) < edge_cnt:
      u = randint(start, start + n - 1)
      v = randint(start, start + n - 1)

      if u == v:
        continue

      if (u, v) in used:
        continue

      used.add((u, v))
      edges.append((u, v))

    shuffle(edges)
    return n, edges


def dag_gen(mx_n: int, edge_cnt: int | None = None,
            mn_n: int | None = None,
            start: int = 1) -> tuple[int, list[DEdge]]:
  """
  Directed Acyclic Graph
  Edges always go from lower index → higher index
  """

  n = random_size(mx_n, mn_n)

  max_edges = n * (n - 1) // 2
  if edge_cnt is None:
    edge_cnt = randint(0, max_edges)

  if not (0 <= edge_cnt <= max_edges):
    raise ValueError("Too many edges")

  edges: list[DEdge] = []
  used = set()

  while len(edges) < edge_cnt:
    u = randint(1, n)
    v = randint(1, n)

    if u >= v:
      continue

    if (u, v) in used:
      continue

    used.add((u, v))
    edges.append((u + start - 1, v + start - 1))

  shuffle(edges)
  return n, edges


# =========================================================
# SPECIAL GRAPHS
# =========================================================

def path_gen(n: int) -> tuple[int, list[Edge]]:
    edges = [(i, i + 1) for i in range(1, n)]
    randomize_edges(edges)
    return n, edges


def cycle_gen(n: int) -> tuple[int, list[Edge]]:
    edges = [(i, i + 1) for i in range(1, n)]
    edges.append((n, 1))
    randomize_edges(edges)
    return n, edges


def star_gen(n: int) -> tuple[int, list[Edge]]:
    edges = [(1, i) for i in range(2, n + 1)]
    randomize_edges(edges)
    return n, edges


def complete_graph_gen(n: int, m: int | None = None) -> tuple[int, list[Edge]]:
    edges = [(i, j) for i in range(1, n + 1)
             for j in range(i + 1, n + 1)]
    shuffle(edges)

    if m is not None:
        edges = edges[:m]

    return n, edges


# =========================================================
# MAIN TEST
# =========================================================

if __name__ == "__main__":
    # print("TREE")
    # show(*tree_gen(10))
    #
    # print("\nFOREST")
    # show(*forest_gen(6, edge_cnt=3))
    #
    # print("\nGRAPH")
    # show(*graph_gen(6, edge_cnt=8))

    print("\nARRAY")
    print(array_gen(15, 5, 1, 100))

    # print("\nSTRING")
    # print(string_gen(10, alphabet="abc"))
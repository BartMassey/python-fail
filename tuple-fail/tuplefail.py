l1 = [["a"], ["b"]]
s1 = set(tuple(d) for d in l1)
l2 = sorted(s1)
# This assertion will fail, since l1 is a list of sets
# and l2 is a list of tuples.
# assert l1 == l2, f"{l1} {l2}"

l1 = ["a", "b"]
s1 = set(l1)
s2 = frozenset(l1)
# This assertion succeeds, even though
# s1 is a set and s2 is a frozenset.
assert s1 == s2, f"{s1} {s2}"


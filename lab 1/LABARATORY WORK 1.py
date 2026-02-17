# 4 задача
f = lambda s: ' '.join(w.lower() for w in s.split() if sum(c.isupper() for c in w[1:-1]) == 1)
class Option:
    def __init__(self, data) -> None:
        self.data = data

    def get(self):
        return self.data

    def map(self, fn):
        return Option(fn(self.get()))


def G(fn):
    return lambda opt: opt.map(fn)


def f(x):
    return len(x)


# 圏B の対象 Option[str]
B_x = Option("Books")

G_f = G(f)

print(G_f(B_x).get())

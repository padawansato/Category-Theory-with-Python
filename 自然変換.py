# Option クラス
class Option:
    def __init__(self, data):
        self._data = data

    def get(self):
        return self._data

    def map(self, fn):
        return Option(fn(self.get()))

    def tolist(self):
        return [self.get()]


# List[str] → List[int]
def F(fn):
    return lambda xlist: [fn(x) for x in xlist]


# Option[str] → Option[int]
def G(fn):
    return lambda opt: opt.map(fn)


# Option関手から List関手へ変換
def H(option):
    return option.tolist()


# 圏A の射 f
f = lambda x: len(x)


# 合成関数
def compose(fn1, fn2):
    return lambda x: fn2(fn1(x))


B_x = Option('Books')

# H[int]·G(f)
H_G_f = compose(G(f), H)

# F(f)·H[str]
F_f_H = compose(H, F(f))

# 値が一致するか検証
print(H_G_f(B_x)[0])
print(F_f_H(B_x)[0])

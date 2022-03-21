def F(fn):
    def tmp(xlist):
        return [fn(x) for x in xlist]
    return tmp


def compose(fn1, fn2):
    return lambda x: fn2(fn1(x))


def main():
    # 圏 A の射 f
    f = lambda x: len(x)

    # 圏 A の射 g
    g = lambda y: y >= 5

    # 圏 A の List[str]
    B_x = ["Book", "Books"]

    # F(g) · F(f)
    F_g_F_f = compose(F(f), F(g))

    # F(g·f)
    F_g_f = F(compose(f, g))
    # 値を確認
    print(f"F_g_F_f\t=\t{F_g_F_f(B_x)}")
    print(f"F_g_f\t=\t{F_g_f(B_x)}")


if __name__ == "__main__":
    main()

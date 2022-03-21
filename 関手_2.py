def F(fn):
    def tmp(xlist):
        return [fn(x) for x in xlist]
    return tmp


def main():
    # 圏 A の射 f
    # def f(x):
        # return lambda x: len(x)

    f = lambda x: len(x)

    B_x = ["Book", "Books"]

    # F(f) を取得
    F_f = F(f)

    # 関数 F(f) に文字列リストを渡す
    B_y = F_f(B_x)

    # 値を確認
    print(B_y)


if __name__ == "__main__":
    main()

def F(fn):
    def tmp(xlist):
        return [fn(x) for x in xlist]
    return tmp


def main():
    # 圏 A の射 g
    g = lambda y: y >= 5

    # 圏 B の List[int]
    B_y = [4, 5]

    # F(f) を取得
    F_g = F(g)

    # 関数 F(f) に文字列リストを渡す
    B_y = F_g(B_y)

    # 値を確認
    print(B_y)


if __name__ == "__main__":
    main()

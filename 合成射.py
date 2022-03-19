# -*- coding:utf8 -*-
class Arrow:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def log(self):
        return self.x + "-" + self.y

    def compose(self, arrow):
        return Arrow(self.x, arrow.y)


def main():
    # 射 f: "こ" - "ねこ"
    f = Arrow("こ", "ねこ")
    print(f.log())

    # 射 g: "ねこ" - "みけねこ"
    g = Arrow("ねこ", "みけねこ")
    print(g.log())

    # 合成
    gf = f.compose(g)
    print(gf.log())


if __name__ == "__main__":
    main()

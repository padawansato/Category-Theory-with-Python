# -*- coding:utf8 -*-
class Arrow:
    def __init__(self, x, y) -> None:
        if y < x:
            raise Exception('err')

        self.x = x
        self.y = y

    def log(self):
        return f"{self.x}-{self.y}"

    def compose(self, arrow):
        if self.y != arrow.x:
            raise Exception("err")

        return Arrow(self.x, arrow.y)


def main():
    f = Arrow(1, 2)
    print(f.log())
    g = Arrow(2, 5)
    print(g.log())
    h = Arrow(5, 10)
    print(h.log())

    hg = g.compose(h)
    print(hg.log())

    hgf = f.compose(hg)
    print(hgf.log())


if __name__ == "__main__":
    main()

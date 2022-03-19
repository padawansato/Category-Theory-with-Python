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
    id_1 = Arrow(1, 1)
    id_2 = Arrow(2, 2)
    f = Arrow(1, 2)
    print(f.log())

    # f·id_1
    f·id_1 = id_1.compose(f)
    print(f·id_1.log())

    # id_2·f
    id_2·f = f.compose(id_2)
    print(id_2·f.log)


if __name__ == "__main__":
    main()

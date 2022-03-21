from typing import List


def f(x: str):
    return len(x)


def g(x: int):
    return x >= 5


def F(x: List[str]) -> List[int]:
    return list(map(f, x))


def G(x: List[int]):
    return list(map(g, x))


def main():
    x = ["Book", "Books"]
    print(f"F(x)={F(x)}")
    print(f"G(F(x))={G(F(x))}")


if __name__ == "__main__":
    main()

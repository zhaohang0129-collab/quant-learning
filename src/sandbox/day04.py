from day02 import Position
import day03 as d3

if __name__ == "__main__":
    p = Position("600519", 1500.0, 100)
    p.add(1600.0, 100)
    print(p)  # 应该打出 Position(code='600519', cost=1550.0, shares=200)

    """
    # file: a.py
    print("hello from a")
    X = 10
    # file: b.py
    import a
    import a
    import a
    print(a.X)    只会出现一次 因为import只调用一次 多了也是第一次 
    """

    """三种写法的练习 
    import math

    print(math.sqrt(16))
    print(math.pi)
    from math import sqrt, pi

    print(sqrt(16))
    print(pi)
    from math import sqrt as s, pi as p

    print(s(16))
    print(p)
    """

    """
    from day02 import Position

    class Position:
        def __init__(self):
            self.x = 1

    p = Position("600519", 1500.0, 100) 应该会报错 后面定义的p把前面定义的p覆盖了 没办法接受那三个参数
    """
    d3.save_lines("test_codes.txt", ["600519", "000001"])
    print(d3.load_lines("test_codes.txt"))

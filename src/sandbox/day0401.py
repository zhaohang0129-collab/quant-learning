# 待做:用绝对导入,从 quant 包导入 Position
# 写法:from quant.portfolio import Position
from quant.portfolio import Position

if __name__ == "__main__":
    p = Position("600519", 1500.0, 100)
    p.add(1600.0, 100)
    print(p)

    """
    from quant.portfolio import Position      # A

    from portfolio import Position            # B
    A可以运行 因为他是绝对导入 day05和导入的.py不在一个文件夹下
    """

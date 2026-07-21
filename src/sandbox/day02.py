class Position:
    """一笔股票持仓"""

    def __init__(self, code, cost, shares):
        self.code = code
        self.cost = cost
        self.shares = shares

    def market_value(self, price):
        return price * self.shares

    def pnl(self, price):
        return self.shares * (price - self.cost)

    def pnl_pct(self, price):
        if self.cost == 0:
            raise ValueError("Cost cannot be zero for percentage calculation.")
        return (price - self.cost) / self.cost

    def add(self, price, shares):
        total_money = self.cost * self.shares + price * shares
        total_shares = self.shares + shares
        self.cost = total_money / total_shares
        self.shares = total_shares

    def __repr__(self):
        return f"Position(code={self.code!r}, cost={self.cost}, shares={self.shares})"

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return (self.code, self.cost, self.shares) == (other.code, other.cost, other.shares)


class Bar:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f"Bar-{self.n}"  # 只有 __str__，没有 __repr__


if __name__ == "__main__":
    p = Position("600519", 1500.0, 100)
    p.add(1600.0, 100)
    print(p.shares, p.cost)  # 期望 200 1550.0
    p.add(1400.0, 200)
    print(p.shares, p.cost)  # 期望 400 1475.0

    a = Position("600519", 1500.0, 100)
    b = a
    b.add(1600.0, 100)
    print(a.shares)  # 200 理由：b和a是同一个对象 对b add a也改变
    c = Position("600519", 1500.0, 100)
    print(a is c)  # False理由：c是新创建的对象 和a不是同一个对象
    print(a.shares == c.shares)  # False理由：c.shares是100 a.shares是200

    p = Position("600519", 1500.0, 100)
    print(p)
    print([p, p])
    p.add(1600.0, 100)
    print(p)  # cost 应该跟着变成 1550.0

    x = Position("600519", 1500.0, 100)
    y = Position("600519", 1500.0, 100)
    z = Position("000001", 1500.0, 100)
    print(x == y)  # True
    print(x is y)  # False
    print(x == z)  # False
    print(x == "hello")  # False，不是报错

    b = Bar(1)
    print(b)  # ?
    print([b, b])  # ?

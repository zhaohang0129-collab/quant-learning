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

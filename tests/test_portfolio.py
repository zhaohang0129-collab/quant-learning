from quant.portfolio import Position
import pytest

def test_market_value():
    # 待做:100 股、现价 1600,市值应该是 160000.0
    p=Position("600519", 1500, 100)
    assert p.market_value(1600) == 160000.0

def test_pnl_positive():
    # 待做:成本1500、100股、现价1600,pnl 应该是 10000.0
    # (如果你的 Position 有 pnl 方法;没有就测 market_value 的别的数)
    p=Position("600519", 1500, 100)
    assert p.pnl(1600) == 10000.0


def test_add_updates():
    # 待做:1500成本100股,add(1600, 100) 之后,
    # shares 应该 200,cost 应该 1550.0
    # 用两个 assert
    p=Position("600519", 1500, 100)
    p.add(1600, 100)
    assert p.shares == 200
    assert p.cost == 1550.0

def test_zero_cost_raises():
    # 待做:成本为 0 的 Position,调 pnl_pct 应该抛 ValueError
    # 用 with pytest.raises(ValueError):
    p=Position("600519", 0, 100)
    with pytest.raises(ValueError):
        p.pnl_pct(1600)

def check_market_value():          # 这个函数不会被执行 因为他不是test_开头的函数 python -m pytest tests/ -v 这个命令是运行所有test_开头的函数
    p = Position("600519", 1500.0, 100)
    assert p.market_value(1600.0) == 160000.0

assert 1 + 1 == 2        # 通过
assert 1 + 1 == 3        # 报错
assert "abc".upper() == "ABC"    # 通过
assert [1, 2] == [1, 2]  # 通过

import functools


# ---- 装饰器(现成工具,今天不用会写,复制来用即可)----
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [调用前] 即将执行 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  [调用后] {func.__name__} 返回了 {result}")
        return result

    return wrapper


# ---- 第1题:函数是值 ----
def shout():
    return "HELLO"


# ---- 第2题:两个版本,改名共存,证明 @ 就是手动赋值的简写 ----
@my_decorator
def multiply_a(a, b):
    return a * b


def multiply_b(a, b):
    return a * b


multiply_b = my_decorator(multiply_b)


# ---- 第3题:带不带括号 ----
@my_decorator
def foo():
    return 42


# ---- 第4题:lru_cache ----
@functools.lru_cache
def fib(n):
    print(f"  计算 fib({n})")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print("===== 第1题 =====")
    x = shout  # 不带括号
    y = shout()  # 带括号
    print(x)  # 函数本身
    print(y)  # HELLO
    print(x())  # HELLO

    print("\n===== 第2题:@ 版 vs 手动版,输出应完全一样 =====")
    print("multiply_a(3, 4) =", multiply_a(3, 4))
    print("multiply_b(3, 4) =", multiply_b(3, 4))

    print("\n===== 第3题:foo 不带括号 vs 带括号 =====")
    print("--- 写 foo(不调用),应该不打日志 ---")
    foo
    print("--- 写 foo()(调用),应该打日志 ---")
    foo()

    print("\n===== 第4题:fib(5),看每个 n 计算几次 =====")
    print("结果 =", fib(5))
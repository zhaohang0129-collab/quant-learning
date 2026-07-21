def squares_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result


def squares_gen(n):
    for i in range(n):
        yield i * i


def gen():
    print("step A")
    yield 1
    print("step B")
    yield 2


def count_up():
    # 待做:从 0 开始,无限 yield 下一个整数
    # 提示:while True + 一个计数变量
    count = 0
    while True:
        yield count
        count += 1


if __name__ == "__main__":
    print(squares_list(5))  # [0, 1, 4, 9, 16]
    print(squares_gen(5))  # <generator object ...>
    print(list(squares_gen(5)))  # [0, 1, 4, 9, 16]
    for x in squares_gen(5):
        print(x, end=" ")
    g = gen()  # 这行会打印 step A 吗? 不会 得用next/for 惰性不会运行
    print("---")
    first = next(g)  # 打印什么?first 是几? 会出现step A first 是 1
    print("---")

    g = squares_gen(4)
    a = list(g)
    b = list(g)
    print(a)  # ?0 1 4 9
    print(b)  # ?没有了 生成器不会有以前的值了

    total = sum(i * i for i in range(10))  # 待做:sum( 生成器表达式 )
    print(total)  # 应该 285

    g = count_up()
    for _ in range(5):
        print(next(g), end=" ")  # 0 1 2 3 4

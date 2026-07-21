def save_lines(path, lines):

    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def load_lines(path):

    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def append_log(path, msg):
    # 待做：用 "a" 模式，把 msg 追加为新的一行
    with open(path, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


if __name__ == "__main__":
    codes = ["600519", "000001", "300750"]
    save_lines("codes.txt", codes)
    back = load_lines("codes.txt")
    print(back)
    print(back == codes)  # 应该 True

    with open("x.txt", "w", encoding="utf-8") as f:
        f.write("aaa")
    with open("x.txt", "w", encoding="utf-8") as f:
        f.write("bb")
    # x.txt 应该是bb
    print("600519\n".rstrip("\n"))  # 600519
    print("6005190".rstrip("0"))  # 600519
    append_log("log.txt", "trade1")
    append_log("log.txt", "trade2")
    append_log("log.txt", "trade3")
    print(load_lines("log.txt"))  # 应该 ['trade1', 'trade2', 'trade3']

def fibonacci(n):
    if n <= 0:
        return []
    result = [0]
    if n == 1:
        return result
    result.append(1)

    for i in range(2, n):
        result.append(result[-1] + result[-2])
    return result


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

evens = [x for x in nums if x % 2 == 0]
odd_squares = [x**2 for x in nums if x % 2 != 0]
print(evens)
print(odd_squares)


def word_count(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


s = "the quick brown fox jumps over the lazy dog the fox"
print(word_count(s))

nums1 = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums1[::-1])
print(nums1[5:2:-1])


def stats(nums):
    if not nums:
        raise ValueError("stats() requires a non-empty list")
    return max(nums), min(nums), sum(nums) / len(nums)


print(stats([3, 1, 4, 1, 5, 9, 2, 6]))  # (9, 1, 3.875)

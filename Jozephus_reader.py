def counting(n: int, k: int):
    if n == 1:
        return 1
    return (counting(n - 1, k) + k - 1) % n + 1


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(counting(n, k))

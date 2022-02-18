def sum_first(n):

    if n == 0:
        return n

    else:
        return n + sum_first(n - 1)

def main():
    print(sum_first(3))


main()

def prod(n, n2):


    if n2 == 1:
        return n
    
    else:
        return n + (prod(n, n2 - 1))


def main():
    print(prod(8,5))


main()

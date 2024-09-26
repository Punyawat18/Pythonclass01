def main():
    userinput = int(input("num"))
    print(printuser(userinput, 2))
    print(type(printuser(userinput, 2)))
    a = printuser(userinput, 2)
    print(a[0])


def printuser(b, t):
    return b, t

main()
ar
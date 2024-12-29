
def recursion(n: int):
    print(n)
    if n == 1:
        print("done with function")
        return
    recursion(n-1)

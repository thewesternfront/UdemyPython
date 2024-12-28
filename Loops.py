
def loopTests1():
    print('loop tests')

    for x in range(10):
        print(x)

    text = "abcdefg"
    i = 0
    while i < len(text) and text[i] != 'd':
        print(text[i])
        i = i + 1
def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)

if __name__ == "__main__":
    print(fibonacci(int(input())))
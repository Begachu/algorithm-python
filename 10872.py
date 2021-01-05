def factorial(index):
    if index == 0:
        return 1
    else:
        return index * factorial(index-1)
        
if __name__ == "__main__":
    print(factorial(int(input())))

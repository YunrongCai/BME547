def my_function(n):
    # creates an error
    if type(n) is str:
        raise TypeError ("Cannot send a string")
    a = 8
    b = "put"
    if a > b:
        print(a)

def main():
    try:
        my_function("6")
    except TypeError:
        print("All the best")


if __name__ == "__main__":
    main()
def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    number = 0
    while number <= 0 or number >= 100:
        number = int(input('Enter your input: '))

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()

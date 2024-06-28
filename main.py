def main():
    number = int(input('Please input a number in the range: '))
    
    while number<0 or number>100:
        number = int(input('Please enter a valid number: '))

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()

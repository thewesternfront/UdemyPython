
def user_input():
    userinput = input("Enter a number: ")

    try:
        number = float(userinput)
        print(number)
        #number /= 0
    except ValueError:
        print('You entered an invalid value, try again ...')
        user_input()
    except ZeroDivisionError:
        print('Division by Zero not allowed')
        user_input()
    except Exception as e:
        print('Something went wrong', e)
    else:
        print('You were successful')
    finally:
        print('This sill always run')

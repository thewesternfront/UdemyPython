def user_input():
    userinput = input("Enter a number: ")

    try:
        number = float(userinput)
        print(number)
        # number /= 0
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
        print('This sill always runs')

    # manually raise an error
    userinput = input("Enter: ")



def connect_to_internet(is_connected: bool):
    if not is_connected:
        raise Exception("No Internet connection")
    else:
        print("Connected to the Internet")

try:
    connect_to_internet(False)
except Exception as e:
    print(e)
else:
    print("Successful Connection")

def save_history(expression, result):
    with open("history.txt", "a") as file:
        file.write(f"{expression} = {result}\n")


def calculator():

    print("===== Python Calculator =====")
    print("Type 'exit' to close calculator")

    while True:

        try:
            expression = input("\nEnter calculation: ")

            # exit condition
            if expression.lower() == "exit":
                print("Calculator closed")
                break

            # calculate expression
            result = eval(expression)

            print("Answer =", result)

            # save calculation
            save_history(expression, result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

        except SyntaxError:
            print("Error: Invalid expression")

        except ValueError:
            print("Error: Enter valid value")

        except:
            print("Error: Something went wrong")


calculator()
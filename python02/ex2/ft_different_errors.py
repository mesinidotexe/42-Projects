def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("missing.txt")
    elif operation_number == 3:
        "text" + 5
    else:
        return "No error"


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    operations = [0, 1, 2, 3]

    for op in operations:
        try:
            print(f"Testing operation {op}...")
            garden_operations(op)
        except ValueError:
            print("Caught ValueError: invalid value provided")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: cannot divide by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: file does not exist")
        except TypeError:
            print("Caught TypeError: incompatible types used together")
        finally:
            print()

    print("Testing multiple errors together...\n")

    for op in operations:
        try:
            garden_operations(op)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
            print(f"Caught an error in operation {op}, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == '__main__':
    test_error_types()

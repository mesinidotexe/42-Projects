def garden_operations(error):
    match error:
        case 0:
            error == 'abc'
        case 1:
            error / 0
        case 2:
            open("test.txt")
        case 3:
            dict = {"num": 5, "str": 'abc'}
            print(dict["bla"])

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    
    try:
        garden_operations('abc')
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()")
    finally:
        print()
    try:
        garden_operations(45)
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero")
    finally:
        print()
    try:
        garden_operations(open('test.txt'))
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    finally:
        print()
    try:
        garden_operations(dict)
        print("Testing KeyError...")
        print("Caught KeyError: 'missing\_plant'")
    finally:
        print()
    try:
        garden_operations('abc')
        garden_operations(45)
        garden_operations(open('test.txt'))
        garden_operations(dict)
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!")
    finally:
        print()
    print("All error types tested successfully!")

if __name__ == '__main__':
    test_error_types()
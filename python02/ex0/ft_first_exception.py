def check_temperature(temp_str):
    try:
        int(temp_str)
        print(f"Testing Temperature: {temp_str}")
    except ValueError:
        print(f'Error: "{temp_str}" is not a valid number')
    except Exception:
        print('Something went wrong!')


if __name__ == '__main__':
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print('\nAll tests completed - program didnt crash!')

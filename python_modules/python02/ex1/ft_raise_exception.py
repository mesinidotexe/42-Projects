def input_temperature(temp_str):
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    else:
        raise ValueError(f"Temperature {temp} is out of valid range (0-40)")


def test_temperature():
    print("=== Temperature Tests ===\n")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        try:
            temp = input_temperature(value)
            print(f"Valid temperature: {temp}")
        except ValueError as e:
            print(f'Error with "{value}": {e}')

    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()

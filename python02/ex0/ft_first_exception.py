def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    test_values = ["25", "abc"]

    for value in test_values:
        try:
            temp = input_temperature(value)
            print(f"Valid temperature: {temp}")
        except ValueError:
            print(f'Error: "{value}" is not a valid number')

    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()

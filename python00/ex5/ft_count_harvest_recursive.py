def ft_count_harvest_recursive(current_day, total_days=None):
    if total_days == None:
        total_days = int(input("Days until harvest: "))
        current_day = 1
    if current_day > total_days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    ft_count_harvest_recursive(current_day + 1, total_days)
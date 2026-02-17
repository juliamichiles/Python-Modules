def print_days(days):
    if days == 0:
        return
    else:
        print_days(days - 1)
        print('Day', days)


def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))
    print_days(days)
    print('Harvest time!')

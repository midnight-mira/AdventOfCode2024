def is_valid_order(order, rules):
    for first, second in rules:
        if first not in order or second not in order:
            continue

        if order.index(first) > order.index(second):
            return False
        
    return True

def part1():
    orders = []
    rules = []
    result = 0

    with open("input.txt", "r") as file:
        for line in file.readlines():
            if "|" in line:
                rules.append(tuple(map(int, line.split("|"))))
            if "," in line:
                orders.append(list(map(int, line.split(","))))

    orders_list = []
    for order in orders:
        if is_valid_order(order, rules):
            orders_list.append(order)

    for order in orders_list:
        result += order[len(order)//2]
    
    return result


def part2():
    orders = []
    rules = []
    result = 0

    with open("input2.txt", "r") as file:
        for line in file.readlines():
            if "|" in line:
                rules.append(tuple(map(int, line.split("|"))))
            if "," in line:
                orders.append(list(map(int, line.split(","))))

    invalid_orders_list = []
    for order in orders:
        if not is_valid_order(order, rules):
            invalid_orders_list.append(order)

    for invalid_order in invalid_orders_list:
        while not is_valid_order(invalid_order, rules):
            for first, second in rules:
                if first not in invalid_order or second not in invalid_order:
                    continue
                first_index= invalid_order.index(first)
                second_index = invalid_order.index(second)
                if first_index > second_index:
                    invalid_order[first_index] = second
                    invalid_order[second_index] = first

    for order in invalid_orders_list:
        result += order[len(order)//2]
    
    return result


if __name__ == "__main__":
    print("part 1 " + str(part1()))
    print("part 2 " + str(part2()))
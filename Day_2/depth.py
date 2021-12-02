strip_data = open('input.txt').read().splitlines()


def gather_measurements(data):
    x = 0
    y = 0
    for measurement in data:
        (direction, value) = measurement.split()
        value = int(value)

        if direction == "forward":
            x += value
        elif direction == "down":
            y += value
        elif direction == "up":
            y -= value
    output = x * y
    print(f"part 1 output: {output}")


def part_two_measurements(info):
    x = 0
    y = 0
    aim = 0
    for measurement in info:
        (direction, value) = measurement.split()
        value = int(value)

        if direction == "forward":
            x += value
            y += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    output = x * y
    print(f"part 2 output: {output}")


gather_measurements(strip_data)
part_two_measurements(strip_data)

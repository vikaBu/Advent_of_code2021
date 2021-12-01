def submarine():
    with open('input.txt') as f:
        sonar_increase = 0
        scan_results = [int(line.strip()) for line in f]
        for i in range(1, len(scan_results)):
            if scan_results[i] > scan_results[i - 1]:
                sonar_increase += 1
    print("Depth measurement has increased", sonar_increase, "times")


submarine()

# part 2


def sliding_window():
    with open('input.txt') as f:
        input_counter = 0
        measurements = [int(line.strip()) for line in f]
        for one_case in range(3, len(measurements)):
            first_sum = sum(measurements[one_case - 3:one_case])
            second_sum = sum(measurements[one_case - 2:one_case + 1])
            if second_sum > first_sum:
                input_counter += 1
    print(input_counter, "sums are larger than the previous one")


sliding_window()

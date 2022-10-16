import itertools


def input_for_consecutive_check(current_readings):
    value = []
    for i in range(15):
        if i in current_readings:
            value.append(i)
            continue
        value.append(0)
    return value


def get_consecutive_groups(current_counts):
    return [list(y) for x, y in itertools.groupby(current_counts, lambda z: z == 0) if not x]


def current_ranges_and_count(current_readings):
    samples = input_for_consecutive_check(current_readings)
    consecutive_samples = get_consecutive_groups(samples)
    ranges_count = []
    for i in range(len(consecutive_samples)):
        occurrences = 0
        for element in consecutive_samples[i]:
            occurrences += current_readings.count(element)
        between_range = str(min(consecutive_samples[i])) + '-' + str(max(consecutive_samples[i]))
        ranges_count.append((between_range, str(occurrences)))
    string_format = ""
    for item in ranges_count:
        string_format += "{}, {}".format(item[0], item[1])
    return string_format


if __name__ == '__main__':
    current_ranges_and_count([4, 5])

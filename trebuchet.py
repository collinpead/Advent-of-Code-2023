# Part One Solution
def calibrate_sum(file) -> int:
    sum = 0
    for line in file:
        first = None
        # Function for part two solution
        line = edit_line(line, 0, len(line))
        for curr in line:
            if curr.isnumeric() and first is None:
                first = curr
            if curr.isnumeric():
                last = curr
        sum += int(str(first) + str(last))
    return sum

# Part Two Solution
# Iteratively parse through the line, replacing words with numbers at the earliest occurrence
# Preserves the last character, as words are permitted to share their last and first characters
# For example, 'sevenine' should translate as '79' instead of '7ine'
def edit_line(line: str, position: int, length: int) -> str:
    buffer = ""
    new_line = ""

    while position < length:
        buffer += line[position]
        if line[position].isnumeric():
            new_line += line[position]

        if "one" in buffer:
            new_line += "1"
            buffer = "e"
        if "two" in buffer:
            new_line += "2"
            buffer = "o"
        if "three" in buffer:
            new_line += "3"
            buffer = "e"
        if "four" in buffer:
            new_line += "4"
            buffer = "r"
        if "five" in buffer:
            new_line += "5"
            buffer = "e"
        if "six" in buffer:
            new_line += "6"
            buffer = "x"
        if "seven" in buffer:
            new_line += "7"
            buffer = "n"
        if "eight" in buffer:
            new_line += "8"
            buffer = "t"
        if "nine" in buffer:
            new_line += "9"
            buffer = "e"
        position += 1
    
    return new_line


if __name__ == "__main__":
    file = open("day1.txt", "r")
    print(calibrate_sum(file))
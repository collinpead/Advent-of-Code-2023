def find_part_sum(file):

    schematic_2d = []
    is_valid_part = False
    current_num = ""
    sum = 0

    for line in file:
        line_contents = line.strip("\n")

        schematic_2d.append(line_contents)

    #  First index is the line number, second index is the length of each line
    num_lines = len(schematic_2d)
    chars_per_line = len(schematic_2d[0])

    for i in range(num_lines):
        for j in range(chars_per_line):
            if schematic_2d[i][j].isnumeric():
                is_valid_part = is_valid_part or check_adjacent_symbols(schematic_2d, i, j, num_lines, chars_per_line)
                current_num = current_num + str(schematic_2d[i][j])
                # Correct for an edge case where a number is at the end of a line
                # Just in case there another number at the start of the next line, the two will not be concatenated
                if j + 1 == chars_per_line:
                    if (is_valid_part):
                        sum += int(current_num)
                        is_valid_part = False
                    current_num = ""
            elif current_num != "":
                if (is_valid_part):
                    sum += int(current_num)
                    is_valid_part = False
                current_num = ""

    return sum

def check_adjacent_symbols(schematic_2d, line, character, max_lines, max_chars):
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Check if within boundaries
            if (line + i >= 0) and (line + i < max_lines) and (character + j >= 0) and (character + j < max_chars):
                # Check if it is an adjacent special symbol
                if (schematic_2d[line + i][character + j] != '.') and not (schematic_2d[line + i][character + j].isnumeric()):
                    return True
    
    return False


    

if __name__ == "__main__":
    file = open("day3.txt", "r")
    print(find_part_sum(file))
import re

# Part One Solution
def check_valid_games(file) -> int:
    # Total number of reds in the bag
    max_reds = 12
    # Total number of greens in the bag
    max_greens = 13
    # Total number of blues in the bag
    max_blues = 14
    # Sum of IDs of all valid games
    sum = 0
    # Counter to track the number of the current game
    game_counter = 1

    for line in file:
        # Boolean evaluates if the current game is possible
        valid_line = True

        line = re.split(": ", line)[1]
        sets = re.split("; ", line)
        # Split into ";" delimited sets
        for curr_set in sets:
            tokens = re.split(", ", curr_set)
            # Split into individual tokens, consisting of a value and a color
            for curr_token in tokens:
                value = int(re.split(" ", curr_token)[0])
                color = re.split(" ", curr_token)[1]

                if "blue" in color and value > max_blues:
                    valid_line = False
                    break
                if "red" in color and value > max_reds:
                    valid_line = False
                    break
                if "green" in color and value > max_greens:
                    valid_line = False
                    break
        
        if valid_line:
            sum += game_counter
        game_counter += 1
    
    return sum

# Part Two Solution
def check_power_sum(file) -> int:
    # Power sum of IDs
    sum = 0

    for line in file:
        # Least number of reds needed for the game
        fewest_reds = 0
        # Least number of greens needed for the game
        fewest_greens = 0
        # Least number of blues needed for the game
        fewest_blues = 0

        line = re.split(": ", line)[1]
        sets = re.split("; ", line)
        # Split into ";" delimited sets
        for curr_set in sets:
            tokens = re.split(", ", curr_set)
            # Split into individual tokens, consisting of a value and a color
            for curr_token in tokens:
                value = int(re.split(" ", curr_token)[0])
                color = re.split(" ", curr_token)[1]

                if "blue" in color and value > fewest_blues:
                    fewest_blues = value
                if "red" in color and value > fewest_reds:
                    fewest_reds = value
                if "green" in color and value > fewest_greens:
                    fewest_greens = value
        
        sum += fewest_blues * fewest_greens * fewest_reds
    
    return sum

if __name__ == "__main__":
    file = open("day2.txt", "r")
    print(check_valid_games(file))
    file = open("day2.txt", "r")
    print(check_power_sum(file))
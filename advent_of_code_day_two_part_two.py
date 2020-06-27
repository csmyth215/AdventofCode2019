# number_list[1] = noun - options between 0 and 99
# number_list[2] = verb - options between 0 and 99
# [0] = operator
# [3] = value that indicates new position
# output = 19690720
# can I save the initial, unchanged number_list as a separate variable to be called again and not overriden?

with open("advent_of_code_puzzle_file_day_two.txt") as number_sequence:    
    number_string = number_sequence.read()
    split_string = number_string.split(',')
    original_input = [int(i) for i in split_string]

for i in range(0, 100):
    for j in range(0, 100):
        number_list = original_input[:]
        number_list[1] = i
        number_list[2] = j

        x = 0
        while True:
            if number_list[x] == 99:
                break
            
            if number_list[x] == 1:
                output = number_list[number_list[x+1]] + number_list[number_list[x+2]]
            elif number_list[x] == 2:
                output = number_list[number_list[x+1]] * number_list[number_list[x+2]]
            else:
                print("We have a problem")

            number_list[number_list[x+3]] = output
            x += 4

        if number_list[0] == 19690720:
            print(f"Your noun is {i}; your verb is {j}")
            answer = 100 * i + j
            print(answer)
            exit()
            
            

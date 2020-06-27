# [0] = action (1 = addition, 2 = multiplication)
# [1] = position of first input
# [2] = position of second input
# [3] = position of new output (override existing number)
# then move ahead from optcode (action) four spaces

with open("advent_of_code_puzzle_file_day_two.txt") as number_sequence:    
    number_string = number_sequence.read()
    split_string = number_string.split(',')
    number_list = [int(i) for i in split_string]
    
number_list_length = len(number_list)

number_list[1] = 12
number_list[2] = 2

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

print(number_list[0])



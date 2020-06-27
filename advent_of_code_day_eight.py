with open("AdventofCode/advent_of_code_day_eight_textfile.txt") as number_sequence:    
    number_string = number_sequence.read()
    digits = []
    for n in number_string:
        digits.append(int(n))

def group_rows(digits):
    count = [i for i in range(len(digits) // 25 // 6)]
    current_starting_position = 0
    current_ending_position = current_starting_position + 150
    rows = []
    for i in count:
        this_row = digits[current_starting_position:current_ending_position]
        rows.append(this_row)
        current_starting_position += 150
        current_ending_position += 150
    return rows

def count_zeros(digits):
    count_of_zeros = []
    for n in digits:
        this_count_of_zeros = 0
        for i in n:
            if i == 0:
                this_count_of_zeros += 1
        count_of_zeros.append(this_count_of_zeros)
    return count_of_zeros
      
def count_ones_and_twos(digits):
    ones = 0
    twos = 0
    for i in digits:
        if i == 1:
            ones += 1
        elif i ==2:
            twos += 1
    return ones, twos

our_rows = group_rows(digits)
zeros = count_zeros(our_rows)

smallest = 25
for n in zeros:
    if n < smallest:
        smallest = n

fewest_zeros = zeros.index(smallest)
wanted_image = our_rows[fewest_zeros]
ones, twos = count_ones_and_twos(wanted_image)
answer = ones * twos

# 0 black, 1 white, 2 transparent
def set_colour(layers, current_colour):
    this_layer = layers.pop()
    for i in range(len(this_layer)):
        if this_layer[i] == 0:
            current_colour[i] = 'B'
        elif this_layer[i] == 1:
            current_colour[i] = 'W'
        else:
            pass

bottom_layer = our_rows[-1]
result = bottom_layer

while len(our_rows) > 0:
    set_colour(our_rows, result)

def draw_image_line(code):
    line_of_image = " "
    for n in code:
        if n == 'W':
            n_string = " "
            line_of_image += n_string
        elif n == 'B':
            n_string = "#"
            line_of_image += n_string
        else:
            pass
    return line_of_image

first_line = draw_image_line(result[0:25])
second_line = draw_image_line(result[25:50])
third_line = draw_image_line(result[50:75])
fourth_line = draw_image_line(result[75:100])
fifth_line = draw_image_line(result[100:125])
sixth_line = draw_image_line(result[125:150])

print(first_line)
print(second_line)
print(third_line)
print(fourth_line)
print(fifth_line)
print(sixth_line)
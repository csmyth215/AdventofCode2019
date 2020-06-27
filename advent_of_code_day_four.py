# six-digit number
# within range of puzzle input --> 387638-919123
# two adjacent digits the same
# digits only increase

potentially_qualified = []

for integer in range(387638,919123):
    potential = True
    integer_string = str(integer)
    for n in range(5):
        digit = int(integer_string[n])
        next_digit  = int(integer_string[n + 1])
        if next_digit < digit:
            potential = False
            break
    if potential:
        potentially_qualified.append(integer_string)

dedupe_potentially_qualified = set(potentially_qualified)
list_potentially_qualified = list(dedupe_potentially_qualified)

list_of_doubles = []
for number in list_potentially_qualified:
    integer_string_two = str(number)
    for n in range(5):
        digit = int(integer_string_two[n])
        next_digit  = int(integer_string_two[n + 1])
        if next_digit == digit:
           list_of_doubles.append(integer_string_two)
           break
     
qualified = set(list_of_doubles)
print(len(qualified))

def candidature(number):
    candidate_string = str(number)
    for i in range(3, 10):
        digits = list(filter(lambda x: x == str(i), candidate_string))
        if len(digits) == 2:
            return True
    return False

finallists = 0
for i in qualified:
    if candidature(i):
        finallists += 1
print(finallists)

# finallists = [x for x in qualified if candidature(x)]





     
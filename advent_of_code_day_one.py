# def this_fuel_amount(mass):
    # module_fuel = int(mass/3) - 2
    # return module_fuel

def repeating_fuel_calculator(module_fuel, mass):
    fuel = int(mass/3) - 2
    if fuel <= 0:
        return module_fuel
    else:
        module_fuel += fuel
        return repeating_fuel_calculator(module_fuel, fuel)
    
with open("advent_of_code_puzzle_file.txt") as text_of_masses:
    str_masses = text_of_masses.readlines()
    fuel_total = 0
    masses = []
    for item in str_masses:
        mass = int(item)
        masses.append(mass)
        this_fuel = repeating_fuel_calculator(0, mass)
        fuel_total += this_fuel
    print(fuel_total)



#   masses = [int(item) for item in str_masses]
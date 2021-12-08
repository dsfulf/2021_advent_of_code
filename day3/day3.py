with open('input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

zipped = list(zip(*data))

# part 1
gamma_arr = [None] * len(zipped)
epsilon_arr = [None] * len(zipped)

for i, zip_ in enumerate(zipped):
    count_0 = len([z for z in zip_ if z == '0'])
    count_1 = len([z for z in zip_ if z == '1'])
    if count_1 >= count_0:
        gamma_arr[i] = '1'
        epsilon_arr[i] = '0'
    else:
        gamma_arr[i] = '0'
        epsilon_arr[i] = '1'


gam_str = ''.join(g for g in gamma_arr)
gamma = int(gam_str, 2)
print(f'Gamma: {gam_str} - {gamma}')

eps_str = ''.join(g for g in epsilon_arr)
epsilon = int(eps_str, 2)
print(f'Gamma: {eps_str} - {epsilon}')

pwr = gamma * epsilon
print(f'Power Consumption: {pwr}')


# part 2
first = [z for z in zipped[0]]
oxygen_arr = [d for d in data]
co2_arr = [d for d in data]

for i in range(len(zipped)):
    if len(oxygen_arr) <= 1:
        break

    count_0 = len([o[i] for o in oxygen_arr if o[i] == '0'])
    count_1 = len([o[i] for o in oxygen_arr if o[i] == '1'])
    if count_1 >= count_0:
        cmn = '1'
    else:
        cmn = '0'

    j = 0
    while j < len(oxygen_arr) and len(oxygen_arr) > 1:
        if oxygen_arr[j][i] != cmn:
            oxygen_arr.pop(j)
        else:
            j += 1

for i in range(len(zipped)):
    if len(co2_arr) <= 1:
        break

    count_0 = len([o[i] for o in co2_arr if o[i] == '0'])
    count_1 = len([o[i] for o in co2_arr if o[i] == '1'])
    if count_1 >= count_0:
        cmn = '1'
    else:
        cmn = '0'

    j = 0
    while j < len(co2_arr) and len(co2_arr) > 1:
        if co2_arr[j][i] == cmn:
            co2_arr.pop(j)
        else:
            j += 1

oxygen = int(oxygen_arr[0], 2)
co2 = int(co2_arr[0], 2)

life_support = oxygen  * co2

print()
print(f'Oxygen_arr: {oxygen_arr[0]} - {oxygen}')
print(f'CO2_arr: {co2_arr[0]} - {co2}')
print(f'Life Support: {life_support}')

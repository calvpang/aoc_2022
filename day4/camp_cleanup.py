with open('input.txt', 'r') as f:
    lines = f.readlines()

result_1 = 0
result_2 = 0

for line in lines:
    ranges = line.strip().split(',')

    elf1_range = ranges[0].split('-')
    elf2_range = ranges[1].split('-')

    elf1_list = list(range(int(elf1_range[0]), int(elf1_range[1])+1))
    elf2_list = list(range(int(elf2_range[0]), int(elf2_range[1])+1))
    
    # Part 1
    if set(elf1_list).issubset(elf2_list) or set(elf2_list).issubset(elf1_list):
        result_1 += 1
    
    # Part 2
    intersect = list(set(elf1_list) & set(elf2_list))

    if intersect != []:
        result_2 += 1
    
print(f"Part 1: {result_1}")
print(f"Part 2: {result_2}")
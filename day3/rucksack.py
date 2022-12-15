import string

# Generating the Priorities Map
strings = (string.ascii_lowercase[:26] + string.ascii_uppercase[:26])
strings_list = list(strings)
priorities_map = {strings_list[i]: i+1 for i in range(len(strings_list))}

# Reading the Input File
with open('input.txt', 'r') as f:
    lines = f.readlines()

results = []

# Part 1
# for line in lines:
#     first_compartment = line[:len(line)//2]
#     second_compartment = line[len(line)//2:]
#     print(f"First Compartment: {first_compartment}")
#     print(f"Second Compartment: {second_compartment}")

#     intersect = list(set(first_compartment) & set(second_compartment))
#     print(f"Intersect: {intersect}")

#     results.extend(priorities_map[item] for item in intersect)

# # Testing Sample
# if results == [16, 38, 42, 22, 20, 19] and sum(results) == 157:
#     print("Passing!")
# else:
#     print("FAILING!")

# Sum of Priorities
# print(f"Sum of Priorities: {sum(results)}")

# Part 2
for i in range(0, len(lines), 3):
    elf_1, elf_2, elf_3 = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()

    print(f"Elf 1: {elf_1} \nElf 2: {elf_2} \nElf 3 {elf_3}")

    intersect = list(set(elf_1) & set(elf_2) & set(elf_3))
    print(f"Intersect: {intersect}")
    results.extend(priorities_map[item] for item in intersect)

# # Testing Sample
# if results == [18, 52] and sum(results) == 70:
#     print("Passing!")
# else:
#     print("Failing!")

# Sum of Priorities
print(f"Sum of Priorities: {sum(results)}")
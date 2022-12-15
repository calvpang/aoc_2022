with open('input.txt', 'r') as f:
    lines = f.readlines()

elves = [[]]

for i in lines:
    if i == '\n':
        elves.append([])
    else:
        elves[-1].append(int(i))

calories = [sum(elf) for elf in elves]
calories.sort(reverse=True)

# Finding the Maximum
print(f"Maximum Number of Calories: {calories[0]}")

# Finding the Total Calories of the Top 3 Elves
print(f"Total Number of Calories for the Top 3 Elves: {sum(calories[:3])}")
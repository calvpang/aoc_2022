def decrypt_line(x, y, part1=True):
    if part1:
        clues = {'A': 'Rock', 'B': 'Paper', 'C':'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    else:
        clues = {'A': 'Rock', 'B': 'Paper', 'C':'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
    return clues[x], clues[y]

def determine_play(x, y):
    if x in ['Rock', 'Paper', 'Scissors'] and y == 'Draw':
        return x
    elif (x == 'Rock' and y == 'Win'):
        return 'Paper'
    elif (x == 'Paper' and y == 'Win'):
        return 'Scissors'
    elif (x == 'Scissors' and y == 'Win'):
        return 'Rock'
    elif (x == 'Paper' and y == 'Lose'):
        return 'Rock'
    elif (x == 'Scissors' and y == 'Lose'):
        return 'Paper'
    elif (x == 'Rock' and y == 'Lose'):
        return 'Scissors'

def calculate_outcome_score(x,y):
    outcome_scores = {'Lost': 0, 'Draw': 3, 'Won': 6}
    if x == y:
        return outcome_scores['Draw']
    elif (x == 'Rock' and y == 'Scissors') or (x == 'Scissors' and y == 'Paper') or (x == 'Paper' and y == 'Rock'):
        return outcome_scores['Lost']
    else:
        return outcome_scores['Won']

def calculate_shape_score(y):
    shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    return shape_scores[y]

with open('sample.txt', 'r') as f:
    strategies = f.readlines()
    total_score = []

for strategy in strategies:
    results = strategy.strip().split(' ')

    # # Part 1
    # x,y = decrypt_line(results[0], results[1], part1=True)
    # score = calculate_outcome_score(x, y) + calculate_shape_score(y)
    # total_score.append(score)

# # Testing
# if total_score == [8, 1, 6] and sum(total_score) == 15:
#     print('Passed!')
# else:
#     print('Failed!')

    # Part 2
    x, y = decrypt_line(results[0], results[1], part1=False)
    play = determine_play(x,y)
    score = calculate_outcome_score(x, play) + calculate_shape_score(play)
    total_score.append(score)

# # Testing
# if total_score == [4, 1, 7] and sum(total_score) == 12:
#     print('Passed!')
# else:
#     print('Failed!')

print(f"Outcomes for each Round: {total_score}")
print(f"Total Score: {sum(total_score)}")

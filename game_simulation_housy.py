import random

def is_housy(player_matrix):
    sum_ = 0
    for row in player_matrix:
        sum_ += sum(row)

    return sum_ == 0
    
#n = int(input('Enter number of players :'))
#names = list(map(str, input('Enter players names : ').split(' ')))
names = list(map(str, 'srikanth ganesh vipin ram_reddy mohan charani'.split()))
number_of_games = int(input('Enter number of games : '))

# jaldi_5 = int(input('Enter jaldi_5 score : '))
# row = int(input('Enter row score : '))
# housy = int(input('Enter housy score : '))

jaldi_5 = 110
row = 80
housy = 250

scores = {'jaldi_5' : jaldi_5, 'row_0' : row, 'row_1' : row, 'row_2' : row, 'housy' : housy}

player_scores = {}
for elem in names:
    player_scores[elem] = number_of_games*(-100)

for i in range(number_of_games):
    
    dict_ = {}
    for player in names:
        matrix = [[0]*9 for _ in range(3)]
        numbers = random.sample(range(1,101), 15)
        i = 0
        for row in range(3):
            fill_random_indices = random.sample(range(9), 5)
            for elem in fill_random_indices:
                matrix[row][elem] = numbers[i]
                i += 1
    
        dict_[player] = matrix
    
    #print(dict_)

    board = set([i+1 for i in range(100)])

    jaldi_5 = {}
    for player in names:
        jaldi_5[player] = 0

    row_numbers_happened = [0, 0, 0]
    jaldi_5_happened = 0

    winner = {}
    player = {}
    flag = False

    while True:
        #number = random.sample()
        random_element = random.choice(list(board))
        board.remove(random_element)

        for player in names:
            #cur_row = 0
            for cur_row, row in enumerate(dict_[player]):
                #print('cur_row', cur_row)
                for index in range(9):
                    if row[index] == random_element:
                        row[index] = 0
                        jaldi_5[player] += 1
                    
                    if jaldi_5[player] == 5 and jaldi_5_happened == 0:
                        winner['jaldi_5'] = player
                        jaldi_5_happened == 1

        
                if sum(row) == 0 and row_numbers_happened[cur_row] == 0:
                    row_numbers_happened[cur_row] = 1
                    winner['row_' + str(cur_row)] = player

                #cur_row += 1

            if is_housy(dict_[player]):
                winner['housy'] = player
                flag = True
                break
    
        if flag:
            break

    #print(winner)
    for winning_type in winner:
        player_scores[winner[winning_type]] += scores[winning_type]

    #print(f'After round {i} ', player_scores)

print('final_scores : ', player_scores)


        





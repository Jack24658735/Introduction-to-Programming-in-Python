import random
def battle(your_sign, my_sign):
    rock_dict = {'rock' : 'tied!', 'paper' : 'I lose!', 'scissors' : 'you lose!'}
    paper_dict = {'rock' : 'you lose!', 'paper' : 'tied!', 'scissors' : 'I lose!'}
    scissors_dict = {'rock' : 'I lose!', 'paper' : 'you lose!', 'scissors' : 'tied!'}
    battle_dict = {'rock' : rock_dict, 'paper' : paper_dict, 'scissors' : scissors_dict}
    s = ''
    s += 'I am '
    if your_sign == my_sign:
        s += 'also '
    s += my_sign
    s += ' - '
    s += battle_dict[my_sign][your_sign]
    print(s)

if __name__ == '__main__':
    flag = False
    while True:
        if not flag:
            sign = input('rock, paper, scissors? ')
            flag = False
        if sign == 'quit':
            print('bye')
            break
        if sign in {'rock', 'paper', 'scissors'}:
            AI_sign = random.choice(['rock', 'paper', 'scissors'])
            battle(sign, AI_sign)
            flag = False
        else:
            sign = input('f{sign} is invalid - try again? ')
            flag = True

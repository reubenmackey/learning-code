from random import randint

selection = ['stone','scissors','paper']

def cpu_selection():
    index = randint(0,2)
    return selection[index]

def start_game():

    def play_again():
        while True:
            play = input('Do you want to play again - Y/N: \n')
            if play.lower() == 'n' or play.lower() == 'no':
                print('Application Exited')
                exit()
            elif play.lower() == 'y' or play.lower == 'yes':
                start_game()
            else:
                print('That is not a valid option, try again!!')
    while True:
        cpu_hand = cpu_selection()
        user_hand = input("Choose your hand: ")
        if user_hand not in selection:
            print('That is not a valid hand, try again: ')
            continue
        elif user_hand == cpu_hand:
            user_hand = user_hand.capitalize()
            cpu_hand = cpu_hand.capitalize()
            print('You have selected {} and the CPU selected {} which means it is a DRAW!!'.format(user_hand,cpu_hand))
            continue
        else:
            user_hand = user_hand.capitalize()
            cpu_hand = cpu_hand.capitalize()
            if user_hand == 'Stone' and cpu_hand == 'Paper':
                print('YOU selected {} and CPU selected {}. CPU WINS!!'.format(user_hand,cpu_hand))
            elif user_hand == 'Paper' and cpu_hand == 'Stone':
                print('YOU selected {} and CPU selected {}. YOU WIN!!'.format(
                    user_hand, cpu_hand))
            elif user_hand == 'Scissors' and cpu_hand == 'Stone':
                print('YOU selected {} and CPU selected {}. CPU WINS!!'.format(
                    user_hand, cpu_hand))
            elif user_hand == 'Stone' and cpu_hand == 'Scissors':
                print('YOU selected {} and CPU selected {}. YOU WIN!!'.format(
                    user_hand, cpu_hand))
            elif user_hand == 'Paper' and cpu_hand == 'Scissors':
                print('YOU selected {} and CPU selected {}. CPU WINS!!'.format(
                    user_hand, cpu_hand))
            elif user_hand == 'Scissors' and cpu_hand == 'Paper':
                print('YOU selected {} and CPU selected {}. YOU WIN!!'.format(
                    user_hand, cpu_hand))
        play_again()

if __name__ == '__main__':
    print('Game Started\t\n')
    print('****STONE ****SCISSORS ****PAPER\t\n')
    start_game()

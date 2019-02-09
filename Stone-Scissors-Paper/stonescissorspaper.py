from random import randint                              #import randint module

selection = ['stone','scissors','paper']                #List created for cpu selection

def cpu_selection():
    index = randint(0,2)                                #assign random integer between 0 and 2 to assign to the variable 'index'
    return selection[index]                             #selecting an option from the selection list using the random 'index' variable to select an item from the list randomly at it's index position.

def start_game():                                       #function that starts the game

    def play_again():                                   #Runs after the inital and subsequent games to prompt user to play again
        while True:
            play = input('Do you want to play again - Y/N: \n')
            if play.lower() == 'n' or play.lower() == 'no':
                print('Application Exited')
                exit()
            elif play.lower() == 'y' or play.lower == 'yes':
                start_game()
            else:
                print('That is not a valid option, try again!!')

    def cpu_wins(you,cpu):
        return 'YOU selected {} and CPU selected {}. CPU WINS!!'.format(you,cpu)    #created Function to remove repeatable text if CPU wins.

    def you_win(you,cpu):
        return 'YOU selected {} and CPU selected {}. YOU WIN!!'.format(you,cpu)     #created Function to remove repeatable text is you win.

    while True:                                                                     #Logic run to Determine if a hand is valid or a DRAW before passing to the Logic part of the code to determine the winnner.
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
        else:                                                                       #Logic run to determine the winner
            user_hand = user_hand.capitalize()
            cpu_hand = cpu_hand.capitalize()
            if user_hand == 'Stone' and cpu_hand == 'Paper':
                print(cpu_wins(user_hand,cpu_hand))
            elif user_hand == 'Paper' and cpu_hand == 'Stone':
                print(you_win(user_hand,cpu_hand))
            elif user_hand == 'Scissors' and cpu_hand == 'Stone':
                print(cpu_wins(user_hand,cpu_hand))
            elif user_hand == 'Stone' and cpu_hand == 'Scissors':
                print(you_win(user_hand,cpu_hand))
            elif user_hand == 'Paper' and cpu_hand == 'Scissors':
                print(cpu_wins(user_hand,cpu_hand))
            elif user_hand == 'Scissors' and cpu_hand == 'Paper':
                print(you_win(user_hand,cpu_hand))
        play_again()                                                                #After determining the winner, the play again function runs to prompt the user to play again.

if __name__ == '__main__':
    print('Game Started\t\n')
    print('****STONE ****SCISSORS ****PAPER\t\n')
    start_game()

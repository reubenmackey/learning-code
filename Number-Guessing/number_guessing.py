from random import randint                  #Import randint module

def get_cpu_num():                          #Function to get random number for cpu player.
    return randint(0,10)

cpu_num = get_cpu_num()                     #Assign random number function to the cpu_num variable
guess_num = None                            #Assign None value to guess_num variable
count = 1                                   #Added count variable to count the number of guesses.

while guess_num != cpu_num:                                 #logic addedd to determine whether guess was correct, too low or too high.
    guess_num = input("Guess the number (between 1-10)?: ")
    try:
        guess_num =int(guess_num)
    except:
        print('That is an incorrect number or type, try again: ')
        continue
    else:
        if guess_num == cpu_num:
            print('You Guessed it!!, it took you {} tries to guess this number.'.format(count))
            break
        elif guess_num > cpu_num:
            print('Guess number {} was too high, try lower'.format(count))
            count += 1
            continue
        elif guess_num < cpu_num:
            print('Guess number {} was too low, try higher'.format(count))
            count += 1
            continue

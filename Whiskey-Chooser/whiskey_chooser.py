#This App was created as we have a regular Whiskey night and no one could decide on which Whiskey to try first.

from random import randint                             #Import randint module (used to select a random integer)
from time import sleep                                 #Import sleep module (used to delay time)
import inflect                                         #Import inflect module (used to give 1st, 2nd, 3rd... etc..)

st = inflect.engine()
count = 0                                              #Count added to hold the number of whiskey's in order from (1st, 2nd, 3rd... etc..)
ordered_list = []

def num_of_bottles():                                  #Function created to prompt for the number of whiskey bottles.
    while True:
        bottle_num = input("How many bottles of whiskey do you have?: ")
        try:
            bottle_num = int(bottle_num)
            return bottle_num
        except:
            print('That is an incorrect number or type, try again: ')
            continue

def name_of_whiskey(bottle_num):                        #Function created to name each of the whiskey bottles.
    whiskey_list = []
    for num in range(1,bottle_num+1):
        whiskey_name = input('Enter the name of the {} Whiskey: '.format(st.ordinal(num)))
        whiskey_list.append(whiskey_name)
    return whiskey_list

def select_random(whiskey_list):                        #Functions created to randomly select a whiskey bottle, then to remove it from the list (so it won't be used twice).
    global ordered_list
    global count
    rand_index = randint(0,len(whiskey_list)-1)
    whiskey_selected = whiskey_list[rand_index]
    ordered_list.append(whiskey_selected)
    whiskey_list.remove(whiskey_selected)
    count += 1
    return whiskey_selected

def countdown():                                        #Countdown from 3 seconds inserted in between each randomly selected whiskey.
    range_count = 3
    while range_count != 0:
        sleep(1)
        print(range_count)
        range_count -= 1

if __name__ == '__main__':                              #Functions assigned to variables and run in order.
    bottle_num = num_of_bottles()
    whiskey_list = name_of_whiskey(bottle_num)
    whiskey_selected = select_random(whiskey_list)
    timer_countdown = countdown()
    print('The {} Whiskey selected is: {}'.format(st.ordinal(count),whiskey_selected))

    while len(whiskey_list) > 0:                        #Contiunes to prompt to choose the next whiskey at random as long as there is a whiskey in the list.
        prompt = input('Are you ready for the next Whiskey (enter Y/y to continue): ')
        if prompt.lower() == 'y' or prompt.lower() == 'y':
            whiskey_selected = select_random(whiskey_list)
            countdown()
            print('The {} Whiskey selected is: {}'.format(st.ordinal(count),whiskey_selected.lower().capitalize()))
        else:
            print('That is an invalid option, please try again: ')

    print('\n')
    print('All Whiskeys have been selected in this order: ')
    file = open('whiskey-night.txt','w')
    file.write('All Whiskeys have been selected in this order: \n\n')
    whiskey_count = 1
    for whiskey in ordered_list:
        file.write("{}: {} \n".format(whiskey_count,whiskey.lower().capitalize()))
        print("{}: {}".format(whiskey_count,whiskey.lower().capitalize()))      #Prints a list of whiskeys and saves this information to a text file named 'whiskey-night.txt'.
        whiskey_count += 1
    file.close()
    print('File Saved to whiskey-night.txt')

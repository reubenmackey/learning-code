#Help Choose a name, thing or person at Random

from random import randint                             #Import randint module (used to select a random integer)
from time import sleep                                 #Import sleep module (used to delay time)
import inflect                                         #Import inflect module (used to give 1st, 2nd, 3rd... etc..)

st = inflect.engine()
count = 0                                              #Count added to hold the number of entry's in order from (1st, 2nd, 3rd... etc..)
ordered_list = []

def num_of_entries():                                  #Function created to prompt for the number of entries.
    while True:
        entry_num = input("How many Entries do you have?: ")
        try:
            entry_num = int(entry_num)
            return entry_num
        except:
            print('That is an incorrect number or type, try again: ')
            continue

def name_of_entries(entry_num):                        #Function created to name each of the entries.
    name_list = []
    for num in range(1,entry_num+1):
        entry_name = input('Enter the {} entry: '.format(st.ordinal(num)))
        name_list.append(entry_name)
    return name_list

def select_random(name_list):                        #Functions created to randomly select an entry, then to remove it from the list (so it won't be used twice or more).
    global ordered_list
    global count
    rand_index = randint(0,len(name_list)-1)
    entry_selected = name_list[rand_index]
    ordered_list.append(entry_selected)
    name_list.remove(entry_selected)
    count += 1
    return entry_selected

def countdown():                                        #Countdown from 3 seconds inserted in between each randomly selected entry.
    range_count = 3
    while range_count != 0:
        sleep(1)
        print(range_count)
        range_count -= 1

if __name__ == '__main__':                              #Functions assigned to variables and run in order.
    entry_num = num_of_entries()
    name_list = name_of_entries(entry_num)
    entry_selected = select_random(name_list)
    timer_countdown = countdown()
    print('The {} entry selected is: {}'.format(st.ordinal(count),entry_selected))

    while len(name_list) > 0:                        #Contiunes to prompt to choose the next entry at random as long as there is a entry in the list.
        prompt = input('Are you ready for the next Entry (enter Y/y to continue): ')
        if prompt.lower() == 'y' or prompt.lower() == 'y':
            entry_selected = select_random(name_list)
            countdown()
            print('The {} Entry selected is: {}'.format(st.ordinal(count),entry_selected.lower().capitalize()))
        else:
            print('That is an invalid option, please try again: ')

    print('\n')
    print('All Entries have been selected in this order: ')
    file = open('entry-night.txt','w')
    file.write('All Entries have been selected in this order: \n\n')
    entry_count = 1
    for entry in ordered_list:
        file.write("{}: {} \n".format(entry_count,entry.lower().capitalize()))
        print("{}: {}".format(entry_count,entry.lower().capitalize()))      #Prints a list of entrys and saves this information to a text file named 'entry-night.txt'.
        entry_count += 1
    file.close()
    print('File Saved to entry-night.txt')

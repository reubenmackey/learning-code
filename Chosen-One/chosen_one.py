from time import sleep                              #import sleep module
from random import randint                          #import randint module

def name_inputs():                                  #Function created to Input 3 Persons Names
    name1 = input("Please Enter the First Person's Name: ")
    name2 = input("Please Enter the Second Person's Name: ")
    name3 = input("Please Enter the Third Person's Name: ")
    return [name1,name2,name3]                      #Returns as a List of all 3 name inputs

def countdown():                                    #Function created to do the countdown from 10
    sleep(1)
    print('Thank you for providing these details, who is the chosen one?:')
    count = 10
    while count >= 0:
        sleep(1)
        print(count)
        count -=1

if __name__ == '__main__':
    name_list = name_inputs()                       #name_inputs Function called and assigned to name_list
    countdown()                                     #countdown Function called
    index = randint(0,2)                            #A randomly generated between number between 0-2 is assigned to the index variable
    name_list[index]                                #The randomly chosen index position (above) has selected the name from the list of names and this is printed as the chosen one.
    print("{} is the chosen one!!".format(name_list[index]))

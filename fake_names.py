from faker import Faker                     #Import fake data module
from random import randint                  #Import randint module
from datetime import datetime               #Import datetime module

fake_data = Faker()                         #Assign fake data module to the varible fake_data

def populate_fake_data():                   #Create a fake data function that promps for a filename and the number of entries then iterates through to populate data in a text file.
    name = input('Enter the name of the file: ')
    if len(name) == 0:
        name = 'names.txt'
    elif not name.endswith('.txt'):
        name = name+'.txt'
    else:
        name = name
        pass
    file = open(name,'w')
    while True:
        num_entries = input('How many records do you need (select 1-2000)?')
        try:
            num_entries = int(num_entries)
            break
        except:
            print('That is an incorrect number or type, please try again')

    for num in range(1,num_entries+1):
        first_name = fake_data.first_name()
        last_name = fake_data.last_name()
        file.write('{} {} \n'.format(first_name,last_name))
    file.close()

if __name__ == '__main__':
    populate_fake_data()                                    #Runs the populate data function
    start_time = datetime.now()                             #gets start time
    print('Populating Data....')
    end_time = datetime.now()                               #gets end time
    print('Populating Data Completed in {} milliseconds'.format(str(end_time-start_time)[6:]))

    #Prints the end time - start time to give the time taken to complete populating of data.

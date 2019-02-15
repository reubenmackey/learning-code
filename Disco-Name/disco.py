from termcolor import colored                           #Import colored module (to color text)
from time import sleep                                  #Import sleep module to delay timing between printing text to the screen.

colors = ['blue','green','red','yellow','magenta','cyan']*2       #List of colors

def change_color(name):                                 #Function created to iterate through colors list to use with the colored module (takes 2 arguments - the name and the color)
    for color in colors:
        sleep(1)
        print(colored(name,color))

name = input("Please Enter a Name: ")                  #Name Input prompts to enter a name


if __name__ == '__main__':
    change_color(name)                                 #Runs the change_color function and take name as the argument.

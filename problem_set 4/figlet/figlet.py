from pyfiglet import Figlet
import sys
import random
def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        text = input('Input: ')
        figlet.setFont(font = random.choice(figlet.getFonts()))
        print(figlet.renderText(text))
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in figlet.getFonts()):
        text = input('Input: ')
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit('follow the intsructions man')

main()


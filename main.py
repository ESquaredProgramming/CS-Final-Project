# main.py

from gui import *


def main():
    window = Tk()
    window.title('TV Remote')
    window.geometry('400x450')
    window.resizable(False, False)
    
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()

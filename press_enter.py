import sys
import time
import getopt
import pyautogui as pg

def main(argv):

    while True:
        time.sleep(1)
        print('Pressing Enter...')
        pg.press('enter')
        print('Ok')

if __name__ == "__main__":
   main(sys.argv[1:])

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:30:42 2016

@author: young
"""

import os
import time
qwhitespace = ['        ', '        ', '        ', '        ', '        ', '        ', '        ']
def kunnoname(name, lens):
    qA = ['   #    ', ' #   #  ', '#     # ', '# ### # ', '#     # ', '#     # ', '#     # ']
    qB = [' #####  ', '#     # ', '#     # ', '######  ', '#     # ', '#     # ', ' #####  ']
    qC = [' #####  ', '#     # ', '#       ', '#       ', '#       ', '#     # ', ' #####  ']
    qD = ['######  ', '#     # ', '#     # ', '#     # ', '#     # ', '#     # ', '######  ']
    qE = ['####### ', '#       ', '#       ', '######  ', '#       ', '#       ', '####### '] 
    qF = ['####### ', '#       ', '#       ', '#####   ', '#       ', '#       ', '#       ']
    qG = [' #####  ', '#       ', '#       ', '#   ### ', '#     # ', '#    ## ', ' #### # ']
    qH = ['#     # ', '#     # ', '#     # ', '####### ', '#     # ', '#     # ', '#     # ']
    qI = [' #####  ', '   #    ', '   #    ', '   #    ', '   #    ', '   #    ', ' #####  ']
    qJ = ['  ##### ', '     #  ', '     #  ', '     #  ', '     #  ', ' #   #  ', '  ###   ']
    qK = ['#     # ', '#    #  ', '#   #   ', '####    ', '#   #   ', '#    #  ', '#     # ']
    qL = [' #      ', ' #      ', ' #      ', ' #      ', ' #      ', ' #      ', ' #####  ']
    qM = ['#     # ', '##   ## ', '# # # # ', '#  #  # ', '#     # ', '#     # ', '#     # '] 
    qN = ['#     # ', '##    # ', '# #   # ', '#  #  # ', '#   # # ', '#    ## ', '#     # ']
    qO = [' #####  ', '#     # ', '#     # ', '#     # ', '#     # ', '#     # ', ' #####  '] 
    qP = ['######  ', '#     # ', '#     # ', '######  ', '#       ', '#       ', '#       ']
    qQ = [' #####  ', '#     # ', '#     # ', '#     # ', '#   # # ', '#    #  ', ' #### # '] 
    qR = ['######  ', '#     # ', '#     # ', '######  ', '#   #   ', '#    #  ', '#     # '] 
    qS = [' ###### ', '#       ', '#       ', ' #####  ', '      # ', '      # ', '######  ']
    qT = ['####### ', '   #    ', '   #    ', '   #    ', '   #    ', '   #    ', '   #    ']
    qU = ['#     # ', '#     # ', '#     # ', '#     # ', '#     # ', '#     # ', ' #####  ']
    qV = ['#     # ', '#     # ', '#     # ', ' #   #  ', ' #   #  ', '  # #   ', '   #    ']
    qW = ['#     # ', '#     # ', '#  #  # ', '#  #  # ', '#  #  # ', '# # # # ', ' #   #  ']
    qX = ['#     # ', ' #   #  ', '  # #   ', '   #    ', '  # #   ', ' #   #  ', '#     # ']
    qY = ['#     # ', '#     # ', ' #   #  ', '  # #   ', '   #    ', '   #    ', '   #    ']
    qZ = ['####### ', '     #  ', '    #   ', '   #    ', '  #     ', ' #      ', '####### ']
    alphabet = {'whitespace':qwhitespace, 'a':qA, 'b':qB, 'c':qC, 'd':qD, 'e':qE, 'f':qF, 'g':qG, 'h':qH, 'i':qI, 'j':qJ, 'k':qK, 'l':qL, 'm':qM, 'n':qN, 'o':qO, 'p':qP, 'q':qQ, 'r':qR, 's':qS, 't':qT, 'u':qU, 'v':qV, 'w':qW, 'x':qX, 'y':qY, 'z':qZ}
    screen = [' ']*7
    for x in range(20):   
        for j in range(7):
            for i in range(lens):
                screen[j] =' '*x + screen[j] + alphabet[name[i]][j]   #get your name use "#"
            print screen[j]   
            screen = [' ']*7
        time.sleep(0.3)
        os.system('cls')
        print ('\n')*x
    return screen 

def main():
    name = raw_input('please input your English name:')   
    lens = len(name)
    name = name.lower()  # exchange what you input into lower case letters
    kunnoname(name,lens)
main()
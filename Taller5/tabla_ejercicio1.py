# -*- coding: utf-8 -*-
import numpy as np
from texttable import Texttable

def table(results):
    n,m = results.shape
    
    table = Texttable() # create the table to put the data inside
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype([            't',  # text
                                  'e',  # float (exponent)
                                  'e',  # float (exponent)
                                  'e'])  # float (exponent)
    
    table.set_cols_align(["c","c","c","c"])
    
    table.add_rows([['A',
                 'KF(A)',
                 '||I - AB||F',
                 '||I - Ainv(A)||F']])
    
    
    table.add_row(["rand(5,5)",results[0][0],results[0][1],results[0][2]])
    table.add_row(["hilbert(5,5)",results[1][0],results[1][1],results[1][2]])
    table.add_row(["rand(20,20)",results[2][0],results[2][1],results[2][2]])
    table.add_row(["hilbert(20,20)",results[3][0],results[3][1],results[3][2]])

    print(table.draw() + "\n")
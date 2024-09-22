"""LIBRARIES"""
import pandas as pd
import telnetlib3
import re
import asyncio

"""FUNCTIONS"""

def readFromExcel(fileName):
    df = pd.read_excel(fileName)
    Encoders = {}

    for index, row in df.iterrows():
        if row.iloc[3] not in Encoders:
            Encoders[row.iloc[3]] = {}
        Encoders[row.iloc[3]][row.iloc[1]] = {'multiIP' : row.iloc[4],'multiPort' : row.iloc[5]} 

    for keys,values in Encoders.items():
        print(keys)
        for key, value in values.items():
            print(key, value)
    return Encoders
            
"""VARIABLES"""
fileName = 'encoder list.xlsx'

"""MAIN CODE"""

# encoderIP = 'localhost'
# port = 8023
Encoders = readFromExcel(fileName)

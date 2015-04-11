__author__ = 'rodolfo'


# This programm has some visualisation using pandas.

import pandas as pd
import numpy as np

# Buys Table
def buysTable():
    buys = pd.read_csv("data/yoochoose-buys.dat",
                   names=["session", "timestamp", "item", "price", "qty"],
                   parse_dates=["timestamp"], nrows = 100)

    time = buys["timestamp"]

    print "\n Buys head \n \n"
    return time

# Main
def main():
    print buysTable()
    pass


if __name__ == '__main__':
    main()
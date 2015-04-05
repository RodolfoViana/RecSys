__author__ = 'rodolfo'


# This programm has some visualisation using pandas.

import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib as mpl

# sns.set_palette("hls")

# Buys Table Head
def buysTable():
    buys = pd.read_csv("data/yoochoose-buys.dat",
                   names=["session", "timestamp", "item", "price", "qty"],
                   parse_dates=["timestamp"])

    print "\n Buys head \n \n"
    return buys

# Clicks Table Head
def clicksTable():
    clicks = pd.read_csv("data/yoochoose-clicks.dat",
                     names=["session", "timestamp", "item", "category"],
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

    print "\n Clicks head \n \n"
    #print clicks
    return clicks


# Tell how many itens was bought
def sessionItemBuys():
    buys = buysTable()
    session_item_buys = buys[["session", "item", "qty"]].groupby(["session", "item"]).sum()
    session_item_buys = session_item_buys["qty"]
    session_item_buys = session_item_buys.to_frame("bought")
    del buys


    print "comecou cliks"
    clicks = clicksTable()
    session_item_clicks = clicks[["session", "item", "timestamp"]].groupby(["session", "item"]).count()
    del clicks
    session_item_clicks = session_item_clicks["timestamp"]
    session_item_clicks = session_item_clicks.to_frame(name="clicks")
    #print clicks.groupby(["session"]).get_group(12)

    print "comecou merge"
    session_item_merge = pd.merge(session_item_clicks, session_item_buys, how='outer', left_index=True, right_index=True)
    session_item_merge.fillna(0, inplace=True)
    session_item_merge.to_csv("clicksvsbought.csv")
    print "fim"

# Main
def main():
    sessionItemBuys()
    pass


if __name__ == '__main__':
    main()
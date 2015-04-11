__author__ = 'rodolfo'

# This programm has the fist pre-preocessing
# at the end the file will have the format
# session   item   bought


import pandas as pd

# Buys Table
def buysTable():
    buys = pd.read_csv("data/yoochoose-buys.dat",
                   names=["session", "timestamp", "item", "price", "bought"],
                   parse_dates=["timestamp"])

    print "\n Buys head \n \n"
    return buys

# Clicks Table
def clicksTable():
    clicks = pd.read_csv("data/yoochoose-clicks.dat",
                     names=["session", "timestamp", "item", "category"],
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

    print "\n Clicks head \n \n"
    return clicks


# Tell how many itens was bought
def sessionItemBuys():
    buys = buysTable()

    buys = buys.drop("timestamp", 1)
    buys = buys.drop("price", 1)

    # So far we have

    # session item
    # 11      214821371
    # 12      214717867
    # 21      214548744
    # 21      214838503
    # 33      214706441

    print "comecou cliks"
    clicks = clicksTable()
    clicks = clicks.drop("timestamp", 1)
    clicks = clicks.drop("category", 1)

    # session item
    # 1       214536500
    # 1       214536502
    # 1       214536506
    # 1       214577561
    # 2       214551617
    # 2       214662742
    # 2       214757390
    # 2       214757407

    print "comecou merge"

    session_item_merge =  pd.merge(clicks, buys, how='outer', left_on=["session", "item"], right_on=["session", "item"])
    session_item_merge.fillna(0, inplace=True)
    session_item_merge.loc[session_item_merge["bought"] != 0, "bought"] = 1
    session_item_merge.to_csv("sessionitemboughtcomplet.csv")

    # Now we have a table like this

    # session   item       bought
    # 490437  214716975       1
    # 490459  214639327       0
    # 490783  214706460       1
    # 490792  214821277       0

    print "\n fim"

# Main
def main():
    sessionItemBuys()
    pass


if __name__ == '__main__':
    main()
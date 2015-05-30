__author__ = 'rodolfo'


def readAquivo():
    arquivoOriginal = open("tudao-sort.txt", "r")
    newFile = open("tudao-sortStart.csv", "w")


    oldsession = -1
    print arquivoOriginal.readline()
    for line in arquivoOriginal:
        session = line.split(",")[0]

        if (oldsession == session):
            print "bb"
            newline = line.split(",")[0]+","+line.split(",")[1]+","+tempo+"," + line.split(",")[2] + "," + line.split(",")[3] + "," + line.split(",")[4] + "," +line.split(",")[5] + "," +line.split(",")[6]
            newFile.write(newline)
        else:
            tempo = line.split(",")[1]
            print "aa"
            newline = line.split(",")[0]+","+line.split(",")[1]+","+tempo+","+line.split(",")[2] + "," + line.split(",")[3] + "," + line.split(",")[4] + "," +line.split(",")[5] + "," +line.split(",")[6]
            newFile.write(newline)
        oldsession = session

    


# Main
def main():
    readAquivo()
    pass

if __name__ == '__main__':
    main()



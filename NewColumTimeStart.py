__author__ = 'rodolfo'


def readAquivo():
    arquivoOriginal = open("MyData.csv", "r")
    newFile = open("newclicks100.csv", "w")




    oldsession = -1
    for line in arquivoOriginal:
        session = line.split(",")[2]

        if (oldsession == session):
            print "bb"
            newline = line.split(",")[0] + "," + line.split(",")[1] + "," + line.split(",")[2] + "," + line.split(",")[3] + "," + tempo + "," + line.split(",")[4] + "," +line.split(",")[5]
            newFile.write(newline)
        else:
            tempo = line.split(",")[3]
            print "aa"
            newline = line.split(",")[0] + "," + line.split(",")[1] + "," + line.split(",")[2] + "," + line.split(",")[3] + "," + tempo + "," + line.split(",")[4] + "," +line.split(",")[5]
            newFile.write(newline)
        oldsession = session


# Main
def main():
    readAquivo()
    pass

if __name__ == '__main__':
    main()
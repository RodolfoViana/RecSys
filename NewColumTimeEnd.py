__author__ = 'rodolfo'


def readArquivo():
    arquivoOriginal = open("inverseclicksWithTime", "r")
    newFile = open("inverseclicksWithTimeWithEnd", "w")

    # sed '1!G;h;$!d' clicksWithTime > inverseclicksWithTime


    # sed -i '$ d' inverseclicksWithTime
    oldsession = -1
    for line in arquivoOriginal:
        session = line.split(",")[3]

        if (oldsession == session):
            print "bb"
            newline = line.split(",")[0] + "," + line.split(",")[1] + "," + line.split(",")[2] + "," + line.split(",")[3] + "," + line.split(",")[4] + "," +line.split(",")[5] + "," + tempo + "," + line.split(",")[6] + "," +line.split(",")[7] + "," + line.split(",")[8]
            print newline
            newFile.write(newline)
        else:
            tempo = line.split(",")[4]
            print "aa"
            newline = line.split(",")[0] + "," + line.split(",")[1] + "," + line.split(",")[2] + "," + line.split(",")[3] + "," + line.split(",")[4] + "," +line.split(",")[5] + "," + tempo + "," + line.split(",")[6] + "," + line.split(",")[7] + "," + line.split(",")[8]
            print newline
            newFile.write(newline)
        oldsession = session



# Main
def main():
    readArquivo()
    pass

if __name__ == '__main__':
    main()
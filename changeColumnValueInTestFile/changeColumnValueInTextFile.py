def changeValue(listFiles, delimiter, columnName, newValue):

    counter = 0

    for fileName in listFiles:
        counter += 1

        newFileContents = []

        infile = open(fileName, 'r')

        header = infile.readline().strip()
        headerList = header.split(delimiter)
        columnIndex = headerList.index(columnName)

        newFileContents.append(header)

        for line in infile:
            newLine = []

            lineList = line.split(delimiter)

            for i in range(len(lineList)):

                if i == columnIndex and lineList[i] == "":
                    tempString = newValue
                else:
                    tempString = lineList[i]

                newLine.append(tempString.strip())

            newFileContents.append(delimiter.join(newLine))


        infile.close()

        outfile = open(fileName, 'w')
        outfile.write("\n".join(newFileContents))
        outfile.close()

        print("File {0} of {1} done".format(counter, len(listFiles)))

    print("Process Complete")


#For testing
#fileList = [r"Flat01.txt", r"Flat02.txt"]
#changeValue(fileList,"|","Name","Unknown Buyer")
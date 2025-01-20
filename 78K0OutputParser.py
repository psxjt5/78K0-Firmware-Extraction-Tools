import sys

lastPosition = 0
currentByte = ""

clock = ""
lsb = ""
mid = ""
msb = ""
data = ""

def main():
    global clock
    global lsb
    global mid
    global msb
    global data

    if len(sys.argv) <= 1:
        sys.stderr.write("Usage: 78K0OutputParser <output.txt>")
        sys.exit(1)

    # Open the file specified in the arguments.
    filename = sys.argv[1]
    fileLines = []

    # Read all lines from the text file.
    with open(filename, 'r') as f:
        fileLines = f.readlines()

    # Iterate through all lines in the file.
    count = 0
    for line in fileLines:
        count += 1

        lineSplit = line.replace("\n", "")
        lineSplit = lineSplit.replace("\r", "")
        lineSplit = lineSplit.split(":")

        # Remove spaces
        lineSplit[1] = lineSplit[1].replace(" ", "")

        # Check the Label and collate the results
        if (lineSplit[0] == "D0 - Clock (P120)"):
            # Clock Line
            clock += lineSplit[1]
        elif (lineSplit[0] == "D2 - Position LSB (P50)"):
            # LSB Line
            lsb += lineSplit[1]
        elif (lineSplit[0] == "D4 - Position MID (P51)"):
            # MID Line
            mid += lineSplit[1]
        elif (lineSplit[0] == "D5 - Position MSB (P52)"):
            # MSB Line
            msb += lineSplit[1]
        elif (lineSplit[0] == "D7 - Data (P53)"):
            # Data Line
            data += lineSplit[1]

    # Analyse the data
            
    prevClock = 0
    count = 0
    previousPosition = 8
    currentByte = ""

    for clockMeasurement in clock:

        #print(clockMeasurement, end="")
        
        if (prevClock == "1" and clockMeasurement == "0"):
            # Found a falling edge

            currentLSB = lsb[count]
            currentMID = mid[count]
            currentMSB = msb[count]

            #print("LSB " + currentLSB)
            #print("MID " + currentMID)
            #print("MSB " + currentMSB)
            #print("Position " + str(count + 1))

            # Get the current position
            currentPosition = currentMSB + currentMID + currentLSB
            currentPosition = int(currentPosition, 2)

            #print("")
            #print("Current Position: " + str(currentPosition))
            #print("Previous Position: " + str(previousPosition))

            if (currentPosition != previousPosition + 1):
                #print("Potential Mis-sequence")

                if (not(previousPosition == 7 and currentPosition == 0)):

                    # Maybe a mis-sequence unless first bit.
                    if (not(previousPosition == 8)):
                        # Not the first bit, error.
                        print("Current Position " + str(currentPosition))
                        print("Previous Position" + str(previousPosition))
                        print("Mis-sequence")
                        print(str(count))
                        sys.exit();
            
                else:
                    # Reached the end of the previous byte
                    print("%02x" % int(currentByte, 2), end="")
                    #print(currentByte, end="")

                    currentByte = ""

            # Get the data
            currentData = data[count]
            currentByte = currentData + currentByte

            previousPosition = currentPosition

        # if (count == 2000000):
        #     sys.exit()

        prevClock = clockMeasurement
        count += 1





main()
def main():  #define module
    iFile = open("JumbledMsg.txt", 'r')  #sets variable iFile to open txt file and set it to read

    oFile = open("MsgCGB.txt", 'w')  #sets variable oFile to create new txt file and set it to write

    msg = str(iFile.read())  #creates msg variable; sets iFile to read the text inside of file

    for num in msg:  #for loop to find numbers in msg
        if num in "01":  #if the numbers 0 or 1 are found in msg
            msg = msg.replace(num, "")  #replace those found numbers with "" (nothing)

    oFile.write(msg)  #writes the msg variable into new file we created

    oFile.close()  #closes that newly written file

main()  #runs main

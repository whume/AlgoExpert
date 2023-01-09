string = "aaaaaaaaaaaabbccccdd"

def runLengthEncoding(string):
    encodeStringCharacters = []
    currentRunLength = 1
    
    for i in range(1, len(string)):
        currentcharacter = string[i]
        previousCharacter = string[i -1]

        if currentcharacter != previousCharacter or currentRunLength == 9:
            encodeStringCharacters.append(str(currentRunLength))
            encodeStringCharacters.append(previousCharacter)
            currentRunLength = 0
        
        currentRunLength += 1
    encodeStringCharacters.append(str(currentRunLength))
    encodeStringCharacters.append(string[len(string) - 1])

    return "".join(encodeStringCharacters)

print(runLengthEncoding(string.capitalize()))
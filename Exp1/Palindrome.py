
checkString = input("Enter the string to be checke for Palindrome: ")

firstIndex = 0
lastIndex = len(checkString) - 1

while firstIndex <= lastIndex :

    if checkString[firstIndex] != checkString[lastIndex] :
          print(checkString + " is not a palindrome")
          break 

    firstIndex += 1
    lastIndex -= 1

if firstIndex > lastIndex :
        print(checkString + " is a palindrome")


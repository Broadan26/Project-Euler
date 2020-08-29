def isPalindrome(val_1, val_2):
    val_3 = val_1 * val_2   #Get product
    temp = val_3            #Temporary val_3 holder
    reverse = 0             #Reverse number

    while (val_3 > 0):                      #Go until val_3 is empty
        digit = val_3 % 10                  #Get last digit
        reverse = (reverse * 10) + digit    #Shift reverse, add new digit
        val_3 = val_3 // 10                 #Take floor of val_3 divided by 10

    if temp == reverse:                     #Check for palindrome
        return True
    else:
        return False

def Euler4OnlyRealSolution():
    val_1 = 100
    val_2 = 100
    largest_1 = 0
    largest_2 = 0
    largest_palindrome = -1

    while val_1 < 1000:                                     #Iterate for val_1
        while val_2 < 1000:                                 #Iterate for val_2
            if isPalindrome(val_1, val_2):                  #Check if palindrome
                if (val_1 * val_2) > largest_palindrome:
                    largest_palindrome = val_1 * val_2      #Store if larger
                    largest_1 = val_1
                    largest_2 = val_2
            val_2 = val_2 + 1
        val_1 = val_1 + 1
        val_2 = 100
    print('Largest Palindrome:', largest_palindrome, 'made from', largest_1, 'and', largest_2)

if __name__ == "__main__": #Driver
    Euler4OnlyRealSolution()
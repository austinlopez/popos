

def isPalindrome(num):
    test = str(num)
    final = ''
    for x in range(len(test)-1,-1,-1):
        final += test[x]
    if final == test:
        return True
    return False

def findLargestPalindrome():
    palindromes = []
    for x in range(2,1000):
        for y in range(2,1000):
            if isPalindrome(x*y):
                palindromes.append(x*y)
    return max(palindromes)

if __name__ == '__main__':
    print(findLargestPalindrome())
def palindrome(word):
    paland = word
    paland = paland[::-1]
    if word.lower() == paland.lower():
        print(f'{word}, is an palandrome')
    else:
        print(f'{word}, is not an palandrome') 

# Tests
palindrome("test")
palindrome("sus")
palindrome("subject")
palindrome("Able was I ere I saw Elba")
palindrome("1881")

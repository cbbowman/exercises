
# Implement an algorithm to determine if all characters in a string are unique. 
# What if you cannot use additional data structures?

# use an array of the character set
def is_unique1(str, char_set = 128):
    # edge case; zero length string
    if len(str) == 0:
        return True

    # if the string is longer than the possible characters
    if len(str) > char_set:
        return False
    
    # initialize an array for the character set
    char_array = [0]*char_set

    # set the value to True if a character is found
    for i in range(len(str)):
        val = ord(str[i])

        # if the character has already been found, return false
        if char_array[val]:
            return False
        else:
            char_array[val] = True

    # return true if no duplicates found
    return True

test1 = is_unique1("abcdeuigntf")==True
test2 = is_unique1("abcdxxef")==False
if test1 & test2:
    print("is_unique1 passed")
else:
    print("is_unique1 failed")

def is_unique2(str, char_set = 128):
    if len(str) == 0:
        return True
        
    if len(str) > char_set:
        return False

    checker = bool(0)

    for i in range(0, len(str)):
        val = ord(str[i]) - ord("a")
        if checker & (bool(1) << val):
            return False
        else:
            checker |= (1 << val)

    return True    
    

test1 = is_unique2("abcdeuigntf")==True
test2 = is_unique2("abcxdxef")==False
if test1 & test2:
    print("is_unique2 passed")
else:
    print("is_unique2 failed")


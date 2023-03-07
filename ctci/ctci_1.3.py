# Write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient space the end to hold the additional characters, and that you are given the "true" length of the string. 

# edit from end working backwards
def urlify(str, true_length):
    # edge case: empty string
    if true_length == 0:
        return ""

    #count the number of spaces
    spaces = count_of_char(str, 0, true_length, " ")

    # check if the arguments are correct
    if len(str) != true_length + (2 * spaces):
        return "Bad input"
    
    #set the index at the back of the string
    new_index = true_length - 1 + (spaces * 2)

    l = list(str)

    for i in range(true_length-1, -1, -1):
        if l[i] == ' ':
            l[new_index] = "0"
            l[new_index - 1] = "2"
            l[new_index - 2] = "%"
            new_index -= 3
        else:
            l[new_index] = l[i]
            new_index -= 1

    return "".join(l)

# count spaces in the string
def count_of_char(str, start, end, target):
    count = 0
    l = list(str)
    for i in range(start, end):
        if l[i] == target:
            count += 1
    return count
    

test1 = urlify("a 3  ", 3)=="a%203"
test2 = urlify(" 45sdf  ", 6)=="%2045sdf"
if test1 & test2:
    print("urlify passed")
else:
    print("urlify failed")

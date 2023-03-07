def main():
<<<<<<< HEAD
    # test0 = addBinary("1010","1011") == "10101"
    test1 = addBinary("11","1") == "100"

    # print(addBinary("1010","1011"))
    print(test1)

def addBinary(a, b):
    if a == "" or b == "":
        return a + b
    
    i = 1
    len_a = len(a)
    len_b = len(b)
    carry = 0
    result = ""

    while i <= len_a and i <= len_b:
        sum = int(a[-i]) + int(b[-i]) + carry
        print([i,sum])
        if sum < 2:
            result = str(sum) + result
            carry = 0
        else:
            carry = 1
            result = str(sum-2) + result
        print(result)
        i += 1

    if len_b > len_a:
        while i < len_b:
            sum = int(b[-i]) + carry
            if sum < 2:
                result = str(sum) + result
            else:
                carry = 1
                result = "0" + result
            print(result)
            i += 1

    else:
        while i < len_a:
            sum = int(a[-i]) + carry
            if sum < 2:
                result = str(sum) + result
            else:
                carry = 1
                result = "0" + result
            print(result)
            i += 1

    if carry == 1:
        result = "1" + result

    return result
=======
    test1 = addBinary("1010", "1011") == "10101"
    test2 = addBinary("1", "11") == "100"

    print(test1)
    print(test2)

def addBinary(a, b):
        i = 1
        carry = 0
        
        len_a = len(a)
        len_b = len(b)
        c = ""
        
        while i <= len_a and i <= len_b:
            sum = carry + int(a[-i]) + int(b[-i])
            if sum > 1:
                carry = 1
                c = str(sum - 2) + c
            else:
                carry = 0
                c = str(sum) + c
            i += 1
                
        if i > len_a:
            longer = b
            m = len_b
        else:
            longer = a
            m = len_a
        
        while i <= m:
            sum = carry + int(longer[-i])
            if sum > 1:
                carry = 1
                c = str(sum - 2) + c
            else:
                carry = 0
                c = str(sum) + c
            i += 1
        
        if carry == 1:
            c = str(1) + c
        
        return c
>>>>>>> 8194675644e179b585f35999cf502a156adef4cf

if __name__ == "__main__":
    main()
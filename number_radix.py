#!/usr/bin/python

def checkio(str_number, radix):
    answer = 0 
    powers_list = [radix**y for y in range(0,10)]
    for i in range(0,len(str_number)):
        if str_number[len(str_number)-i-1].isalpha():
            if (ord(str_number[len(str_number)-i-1]) - 55) >= powers_list[1] : return -1
            sum =((ord(str_number[len(str_number)-i-1]) - 55) * powers_list[i])
        else:
            if int(str_number[len(str_number)-i-1]) >= powers_list[1]: return -1
            sum = int(str_number[len(str_number)-i-1]) * powers_list[i]
        answer += sum
    if answer == 0: return -1
    return answer 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
    assert checkio("909", 9) == -1, "last one"

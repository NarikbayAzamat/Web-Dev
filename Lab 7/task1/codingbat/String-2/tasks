#double_char
def double_char(str):
    result = ""
    for c in str:
        result += c * 2
    return result

#count_code
def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
            count += 1
    return count

#count_hi
def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == "hi":
            count += 1
    return count

#end_other
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

#cat_dog
def cat_dog(str):
    return str.count("cat") == str.count("dog")

#xyz_there
def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz" and (i == 0 or str[i-1] != '.'):
            return True
    return False
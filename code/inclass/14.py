def find(text, pattern):
    """Implementation of find method

    >>> find("good moorning", "od")
    2
    >>> find("good moorning", "odd")
    -1
    """

    cnt = 0
    for i in text:
        flag = False
        if i == pattern[0]:
            flag = True
            j = cnt + 1
            for p in pattern[1:]:
                if j >= len(text) or text[j] != p:
                    flag = False
                    break
                j += 1
        if flag:
            return cnt
        cnt += 1
    return -1


# for i in range(2, 10, 2):
#     print(i)
# 
# cdn = "hour"

# if cdn[1:2] == "o":
#     print("Equal")
# 
# if cdn[1:-1] == "our":
#     print("Equal")
# else:
#     print("No equal")
# 
# print(cdn[::2])
# 
# cdn[-4::3]
# 
# cdn = "hour"
# if cdn == "hour ":
#     print("Equal")
# else:
#     print("No equal")
# 
# 
# if cdn > " Hour":
#     print("Greater")
# 

def find2(cdn, pattern, case_sensitive=True):
    if case_sensitive:
        print("case_se", cdn, pattern)
        return find(cdn, pattern)
    return find(cdn.lower(), pattern.lower())

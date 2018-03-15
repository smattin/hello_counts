# function that counts the number of occurences of each character in a string
# 'hello' -> 'h' - 1; 'e' - 1; 'l' - 2; 'o' - 1

done =[]
def counts(s):
    for c in s:
        if c not in done:
            print("{} -> {}".format(c,nchar(c,s)))

def nchar(c,s):
    cs = ""
    for i in s:
        if i == c:
            cs.append(c)
    return len(cs)
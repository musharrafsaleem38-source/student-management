string = input("enter string :")

vowel = 0
constant = 0

length = len(string)
print("lnegth of string", length)

for ch in string.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowel +=1
            
        else:
            constant += 1
            
print(f"there are {vowel} vowel  and {constant} constant in latter")
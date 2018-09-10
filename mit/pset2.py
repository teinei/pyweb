# eg string s
s = 'azcbobobegghakl'
# copy from this line
# Paste your code into this box 
subAl = ""
for i in range(0,len(s)):
    currChar = s[i:i+3]
    if (currChar == 'bob'):
        nBob += 1
print("Longest substring in alphabetical order is: "+str(subAl))
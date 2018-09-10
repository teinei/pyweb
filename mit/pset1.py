# Paste your code into this box 
s = 'azcbobobegghakl'
nVowels = 0
for currChar in s:
    if(currChar == 'a' or currChar == 'e' or currChar == 'i' or currChar == 'o' or currChar == 'u'):
        nVowels += 1
print("Number of vowels: "+str(nVowels))
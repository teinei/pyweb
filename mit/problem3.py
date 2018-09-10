s = 'abcdefghijklmnopqrstuvwxyz' # s[0:len(s)] is longest
s = 'zyxwvutsrqponmlkjihgfedcba' # s[0] is longest
s = 'sxgjbouktskpslxtoz'
s = 'qjulokgwfvymo'
s = 'tecyuagxhijydclcywr'
s = 'hlvjvmklzddokvukyoxa'
#s = 'zyxwvutsrqponmlkjihgfedcba'

lss='' # longest string
css='' # current sub string
# update i inside loop
for i in range(1,len(s)):
    # update i inside loop
    prevChar = s[i-1] # previous char of s
    prevCharOrd = ord(prevChar) # the int value of previous char
    currChar = s[i] # current char
    currCharOrd = ord(currChar) # current char int value
    # difference between current char ord and prev Char ord
    dcp = currCharOrd - prevCharOrd 
    b = dcp > 0 or dcp == 0
    #
    if(b): # in alpabet order
        if (css == ''):
            css = s[i-1]
        css += s[i]        #
    else: # dcp < 0, currentChar < prevChar
        css = s[i-1]
        if (len(css)>len(lss)): # if currentSubString is longer
            lss = css # longestSubString is currentSubString
        css='' #currentSubString is ended
    if (len(css)>len(lss)): 
        lss = css
print("Longest substring in alphabetical order is: "+lss)
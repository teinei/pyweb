lss='' # longest string
css='' # current sub string

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

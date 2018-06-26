#s='azcbobobegghakl'
s='abcbcd'
temp,largest_temp,largest='','',''
temp2=s[-1]
for i in range(len(s)):
    
    if i==len(s)-1 and s[i]<=temp2:
        temp+=s[i]
        largest_temp=temp
        temp=''
    elif s[i]<=s[i+1]:
         temp+=s[i]
    else:
        temp+=s[i]
        largest_temp=temp
        temp=''
    if (len(largest_temp)>len(largest)):
        largest=largest_temp
        
print ("Longest substring in alphabetical order is:"+str(largest))


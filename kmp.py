import sys
#This is a program to implement the KMP string matching algorithm
lps=[]
def calculate_lps(pattern,lps):
    length=0
    i=1
    lps[0]=0
    while(i<len(pattern)):
        if(pattern[i]==pattern[length]):
            print 'First and last character match'
            length+=1
            lps[i]=length
            i+=1
        else:
            if(length!=0):
                print 'Characters do not match and length is not 0'
                length=lps[length-1]
            else:
                print 'Characters match and length is 0'
                lps[i]=length
                i+=1
    return;
text=raw_input('Enter the main text: ')
pat=raw_input('Enter the pattern to search: ')

lps=[None]*len(pat)
print 'Checking inputs please wait...'
if(len(text)<len(pat)):
    print 'Your inputs are not valid. Text should be larger than pattern. Please try again.'
    sys.exit()
else:
    print 'done, inputs are valid. Calculating lps array[]...'
    j=0
    calculate_lps(pat,lps)
    i=0
    while(i<len(text)):
        if(pat[j]==text[i]):
            i+=1
            j+=1
        if(j==len(pat)):
            print 'Found pattern at position: ',i-j
            j=lps[j-1]
        elif (i<len(text) and (text[i]!=pat[j])):
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1
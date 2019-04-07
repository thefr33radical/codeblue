import PyPDF2
import codecs
import sys

fp = open("/home/alienware/Downloads/All_MOUs.pdf","rb")
data = PyPDF2.PdfFileReader(fp)
#page = data.getPage(752)
#print(page.extractText())
fp.close()

"1360 Office Services Assistant 1763 36,811-45,748"
# ID and title name
import re

txt='1360 Office Services Assistant 1763 36,811-45,748'

re1='(\\d+)'	# Integer Number 1
re2='(\\s+)'	# White Space 1
re3='((?:[a-z][a-z]+))'	# Word 1
re4='(\\s+)'	# White Space 2
re5='((?:[a-z][a-z]+))'	# Word 2
re6='(\\s+)'	# White Space 3
re7='((?:[a-z][a-z]+))'	# Word 3
re8='(\\s+)'	# White Space 4

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    int1=m.group(1)
    ws1=m.group(2)
    word1=m.group(3)
    ws2=m.group(4)
    word2=m.group(5)
    ws3=m.group(6)
    word3=m.group(7)
    ws4=m.group(8)
    print ("("+int1+")"+"("+ws1+")"+"("+word1+")"+"("+ws2+")"+"("+word2+")"+"("+ws3+")"+"("+word3+")"+"("+ws4+")"+"\n")

# salary
import re

txt='1360 Office Services Assistant 1763 36,811-45,748'

re1='.*?'	# Non-greedy match on filler
re2='\\s+'	# Uninteresting: ws
re3='.*?'	# Non-greedy match on filler
re4='\\s+'	# Uninteresting: ws
re5='.*?'	# Non-greedy match on filler
re6='\\s+'	# Uninteresting: ws
re7='.*?'	# Non-greedy match on filler
re8='\\s+'	# Uninteresting: ws
re9='.*?'	# Non-greedy match on filler
re10='(\\s+)'	# White Space 1
re11='(\\d+)'	# Integer Number 1
re12='(.)'	# Any Single Character 1
re13='(\\d+)'	# Integer Number 2

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    ws1=m.group(1)
    int1=m.group(2)
    c1=m.group(3)
    int2=m.group(4)
    print("("+ws1+")"+"("+int1+")"+"("+c1+")"+"("+int2+")"+"\n")

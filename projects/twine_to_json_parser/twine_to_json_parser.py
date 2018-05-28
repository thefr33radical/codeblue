'''
Code used to convert files that are output of the Twine software to formatted json objects
 '''
import re
import xml.etree.ElementTree as et
import json
from json import dump

##open raw twine html file

##file_name=raw_input("Enter file name (file needs to be in same directory):")

#input a sample twine test file 
with open("xyz.html") as file:
    raw_html=file.read()
    
#convert raw html to string type
raw=str(raw_html)

##Read only part of file thats necessary

start="<tw-storydata"
end="</tw-storydata>"

x=re.compile(r'%s.*?%s'%(start,end),re.S)
parsed_html=x.search(raw).group(0)

#There is word called hidden that troubles  the xml parser, so it needs to be removed.
parsed_html=parsed_html.replace(r"hidden","")
#print parsed_html

with open("twine.xml","w+") as file:
    file.write(parsed_html)
    file.close()
       
output_json=dict()
output_json={'text':[],'label':{},'actions':{'type':{},'response':{},'payload':{} }}


#open xml file and parse 0r use parsed_html----------->delete hidden in tw-storydata

arr_txt=[]
arr_txt2=[]

data=et.parse('twine.xml')
root=data.getroot()

#print root[0].attrib


with open("output_parser.json", 'w+') as f:
            #print json.dumps(output_json)
            #dump(output_json, f, indent=4)
            f.write("[")#####
            f.close()

for i in root.iter('tw-passagedata'):
    #print i.attrib
    output_json['label']=i.attrib['name']
    
    temp=i.text
    temp=str(temp)
    trigger_count=0
    ans_count=0
    #print temp
    #print output_json['text']
    
    if temp is not None:
        arr_txt=temp.split("\n")
       # print arr_txt
        #
        for j in arr_txt:
            x=0
            if j is not None:
                response=re.search(r'\[\[(.*)\|',j)
                if response:
                    #print "Answer matched expression =",response.group(1)
                    output_json['actions']["response"]=response.group(1)
                    ans_count=1
                    #print output_json['actions']["response"]
                
                #Extract Trigger                                
                trigger=re.search(r'\|(.*)\]\]',j)
                if trigger:
                    #print "Trigger matched expression =",trigger.group(1)
                    output_json['actions']["payload"]=trigger.group(1)
                    trigger_count=1
                    #print output_json['actions']["payload"]
                    
                # elif trigger_count==1|ans_count==1:
                #    output_json['actions']["ty"]
                    
                else:
                    random=j.split(",")
                    for z in random:
                        if z!='':
                            #print "split words",z
                        
                            pattern1=re.search(r'"(.*)"',z)
                            pattern2=re.search(r'\\(.*)',z)
                            
                            if pattern1:
                                #print "pattern1",pattern1.group(1)
                                output_json["text"].append(pattern1.group(1))
                                x=1
                                break
                            
                            elif pattern2:
                                 #print "pattern2",output_json["text"].append(pattern2.group(1))
                                 output_json["text"].append(pattern2.group(1))
                                 break
                        
                    if (z!=""):
                        if(x!=1):
                            output_json["text"].append(j)
                    
        output_json['actions']["type"]="postback"
        # output_json
        print output_json
        with open("output_parser.json", 'a') as f:
            #print json.dumps(output_json)
            dump(output_json, f, indent=4)
            f.write(",")
            
            f.close()
    output_json={'text':[],'label':{},'actions':{'type':{},'response':{},'payload':{} }}
   

with open("output_parser.json", 'a+') as f:
            #print json.dumps(output_json)
            #dump(output_json, f, indent=4)
            f.write("]")
            
            f.close()
    
#print output_json
    
    
    
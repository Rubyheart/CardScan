import os, json
from mtgsdk import Card
text = input("Please enter text: ")
print(f"You have entered \"{text}\" word to search.")
current_path = os.getcwd()
current_path
path = '/home/scott/Documents/CardScan/json/AllSetFiles(1)'
path
os.chdir(path) # Change the current working directory to specified path.
default = 'default.json'
os.listdir(path='.')

def lookUp(text):
    with open('default.json') as f:
        if text in f.read():
            print("true lookup")

def searchText(path):
    
    os.chdir(path)
    files = os.listdir()
    global foundeffect, setfound
    setfile = 'set'
    effect = 'effect'
    #foundeffect = ''
    #setfound = ''
    #print(files)
    for file_name in files:
        #print(file_name)
        abs_path = os.path.abspath(file_name)
        #print("Absolute path of the file: ", abs_path)
        with open(file_name, "r") as file:
            data = json.load(file) 
            #print(data)
            for i in data['data']['cards']:
                #if foundeffect != None:
                #print(i)
                    if i['name'] == text:
                    #break
                        print(i['text'])
                        print("File: ", abs_path)
                    #continue
                        global foundeffect
                        global setfound
                        setfile = ("You have entered " + abs_path + " to search.")
                        effect = i['text']
                    #print(setfile)
                        #setfound = setfile
                        #foundeffect = effect
                    #print(effect)
                    #continue
                        #break
                #break
                    #continue
            #continue
            #break
            #pass
            #break
            #print(effect)
            #foundeffect = effect
            #print(foundeffect)
        
        if os.path.isdir(abs_path):
            searchText(abs_path)
pass
#searchText(path)
#lookUp(text)

if lookUp(text):
    with open(default, "r") as file:
        
        data = json.load(file)
        print (data['data']['cards'][text]['text'])
else:
    searchText(path)
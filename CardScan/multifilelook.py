import os, json
text = input("Please enter text: ")
print(f"You have entered \"{text}\" word to search.")
current_path = os.getcwd()
path = current_path+'/json/AllSetFiles(1)'
global foundeffect, setfile
setfile = "set"
foundeffect = 'temp'
effect = "effect"


def searchText(path):

    files = os.listdir(path)
    global foundeffect, setfound
    setfile = 'set'
    effect = 'effect'
  
    for file_name in files:
        file_path = f'{path}/{file_name}'
        abs_path = os.path.abspath(file_path)
        
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file) 
            #print(data)
            for i in data['data']['cards']:
                
                    if i['name'].lower() == text.lower():
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
searchText(path)
print(effect)
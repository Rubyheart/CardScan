import os, json




def searchText(path):
    
    files = os.listdir(path)
    text = input("Please enter a card name: ")
    print(f"Searching for {text}.")
    sets = []
    global lastCard
  
    for file_name in files:
        file_path = f'{path}/{file_name}'
        abs_path = os.path.abspath(file_path)
        
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file) 
            for i in data['data']['cards']:
                
                    if i['name'].lower() == text.lower():
                        set = os.path.splitext(os.path.basename(abs_path))[0]
                        sets.append(set)
                        lastCard = i

    if 10 > len(sets) > 0:
         print(f'{text} appears in {len(sets)} sets', sets, "\n")
         print(lastCard['text'])
    
    elif 10 < len(sets) > 0:
         print(f'{text} appears in {len(sets)} sets', "\n")
         print(lastCard['text'])
    else:
         print('No matches found.')
         
    

if __name__ == "__main__":
     current_path = os.getcwd()
     path = current_path+'/json/AllSetFiles(1)'
     searchText(path)
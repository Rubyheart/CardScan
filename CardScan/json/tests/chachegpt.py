import json
import os
search_text = input("Please enter text: ")

def search_text_in_json(filename, search_text):
    # Check if the search text is present in the default.json file
    with open(filename, 'r') as file:
        data = json.load(file)
        #for i in data['data']['cards']:
            #print(i)
        for i in data['data']['cards']:
            print(i['name'])
            #for i in data['cards']['name']:
             #   print(i)
            #if i['data']['cards'] and i['data']['cards']['name'] == search_text:
                #return i['text']
    
    # If the search text is not found, loop through the list of files
    files = ['CMM.json', 'default.json', 'PMH1.json']  # Replace with your list of files
    for file in files:
        with open(file, 'r') as file:
            data = json.load(file)
            for item in data:
                if 'text' in item and item['text'] == search_text:
                    # Add the matching item to default.json
                    with open(filename, 'a') as default_file:
                        json.dump(item, default_file)
                        default_file.write('\n')
                    return item['text']
    
    # If no match is found, return None
    return None

# Usage example
searched_text = "example text"
result = search_text_in_json('default.json', searched_text)
if result:
    print(f"Found match in default.json: {result}")
else:
    print(f"No match found in default.json. Searching other files...")

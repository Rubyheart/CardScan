import json
import os

def search_card_text(filename, card_name, default_filename):
    # Check if the card name is present in the specified JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
        cards = data['data']['cards']
        for card in cards:
            if card['name'] == card_name:
                return card['text']
    
    # If the card name is not found, search through all files in a folder
    folder_path = '/home/scott/Documents/CardScan/json/AllSetFiles(1)'  # Replace with the path to your folder containing card files
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
            cards = data['data']['cards']
            for card in cards:
                if card['name'] == card_name:
                    # Add the matching card to the default JSON file
                    with open(default_filename, 'r+') as default_file:
                        default_data = json.load(default_file)
                        default_data['data']['cards'].append(card)
                        default_file.seek(0)
                        json.dump(default_data, default_file, indent=4)
                        default_file.truncate()
                    return card['text']
    
    # If no match is found, return None
    return None

# Usage example
card_name = input("Please enter text: ")
json_file_path = "/home/scott/Documents/CardScan/json/tests/default.json"
default_json_path = "/home/scott/Documents/CardScan/json/tests/default.json"  # Replace with the path to your default JSON file
result = search_card_text(json_file_path, card_name, default_json_path)
if result:
    print(f"Found match for {card_name} in {json_file_path}: {result}")
    print("\n" + result)
else:
    folder_path = '/home/scott/Documents/CardScan/json/AllSetFiles(1)'  # Replace with the path to your folder containing card files
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        result = search_card_text(file_path, card_name, default_json_path)
        if result:
            print(f"Found match for {card_name} in {file_path}: {result}")
            break
    else:
        print(f"No match found for {card_name} in {json_file_path} and other files in {folder_path}.")

import json
import os

def search_card_text(filename, card_name):
    # Check if the card name is present in the specified JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
        cards = data['data']['cards']
        for card in cards:
            if card['name'] == card_name:
                return card['text']
    
    # If the card name is not found, return None
    return None

# Usage example
card_name = "Morophon, the Boundless"
json_file_path = "/home/scott/Documents/CardScan/json/tests/PMH1.json"
result = search_card_text(json_file_path, card_name)
if result:
    print(f"Found match for {card_name} in {json_file_path}: {result}")
else:
    print(f"No match found for {card_name} in {json_file_path}.")

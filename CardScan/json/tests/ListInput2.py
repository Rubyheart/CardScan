import json
import subprocess
from runtest import *

def save_card_data(card_data):
    with open('card_data.json', 'w') as file:
        json.dump(card_data, file, indent=4)

def load_card_data():
    try:
        with open('card_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def process_card(card_name):
    # Call your other program or function here, passing the card name as an argument
    subprocess.run(['python', 'runtest.py', card_name])

def main():
    card_data = load_card_data()

    while True:
        card_name = input('Enter a card name (or "quit" to exit): ')
        if card_name == 'quit':
            break

        if card_name in card_data:
            card_data[card_name] += 1
        else:
            card_data[card_name] = 1

        process_card(card_name)

    save_card_data(card_data)

    num_unique_cards = len(card_data)
    num_duplicates = sum(card_data.values()) - num_unique_cards

    print(f"Number of unique cards: {num_unique_cards}")
    print(f"Number of duplicates: {num_duplicates}")

if __name__ == '__main__':
    main()

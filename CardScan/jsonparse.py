def print_json_params(json_obj, indent=""):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            print(f"{indent}{key}:")
            print_json_params(value, indent + "  ")
    elif isinstance(json_obj, list):
        for item in json_obj:
            print_json_params(item, indent + "  ")
    else:
        print(f"{indent}{json_obj}")
        
        
import json

# Open the JON file
with open('./CompiledList.json') as file:
    # Load the JSON data
    json_data = json.load(file)
    
    # Print all parameters
    print_json_params(json_data)
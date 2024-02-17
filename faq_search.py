import json

def search_and_return_id(json_data, search_string):
    # Iterate over the list of FAQ items in the json_data under the key 'faqs'
    for item in json_data['faqs']:  # Access the list via json_data['faqs']
        if 'ID' in item and 'question' in item:  # Check if both 'ID' and 'question' keys exist
            if search_string in item['question']:  # Look for search_string within 'question'
                return item['ID']  # Return the 'ID' if a match is found

    return "No match found."

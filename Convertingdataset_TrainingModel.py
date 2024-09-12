import json
import spacy
from spacy.training import Example

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
        return None

def create_training_data(data):
    training_data = []
    for item in data:
        text = item['resume_text']
        name = item['name']
        start_idx = text.find(name)
        if start_idx != -1:
            end_idx = start_idx + len(name)
            annotations = {'entities': [(start_idx, end_idx, 'NAME')]}
            training_data.append((text, annotations))
        else:
            print(f"Name '{name}' not found in the text.")
    return training_data

def main():
    data = load_data('/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/dataset.json')
    if data is not None:
        training_data = create_training_data(data)
        with open('/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/training_data.json', 'w') as f:
            json.dump(training_data, f)
        print("Training data created successfully.")
    else:
        print("Failed to load data.")

if __name__ == '__main__':
    main()
import json
import spacy
from spacy.training import Example
import os

# Load SpaCy's pre-trained model for English
nlp = spacy.blank("en")

# Add the NER component to the pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Add labels for the entities
ner.add_label("NAME")
ner.add_label("ORG")

# Load the training data
def load_training_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            print(f"Loaded training data: {data[:2]}")  # Print first 2 items for debugging
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
        return None

def train_model(training_data):
    # Initialize the optimizer
    optimizer = nlp.begin_training()
    
    for epoch in range(20):  # Increase the number of training epochs
        print(f"Starting epoch {epoch + 1}")
        for i, item in enumerate(training_data):
            text = item['resume_text']
            annotations = {'entities': item['entities']}
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.35, sgd=optimizer)  # Adjust dropout rate
            
            # Print progress every 1000 samples
            if (i + 1) % 1000 == 0:
                print(f"Processed {i + 1} samples in epoch {epoch + 1}")
        
        # Save the model after each epoch
        model_path = os.path.join("/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File", f"ner_model_epoch_{epoch + 1}")
        nlp.to_disk(model_path)
        print(f"Model saved after epoch {epoch + 1} at {model_path}")
    
    print("Model training complete and saved to disk.")

def main():
    training_data = load_training_data('/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/synthetic_training_data_with_prefixes_suffixes.json')
    if training_data is not None:
        train_model(training_data)
        print("Model trained and saved successfully.")
    else:
        print("Failed to load training data.")

if __name__ == '__main__':
    main()
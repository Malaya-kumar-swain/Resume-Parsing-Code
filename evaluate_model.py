import spacy
import json
from spacy.training import Example, offsets_to_biluo_tags
from spacy.scorer import Scorer

# Load the trained model
nlp = spacy.load("/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/ner_model_epoch_20")

# Load the validation data
def load_validation_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
        return None

def evaluate_model(nlp, validation_data):
    examples = []
    for item in validation_data:
        text = item['resume_text']
        entities = item['entities']
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, {"entities": entities})
        examples.append(example)
    
    scorer = Scorer()
    scores = scorer.score(examples)
    return scores

# Load validation data
validation_data = load_validation_data("/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/validation_data.json")

if validation_data:
    # Evaluate the model
    scores = evaluate_model(nlp, validation_data)
    print("Overall Metrics:")
    print(f"Token Accuracy: {scores['token_acc']}")
    print(f"Token Precision: {scores['token_p']}")
    print(f"Token Recall: {scores['token_r']}")
    print(f"Token F1 Score: {scores['token_f']}")
    print(f"Entity Precision: {scores['ents_p']}")
    print(f"Entity Recall: {scores['ents_r']}")
    print(f"Entity F1 Score: {scores['ents_f']}")
    print("Entity Metrics per Type:")
    for entity_type, metrics in scores['ents_per_type'].items():
        print(f"Entity Type: {entity_type}")
        print(f"  Precision: {metrics['p']}")
        print(f"  Recall: {metrics['r']}")
        print(f"  F1 Score: {metrics['f']}")
    print(f"Processing Speed: {scores.get('speed', 'N/A')} tokens per second")

    # Print model predictions for each text
    for item in validation_data:
        text = item['resume_text']
        doc = nlp(text)
        print(f"\nText: {text}")
        print("Entities:")
        for ent in doc.ents:
            print(f"  {ent.text} ({ent.label_})")
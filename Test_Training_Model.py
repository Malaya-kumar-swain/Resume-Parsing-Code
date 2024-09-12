import spacy

# Load the trained model
nlp = spacy.load("ner_model")

def test_model(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.label_)

if __name__ == "__main__":
    # List of test texts
    test_texts = [
        "John Doe is a software engineer at Google.",
        "Jane Smith works at Microsoft.",
        "Alice Johnson is a data scientist.",
        "Bob Brown is a project manager at Amazon."
    ]
    
    for text in test_texts:
        print(f"Testing text: {text}")
        test_model(text)
        print("-" * 40)
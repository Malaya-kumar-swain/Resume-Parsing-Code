import json

# Load the generated training data
with open('/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/synthetic_training_data_with_prefixes_suffixes.json', 'r') as f:
    training_data = json.load(f)

# Print a few samples to verify
for sample in training_data[:5]:
    print(json.dumps(sample, indent=4))
import json
import random
import spacy
from spacy.training import offsets_to_biluo_tags

# Sample names and organizations
names = [
    "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Robert Brown",
    "Alice Johnson", "Samuel Carter", "Jessica Lee", "Brian Harris", "Laura Wilson",
    "John A. Doe", "Robert A. Smith", "Marie Curie", "Thomas Anderson", "Lisa Adams",
    "James Brown", "Alexander Hamilton", "Sofia Martinez", "Oliver Twist", "Daniel Craig",
    "Natalie Portman", "James Bond", "Rachel Green", "William Shakespeare", "George Orwell",
    "Leonardo da Vinci", "Albert Einstein", "Ada Lovelace", "Charles Darwin", "Nikola Tesla",
    "Thomas Edison", "Florence Nightingale", "Steve Jobs"
]

# Organizations to add context for the data
organizations = [
    "Google", "Microsoft", "Amazon", "Facebook", "Apple", "IBM", "Intel", "Oracle", "Salesforce",
    "Adobe", "Netflix", "Spotify", "Twitter", "LinkedIn", "Snapchat", "Pinterest", "Reddit",
    "Dropbox", "Slack", "Zoom", "Uber", "Lyft", "Airbnb", "Tesla", "SpaceX", "Nvidia", "AMD",
    "Qualcomm", "Cisco", "HP", "Dell", "Lenovo", "Samsung", "LG", "Sony", "Panasonic", "Philips"
]

# Prefixes and suffixes to simulate issues in names
prefixes = [
    "Sr.", "Mr.", "Ms.", "Dr.", "Mrs.", "Prof.", "Eng.", "Technical Architect", "18", "Date", "Name", "Recruiter"
]
suffixes = [
    "PhD", "Sr.", "Jr.", "II", "III", "MSc", "Esq", "18", "CEO", "Recruiter", "Manager", "Analyst"
]

# Function to generate random training data with prefixes and suffixes
def generate_training_data(num_samples):
    nlp = spacy.blank("en")  # Load a blank English model
    training_data = []
    misaligned_count = 0
    
    for _ in range(num_samples):
        name = random.choice(names)
        org = random.choice(organizations)
        
        # Randomly apply a prefix and/or suffix
        if random.random() > 0.5:
            name = random.choice(prefixes) + " " + name
        if random.random() > 0.5:
            name = name + " " + random.choice(suffixes)
        
        # Generate different scenarios
        scenarios = [
            f"{name} is a software engineer at {org}.",
            f"{name} works at {org}.",
            f"{name} is employed by {org}.",
            f"{name} is a part of {org}.",
            f"{name} is a team member at {org}.",
            f"{name} is a project manager at {org}.",
            f"{name} is a data scientist at {org}.",
            f"{name} is a senior developer at {org}.",
            f"{name} is a technical lead at {org}.",
            f"{name} is a consultant at {org}.",
        ]
        
        text = random.choice(scenarios)
        
        # Find the start and end positions of the name and org for annotation
        name_start = text.find(name)
        name_end = name_start + len(name)
        org_start = text.find(org)
        org_end = org_start + len(org)
        
        # Ensure no overlapping entities
        if name_end <= org_start or org_end <= name_start:
            entities = [(name_start, name_end, "NAME"), (org_start, org_end, "ORG")]
            
            # Check alignment
            doc = nlp.make_doc(text)
            try:
                tags = offsets_to_biluo_tags(doc, entities)
                if '-' not in tags:  # Ensure no misaligned entities
                    training_data.append({"resume_text": text, "entities": entities})
                else:
                    misaligned_count += 1
                    print(f"Misaligned entity found: {text} with entities {entities}")
            except ValueError:
                misaligned_count += 1
                print(f"ValueError for misaligned entity in: {text}")
    
    print(f"Total misaligned entities skipped: {misaligned_count}")
    return training_data

# Generate 10,000 samples
training_data = generate_training_data(10000)

# Save to JSON file
with open('/Users/malayakumarswain/Desktop/AppTad/Python_Project/Python_File/synthetic_training_data_with_prefixes_suffixes.json', 'w') as f:
    json.dump(training_data, f, indent=4)

print("Synthetic training data with prefixes and suffixes generated and saved.")
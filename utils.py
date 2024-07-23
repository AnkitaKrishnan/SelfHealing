import re
import pandas as pd

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text

def create_meta(description, pool_of_words):
    description = preprocess_text(description)
    words = description.split()
    matched_words = [word for word in words if word in pool_of_words]
    return ' '.join(set(matched_words))

def load_data():
    kb_df = pd.read_csv('data/kb_data.csv')
    incident_df = pd.read_csv('data/incident_data.csv')
    
    kb_df['meta'] = kb_df['meta'].apply(preprocess_text)
    
    pool_of_words = set()
    for meta in kb_df['meta']:
        pool_of_words.update(meta.split())
    
    incident_df['meta'] = incident_df['description'].apply(lambda x: create_meta(x, pool_of_words))
    
    return kb_df, incident_df, pool_of_words

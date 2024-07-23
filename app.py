from flask import Flask, request, jsonify
import torch
from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils import preprocess_text, create_meta, load_data

app = Flask(__name__)

# Load data and pre-trained BERT model and tokenizer
kb_df, incident_df, pool_of_words = load_data()
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

def get_embeddings(text_list):
    inputs = tokenizer(text_list, return_tensors='pt', padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

# Generate embeddings for kb_df meta column
kb_embeddings = get_embeddings(kb_df['meta'].tolist())

@app.route('/get_kb', methods=['POST'])
def get_kb():
    data = request.json
    incident_number = data['incident_number']
    description = data['description']
    
    meta = create_meta(description, pool_of_words)
    input_embedding = get_embeddings([meta])
    
    similarities = cosine_similarity(input_embedding, kb_embeddings)
    max_sim_index = np.argmax(similarities, axis=1)[0]
    matched_kb_number = kb_df.iloc[max_sim_index]['kb_number']
    
    return jsonify({'incident_number': incident_number, 'kb_number': matched_kb_number})

if __name__ == '__main__':
    app.run(debug=True)

import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the JSON data obtained from the Scrapy crawler
with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract URLs and content from the JSON data
urls = [item['url'] for item in data]
contents = [item['content'] for item in data]

# Step 1: Text Vectorization with TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(contents)

# Step 2: Calculate Cosine Similarity
cosine_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 3: Construct the Inverted Index
inverted_index = {
    'urls': urls,
    'tfidf_matrix': tfidf_matrix,
    'cosine_sim_matrix': cosine_sim_matrix,
    'vectorizer_vocabulary': vectorizer.vocabulary_,
    'vectorizer_stop_words': list(vectorizer.stop_words_)  # Convert set to list
}

# Step 4: Save the Inverted Index in pickle format
with open('inverted_index.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)

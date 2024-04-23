from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the inverted index from the pickle file
with open('inverted_index.pkl', 'rb') as f:
    inverted_index = pickle.load(f)

urls = inverted_index['urls']
tfidf_matrix = inverted_index['tfidf_matrix']
cosine_sim_matrix = inverted_index['cosine_sim_matrix']
vectorizer_vocabulary = inverted_index['vectorizer_vocabulary']

# Route for handling queries
@app.route('/query', methods=['POST'])
def query():
    query_text = request.form.get('query', '').lower()
    if not query_text:
        return jsonify({'error': 'Empty query'})

    # Vectorize the query text using the same vectorizer
    query_vectorizer = TfidfVectorizer(vocabulary=vectorizer_vocabulary)
    query_tfidf_matrix = query_vectorizer.fit_transform([query_text])

    # Calculate cosine similarity between query vector and document vectors
    query_cosine_similarities = cosine_similarity(query_tfidf_matrix, tfidf_matrix)[0]

    # Sort the results based on cosine similarity scores
    sorted_indices = query_cosine_similarities.argsort()[::-1]

    # Get top-K results (here, we are getting top 10 results)
    top_k = 10
    results = [{'url': urls[idx], 'score': query_cosine_similarities[idx]} for idx in sorted_indices[:top_k]]

    return jsonify(results)

# Route for rendering the search form
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


Overview:This project aims to develop a simple web search engine using web crawling, text indexing, and query processing techniques. It consists of three main components: a web crawler built with Scrapy, an indexer implemented in Python, and a query processor using Flask. The search engine allows users to submit queries through a web interface and retrieves relevant search results based on TF-IDF representation and cosine similarity scoring.


Components:
1)Web Crawler (quote.py): A Scrapy-based web crawler that fetches web documents from the Quotes to Scrape website (https://quotes.toscrape.com/) and extracts relevant content such as quotes and authors.
2)Indexer (indexer.py): Constructs an inverted index using TF-IDF representation and cosine similarity scoring. The indexer processes the crawled data, vectorizes the text using the TfidfVectorizer from Scikit-Learn, and calculates cosine similarity scores to build the index.
3)Query Processor (app.py): A Flask-based web application that handles user queries, retrieves relevant documents from the inverted index, and presents search results through a simple web interface. Users can submit queries via a search form and receive a list of relevant URLs along with their cosine similarity scores.


Usage:
Setup:
Install Python 3.10+ and required libraries (Scrapy, Flask, Scikit-Learn).
Clone the repository and navigate to the project directory.

Crawling:
Run the web crawler (quote.py) to fetch web documents and store them in JSON format (output.json).
Indexing:
Execute the indexer (indexer.py) to construct the inverted index and save it in pickle format (inverted_index.pkl).

Query Processing:
Start the Flask web server by running the query processor (app.py).
Access the search interface in a web browser and submit queries to retrieve search results.


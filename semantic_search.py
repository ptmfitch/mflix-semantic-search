import sys
from openai import OpenAI
from pymongo import MongoClient

# Update config.py with your OpenAI API Key
# and MongoDB Atlas connection string first
from config import api_key, connection_string

# Finds movie titles by running a semantic search on plot_embeddings
# Usage: python semantic_search.py "<semantic search query>"
# e.g.   python semantic_search.py "superheros fighting aliens"

text = sys.argv[1]

openai_client = OpenAI(api_key=api_key,)
mongodb_client = MongoClient(connection_string)

embedding = openai_client.embeddings.create(
  # Must use OpenAI's text-embedding-ada-002 model
  # as this was used to generated plot_embeddings
  model="text-embedding-ada-002",
  input=text,
  encoding_format="float"
)

# Should probably add some error handling
query_vector = embedding.data[0].embedding

result = mongodb_client['sample_mflix']['embedded_movies'].aggregate([
    {
        '$vectorSearch': {
            'index': 'default', 
            'path': 'plot_embedding', 
            'queryVector': query_vector, 
            'numCandidates': 200, 
            'limit': 20
        }
    },
    {
        # De-duplicate titles
        '$group': {
            '_id': '$title',
            'year': {'$first': '$year'}
        }
    },
    {
        '$limit': 10
    }
])

for movie in result:
  print(f"{movie['_id']} ({movie['year']})")

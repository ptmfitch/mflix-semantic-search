# mflix-semantic-search

## Setup

Follow the [How to Perform Semantic Search Against Data in Your Atlas Cluster](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-tutorial/) tutorial

Create an OpenAI account and [API key](https://platform.openai.com/api-keys), ensuring you have credits on your account (the embeddings model used in this demo has miniscule costs associated with it for our purposes)

Open a terminal and clone this repo then cd into the directory

```bash
git clone https://github.com/ptmfitch/mflix-semantic-search
cd mflix-semantic-search
```

Create a python environment then install the required python libraries

```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Update config.py with your MongoDB Atlas connection string and OpenAI API key

## Run

From your terminal, run the script

```bash
python3 semantic_search.py "search query goes here"
```
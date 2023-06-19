'''
This script builds the vector store index and saves it to disk.
'''
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = 'your key here'

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist()

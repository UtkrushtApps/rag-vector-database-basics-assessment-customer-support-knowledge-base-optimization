import chromadb
import json
client = chromadb.PersistentClient(path='chroma.db')
col = client.get_or_create_collection('support_docs')
# Load legacy improper chunks (already populated for this task)
# Your new pipeline will insert improved chunks during assessment
print('Chroma DB initialized and populated.')

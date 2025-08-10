import chromadb
client = chromadb.PersistentClient(path='chroma.db')
col = client.get_or_create_collection('support_docs')
chunks = col.get(limit=3)
for i, (cid, meta) in enumerate(zip(chunks['ids'], chunks['metadatas'])):
    print(f'Chunk {i+1} — ID: {cid}')
    for k, v in meta.items():
        print(f'  {k}: {v}')
    print()
print(f'Total chunks in collection: {col.count()}')

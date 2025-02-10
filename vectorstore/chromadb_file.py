import chromadb

client = chromadb.Client()
collection = client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This doc is about New York",
        "This doc is about Delhi",
    ],
    ids = ['id1', 'id2' ]
)

all_docs = collection.get()

results = collection.query(
    query_texts=['Query is about dirty rivers'],
    n_results = 1
)
print(results)

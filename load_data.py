import json
import chromadb
with open("data/internships.json", encoding="utf-8") as f:
    data = json.load(f)

client = chromadb.PersistentClient(path="./chroma_db")
try:
    client.delete_collection("internships")
except Exception:
    pass
collection = client.get_or_create_collection(name="internships")
documents = []
ids = []
metadatas = []

for info in data:
    documents.append(f"{info["title"]} at {info["company"]}. {info["description"]}")
    ids.append(info["id"])
    metadatas.append({"title": info["title"], "company": info["company"]})
collection.add(documents=documents, ids=ids, metadatas=metadatas)
print("Loaded:", collection.count())
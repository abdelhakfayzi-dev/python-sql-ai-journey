import chromadb

# 1. Initialize the local database (it will create a folder called 'chroma_db')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="internships")

# 2. Seed the database with 4 fake internship descriptions
internships = [
    "Data Science Intern: Requires Python, Pandas, Scikit-learn, and SQL for data analysis.",
    "Backend Engineer Intern: Requires Java, Spring Boot, and PostgreSQL for API development.",
    "AI Research Intern: Requires Machine Learning, PyTorch, Deep Learning, and mathematics.",
    "Frontend Web Intern: Requires HTML, CSS, JavaScript, and React for building user interfaces."
]

# ChromaDB automatically turns this text into 768-number vectors (embeddings) behind the scenes
collection.add(
    documents=internships,
    ids=[f"intern_{i}" for i in range(len(internships))]
)
print("✅ Database seeded with 4 internships.")

# 3. The Magic: Query by MEANING, not keywords
# Notice: The query doesn't use the exact words "Machine Learning" or "AI Research"
query = "I am into buidlding websites."

results = collection.query(
    query_texts=[query], 
    n_results=2 # Ask for the top 2 closest matches
)

print(f"\n🔍 Query: '{query}'")
print("🏆 Top 2 Matches found by the Librarian:")
for i, doc in enumerate(results['documents'][0]):
    print(f"{i+1}. {doc}")
import streamlit as st
import os
from openai import OpenAI
from pypdf import PdfReader
import chromadb
import json

# --- 1. UI SETUP ---
st.title("CV/Internship Fit Scorer (Level 2 RAG)")
st.write("Upload a CV and let the AI automatically find and analyze the best matching internships from our database.")

student_name = st.text_input("Student Name", "Ahmed")

st.subheader("Student Data")
uploaded_cv = st.file_uploader("Upload Student CV (PDF)", type=["pdf"])

cv_text = ""
if uploaded_cv is not None:
    try:
        reader = PdfReader(uploaded_cv)
        for page in reader.pages:
            cv_text += page.extract_text() or ""
        cv_text = cv_text[:10000]
        st.success(f"CV parsed: {len(cv_text)} characters extracted.")
    except Exception as e:
        st.error(f"Failed to read PDF: {e}")

manual_skills = st.text_area("Or paste Student Skills manually (comma separated)", "Python, SQL, Git, Linux, C, Machine Learning")

# --- 2. THE LIBRARIAN (Cached so it only loads once) ---
@st.cache_resource
def get_chroma_client():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="internships")
    
    if collection.count() == 0:
        with open("data/internships.json", encoding="utf-8") as f:
            data = json.load(f)
            
        documents, ids, metadatas = [], [], []
        for entry in data:
            documents.append(f"{entry['title']} at {entry['company']}. {entry['description']}")
            ids.append(entry["id"])
            metadatas.append({"title": entry["title"], "company": entry["company"]})
            
        collection.add(documents=documents, ids=ids, metadatas=metadatas)
        
    return collection

collection = get_chroma_client()

# --- 3. AI LOGIC ---
def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

def extract_skills_from_cv(client, cv_text):
    prompt = f"""Extract the technical skills from this CV text.
Return ONLY a comma-separated list of skills. No sentences, no explanations.

CV TEXT:
{cv_text}"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

def get_ai_analysis(client, student_name, student_skills, matched_internships):
    internships_text = "\n\n".join([f"Internship {i+1}: {intern}" for i, intern in enumerate(matched_internships)])
    prompt = f"""
You are a technical recruiter.

Student: {student_name}
Student skills: {', '.join(student_skills)}

Top matching internships found in our database:
{internships_text}

Analyze how well the student fits these specific internships.
Highlight the best fit and mention any missing skills.
Keep it under 150 words. No generic motivation.
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

# --- 4. EXECUTION ---
if st.button("Find & Score Best Internships"):
    client = get_client()
    if client is None:
        st.error("GROQ_API_KEY missing. Set it in your terminal.")
    else:
        with st.spinner("Analyzing CV and searching database..."):
            # Step A: Get Skills
            if cv_text:
                skills_raw = extract_skills_from_cv(client, cv_text)
                student_skills = [s.strip() for s in skills_raw.split(",") if s.strip()]
                st.info(f"**Skills detected in CV:** {', '.join(student_skills)}")
            else:
                student_skills = [s.strip() for s in manual_skills.split(",") if s.strip()]

            if not student_skills:
                st.warning("Upload a CV or enter your skills manually.")
                st.stop()

            # Step B: Query Vector DB (The Magic)
            query_text = ", ".join(student_skills)
            results = collection.query(
                query_texts=[query_text],
                n_results=3
            )
            matched_internships = results['documents'][0]

            st.subheader("Top 3 Matched Internships")
            for i, doc in enumerate(results['documents'][0]):
                 meta = results['metadatas'][0][i]
                 st.markdown(f"**{i+1}. {meta['title']} @ {meta['company']}**")
                 st.caption(doc)

            # Step C: Final AI Analysis
            analysis = get_ai_analysis(client, student_name, student_skills, matched_internships)

            st.divider()
            st.subheader("Recruiter Analysis")
            st.info(analysis)
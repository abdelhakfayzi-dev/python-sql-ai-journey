import os
from openai import OpenAI

student = {
    "name": "Ahmed",
    "skills": ["Python", "SQL", "Git", "Linux"],
    "education": "Engineering student, ENSAO",
    "experience": "No experience yet"
}

internships = [
    {"company": "Google", "role": "Software Engineer", "required_skills": ["Python", "SQL", "C", "Git"]},
    {"company": "IBM", "role": "Data Analyst", "required_skills": ["SQL", "Excel", "Power BI"]},
    {"company": "Amazon", "role": "Backend Engineer", "required_skills": ["Java", "AWS", "SQL", "Docker"]},
    {"company": "Meta", "role": "DevOps Engineer", "required_skills": ["Python", "Linux", "Docker", "Git"]}
]




def get_ai_analysis(student_name, student_skills, role, required_skills, match_percent):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "API key missing — analysis skipped."

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    prompt = f"""
You are a technical recruiter.

Student: {student_name}
Student skills: {', '.join(student_skills)}
Role: {role}
Required skills: {', '.join(required_skills)}
Skill match: {match_percent}%

Explain in 3-5 sentences why this student fits or does not fit the role.
Be specific. Mention missing skills if needed. No bullets. No generic motivation.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    
    return response.choices[0].message.content.strip()

results = []

for internship in internships:
    matched = 0

    for skill in student["skills"]:
        if skill in internship["required_skills"]:
            matched += 1

    match_percent = round(matched * 100 / len(internship["required_skills"]))

    results.append({
        "company": internship["company"],
        "role": internship["role"],
        "required_skills": internship["required_skills"],
        "match_percent": match_percent
    })

results.sort(key=lambda x: x["match_percent"], reverse=True)
top_3 = results[:3]

print("=== CV Scoring Results ===")

for i, result in enumerate(top_3, 1):
    role = f"{result['company']} ({result['role']})"

    analysis = get_ai_analysis(
        student["name"],
        student["skills"],
        role,
        result["required_skills"],
        result["match_percent"]
    )

    print(f"{i}. {role}: {result['match_percent']}% match")
    print(f"   AI Analysis: {analysis}\n")
 
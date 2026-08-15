import sqlite3
conn = sqlite3.connect('internships.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS internships')
cursor.execute('''
CREATE TABLE internships (
 id INTEGER PRIMARY KEY,
 company TEXT,
 role TEXT,
 required_skills TEXT,
 location TEXT
)''')
cursor.execute('DROP TABLE IF EXISTS students')
cursor.execute('''
CREATE TABLE students (
 id INTEGER PRIMARY KEY,
 name TEXT,
 skills TEXT,
 city TEXT
)''')
internships = [
    (1,'Google','Software Engineer','Python,SQL,C','Remote'),
    (2,'Microsoft','AI engineer','Python,Javascript','New York'),
    (3,'META','Cloud Engineer','Azure aws,SQL','Remote'),
    (4, 'IBM', 'Data Analyst', 'Python, SQL, Excel', 'Austin'),
    (5, 'Amazon', 'Backend Engineer', 'Java, AWS, SQL', 'Seattle'),
]
cursor.executemany('INSERT INTO internships VALUES (?,?,?,?,?)',internships)
conn.commit()
students = [
    (1,'Ahmed','Python,SQL,C','Remote'),
    (2,'Rachid','Azure aws,SQL','New York'),
    (3,'Layla','Java, AWS, SQL','Seattle'),
]
cursor.executemany('INSERT INTO students VALUES (?,?,?,?)',students)
conn.commit()
print('Data inserted successfully.')
print("\n=== Skill Matcher ===\n")
cursor.execute('SELECT * FROM students')
students_data = cursor.fetchall()
cursor.execute('SELECT * FROM internships')
internships_data = cursor.fetchall()
for student in students_data:
    s_id,s_name,s_skills,s_city = student
    student_skills = [s.strip() for s in s_skills.split(',')]
    for internship in internships_data:
        i_id,company,role,required_skills_str,location = internship
        required_skills = [s.strip() for s in required_skills_str.split(',')]
        matched = 0
        for skill in student_skills:
            if skill in required_skills:
                matched+=1
        total_required = len(required_skills)
        print(f"{s_name} vs {company} ({role}): {matched}/{total_required} skills matched")
conn.close()


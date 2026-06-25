import fitz
import random

SKILL_QUESTIONS = {
"python": [
"Explain Python decorators.",
"What is the difference between lists and tuples?",
"Explain generators in Python."
],
"sql": [
"Explain different types of SQL joins.",
"What is normalization?",
"Difference between DELETE, TRUNCATE and DROP?"
],
"machine learning": [
"Explain overfitting and underfitting.",
"What is Random Forest?",
"Difference between supervised and unsupervised learning?"
],
"power bi": [
"What are DAX measures?",
"Difference between calculated column and measure?",
"Explain Power Query."
],
"java": [
"Explain JVM.",
"What is polymorphism?",
"Difference between abstract class and interface?"
]
}

def extract_text(pdf):
doc = fitz.open(pdf)
text = ""

```
for page in doc:
    text += page.get_text()

return text.lower()
```

def detect_skills(text):
detected = []

```
for skill in SKILL_QUESTIONS:
    if skill in text:
        detected.append(skill)

return detected
```

def generate_questions(skills):

```
questions = []

for skill in skills:
    questions.extend(SKILL_QUESTIONS[skill])

random.shuffle(questions)

return questions[:5]
```

if **name** == "**main**":

```
resume = "resume.pdf"

text = extract_text(resume)

skills = detect_skills(text)

questions = generate_questions(skills)

print("\n========== AI INTERVIEW ==========\n")

if not questions:
    print("No interview questions generated.")
else:
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question}")
```

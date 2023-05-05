import random

# Sudarome klausimų sąrašą
questions = [
    {"question": "Kas yra didžiausias žinduolis pasaulyje?", "answers": ["1. Žirafos", "2. Drambliai", "3. Morkos"], "correct_answer": "2"},
    {"question": "Kas yra didžiausias planetas Saulės sistemoje?", "answers": ["1. Marsas", "2. Jupiteris", "3. Plutonas"], "correct_answer": "2"},
    {"question": "Kas yra žmogaus kūno pagrindinė kraujotakos organų sistema?", "answers": ["1. Kvėpavimo sistema", "2. Kraujagyslių sistema", "3. Virškinimo sistema"], "correct_answer": "2"},
    {"question": "Kas yra pirmoji pasaulio programavimo kalba?", "answers": ["1. COBOL", "2. FORTRAN", "3. BASIC"], "correct_answer": "2"},
    {"question": "Kas yra žmogaus kūno pagrindinė širdies ritmo reguliacijos sistema?", "answers": ["1. Centrinė nervų sistema", "2. Endokrininė sistema", "3. Kraujotakos sistema"], "correct_answer": "1"}
]

# Funkcija, kuri atspausdina klausimą ir pasiruošia atsakymo įvedimui
def ask_question(question):
    print(question["question"])
    for answer in question["answers"]:
        print(answer)
    user_answer = input("Įveskite atsakymo numerį: ")
    return user_answer == question["correct_answer"]

# Pagrindinė funkcija, kuri vykdo testą
def run_test():
    score = 0
    random.shuffle(questions) # Sumaišome klausimų sąrašą
    for question in questions:
        if ask_question(question):
            score += 1
    print("Jūsų balų suma:", score)

# Paleidžiame testą
run_test()
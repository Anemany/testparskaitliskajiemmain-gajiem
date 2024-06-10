class app:
    def __init__(self):
        self.questions = [
            {
                "question": "Kā Python programmēšanas valodā var paaugstināt skaitli pakāpē?",
                "options": ["**", "pow(x,y)", "sqrt(x,y)", "round(x)"],
                "answer": ["1", "2"]
            },
            {
                "question": "Kuras no šīm funkcijām prasa 'math' moduli?",
                "options": ["Modulis", "Kvadrātsakne", "Sinuss", "Minimālā vērtība"],
                "answer": ["2", "3"]
            },
            {
                "question": "Kura funkcija NE atgriež tangensu?",
                "options": ["math.tan(x)", "math.cos(x)", "math.floor(x)", "min(x,y)"],
                "answer": ["2", "3", "4"]
            },
            {
                "question": "Kādu vērtību atgriež funkcija 'math.pi'?",
                "options": ["3.141592653589793", "random", "pi skaitlis", "4"],
                "answer": ["1", "3"]
            },
            {
                "question": "Cik radiāni ir 180 grādi?",
                "options": ["pi skaitlis", "3.141592653589793", "2", "360 grādi"],
                "answer": ["1", "2"]
            },
            {
                "question": "Kādu vērtību atgriež funkcija 'math.sin(math.pi/2)'?",
                "options": ["0", "0.0", "1", "1.0"],
                "answer": ["3", "4"]
            },
            {
                "question": "Ko atgriež funkcija 'abs(-5)'?",
                "options": ["-5", "0", "5", "5.0"],
                "answer": ["3", "4"]
            },
            {
                "question": "Kā iegūt kvadrātsakni no skaitļa?",
                "options": ["sqrt = x ** (0.5)", "num = sakne x", "sqrt.math(x)", "math.sqrt(x)"],
                "answer": ["1", "4"]
            },
            {
                "question": "Ko atgriež 'ceil(4.2)'?",
                "options": ["4", "4.5", "5", "5.0"],
                "answer": ["3", "4"]
            },
            {
                "question": "Ko dara funkcija statistics.median()?",
                "options": ["Aprēķina doto datu mediānu", " Aprēķina doto vidējo vērtību", " Aprēķina sakni", "Aprēķina modu"],
                "answer": ["1", "2"]
            }
        ]
        self.score = 0
        self.incorrect_questions = []

    def run_test(self):
        print("Tests par skaitliskajiem mainīgajiem\n")
        for i, q in enumerate(self.questions, start=1):
            print(f"Jautājums {i}: {q['question']}")
            for j, option in enumerate(q["options"], start=1):
                print(f"{j}. {option}")
            answer = input("Jūsu atbilde (ievadiet numuru): ")
            if str(answer) in q["answer"]:
                self.score += 1
            else:
                self.incorrect_questions.append(i)

        print(f"Jūsu rezultāts: {self.score} no {len(self.questions)}")

        if self.incorrect_questions:
            print("Jautājumi, uz kuriem tika atbildēts nepareizi:")
            for i in self.incorrect_questions:
                print(f"Jautājums {i}: {self.questions[i - 1]['question']}")
                correct_answers = " vai ".join(self.questions[i - 1]["answer"])
                print(f"Pareizā atbilde: {correct_answers}\n")

if __name__ == "__main__":
    test = app()
    test.run_test()

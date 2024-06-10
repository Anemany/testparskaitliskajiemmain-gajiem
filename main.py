class main:
    def __init__(self):
        self.questions = [
            {
                "question": "как можно возвести в степень в языке програмирования Python?",
                "options": ["1) **", "2) pow(x,y)", "3) sqrt(x,y)", "4) round(x)"],
                "answer": "1) **" or "2) pow(x,y)"
            },
            {
                "question": "Какой результат будет у выражения 3 * 3 ** 3?",
                "options": ["27", "81", "243", "729"],
                "answer": "81"
            },
            {
                "question": "Как создать функцию в Python?",
                "options": ["function myFunction() {}", "def myFunction():", "create myFunction():", "func myFunction() {}"],
                "answer": "def myFunction():"
            },
            {
                "question": "Какой метод используется для добавления элемента в конец списка?",
                "options": ["add()", "append()", "insert()", "extend()"],
                "answer": "append()"
            },
            {
                "question": "Какой из следующих методов не изменяет исходный список?",
                "options": ["sort()", "sorted()", "reverse()", "append()"],
                "answer": "sorted()"
            }
        ]
        self.score = 0

    def run_test(self):
        print("Тест на знание Python\n")
        for i, q in enumerate(self.questions, start=1):
            print(f"Вопрос {i}: {q['question']}")
            for j, option in enumerate(q["options"], start=1):
                print(f"{j}. {option}")
            answer = input("Ваш ответ (введите номер): ")
            if q["options"][int(answer) - 1] == q["answer"]:
                print("Правильно!\n")
                self.score += 1
            else:
                print(f"Неправильно. Правильный ответ: {q['answer']}\n")

        print(f"Ваш результат: {self.score} из {len(self.questions)}")

if __name__ == "__main__":
    test = main()
    test.run_test()
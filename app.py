from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["Earth", "Mars", "Mercury", "Venus"],
        "answer": "Mercury"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, question in enumerate(questions):
            selected_option = request.form.get(f'question-{i}')
            if selected_option == question['answer']:
                score += 1
        return render_template('result.html', score=score, total=len(questions))
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)

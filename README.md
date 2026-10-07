# TaskFlow - Python To-Do List

A responsive, modern To-Do List application built with **Python, Flask, SQLite, HTML and CSS**.

## Key Features
- Responsive component layout for mobile and desktop
- Modern aesthetics with CSS gradients, cards, shadows and animations
- Add tasks
- Mark tasks as completed/uncompleted
- Delete tasks
- Clear completed tasks
- SQLite database integration for persistent task storage
- Task statistics: total, completed and remaining

## How to Run

1. Install Python 3.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Start the application:
   `python app.py`
4. Open the local URL shown by Flask, normally:
   `http://127.0.0.1:5000`

## Repository Structure

```
todo_list_python/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

The `todo.db` file is created automatically when the application runs.

# Flask CRUD Web App (with SQLite Database)

A simple **Flask** web application that allows users to **add**, **select**, and **edit** items using HTML forms and stores all data in a **SQLite database**.

---

## ✅ Features

- **Home / Selection Page** – Choose which record you want to edit
- **Add Page** – Form for adding new records to the database
- **Edit Page** – Update existing records directly in the database
- **SQLite Database** – All data is stored persistently in a `.db` file
- **Reusable Jinja Templates**
- **Custom Styling** with CSS + Bootstrap

---

## 🛠 Technologies Used

| Type       | Tool          |
|------------|---------------|
| Backend    | Flask         |
| Database   | SQLite        |
| Frontend   | HTML, CSS     |
| Styling    | Bootstrap     |
| Templating | Jinja2        |

---

## 📂 Project Structure

├── main.py # Flask app with routes and database logic

├── instance # File that holds SQLite data in

│ ├──my-top100-movies.db # SQLite database file

├── styles.css # Custom CSS styles

├── templates/

│ ├── select.html # Select record

│ ├── add.html # Add new record

│ ├── edit.html # Edit record

│ ├── base.html # Parent style page

│ ├── index.html # Home page

---

## 🔌 Notes

The app uses a SQLite database (my-top100-movies.db).

You can replace this file with your own database as long as it contains compatible table/column names.

---

## 📝 License

This project is released under the MIT License.

---

## ▶️ Getting Started

1. Clone the Repository
bash
git clone https://github.com/bunyaminenis/flask-crud-app.git
cd flask-crud-app

2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
python main.py

5. Open in Browser
Click http://127.0.0.1:5000

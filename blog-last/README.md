# Blog-Last

A Flask-based personal blog web application where users can create, edit, and manage blog posts.  
This project demonstrates how to build a dynamic blog with a SQLite database, Flask-WTF forms, Bootstrap styling, and a rich-text editor (CKEditor).

---

## ✨ Features

- 📝 **CRUD Operations**: Create, Read, Update, and Delete blog posts.
- 🎨 **Rich Text Editing**: Blog body content powered by CKEditor for formatting.
- 📅 **Auto Timestamp**: Posts include the current date automatically.
- 🌐 **Pages**:
  - **Home** – Displays all blog posts stored in the database.
  - **Single Post View** – Shows full post details with edit option.
  - **Make/Edit Post** – Form to create new or update existing posts.
  - **Delete Post** – Remove posts directly from the database.
  - **About Page** – Static information page.
  - **Contact Page** – Includes a styled contact form (no email integration).
- 💅 **Responsive UI**: Integrated with Bootstrap 5 templates for clean design.

---

## 🛠️ Technologies Used

- **Flask** – Backend web framework
- **Flask-Bootstrap** – Bootstrap 5 integration
- **Flask-WTF** – Form handling & validation
- **Flask-CKEditor** – Rich text editor for blog posts
- **SQLAlchemy** – ORM with SQLite database
- **WTForms** – Form creation & validation

---

## 📂 Project Structure

blog-last/

│── main.py # Application entry point & routes

│── templates/ # HTML templates

│ ├── index.html # Homepage

│ ├── post.html # Single post view

│ ├── make-post.html # Create/Edit post form

│ ├── about.html # About page

│ ├── contact.html # Contact form

│ ├── header.html # Shared header

│ └── footer.html # Shared footer

│── static/ # CSS, JS, and images

│── instance/ # SQLite database storage

---

## 🚀 Getting Started

### 1. Clone the repository
    bash
    git clone https://github.com/bunyaminenis/blog-last.git
    cd blog-last
    
### 2. Create and activate a virtual environment

    python -m venv venv
    source venv/bin/activate   # On Mac/Linux
    venv\Scripts\activate      # On Windows

### 3. Install dependencies

    pip install flask flask-bootstrap flask-sqlalchemy flask-wtf flask-ckeditor

### 4. Run the application

    python main.py

Visit the app in your browser at http://127.0.0.1:5003

---


📜 License

This project is licensed under the MIT License.
  

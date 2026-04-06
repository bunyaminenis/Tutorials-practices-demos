# ☕ Flask Café API

A simple **Flask REST API** connected to a **SQLite database** for managing cafés.  
You can retrieve cafés, search by location, add new cafés, update prices, or delete entries.  
Includes a minimal HTML landing page (`index.html`) and all API endpoints tested/documented in **Postman**.

---

## 🚀 Features

- **Home Page (`/`)** – Welcome page
- **`/random`** – Get details of a random café
- **`/all`** – Retrieve all cafés in the database
- **`/search?loc=<location>`** – Search cafés by location
- **`/add`** (POST) – Add a new café
- **`/update-price/<cafe_id>?new_price=...`** (PATCH) – Update coffee price of a café
- **`/report-closed/<cafe_id>?api-key=TopSecretAPIKey`** (DELETE) – Delete a café (API key required)

---

## 🛠 Technologies Used

- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite (`cafes.db`)
- **Frontend**: Minimal HTML (`index.html`)
- **Testing**: Postman (API docs published)

---

## 📂 Project Structure

├── main.py # Flask app with all routes and API endpoints

  ├── instance 
  
  │ └── cafes.db # SQLite database storing cafes

  ├── templates/

  │ └── index.html # Landing page

---

1. **Clone the Repository**
   
    bash
    git clone https://github.com/bunyaminenis/flask-cafe-api.git
    cd flask-cafe-api

2. **Create Virtual Environment**
   
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows

3. **Install Dependencies**
   
    pip install -r requirements.txt

4. **Run the App**
   
    python main.py

5. **Open in Browser**
    
    http://127.0.0.1:5000

---

📬 API Documentation

All API endpoints have been tested with Postman.
👉 [Published Postman documentation link](https://documenter.getpostman.com/view/47760364/2sB3BLhmX8)

---


📝 License

This project is released under the MIT License.


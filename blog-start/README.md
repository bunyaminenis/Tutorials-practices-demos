📝 Flask Blog with External API Integration
This project is a simple Flask-based blog that dynamically loads post content from an external API and renders it using Jinja templates. It demonstrates how to separate content from logic by fetching structured data and turning it into dynamic web pages.

🚀 Features
Renders a homepage with a list of blog posts

Dynamic routing for individual blog post pages

Fetches blog content from an external API (npoint.io)

Uses Jinja2 templating for clean and structured HTML

Easily extendable with templates, styles, and database support

🛠️ Technologies Used
Python 3.x

Flask

Jinja2

Requests (to fetch post data)

📁 Project Structure

📦 flask-blog/
├── main.py          # Flask app and routing logic

├── post.py          # Post model class

├── templates/

│   ├── index.html   # Homepage template

│   └── post.html    # Individual post template


<div align="center">
  <h1>Nexus Project Manager</h1>
  <p>A premium, role-based project management web application built with Python, Flask, and MongoDB.</p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
</div>

<br />

## ✨ Features

- **User Authentication:** Secure signup and login powered by `Flask-Login` and `Flask-Bcrypt` password hashing.
- **Role-Based Access Control (RBAC):** Distinct `Admin` and `Member` privileges. Admins can create projects and assign tasks, while Members can manage their assigned workflows.
- **Project & Task Management:** Create projects, add team members, assign tasks, and track statuses across a dynamic Kanban board.
- **Due Date Tracking:** Visual overdue indicators automatically highlight tasks that are past their deadline.
- **Premium UI/UX:** A stunning, responsive interface built with modern "Glassmorphism" aesthetics, subtle CSS animations, and dynamic modals.
- **Modular Architecture:** Engineered using Flask Blueprints and the Application Factory pattern for ultimate scalability.

---

## 💻 Local Development Setup

To run this application on your local machine, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Task-Manager.git
cd Task-Manager
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory of the project and add your database configuration:
```env
MONGO_URI=mongodb://localhost:27017/project_manager
SECRET_KEY=your-super-secret-key
```
*(Note: You must have a local instance of MongoDB running on port 27017, or replace the URI with a MongoDB Atlas string).*

### 5. Run the Application
```bash
python run.py
```
The application will be live at `http://127.0.0.1:5000/`.

---

## 🚀 Deployment (Railway)

This application is fully pre-configured for seamless, one-click deployment on [Railway.app](https://railway.app/).

1. **Push to GitHub**: Ensure your latest code is pushed to your GitHub repository.
2. **Create Railway Database**: In Railway, click **New Project** -> **Provision MongoDB**.
3. **Deploy Web App**: In the same Railway project, click **New** -> **GitHub Repo** and select your repository.
4. **Link Variables**: Click your Web Application bubble, go to the **Variables** tab, and add the following:
   - `MONGO_URI` = `${{MongoDB.MONGO_URL}}`
   - `SECRET_KEY` = `any-random-secure-string`
5. **Generate Domain**: Go to your Web Application's **Settings** tab, scroll to **Networking**, and click **Generate Domain**.

Your site is now live on the internet! 

---

## 📁 Project Structure

```text
├── app/
│   ├── models/           # MongoDB data models (User, Project, Task)
│   ├── routes/           # Flask Blueprints (Auth, Projects, Tasks, Views)
│   ├── static/           # CSS and static assets
│   ├── templates/        # HTML Jinja2 templates
│   ├── __init__.py       # App Factory & Initialization
│   ├── config.py         # Environment Configuration
│   ├── db.py             # Database connection logic
│   └── utils/            # Decorators and helpers
├── Procfile              # Gunicorn configuration for Railway deployment
├── requirements.txt      # Python dependencies
└── run.py                # Local development entry point
```

<div align="center">
  <i>Built with ❤️ using Python & Flask</i>
</div>

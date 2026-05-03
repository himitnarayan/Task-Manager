# Nexus - Project Manager

A premium project management web application built with Python, Flask, and MongoDB.

## Features
- User Authentication (Signup / Login)
- Role-based Access Control (Admin / Member)
- Project Management
- Task Assignment & Status Tracking
- Premium Dark-mode UI with Glassmorphism
- RESTful backend routes

## Local Setup

1. **Clone the repository**
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   MONGO_URI=mongodb://localhost:27017/project_manager
   SECRET_KEY=your-super-secret-key
   ```
5. **Run the App:**
   ```bash
   python run.py
   ```

## Secure Railway Deployment Guide (No Public IP Whitelisting)

This guide shows you how to deploy the application completely within Railway's private network using their internal MongoDB service.

### Step 1: Push to GitHub
Ensure your code is pushed to a GitHub repository.
```bash
git remote add origin <your-repo-url>
git push -u origin main
```

### Step 2: Create Project & Database on Railway
1. Go to [Railway.app](https://railway.app/) and sign in.
2. Click **New Project** -> **Provision PostgreSQL, Redis, etc**.
3. Select **MongoDB** from the list. 
4. Railway will now create an empty project and spin up a private MongoDB database for you.

### Step 3: Deploy the Web Application
1. In the same project view (where your new MongoDB bubble is), click the **New** button in the top right.
2. Select **GitHub Repo** and choose the Nexus repository you just pushed.
3. Railway will start building your Python app.

### Step 4: Link the Database (Environment Variables)
1. Click on your newly deployed **Web Application** bubble.
2. Go to the **Variables** tab.
3. Click **New Variable** -> **Reference Variable**.
4. Set the name to `MONGO_URI` and select the value `${MONGO_URL}` (this automatically links to your private MongoDB).
5. Add another variable named `SECRET_KEY` and type any random long string (e.g., `super-secret-prod-key-12345`).

### Step 5: Go Live
1. Still inside your Web Application bubble, go to the **Settings** tab.
2. Scroll down to **Networking** and click **Generate Domain**.
3. Click on the generated URL to view your live app!

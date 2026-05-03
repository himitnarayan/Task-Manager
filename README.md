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

## Render Deployment Guide

To deploy this application on Render.com, follow these steps:

1. **Push to GitHub**
   Ensure your code is pushed to a GitHub repository.
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Setup MongoDB Atlas**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a free cluster.
   - Under "Database Access", create a user and password.
   - Under "Network Access", add `0.0.0.0/0` to allow connections from anywhere (Render).
   - Click "Connect" -> "Drivers" -> Python, and copy the connection string. Replace `<password>` with your database user's password.

3. **Deploy on Render**
   - Go to [Render.com](https://render.com/) and sign in.
   - Click **New** -> **Web Service**.
   - Connect your GitHub account and select the repository.
   - Configure the Web Service:
     - **Name**: `nexus-project-manager` (or your choice)
     - **Region**: Select closest to you
     - **Branch**: `main`
     - **Runtime**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn "app:create_app()"`
   - Scroll down to **Environment Variables** and add:
     - `MONGO_URI` : Paste your MongoDB Atlas connection string.
     - `SECRET_KEY` : A random long string for session security.
     - `PYTHON_VERSION` : `3.10.0` (or whatever python version you prefer)
   
4. **Deploy**
   - Click **Create Web Service**.
   - Render will automatically build and deploy your Flask application.
   - Once complete, you will see a green "Live" badge and your public URL at the top left.

Your application is now live!

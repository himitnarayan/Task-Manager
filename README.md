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

## Railway Deployment Guide

To deploy this application on Railway, follow these steps:

1. **Push to GitHub**
   Ensure your code is pushed to a GitHub repository.
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Setup MongoDB Atlas**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a free cluster.
   - Under "Database Access", create a user and password.
   - Under "Network Access", add `0.0.0.0/0` to allow connections from anywhere (Railway).
   - Click "Connect" -> "Drivers" -> Python, and copy the connection string. Replace `<password>` with your database user's password.

3. **Deploy on Railway**
   - Go to [Railway.app](https://railway.app/) and sign in.
   - Click **New Project** -> **Deploy from GitHub repo**.
   - Select the repository you just pushed.
   - Click **Add Variables** (or go to Variables tab) and add:
     - `MONGO_URI` : Paste your MongoDB Atlas connection string.
     - `SECRET_KEY` : A random long string for session security.
   
4. **Deploy**
   - Railway will automatically detect the Python environment (thanks to `requirements.txt`) and run the application using Gunicorn (thanks to the `Procfile`).
   - Go to the **Settings** tab of your deployed service on Railway.
   - Under **Networking**, click "Generate Domain" to get your live public URL.

Your application is now live!
# Task-Manager

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.task import Task
from app.db import get_db

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
    return redirect(url_for('auth.login'))

@views_bp.route('/dashboard')
@login_required
def dashboard():
    projects = Project.get_all_for_user(current_user.get_id(), current_user.role)
    
    if current_user.role == 'Admin':
        db = get_db()
        tasks = list(db.tasks.find())
    else:
        tasks = Task.get_for_user(current_user.get_id())
        
    total_tasks = len(tasks)
    todo_tasks = len([t for t in tasks if t.get('status') == 'To Do'])
    in_progress_tasks = len([t for t in tasks if t.get('status') == 'In Progress'])
    done_tasks = len([t for t in tasks if t.get('status') == 'Done'])
    
    return render_template('dashboard.html', 
                           projects=projects, 
                           tasks=tasks,
                           stats={
                               'total': total_tasks,
                               'todo': todo_tasks,
                               'in_progress': in_progress_tasks,
                               'done': done_tasks
                           })

@views_bp.route('/project/<project_id>')
@login_required
def project_detail(project_id):
    project = Project.get_by_id(project_id)
    if not project:
        return "Project not found", 404
        
    tasks = Task.get_for_project(project_id)
    
    users = []
    if current_user.role == 'Admin':
        db = get_db()
        users = list(db.users.find())
        
    return render_template('project_detail.html', project=project, tasks=tasks, users=users)

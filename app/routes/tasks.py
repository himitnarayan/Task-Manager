from flask import Blueprint, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.task import Task
from app.utils.decorators import admin_required

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/create', methods=['POST'])
@login_required
@admin_required
def create_task():
    project_id = request.form.get('project_id')
    title = request.form.get('title')
    description = request.form.get('description')
    assignee_id = request.form.get('assignee_id')
    due_date = request.form.get('due_date')
    
    if not title or not project_id:
        flash('Title and Project are required.', 'danger')
        return redirect(url_for('views.project_detail', project_id=project_id))
        
    Task.create(project_id, title, description, assignee_id, due_date=due_date)
    flash('Task created successfully.', 'success')
    return redirect(url_for('views.project_detail', project_id=project_id))

@tasks_bp.route('/<task_id>/update_status', methods=['POST'])
@login_required
def update_status(task_id):
    new_status = request.form.get('status')
    task = Task.get_by_id(task_id)
    
    if task:
        if current_user.role == 'Admin' or str(task.get('assignee_id')) == current_user.get_id():
            Task.update_status(task_id, new_status)
            flash('Task status updated.', 'success')
        else:
            flash('You do not have permission to update this task.', 'danger')
            
    return redirect(request.referrer or url_for('views.dashboard'))

from flask import Blueprint, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.user import User
from app.utils.decorators import admin_required

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/create', methods=['POST'])
@login_required
@admin_required
def create_project():
    title = request.form.get('title')
    description = request.form.get('description')
    if not title:
        flash('Title is required.', 'danger')
        return redirect(url_for('views.dashboard'))
        
    Project.create(title, description, current_user.get_id())
    flash('Project created successfully!', 'success')
    return redirect(url_for('views.dashboard'))

@projects_bp.route('/<project_id>/add_member', methods=['POST'])
@login_required
@admin_required
def add_member(project_id):
    email = request.form.get('email')
    user = User.get_by_email(email)
    if user:
        Project.add_member(project_id, user.get_id())
        flash(f'User {email} added to project.', 'success')
    else:
        flash('User not found.', 'danger')
    return redirect(url_for('views.project_detail', project_id=project_id))

from bson.objectid import ObjectId
from app.db import get_db
from datetime import datetime, timezone

class Task:
    @staticmethod
    def create(project_id, title, description, assignee_id=None, status='To Do', due_date=None):
        db = get_db()
        task_data = {
            'project_id': ObjectId(project_id),
            'title': title,
            'description': description,
            'assignee_id': ObjectId(assignee_id) if assignee_id else None,
            'status': status,
            'due_date': due_date,
            'created_at': datetime.now(timezone.utc)
        }
        result = db.tasks.insert_one(task_data)
        return str(result.inserted_id)

    @staticmethod
    def get_for_project(project_id):
        db = get_db()
        return list(db.tasks.find({'project_id': ObjectId(project_id)}))

    @staticmethod
    def get_for_user(user_id):
        db = get_db()
        return list(db.tasks.find({'assignee_id': ObjectId(user_id)}))

    @staticmethod
    def get_by_id(task_id):
        db = get_db()
        return db.tasks.find_one({'_id': ObjectId(task_id)})

    @staticmethod
    def update_status(task_id, new_status):
        db = get_db()
        db.tasks.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': {'status': new_status}}
        )

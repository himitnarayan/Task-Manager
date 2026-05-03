from bson.objectid import ObjectId
from app.db import get_db
from datetime import datetime, timezone

class Project:
    @staticmethod
    def create(title, description, owner_id):
        db = get_db()
        project_data = {
            'title': title,
            'description': description,
            'owner_id': ObjectId(owner_id),
            'members': [ObjectId(owner_id)],
            'created_at': datetime.now(timezone.utc)
        }
        result = db.projects.insert_one(project_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all_for_user(user_id, role):
        db = get_db()
        if role == 'Admin':
            return list(db.projects.find())
        else:
            return list(db.projects.find({'members': ObjectId(user_id)}))

    @staticmethod
    def get_by_id(project_id):
        db = get_db()
        return db.projects.find_one({'_id': ObjectId(project_id)})

    @staticmethod
    def add_member(project_id, user_id):
        db = get_db()
        db.projects.update_one(
            {'_id': ObjectId(project_id)},
            {'$addToSet': {'members': ObjectId(user_id)}}
        )

from flask import Blueprint, request, jsonify, abort
from models.task import Task, db
from sqlalchemy.exc import SQLAlchemyError

task_bp = Blueprint('task_bp', __name__)

# Get All Tasks
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Create Task
@task_bp.route('/tasks/create', methods=['POST'])
def create_task():
    data = request.json

    if 'title' not in data or 'description' not in data:
        abort(400, "Title and description are required fields.")

    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed', False)

    if not isinstance(title, str) or not isinstance(description, str):
        abort(400, "Title and description must be strings.")

    try:
        new_task = Task(title=title, description=description, completed=completed)
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
0

# Get Task by id
@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

# Update Task
@task_bp.route('/tasks/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json

    title = data.get('title', task.title)
    description = data.get('description', task.description)
    completed = data.get('completed', task.completed)

    if not isinstance(title, str) or not isinstance(description, str):
        abort(400, "Title and description must be strings.")

    try:
        task.title = title
        task.description = description
        task.completed = completed
        db.session.commit()
        return jsonify(task.to_dict())
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Delete Task
@task_bp.route('/tasks/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task Deleted'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

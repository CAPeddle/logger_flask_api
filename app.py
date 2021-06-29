#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, render_template
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_sqlalchemy import SQLAlchemy

import config
from models import Record

# Get the application instance
app = config.app
api = Api(app)
db = config.db

record_fields = {
    'measurement': fields.String,
    'location': fields.String,
    'value': fields.String,
    'unit': fields.String,
    'timestamp': fields.DateTime,
    'uri': fields.Url('task')
}

class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('measurement', type=str, required=True,
                                   help='No measurement provided',
                                   location='json')
        self.reqparse.add_argument('location', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('unit', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        records = Record.query.all()
        return {'records': [marshal(record, record_fields) for record in records]}

    def post(self):
        args = self.reqparse.parse_args()
        print (args)
        record = {
            'measurement': args['measurement']
            ,'location': args['location']
            ,'unit': args['unit']
        }
                
        db.session.add(record)
        return {'record': marshal(record, record_fields)}, 201


class TaskAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        return {'task': marshal(task[0], task_fields)}

    def put(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return {'result': True}


@app.route('/')
def index():
    return render_template('home.html')

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)

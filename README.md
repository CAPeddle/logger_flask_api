# logger_flask_api
Python Flask-Restful api to log data points

need to convert the rest api to the format of the mega tut so that it's easier to use the advice there

use this to add static html - javascript to the project
https://realpython.com/flask-connexion-rest-api/

to get to the config
return app.config['SECRET_KEY']

put or post
PUT method is idempotent.
POST is NOT idempotent

So POST values


/logger/api/log/{temperature}/{emma}
{
    "value":"23.2",
    "unit":"celsius"
}

log table:
id value unit time

/logger/view

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')


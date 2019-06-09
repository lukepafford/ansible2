from celery import Celery

app = Celery('hello')
app.config_from_object('conf')

@app.task
def hello():
	    return 'hello world'

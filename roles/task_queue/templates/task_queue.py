from celery import Celery
import subprocess as sp
app = Celery('hello')
app.config_from_object('conf')

@app.task
def runFlaskPipeline():
		res = sp.run('/var/apps/flask-app/flask-pipeline.sh')
		if res.returncode == 0:
			return 'Pipeline succeeded'
		else:
			return 'Pipeline failed'

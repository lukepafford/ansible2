## Broker settings.
broker_url = '{{ task_queue_brokerUrl }}'

# List of modules to import when the Celery worker starts.
imports = ('{{ role_name }}.tasks',)

## Using the database to store task state and results.
result_backend = '{{ task_queue_backendUrl }}'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}

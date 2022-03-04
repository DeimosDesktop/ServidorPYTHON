from bottle import route, run, template
from datetime import datetime

@route('/')
def index(name='hora'):
    dt = datetime.now()
    time = "{:%d-%m-%Y %H:%M:%S}".format(dt)
    return template('<strong>La hora del servidor actual es: {{t}}</strong>', t=time)

run(host="localhost", port=80)



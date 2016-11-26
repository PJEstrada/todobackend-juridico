from locust import HttpLocust, TaskSet, task

"""
def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")
"""
#prueba de los usuarios disponibles
def users_view(l):
    #obtener usuarios diponsibles
    l.client.get("/users-view")

#prueba de obtencion de expedientes
def get_expedientes(l):
    #obtener 10 expedientes por su id
    for i in range(10):
        #usar name para las estadisticas de locust
        l.client.get("/expediente/%i" % i, name="/expediente/id")


class GeneralBehavior(TaskSet):
    @task
    class UserBehavior(TaskSet):
        tasks = {users_view:2, get_expedientes:1}

    @task
    class UserBehavior2(TaskSet):
        tasks = {users_view:1, get_expedientes:2}

class WebsiteUser(HttpLocust):
    task_set = GeneralBehavior
    min_wait=5000
    max_wait=9000

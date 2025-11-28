from app.src.dao.task_dao import TaskDAO

class TaskService:
    def __init__(self, app):
        self.dao = TaskDAO(app)

    def get_all(self):
        return self.dao.find_all()
    
    def fetch_one(self, _filter={}):
        return self.dao.fetch_one(_filter)
    
    def fetch(self, _filter={}, skip=0, limit=0):
        return self.dao.fetch(_filter, skip=skip, limit=limit)

    def create(self, data):
        return self.dao.insert(data)

    def update(self, task_id, data):
        return self.dao.update(task_id, data)

    def delete(self, task_id):
        return self.dao.delete(task_id)

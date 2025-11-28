from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from app.src.utils.mongo_adapter import MongoAdapter
from uuid import uuid4


class TaskDAO:
    def __init__(self, app):
        client = MongoClient(app.config["MONGO_URI"])
        self.db = client[app.config["MONGO_DATABASE"]]
        self.collection = self.db.tasks
        self.collection.create_index("id", unique=True)
        self.mongo_adapter = MongoAdapter()
    
    def fetch(
        self,
        _filter = {},
        projection = None,
        exclude = True,
        skip = 0,
        limit = 0,
        sort = [("_id", -1)],
        **kwargs
    ):
        _filter = self.mongo_adapter.convert_id_filter(_filter)
        if projection:
            projection = {field: 0 if exclude else 1 for field in projection}
        cur = self.collection.find(
            _filter, 
            projection=projection, 
            skip=skip, 
            limit=limit, 
            sort=sort, 
            **kwargs
        )
        return self.mongo_adapter.serialize_cur(cur)

    def fetch_one(
        self,
        _filter = {},
        projection = None,
        exclude = True,
        **kwargs
    ):
        _filter = self.mongo_adapter.convert_id_filter(_filter)
        if projection:
            projection = {field: 0 if exclude else 1 for field in projection}
        doc = self.collection.find_one(_filter, projection=projection, **kwargs)
        return self.mongo_adapter.serialize_doc(doc) if doc else None

    def insert(self, data):
        data["id"] = str(uuid4())
        now = datetime.utcnow()
        data.update({
            "created_at": now,
            "updated_at": now
        })
        result = self.collection.insert_one(data)
        return self.mongo_adapter.serialize_doc({
            "_id": str(result.inserted_id),
            **data
        })

    def update(self, task_id, data):
        data["updated_at"] = datetime.utcnow()
        self.collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": data}
        )
        return {"updated": True}

    def delete(self, task_id):
        self.collection.delete_one({"_id": ObjectId(task_id)})
        return {"deleted": True}



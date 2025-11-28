import datetime
import json
from typing import Any, Dict, List
from bson import ObjectId


class MongoAdapter:
    
    def default_serializer(self, obj: Any) -> Any:
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif hasattr(obj, "__dict__"):
            return obj.__dict__
        else:
            return str(obj)

    def serialize_cur(self, cur: Any) -> List[Dict[str, Any]]:
        return [self.serialize_doc(doc) for doc in cur]

    def serialize_doc(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        return json.loads(json.dumps(doc, default=self.default_serializer))


    def convert_id_filter(self, _filter):
        if "_id" not in _filter:
            return _filter
        value = _filter["_id"]
        if isinstance(value, list):
            valid_ids = [
                ObjectId(v) for v in value 
                if isinstance(v, str) and ObjectId.is_valid(v)
            ]
            if valid_ids:
                _filter["_id"] = {"$in": valid_ids}
            return _filter
        if isinstance(value, str) and ObjectId.is_valid(value):
            _filter["_id"] = ObjectId(value)
        return _filter

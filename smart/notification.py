import datetime as d
import json

class notification:
    def __init__(self, time, name):
        if not isinstance(time, d.datetime):
            raise TypeError("time must be a datetime object")
        elif not isinstance(name, str):
            raise TypeError("name must be a str object")
        self.time = time
        self.name = name

    #Unverse method to the __str__ method of this class
    #constructs a notification object from a json
    @classmethod
    def from_json(cls, j):
        if not isinstance(j, str):
            raise TypeError("from_json requires a string input")
        try:
            string = json.loads(j)
            return cls(d.datetime.fromtimestamp(int(float(string["time"]))), string["name"])
        except KeyError as e:
            raise e
    
    def __eq__(self, other):
        if not isinstance(other, notification):
            raise TypeError("other object must be a notification object")
        if other.time != self.time:
            return False
        if other.name != self.name:
            return False
        return True
    
    def __dict__(self):
        return {"time": float(d.datetime.timestamp(self.time)), "name": self.name}

    def __str__(self):
        return json.dumps(self.__dict__())

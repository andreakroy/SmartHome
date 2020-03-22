import notification as n
import datetime as d
import json

class reminder(n.notification):
    def __init__(self, time, name, start=None, end=None, msg=None):
        if start == None:
            start = -1
        if end == None:
            end = -1
        super() .__init__(time, name)  
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be integer UNIX timestamps")
        if not isinstance(msg, str) and msg != None:
            raise TypeError("msg must be a string")
        current_time = d.datetime.now().timestamp()
        if start < current_time and start != -1:
            raise ValueError("start time must be after the current time")
        if end < current_time and end != -1:
            raise ValueError("end time must be after the current time")
        self.start = start
        self.end = end
        self.msg = msg

    @classmethod
    def from_json(cls, j):
        string = json.loads(j)
        msg = string["msg"]
        if msg == "null":
            msg = None
        return cls(int(string["time"]), string["name"],
                int(string["start"]), int(string["end"]), msg)

    def __dict__(self):
        result = super().__dict__()
        result["start"] = self.start
        result["end"] = self.end
        result["msg"] = self.msg
        return result

    def __str__(self):
        return json.dumps(self.__dict__())

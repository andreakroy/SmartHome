import json
import datetime as d
import notification as n
import reminder as r
from pathlib import Path

class master_calendar:
    def __init__(self, path=None):
        if path == None:
            self.notification_list = []
            return
        if Path(path).suffix != ".json":
            raise ValueError("The path must point to a valid json file.")
        temp = []
        try:
            with open(path, "r") as f:
                for i in json.load(f)["notifications"]:
                    try:
                        temp.append(r.reminder.from_json(i))
                    except ValueError as e:
                        continue
                    except TypeError as e:
                        continue
        except:
            self.notification_list = []
        
        self.notification_list = temp
    
    def __str__(self):
        str_lst = []
        for i in self.notification_list:
            str_lst.append(json.loads(i.__str__()))
        return json.dumps(str_lst)

x = master_calendar("cal.json")
print(x)

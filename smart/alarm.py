import json
import notification as n
import datetime as d

class alarm(n.notification):
    def __init__(self, time, name):
        super(alarm, self).__init__(time, name)

    @classmethod
    def from_json(cls, j):
        return super().from_json(j)

    def __eq__(self, other):
        if not isinstance(other, alarm):
            return False
        return super(alarm, self).__eq__(other)

    def __dict__(self):
        return super(alarm, self).__dict__()
    
    def __str__(self):
        return super(alarm, self).__str__()

x = alarm(int(d.datetime.now().timestamp()), "alarm")
y = alarm.from_json(x.__str__())
print(y)
print(x == y)

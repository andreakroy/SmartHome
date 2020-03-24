import json
import notification as n

class alarm(n.notification):
    def __init__(self, time, name):
        super(alarm, self).__init__(time, name)

    @classmethod
    def from_json(json):
        return super().from_json(json)

    def __eq__(self, other):
        if not isinstance(other, alarm):
            return False
        return super(alarm, self).__eq__(other)

    def __dict__(self):
        return super().__dict__()

    def __str__(self):
        return super().__str__()

x = alarm(123124235423, "wakeup")
print(x)

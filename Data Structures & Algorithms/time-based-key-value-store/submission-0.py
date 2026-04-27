class TimeMap:

    def __init__(self):
        self.key_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_dict:
            self.key_dict[key] = {}
        if timestamp not in self.key_dict[key]:
            self.key_dict[key][timestamp] = []
        self.key_dict[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_dict:
            return ""
        
        recent = 0
        for time in self.key_dict[key]:
            if time <= timestamp:
                recent = max(time, recent)
        
        return "" if recent == 0 else self.key_dict[key][recent][-1]

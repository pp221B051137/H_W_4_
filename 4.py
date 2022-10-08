class Time:
    def __init__(self,sec):
        self.sec = sec
    def convert_to_minutes(self):
        a = ""
        sec_int = int(self.sec)
        min = int(sec_int/60)
        sec_min = sec_int%60
        a = str(min)+":"+str(sec_min)
        return a
    def convert_to_hours(self):
        o = ""
        sec_int = int(self.sec)
        min = int(sec_int/60)
        sec_min = sec_int%60
        hours = int(min/60)
        o =str(hours)+":"+str(min)+":"+str(sec_min)
        return o
time = Time("230")
print(time.convert_to_minutes())
print(time.convert_to_hours())
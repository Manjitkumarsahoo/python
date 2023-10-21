class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __add__(self, other):
        sec = self.sec + other.sec
        min = self.min + other.min
        hr = self.hr + other.hr

        if min >= 60:
            hr += 1
            min -= 60

        if sec >= 60:
            min += 1
            sec -= 60

        return Time(hr, min, sec)  

    def __str__(self):
        return f"{self.hr:02d}:{self.min:02d}:{self.sec:02d}"

T1 = Time(2, 30, 45)
T2 = Time(1, 45, 30)

result = T1 + T2
print("Time 1:", T1)
print("Time 2:", T2)
print("Time 1 + Time 2:", result)

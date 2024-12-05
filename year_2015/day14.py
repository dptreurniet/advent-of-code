
class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

        self.is_flying = True
        self.time_in_state = 0
        self.distance_travelled = 0
        self.score = 0

    def step(self):
        self.time_in_state += 1
        if self.is_flying:
            self.distance_travelled += self.speed
            if self.time_in_state == self.fly_time: self.flip_state()
        else:
            if self.time_in_state == self.rest_time: self.flip_state()

    def flip_state(self):
        self.is_flying = not self.is_flying
        self.time_in_state = 0

    def __str__(self):
        return f'{self.name} is at {self.distance_travelled} and {['resting', 'flying'][self.is_flying]}'

def get_leading_reindeer(R):
    leading_dist = sorted([r.distance_travelled for r in R])[-1]
    return [r for r in R if r.distance_travelled == leading_dist]

def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]

    R = []
    for line in lines:
        s = line.split()
        name = s[0]
        speed = int(s[3])
        fly_time = int(s[6])
        rest_time = int(s[-2])
        R.append(Reindeer(name, speed, fly_time, rest_time))
    
    for _ in range(2503):
        for r in R:
            r.step()
        for r in get_leading_reindeer(R): r.score += 1

    yield get_leading_reindeer(R)[0].distance_travelled

    yield max([r.score for r in R])
    
    
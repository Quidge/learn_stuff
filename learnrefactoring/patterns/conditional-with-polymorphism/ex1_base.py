def plumages(birds):
    return [(bird['name'], plumage(bird)) for bird in birds]

def speeds(birds):
    return [(bird['name'], air_speed_velocity(bird)) for bird in birds]

def plumage(bird):
    return Bird(**bird).plumage

def air_speed_velocity(bird):
    return Bird(**bird).air_speed_velocity

class Bird:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def plumage(self):
        if self.type == 'EuropeanSwallow':
            return 'average'
        elif self.type == 'AfricanSwallow':
            return 'tired' if self.numberOfCoconuts > 2 else 'average'
        elif self.type == 'NorwegianBlueParrot':
            return 'scorched' if self.voltage > 100 else 'beautiful'
        else:
            return 'unknown'

    @property
    def air_speed_velocity(self):
        if self.type == 'EuropeanSwallow':
            return 35
        elif self.type == 'AfricanSwallow':
            return 40 - 2 * self.numberOfCoconuts
        elif self.type == 'NorwegianBlueParrot':
            return 0 if self.isNailed else 10 + int(self.voltage / 10)
        else:
            return None
    
    

def plumages(birds):
    return [(bird['name'], plumage(bird)) for bird in birds]


def speeds(birds):
    return [(bird['name'], air_speed_velocity(bird)) for bird in birds]


def plumage(bird):
    b = createBird(**bird)
    return b.plumage


def air_speed_velocity(bird):
    b = createBird(**bird)
    return b.air_speed_velocity


def createBird(**kwargs):
    if kwargs['type'] == 'EuropeanSwallow':
        return EuropeanSwallow(**kwargs)
    elif kwargs['type'] == 'AfricanSwallow':
        return AfricanSwallow(**kwargs)
    elif kwargs['type'] == 'NorwegianBlueParrot':
        return NorwegianBlueParrot(**kwargs)
    else:
        return Bird(**kwargs)

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


class EuropeanSwallow(Bird):
    pass


class AfricanSwallow(Bird):
    pass


class NorwegianBlueParrot(Bird):
    pass

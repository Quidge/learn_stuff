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
        return 'unknown'

    @property
    def air_speed_velocity(self):
        return None


class EuropeanSwallow(Bird):
    @property
    def plumage(self):
        return 'average'

    @property
    def air_speed_velocity(self):
        return 35


class AfricanSwallow(Bird):
    @property
    def plumage(self):
        return 'tired' if self.numberOfCoconuts > 2 else 'average'

    @property
    def air_speed_velocity(self):
        return 40 - 2 * self.numberOfCoconuts


class NorwegianBlueParrot(Bird):
    @property
    def plumage(self):
        return 'scorched' if self.voltage > 100 else 'beautiful'

    @property
    def air_speed_velocity(self):
        return 0 if self.isNailed else 10 + int(self.voltage / 10)

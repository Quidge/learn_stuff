def plumages(birds):
    return [(bird['name'], plumage(bird)) for bird in birds]

def speeds(birds):
    return [(bird['name'], air_speed_velocity(bird)) for bird in birds]

def plumage(bird):
    if bird['type'] == 'EuropeanSwallow':
        return 'average'
    elif bird['type'] == 'AfricanSwallow':
        return 'tired' if bird['numberOfCoconuts'] > 2 else 'average'
    elif bird['type'] == 'NorwegianBlueParrot':
        return 'scorched' if bird['voltage'] > 100 else 'beautiful'
    else:
        return 'unknown'

def air_speed_velocity(bird):
    if bird['type'] == 'EuropeanSwallow':
        return 35
    elif bird['type'] == 'AfricanSwallow':
        return 40 - 2 * bird['numberOfCoconuts']
    elif bird['type'] == 'NorwegianBlueParrot':
        return 0 if bird['isNailed'] else 10 + int(bird['voltage'] / 10)
    else:
        return None

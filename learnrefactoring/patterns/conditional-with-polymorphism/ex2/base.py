class Rating:
    def __init__(self, voyage, history):
        self.voyage = voyage
        self.history = history

    @property
    def value(self):
        vp_factor = self.voyage_profit_factor
        vr_factor = self.voyage_risk
        chr_factor = self.captain_history_risk
        print(vp_factor, vr_factor, chr_factor)
        if vp_factor * 3 > (vr_factor + chr_factor * 2):
            return "A"
        else:
            return "B"

    @property
    def voyage_risk(self):
        result = 1
        if self.voyage['length'] > 4:
            result += 2
        if self.voyage['length'] > 8:
            result += self.voyage['length'] - 8
        if self.voyage['zone'] in {'china', 'east-indies'}:
            result += 4
        return max(result, 0)

    @property
    def captain_history_risk(self):
        result = 1
        if len(self.history) < 5:
            result += 4
        result += len(
            [voyage for voyage in self.history if voyage['profit'] < 0])
        return max(result, 0)

    @property
    def voyage_profit_factor(self):
        result = 2
        if self.voyage['zone'] == "china":
            result += 1
        if self.voyage['zone'] == 'east-indies':
            result += 1
        result += self.voyage_length_factor
        result += self.history_length_factor

        return result

    @property
    def history_length_factor(self):
        return 1 if len(self.history) > 8 else 0

    @property
    def voyage_length_factor(self):
        return -1 if self.voyage['length'] > 14 else 0


class ExperiencedChinaRating(Rating):
    @property
    def captain_history_risk(self):
        result = super().captain_history_risk - 2
        return max(result, 0)

    @property
    def history_length_factor(self):
        return 1 if len(self.history) > 10 else 0

    @property
    def voyage_length_factor(self):
        # return 1 if between 12 and 19, else 0
        result = 0
        if self.voyage['length'] > 12:
            result += 1
        if self.voyage['length'] > 18:
            result -= 1
        return result

    @property
    def voyage_profit_factor(self):
        return super().voyage_profit_factor + 3


def rating(voyage, history):
    return createRating(voyage, history).value


def createRating(voyage, history):
    if voyage['zone'] == 'china' and any(
        [v['zone'] == 'china' for v in history]):
        return ExperiencedChinaRating(voyage, history)
    else:
        return Rating(voyage, history)

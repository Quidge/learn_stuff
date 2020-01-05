import pytest
import json
from ex1_base import plumages, plumage, speeds, air_speed_velocity


@pytest.fixture
def json_data():
    with open('ex1-data.json', 'r') as f:
        return json.load(f)


class TestPlumages:
    @pytest.fixture
    def _plumages(self, json_data):
        return plumages(json_data['birds'])

    def test_plumages(self, _plumages):
        assert _plumages == [('Bucky', 'average'), ('Remus', 'tired'),
                             ('Adrian', 'average'), ('Alex', 'scorched'),
                             ('Al', 'beautiful')]

class TestSpeeds:
    @pytest.fixture
    def _speeds(self, json_data):
        return speeds(json_data['birds'])

    def test_speeds(self, _speeds):
        assert _speeds == [('Bucky', 35), ('Remus', 34), ('Adrian', 38),
                           ('Alex', 0), ('Al', 15)]


class TestAirSpeedVelocity:
    @pytest.mark.parametrize("_input,expected",
                             [({
                                 "type": "EuropeanSwallow"
                             }, 35),
                              ({
                                  "type": "AfricanSwallow",
                                  "numberOfCoconuts": 3
                              }, 34),
                              ({
                                  "type": "NorwegianBlueParrot",
                                  "isNailed": True
                              }, 0),
                              ({
                                  "type": "NorwegianBlueParrot",
                                  "isNailed": False,
                                  "voltage": 200
                              }, 30), ({
                                  "type": "UnknownBird"
                              }, None)])
    def test_output_is_expected(self, _input, expected):
        assert air_speed_velocity(_input) == expected


class TestPlumage:
    @pytest.mark.parametrize("_input,expected",
                             [({
                                 "type": "EuropeanSwallow"
                             }, 'average'),
                              ({
                                  "type": "AfricanSwallow",
                                  "numberOfCoconuts": 3
                              }, 'tired'),
                              ({
                                  "type": "AfricanSwallow",
                                  "numberOfCoconuts": 1
                              }, 'average'),
                              ({
                                  "type": "NorwegianBlueParrot",
                                  'voltage': 60
                              }, 'beautiful'),
                              ({
                                  "type": "NorwegianBlueParrot",
                                  "voltage": 200
                              }, 'scorched'), ({
                                  "type": "UnknownBird"
                              }, 'unknown')])
    def test_output_is_expected(self, _input, expected):
        assert plumage(_input) == expected

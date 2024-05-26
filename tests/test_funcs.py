import pytest
from datetime import datetime
from coursework3.funcs import correct_data, json_to_list, five_operations


@pytest.mark.parametrize('list_dict, expected', [
    ([{}], []),
    ([{"date": "2019-04-04T23:20:05.206878", "state": "EXECUTED"}],
     [{"date": datetime.fromisoformat("2019-04-04T23:20:05.206878"), "state": "EXECUTED"}]),
    ([{"date": "2019-04-04T23:20:05.206878"}], []),
    ([{"state": "EXECUTED"}], []),
])
def test_correct_data(list_dict, expected):
    assert correct_data(list_dict) == expected


def test_json_to_list():
    with pytest.raises(FileNotFoundError):
        json_to_list('egegeg/error.txt')


def test_five_operations():
    assert five_operations([]) == []
    assert five_operations([
        {'date': 2},
        {'date': 3},
        {'date': -5},
        {'date': 11},
        {'date': 0},
        {'date': 4}
    ]) == [{'date': 11}, {'date': 4}, {'date': 3}, {'date': 2}, {'date': 0}]
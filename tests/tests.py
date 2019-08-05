"""
   Copyright 2019 Jacob Padley

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

This file contains tests for all of the classes in PyDrake
There is no way to test with live endpoint data, so these tests will test the
parsing capability of all functions using sample data.
"""
import sys
sys.path.append(".")
from pydrake.summonerv4 import Summoner
from pydrake.leaguev4 import RankedSummoner
from pydrake.matchv4 import MatchList, Match
from pydrake.errors import APIError
from pydrake.ddragon import *

import json


def get_attrs(obj):
    """
    Utility function to return all non-function variables in an object
    :param obj: The object to retrieve vars from
    :return: The vars found, excluding all methods
    """
    return [x for x in dir(obj) if not x.startswith('__') and not callable(getattr(obj, x))]


def has_null_attrs(obj):
    """
    Returns a boolean value based on whether any of this object's attributes is
    null or 'None'
    :param obj: The object to check
    :return: True if None attributes are found, else False
    """
    attrs = get_attrs(obj)
    null = [x for x in attrs if getattr(obj, x) is None]
    return len(null) > 0


def evaluate(obj):
    """
    Evaluates the object to see whether it has successfully parsed the data
    :param obj: Object to evaluate
    """
    if has_null_attrs(obj):
        raise ValueError("FAILURE: Null Attributes found!")
    else:
        print("SUCCESS")


# /summoner/v4/summoners/by-name
print("Now Testing: /summoner/v4/summoners/by-name")
with open("summoner-v4-summoners-by-name.json") as raw:
    data = json.loads(raw.read())

summoner = Summoner(data, "euw1")
evaluate(summoner)

# /league/v4/entries/by-summoner
print("Now Testing: /league/v4/entries/by-summoner")
with open("league-v4-entries-by-summoner.json") as raw:
    data = json.loads(raw.read())

evaluate(RankedSummoner(data, summoner))

# ddragon/champion.json
print("Now Testing: ddragon/champion.json")
with open("ddragon-champion.json") as raw:
    data = json.loads(raw.read())

evaluate(Champion(data['data']['Aatrox']))

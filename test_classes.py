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
from pydrake.summonerv4 import Summoner
from pydrake.leaguev4 import RankedSummoner
from pydrake.matchv4 import MatchList, Match
from pydrake.errors import APIError
from pydrake.ddragon import *

from os import path
import unittest
import json

here = path.join(path.abspath(path.dirname(__file__)), "tests/")


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


class TestClasses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(path.join(here, "summoner-v4-summoners-by-name.json")) as raw:
            cls.summonerv4byname = json.loads(raw.read())
        with open(path.join(here, "league-v4-entries-by-summoner.json")) as raw:
            cls.leaguev4bysummoner = json.loads(raw.read())
        with open(path.join(here, "ddragon-champion.json")) as raw:
            cls.ddragonchampions = json.loads(raw.read())
        with open(path.join(here, "match-v4-matches.json")) as raw:
            cls.matchv4matches = json.loads(raw.read())
        with open(path.join(here, "match-v4-matchlists-by-account.json")) as raw:
            cls.matchv4matchlists = json.loads(raw.read())

    def test_summoner_v4_summoners_by_name(self):
        summoner = Summoner(self.summonerv4byname, "euw1")
        self.assertFalse(has_null_attrs(summoner))

        self.assertEqual(summoner.name, "Janoccoli")
        self.assertEqual(summoner.region, "euw1")
        self.assertEqual(summoner.level, 103)

    def test_league_v4_entries_by_summoner(self):
        summoner = Summoner(self.summonerv4byname, "euw1")
        ranked = RankedSummoner(self.leaguev4bysummoner, summoner)
        self.assertFalse(has_null_attrs(ranked))

        solo = ranked.get_ranked_queue("RANKED_SOLO_5x5")
        self.assertFalse(has_null_attrs(solo))

        self.assertEqual(len(ranked._ranks), 2)

        self.assertEqual(solo.rank, 3)
        self.assertEqual(solo.tier, "BRONZE")

    def test_ddragon_champion(self):
        champions = self.ddragonchampions['data'].values()
        champion_objs = [Champion(x) for x in champions]
        self.assertEqual(len(champion_objs), 145)

        for x in champion_objs:
            self.assertFalse(has_null_attrs(x))

    def test_match_v4_matches(self):
        match = Match(self.matchv4matches)
        self.assertFalse(has_null_attrs(match))
        self.assertEqual(len(match.participants), 10)
        self.assertEqual(len(match.teams), 2)

    def test_match_v4_matchlists_by_account(self):
        matchlist = MatchList(self.matchv4matchlists)
        self.assertEqual(len(matchlist._matches), 100)
        self.assertFalse(has_null_attrs(matchlist))

        for x in matchlist._matches:
            self.assertFalse(has_null_attrs(x))


if __name__ == "__main__":
    unittest.main()


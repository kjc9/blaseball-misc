#!/usr/local/bin/python3

import json

DEFENSE = ["anticapitalism", "chasiness", "omniscience", "tenaciousness", "watchfulness"];
PITCHING = ["ruthlessness", "overpowerment", "unthwackability", "shakespearianism", "suppression", "coldness"];
BATTING = ["patheticism", "moxie", "divinity", "musclitude", "thwackability", "buoyancy", "martyrdom"];
BASE_RUNNING = ["base_thirst", "laserlikeness", "continuation", "ground_friction", "indulgence"];

HEADERS = ["name", "team"];

## Primary files
BATTING_FILE = open("../data/s14-batters.csv", "a")
PITCHING_FILE = open("../data/s14-pitching.csv", "a")
DEFENSE_FILE = open("../data/s14-defense.csv", "a")
BASE_RUNNING_FILE = open("../data/s14-base-running.csv", "a")
OFFENSE_FILE = open("../data/s14-offense.csv", "a")


with open('../data/players-20200314.json') as f:
  players = json.load(f)

prefix = "name,team,";
defense = "anticapitalism,chasiness,omniscience,tenaciousness,watchfulness";
pitching = "ruthlessness,overpowerment,unthwackability,shakespearianism,suppression,coldness";
batting = "patheticism,moxie,divinity,musclitude,thwackability,buoyancy,martyrdom";
base_running = "base_thirst,laserlikeness,continuation,ground_friction,indulgence";
offense = batting + "," + base_running;
BATTING_FILE.write(prefix + batting + "\n")
PITCHING_FILE.write(prefix + pitching + "\n")
DEFENSE_FILE.write(prefix + defense + "\n")
BASE_RUNNING_FILE.write(prefix + base_running + "\n")
OFFENSE_FILE.write(prefix + offense + "\n")


for player in players:
    team = player["team"];
    name = player["player_name"];
    if team is None or name is None:
        continue;

    #print(f"player={name}\tteam={team}");
    #print("\tBATTING");
    cur_prefix = name + "," + team;
    cur_batting = "";
    cur_pitching = "";
    cur_defense = "";
    cur_base_running = "";
    cur_offense = "";
    for x in BATTING:
        cur_batting = cur_batting + "," + player[x];
        #print(f"\t\t{x} = {player[x]}");
    for x in PITCHING:
        cur_pitching = cur_pitching + "," + player[x];
        #print(f"\t\t{x} = {player[x]}");
    for x in DEFENSE:
        cur_defense = cur_defense + "," + player[x];
        #print(f"\t\t{x} = {player[x]}");
    for x in BASE_RUNNING:
        cur_base_running = cur_base_running + "," + player[x];
        #print(f"\t\t{x} = {player[x]}");
    cur_offense = cur_batting + cur_base_running;

    BATTING_FILE.write(cur_prefix + cur_batting + "\n")
    PITCHING_FILE.write(cur_prefix + cur_pitching + "\n")
    DEFENSE_FILE.write(cur_prefix + cur_defense + "\n")
    BASE_RUNNING_FILE.write(cur_prefix + cur_base_running + "\n")
    OFFENSE_FILE.write(cur_prefix + cur_offense + "\n")
    

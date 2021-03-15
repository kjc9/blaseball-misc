#!/usr/local/bin/python3

import numpy as np
import csv
import operator
import itertools

DEFENSE = ["anticapitalism", "chasiness", "omniscience", "tenaciousness", "watchfulness"];
PITCHING = ["ruthlessness", "overpowerment", "unthwackability", "shakespearianism", "suppression", "coldness"];
BATTING = ["patheticism", "moxie", "divinity", "musclitude", "thwackability", "buoyancy", "martyrdom"];
BASE_RUNNING = ["base_thirst", "laserlikeness", "continuation", "ground_friction", "indulgence"];
OFFENSE = ["patheticism", "moxie", "divinity", "musclitude", "thwackability", "buoyancy", "martyrdom", "base_thirst", "laserlikeness", "continuation", "ground_friction", "indulgence"]; 

## Primary files
BATTING_FILE = open("../results/s14-batter-sim.txt", "a")
PITCHING_FILE = open("../results/s14-pitching-sim.txt", "a")
DEFENSE_FILE = open("../results/s14-defense-sim.txt", "a")
BASE_RUNNING_FILE = open("../results/s14-base-running-sim.txt", "a")
OFFENSE_FILE = open("../results/s14-offense-sim.txt", "a")

maxStat = {}
minStat = {}

def populate_ranges(input_file, stat_arr):
    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for x in stat_arr:
                if x not in minStat or float(row[x]) < minStat[x]:
                    minStat[x] = float(row[x]);
                if x not in maxStat or float(row[x]) > maxStat[x]:
                    maxStat[x] = float(row[x]);
        

def process(input_file, output_file, stat_arr):
    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        player_dict = {}
        for row in csv_reader:
            name = row["name"];
            team = row["team"];
            key = name + ":" + team;
            player_dict[key] = np.array([]);
            for x in stat_arr:
                float_val = float(row[x])
                new_val = (2.0 * ((float_val - minStat[x]) / (maxStat[x] - minStat[x]))) - 1.0
                player_dict[key] = np.append(player_dict[key], [new_val]);
                    
        sims = {}
        for key in player_dict:
            sims[key] = {}
            src = player_dict[key]
            for compare in player_dict:
                tgt = player_dict[compare]
                cos_sim=np.dot(src,tgt)/(np.linalg.norm(src)*np.linalg.norm(tgt))
                sims[key][compare] = cos_sim
                            
            d = dict(sorted(sims[key].items(), key=operator.itemgetter(1),reverse=True))
            output_file.write(f"\n{key}\n")
            x = itertools.islice(d.items(), 0, 11)
            for k, v in x:
                if k != key:
                    output_file.write(f"\t{k} == {v}\n")
        

populate_ranges("../data/s14-batters.csv", BATTING)
process("../data/s14-batters.csv", BATTING_FILE, BATTING)
maxStats = {}
minStats = {}
populate_ranges("../data/s14-pitching.csv", PITCHING)
process("../data/s14-pitching.csv", PITCHING_FILE, PITCHING)
maxStats = {}
minStats = {}
populate_ranges("../data/s14-defense.csv", DEFENSE)
process("../data/s14-defense.csv", DEFENSE_FILE, DEFENSE)
maxStats = {}
minStats = {}
populate_ranges("../data/s14-base-running.csv", BASE_RUNNING)
process("../data/s14-base-running.csv", BASE_RUNNING_FILE, BASE_RUNNING)
maxStats = {}
minStats = {}
populate_ranges("../data/s14-offense.csv", OFFENSE)
process("../data/s14-offense.csv", OFFENSE_FILE, OFFENSE)

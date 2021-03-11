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
BATTING_FILE = open("../results/s13-batter-sim.txt", "a")
PITCHING_FILE = open("../results/s13-pitching-sim.txt", "a")
DEFENSE_FILE = open("../results/s13-defense-sim.txt", "a")
BASE_RUNNING_FILE = open("../results/s13-base-running-sim.txt", "a")
OFFENSE_FILE = open("../results/s13-offense-sim.txt", "a")

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
                player_dict[key] = np.append(player_dict[key], [float(row[x])]);
                    
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
        


process("../data/s13-batters.csv", BATTING_FILE, BATTING)
process("../data/s13-pitching.csv", PITCHING_FILE, PITCHING)
process("../data/s13-defense.csv", DEFENSE_FILE, DEFENSE)
process("../data/s13-base-running.csv", BASE_RUNNING_FILE, BASE_RUNNING)
process("../data/s13-offense.csv", OFFENSE_FILE, OFFENSE)

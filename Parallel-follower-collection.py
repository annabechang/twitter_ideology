
import twarc 
import pandas as pd 
from tqdm.notebook import tqdm
import time, random
import datetime
import json 
import glob
import os.path
from os import path
import itertools 
import requests, csv
from datetime import date


import multiprocessing
import time
import concurrent.futures 

import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())

import json
import requests
from threading import Thread

import random

# users = a list of user names that haven't been collected

key = secrets[1]

for user in tqdm(random.sample(users,len(users))):
    print(f"username = {user}")
    if path.exists(f"./follower/{user}.json"):

        print(f"Data for {user} already exist!")   

    else:
        !twarc2  --bearer-token "$key"  followers "$user" ./follower/{user}.json
        print(f"Data for {user} collected!")   
        

    # set time to sleep before gathering next user
    # once done print statement indicating so
    print(f"Data for {user} gathered! ")



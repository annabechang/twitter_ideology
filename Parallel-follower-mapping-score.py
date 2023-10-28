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
import pickle

from pandas.plotting import parallel_coordinates
import json
import requests
from threading import Thread

import multiprocessing
import time
import concurrent.futures 

import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())


use_cols_fl = ['username', 'name', 'id', 'landmark', 'phi', 'minmax']
use_cols_video = ['author.id', 'author.username', 'author.name']

files = tar['add'].tolist()
folder = "./yt_follower_mapping"

def tweet_convert(file):
    print(file)
    try: 
        video = pd.read_csv(file, usecols=use_cols_video)
        fquery = file.split("/")[2][:-4]
        video["query"] = fquery
        video = video.rename(columns={'author.id': "id", 'author.username': "username",'author.name':"name"})
        try:



            following = pd.DataFrame()

            for row in tqdm(video.itertuples()):
                dest_folder = "./follower-mapping/"+row.username[:5]+"/"
                dest_f_name = dest_folder+row.username+".csv"
                f_name = row.username+".csv"
                
                if path.exists(dest_f_name):
                    tmp = pd.read_csv(dest_f_name,index_col=0).drop_duplicates()
                    tmp = tmp[use_cols_fl]
                    
                    following = following.append(tmp,ignore_index = True).drop_duplicates()
            
            if len(following!=0):
                print(video.columns)
                print(following.columns)
                
                total2 = pd.merge(video, following, how="left", on=["id"])
                print(total2)

                total2 = total2.drop_duplicates()
                video_dest_f_name = folder + "/"+fquery +".csv"
                total2.to_csv(video_dest_f_name)
                print("finished",video_dest_f_name)

        except Exception as e:
            print(e)
    except KeyboardInterrupt as e:
                raise e
    except Exception as e:
        pass

        


with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:

    
    results = list(tqdm(executor.map(tweet_convert, files) ))
    for result in results:
        print(result)

out = []
for i, future in tqdm(enumerate(results)):
    try:
        out.append(future.result())
    except Exception as e:
        out.append(e)
        

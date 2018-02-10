import pandas as pd
from multiprocessing import Pool
import tqdm
import numpy as np
import os
import glob as glob
from skimage.io import imread
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--params', nargs = '*', dest = 'params', help = 'topcoder args', default = argparse.SUPPRESS)
args = parser.parse_args()

param_list = args.params
param_list =[(directory.replace('data/','wdata/')) for directory in param_list]
# remove the last param
param_list = param_list[:-1]

path_prefix = param_list[0][0:param_list[0].rfind("/")]
if path_prefix[0]=='/':
    path_prefix = path_prefix[1:]
folders = [(folder.split('/')[-1]) for folder in param_list]

print('Extracting metadata data from folders    : {}'.format(param_list))
print('Path prefix initiated for pre-processing : {}'.format(path_prefix))
print('Folder list initiated for pre-processing : {}'.format(folders))
time.sleep(3)

imgs = []

prefix_dict = {
    'mul': 'MUL',
    'muls': 'MUL-PanSharpen',
    'pan': 'PAN',
    'rgbps': 'RGB-PanSharpen',    
}

for folder in folders:
    for prefix in prefix_dict.items():
        g = glob.glob(path_prefix+'/{}/{}/*.tif'.format(folder,prefix[1]))
        imgs.extend(g)
        
img_folders = [(img.split('/')[-3]) for img in imgs]
img_subfolders = [(img.split('/')[-2]) for img in imgs]   
img_files = [(img.split('/')[-1]) for img in imgs]   

def extract_meta_data(img_path):
    try:
        img = imread(img_path)
        statinfo = os.stat(img_path)
        try:
            num_channels = img.shape[2]
        except:
            num_channels = 1
        stats = [img.shape[0], img.shape[1],num_channels,statinfo.st_size,statinfo.st_ctime,statinfo.st_mtime]
    except:
        stats = [0,0,0,0,0,0]
        
    return stats
    

with Pool(11) as p:
    img_meta_data = list(tqdm.tqdm(p.imap(extract_meta_data, imgs), total=len(imgs)))

# transpose the list
img_meta_data = list(map(list, zip(*img_meta_data)))

meta_df = pd.DataFrame()
for i,key in enumerate(['width','height','channels','im_size','ctime','mtime']):
    meta_df[key] = img_meta_data[i]
    
meta_df['img_files'] = img_folders
meta_df['img_folders'] = img_subfolders
meta_df['img_subfolders'] = img_files

meta_df.to_csv('metadata.csv')

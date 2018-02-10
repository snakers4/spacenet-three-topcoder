import argparse
from distutils.dir_util import copy_tree
import time
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--params', nargs = '*', dest = 'params', help = 'topcoder args', default = argparse.SUPPRESS)
args = parser.parse_args()

param_list = args.params
  
# param_list = ['/data/AOI_3_Paris_Roads_Train']

from_directories = [(directory.replace('/data/','data/')) for directory in param_list]
to_directories = [(directory.replace('/data/','wdata/')) for directory in param_list]

print('Copying from directories {}'.format(from_directories))
print('Copying to   directories {}'.format(to_directories))
time.sleep(3)

with tqdm.tqdm(total=len(from_directories)) as pbar:
    for fr,to in zip(from_directories,to_directories):
        copy_tree(fr, to)
        pbar.update(1)
    
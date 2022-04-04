import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    
    full_dataset = os.listdir(os.path.join(data_dir,"training_and_validation"))
    dataset_size = len(full_dataset)

    train_size = int(0.7 * dataset_size) #test_size = 1-train_size
    test_size = int(0.15 * dataset_size) 
    val_size = int(0.15 * dataset_size) 
    random.shuffle(full_dataset)

    #train data
    for filename in full_dataset[:train_size]:
        os.rename(os.path.join(data_dir,"training_and_validation",filename), os.path.join(data_dir,"train",filename))
    #val data
    for filename in full_dataset[train_size:train_size+val_size]:
        os.rename(os.path.join(data_dir,"training_and_validation",filename), os.path.join(data_dir,"val",filename))
    #test data
    for filename in full_dataset[train_size+val_size:]:
        os.rename(os.path.join(data_dir,"training_and_validation",filename), os.path.join(data_dir,"test",filename))



if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)
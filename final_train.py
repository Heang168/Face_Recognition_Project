import train_main as train
import data_preprocess as process
import time

process._data_preprocessing()
print("wating for training images......")
time.sleep(3)
train._train_img()
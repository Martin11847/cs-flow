import pathlib
import csv
from sklearn.model_selection  import train_test_split
import argparse
from shutil import copy2
import config as c

def save_csv(save_name):
    file = open(save_name,'w')
    csv_writer =csv.writer(file)
    for row in train:
        csv_writer.writerow([row.name])
    file.close()

def read_from_csv(filename):
    train_set_csv = open(filename,'r')
    train_set_names = [row[0] for row in csv.reader(train_set_csv)]
    train_set_csv.close()
    return train_set_names

def mk_mvtecdataset_directory(datasetpath,train_set_names):
    dataToAdd = pathlib.Path(datasetpath)
    dataToAdd.mkdir(parents=True, exist_ok=True)
    
    train_directory = dataToAdd.joinpath("train/good")
    train_directory.mkdir(parents=True,exist_ok=True)
    
    test_directory = dataToAdd.joinpath("test")
    test_directory.mkdir(parents=True,exist_ok=True)

    for images_folder in dataImages.iterdir():
        if 'good' in images_folder.name:
            for image in images_folder.iterdir():
                if image.name in train_set_names:
                    #print('HEHE')
                    copy2(image,train_directory.joinpath(image.name))
                else :
                    test_directory.joinpath(images_folder.name).mkdir(exist_ok=True)
                    #print(test_directory)
                    copy2(image,test_directory.joinpath(images_folder.name).joinpath(image.name))         
        else :
            test_directory.joinpath(images_folder.name).mkdir(exist_ok=True)
            for image in images_folder.iterdir():
                copy2(image, test_directory.joinpath(images_folder.name).joinpath(image.name))

if c.to_create :
    dataImages = pathlib.Path(c.orig_dataset_path)
    class_name =  dataImages.name
    imNames = [im for im in dataImages.joinpath('good').glob('*')]
    train, test = train_test_split(imNames,train_size=c.training_set_size)
    save_csv(c.class_name+'_trainig_set_'+str(c.training_set_size)+'.csv')
    train = read_from_csv(c.class_name+'_trainig_set_'+str(c.training_set_size)+'.csv')
    mk_mvtecdataset_directory(c.dataset_path+'/'+c.class_name+str(c.training_set_size),train)

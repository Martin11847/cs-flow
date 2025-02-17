# CS-Flow

This is the code to the WACV 2022 paper "[Fully Convolutional Cross-Scale-Flows for Image-based Defect Detection](
https://arxiv.org/pdf/2110.02855.pdf)" by Marco Rudolph, Tom Wehrbein, Bodo Rosenhahn and Bastian Wandt.

## Getting Started

You will need [Python 3.6](https://www.python.org/downloads) and the packages specified in _requirements.txt_.
We recommend setting up a [virtual environment with pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
and installing the packages there.

Install packages with:

```
$ pip install -r requirements.txt
```

## Configure and Run

All configurations concerning data, model, training, visualization etc. can be made in _config.py_. The default configuration will run a training with paper-given parameters on the provided dummy dataset. This dataset contains images of 4 squares as normal examples and 4 circles as anomaly.

To extract features, run extract_features.py (this was already done here for the dummy dataset, features were extracted to data/features).
To start the training, just run _main.py_!
Please report us if you have issues when using the code.

## Data

The given dummy dataset shows how the implementation expects the construction of a dataset. Coincidentally, the [MVTec AD dataset](https://www.mvtec.com/de/unternehmen/forschung/datasets/mvtec-ad/) is constructed in this way.

Set the variables _dataset_path_ and _class_name_ in _config.py_ to run experiments on a dataset of your choice. The expected structure of the data is as follows:

``` 
train data:

        dataset_path/class_name/train/good/any_filename.png
        dataset_path/class_name/train/good/another_filename.tif
        dataset_path/class_name/train/good/xyz.png
        [...]

test data:

    'normal data' = non-anomalies

        dataset_path/class_name/test/good/name_the_file_as_you_like_as_long_as_there_is_an_image_extension.webp
        dataset_path/class_name/test/good/did_you_know_the_image_extension_webp?.png
        dataset_path/class_name/test/good/did_you_know_that_filenames_may_contain_question_marks????.png
        dataset_path/class_name/test/good/dont_know_how_it_is_with_windows.png
        dataset_path/class_name/test/good/just_dont_use_windows_for_this.png
        [...]

    anomalies - assume there are anomaly classes 'crack' and 'curved'

        dataset_path/class_name/test/crack/dat_crack_damn.png
        dataset_path/class_name/test/crack/let_it_crack.png
        dataset_path/class_name/test/crack/writing_docs_is_fun.png
        [...]

        dataset_path/class_name/test/curved/wont_make_a_difference_if_you_put_all_anomalies_in_one_class.png
        dataset_path/class_name/test/curved/but_this_code_is_practicable_for_the_mvtec_dataset.png
        [...]
``` 

## Credits

Some code of an old version of the [FrEIA framework](https://github.com/VLL-HD/FrEIA) was used for the implementation of Normalizing Flows. Follow [their tutorial](https://github.com/VLL-HD/FrEIA) if you need more documentation about it.


## Citation
Please cite our paper in your publications if it helps your research. Even if it does not, you are welcome to cite us.

        @inproceedings { RudWeh2022,
        author = {Marco Rudolph and Tom Wehrbein and Bodo Rosenhahn and Bastian Wandt},
        title = {Fully Convolutional Cross-Scale-Flows for Image-based Defect Detection},
        booktitle = {Winter Conference on Applications of Computer Vision (WACV)},
        year = {2022},
        url = {arxiv},
        month = jan
        }

        
## License

This project is licensed under the MIT License.

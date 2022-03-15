'''This file configures the training procedure because handling arguments in every single function is so exhaustive for
research purposes. Don't try this code if you are a software engineer.'''

# device settings
device = 'cuda'  # or 'cpu'

# data settings
orig_dataset_path = "../../Datasets/OD2_dataset/linear_color"
dataset_path = "data/images"  # parent directory of datasets
class_name = "MEMS_chip_"  # dataset subdirectory
modelname = "NFFA_MEMS_chip_convnext_test"  # export evaluations/logs with this name
to_create = True
training_set_size = 50
pre_extracted = False  # were feature preextracted with extract_features?

img_size = (1024, 768)  # image size of highest scale, others are //2, //4
img_dims = [1] + list(img_size)

# transformation settings
norm_mean, norm_std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

# network hyperparameters
n_scales = 3  # number of scales at which features are extracted, img_size is the highest - others are //2, //4,...
clamp = 3  # clamping parameter
max_grad_norm = 1e0  # clamp gradients to this norm
n_coupling_blocks = 3  # higher = more flexible = more unstable
fc_internal = 768  # * 4 # number of neurons in hidden layers of s-t-networks
lr_init = 2e-4  # inital learning rate
use_gamma = True

extractor = "effnetB5"  # feature dataset name (which was used in 'extract_features.py' as 'export_name')
#extractor = 'convnext_tiny'
# extractor = "resnet18"
#extractor = "resnext101"
n_feat = {"effnetB5": 304, "resnet18": 304, "resnext101":304, 'convnext_tiny':768 }[extractor]  # dependend from feature extractor
map_size = (img_size[0] // 32, img_size[1] // 32)

# dataloader parameters
load_pretrained = False
batch_size = 1 # actual batch size is this value multiplied by n_transforms(_test)
kernel_sizes = [3] * (n_coupling_blocks - 1) + [5]

# total epochs = meta_epochs * sub_epochs
# evaluation after <sub_epochs> epochs
meta_epochs = 3  # total epochs = meta_epochs * sub_epochs
sub_epochs = 20  # evaluate after this number of epochs

# output settings
verbose = True
hide_tqdm_bar = False
save_model = True

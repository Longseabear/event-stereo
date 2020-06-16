import os
import torch
import torch.utils.data as datalodaer
import torch
import torchvision.transforms as transforms
import random
from PIL import Image, ImageOps, ImageChops

import numpy as np
import matplotlib.pyplot as plt

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

class SceneflowGradientLoader(datalodaer.Dataset):
    def __init__(self):


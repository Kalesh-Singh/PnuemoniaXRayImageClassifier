#!/usr/bin/env python
# coding: utf-8

# In[129]:


# Required modules and imports
from PIL import Image
from glob import glob
import os


# In[130]:


# Expected file structure for raw data

# . |-data |-chest_xray_raw |-test  |- NORMAL
#                                   |- PNUEMONIA
#                           |-train |- NORMAL
#                                   |- PNUEMONIA
#                           |-val   |- NORMAL
#                                   |- PNUEMONIA


# In[131]:


# Store processed data in the following file structure

# . |-data |-chest_xray_processed |-test  |- NORMAL
#                                         |- PNUEMONIA
#                                 |-train |- NORMAL
#                                         |- PNUEMONIA
#                                 |-val   |- NORMAL
#                                         |- PNUEMONIA


# In[132]:


# Constants
RAW_IMG_DIRS = [
    './data/chest_xray_raw/test/NORMAL',
    './data/chest_xray_raw/test/PNEUMONIA',
    './data/chest_xray_raw/train/NORMAL',
    './data/chest_xray_raw/train/PNEUMONIA',
    './data/chest_xray_raw/val/NORMAL',
    './data/chest_xray_raw/val/PNEUMONIA'
]

PROCESSED_IMG_DIR = 'chest_xray_processed'

IMG_WIDTH = 244
IMG_HEIGHT = 244
IMG_EXT = 'jpeg'

SUCCESS_MSG = 'Sucessfully resized and saved new images in ./data/' + PROCESSED_IMG_DIR + '/'


# In[133]:


def getProcessedPath(rawPath):
    """Returns the path to save the resized image."""
    rawPath = rawPath.replace('\\', '/')
    dirs = rawPath.split('/')
    dirs[2]= PROCESSED_IMG_DIR
    new_dir = '/'.join(dirs[:-1])
    if not os.path.exists(new_dir):
            os.makedirs(new_dir)
    return '/'.join(dirs)


# In[134]:


def resizeAndSaveImg(path):
    """Resizes and saves the image."""
    img = Image.open(path)
    img = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
    img.save(getProcessedPath(path))


# In[126]:


def resizeAllImages():
    """Resizes all the raw images."""
    for _dir in RAW_IMG_DIRS:
        img_paths = glob(_dir + '/*.' + IMG_EXT)
        for path in img_paths:
            resizeAndSaveImg(path)
    print(SUCCESS_MSG)


# In[127]:


resizeAllImages()


# In[ ]:





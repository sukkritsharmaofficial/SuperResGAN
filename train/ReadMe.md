# Training your custom model :fire:
<br>

## Preparing Data
#### 1. Download Dataset from the following link : 
https://drive.google.com/open?id=0B7EVK8r0v71pZjFTYXZWM3FlRnM

And save the dataset to data folder

#### 2. Run following command to unzip and place the files in the required folder
```bash
pytho3 unzip.py
```

## Training
Since we cannot practically train for longer time limiting training to 1000 images and 20 epochs

#### Keeping only 1000 images
```python
# run python3 limit.py
import os
path = "data/img_align_celeba"
for filename in os.listdir(path):
  count1 +=1
  if count1 > 1000:
    name = path + '/' + filename
    os.unlink(name)
    count2 += 1
```
#### To train for limited photos say 1000 images run :
```python
python3 ESRGAN.py --n_epoch 10 --checkpoint_interval 100
```

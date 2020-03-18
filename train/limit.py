import os
path = "data/img_align_celeba"
for filename in os.listdir(path):
  count1 +=1
  if count1 > 1000:
    name = path + '/' + filename
    os.unlink(name)
    count2 += 1
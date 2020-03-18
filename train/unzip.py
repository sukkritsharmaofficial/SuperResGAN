import zipfile

file_path = "data/img_aligh_celeba.zip"
save_path = "data/img_align_celeba"

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(save_path)


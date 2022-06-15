from PIL import Image
import os
from tqdm import tqdm

def remove_existing_folder(original_dir):
    if os.path.exists(f'{original_dir}Processed/'):
        os.system(f'rm -rf {original_dir}Processed/')

def get_file_list(original_dir, number_of_slices):
    file_list = list()
    real_list = list()
    for name in os.listdir(original_dir):
        if not name.startswith('.'):
            if name.endswith('.jpg'):
                file_list.append(f'{original_dir}{name}')
    file_list.sort()
    print(f"{len(file_list)} images have been identified.")
    current_img = 0
    counter = (len(file_list) - 1) // (number_of_slices - 1)
    for _ in list(range(number_of_slices)):
        real_list.append(file_list[current_img])
        current_img += counter
    print(f'{len(real_list)} images have been selected for further steps.')
    return real_list

def image_crop(file_list, original_dir, number_of_slices):
    print('Start cropping images...')
    width, height = Image.open(file_list[0]).size
    cut_threshold = round(width / number_of_slices - 0.5)
    left = 0
    top = 0
    bottom = height
    right = cut_threshold
    i = 0
    if os.path.exists(f'{original_dir}processed/') == False:
        os.mkdir(f'{original_dir}processed/')
    for each_pic in tqdm(file_list):
        pic_name = each_pic.split('/')[-1]
        pic = Image.open(each_pic)
        image_new = pic.crop((left,top,right,bottom))
        left += cut_threshold + 1
        right = left + cut_threshold
        image_new.save(f'{original_dir}processed/{pic_name}', quality = 100)
        i += 1
    print(f"Cropping completed. Cropped files saved under {original_dir}processed/")


def stitcher(original_dir, number_of_slices):
    print('Start stitching...')
    file_list = list()
    for name in os.listdir(f'{original_dir}Processed/'):
        if not name.startswith('.'):
            file_list.append(f'{original_dir}Processed/{name}')
    file_list.sort()
    images = [Image.open(x) for x in file_list]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 1
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    if os.path.exists(f'{original_dir}Final/') == False:
        os.mkdir(f'{original_dir}Final/')
    new_im.save(f'{original_dir}Final/FinalResult_{number_of_slices}.jpg', quality=100)
    print(f'Image successfully exported to {original_dir}Final/FinalResult_{number_of_slices}.jpg')

def slicer(original_dir: str, number_of_slices: int=22):
    if original_dir[-1] != "/":
        original_dir += '/'
    remove_existing_folder(original_dir)
    file_list = get_file_list(original_dir, number_of_slices)
    image_crop(file_list, original_dir, number_of_slices)
    stitcher(original_dir, number_of_slices)
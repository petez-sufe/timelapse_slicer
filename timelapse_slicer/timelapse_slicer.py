"""
This is an automated program for photographers who want to create TimeSlice pictures
without installing PS plugins. It will output a folder named "Processed" with two files:
Final_result.jpg and Final_result_gradient.jpg.
The first file is the final result of the TimeSlice. The second file is the gradient version of the
final result.
"""

import os
import numpy as np
from PIL import Image
from tqdm import tqdm

def remove_existing_folder(original_dir):
    """
    This function removes the existing processed folder if it exists.
    """
    if os.path.exists(f'{original_dir}Processed/'):
        os.system(f'rm -rf {original_dir}Processed/')

def get_file_list(original_dir, number_of_slices):
    """
    This function returns a list of all the files in the original directory.
    """
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

def get_gradient_2d(start, stop, width, height, is_horizontal):
    """
    This function returns a 2D gradient.
    """
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    """
    This function returns a 3D gradient.
    """
    result = np.zeros((height, width, len(start_list)), dtype=float)
    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)
    return result

def generate_mask(file_list):
    """
    This function generates a mask for the images.
    """
    width, height = Image.open(file_list[0]).size
    array = get_gradient_3d(width//(len(file_list)-1), height, (255, 255, 255), (0, 0, 0), (True, True, True))
    Image.fromarray(np.uint8(array)).save('gray_gradient_h.jpg', quality=100)

def image_crop(file_list, original_dir, number_of_slices, mode: str='single'):
    """
    This function slices the original images.
    """
    width, height = Image.open(file_list[0]).size
    left = 0
    top = 0
    bottom = height
    i = 0
    if mode == 'single':
        cut_threshold = width // number_of_slices
        right = cut_threshold
        print('Start cropping images in single image mode...')
        if os.path.exists(f'{original_dir}processed/') is False:
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
    if mode == 'multi':
        cut_threshold = width // (number_of_slices - 1)
        right = cut_threshold
        mask = Image.open('gray_gradient_h.jpg').convert('L')
        print(mask.size)
        print("Start cropping images in multi image mode...")
        if os.path.exists(f'{original_dir}processedmulti/') is False:
            os.mkdir(f'{original_dir}processedmulti/')
        for i in tqdm(range(number_of_slices-1)):
            pic_name = file_list[i].split('/')[-1]
            im_1= Image.open(file_list[i])
            im_1_crop = im_1.crop((left,top,right,bottom))
            im_2 = Image.open(file_list[i+1])
            im_2_crop = im_2.crop((left,top,right,bottom))
            im_all = Image.composite(im_1_crop, im_2_crop, mask.resize(im_1_crop.size))
            im_all.save(f'{original_dir}processedmulti/{pic_name}', quality = 100)
            left += cut_threshold + 1
            right = left + cut_threshold
            i += 1
        print(f"Cropping completed. Cropped files saved under {original_dir}processedmulti/")


def stitcher(original_dir, number_of_slices):
    """
    This function stitches the images together.
    """
    print('Start stitching...')
    file_list = []
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
    for image in images:
        new_im.paste(image, (x_offset,0))
        x_offset += image.size[0]
    if os.path.exists(f'{original_dir}Final/') is False:
        os.mkdir(f'{original_dir}Final/')
    new_im.save(f'{original_dir}Final/FinalResult_{number_of_slices}.jpg', quality=100)
    print(f'Image successfully exported to {original_dir}Final/FinalResult_{number_of_slices}.jpg')
    file_list = []
    for name in os.listdir(f'{original_dir}Processedmulti/'):
        if not name.startswith('.'):
            file_list.append(f'{original_dir}Processedmulti/{name}')
    file_list.sort()
    images = [Image.open(x) for x in file_list]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 1
    for image in images:
        new_im.paste(image, (x_offset,0))
        x_offset += image.size[0]
    if os.path.exists(f'{original_dir}Final/') is False:
        os.mkdir(f'{original_dir}Final/')
    new_im.save(f'{original_dir}Final/FinalResult_{number_of_slices}_Gradient.jpg', quality=100)
    print(f'Image successfully exported to {original_dir}Final/FinalResult_{number_of_slices}_Gradient.jpg')

def slicer(original_dir: str, number_of_slices: int=22):
    """
    This function slices the images into desired number of slices.
    :param str original_dir: the directory of the original images
    :param int number_of_slices: the number of slices
    """
    if original_dir[-1] != "/":
        original_dir += '/'
    remove_existing_folder(original_dir)
    file_list = get_file_list(original_dir, number_of_slices)
    generate_mask(file_list)
    image_crop(file_list, original_dir, number_of_slices, mode='single')
    image_crop(file_list, original_dir, number_of_slices, mode='multi')
    stitcher(original_dir, number_of_slices)

slicer('/Users/Peter/Downloads/Timeslice', 22)
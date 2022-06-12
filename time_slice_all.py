from PIL import Image
import os
import math

original_dir = 'YOUR_PATH_HERE/'
number_of_slices = 'YOUR_NUMBER_HERE'

def remove_existing_folder():
    if os.path.exists(f'{original_dir}Processed/'):
        os.system(f'rm -rf {original_dir}Processed/')

def get_file_list():
    file_list = list()
    real_list = list()
    for name in os.listdir(original_dir):
        if not name.startswith('.'):
            file_list.append(f'{original_dir}{name}')
    file_list.sort()
    current_img = 0
    counter = math.floor((len(file_list) - 1)/(number_of_slices - 1))
    for i in list(range(number_of_slices)):
        real_list.append(file_list[current_img])
        current_img += counter
    return real_list

def image_crop(file_list):
    width, height = Image.open(file_list[0]).size
    cut_threshold = round(width / number_of_slices - 0.5)
    left = 0
    top = 0
    bottom = height
    right = cut_threshold
    counter = 0
    i = 0
    if os.path.exists(f'{original_dir}processed/') == False:
        os.mkdir(f'{original_dir}processed/')
    for each_pic in file_list:
        pic_name = each_pic.split('/')[-1]
        pic = Image.open(each_pic)
        image_new = pic.crop((left,top,right,bottom))
        left += cut_threshold + 1
        right = left + cut_threshold
        image_new.save(f'{original_dir}processed/{pic_name}', quality = 100)
        i += 1


def stitcher():
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

def main():
    remove_existing_folder()
    file_list = get_file_list()
    image_crop(file_list)
    stitcher()

main()
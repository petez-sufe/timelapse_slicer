# Timelapse Slicer

## What is this? 这是什么？

This is an automated program for photographers who want to create TimeSlice pictures without installing PS plugins.

这是一个帮助摄影师使用延时摄影照片自动化生成时间切片的python程序。使用此程序无需安装PS插件。

ver 2.0.0 update:

New feature added. Now this program can generate slicelapse photo sequence. A demo video can be found [Here](https://youtu.be/I7bmBJokcgU)

2.0.0 版本更新内容：

新增时间切片延时序列生成功能。[演示视频](https://youtu.be/I7bmBJokcgU)

&nbsp;

## Before using this tool 在使用这个程序之前

Use Lightroom or other photo editing program to process the entire timelapse sequence and move all the colorgraded pictures (jpg) to one folder. LRTimelapse is recommended.

使用LR或者其他图片修改软件处理延时摄影序列并导出为JPG格式，将他们放在一个文件夹中。推荐LR配合LRTimelapse使用。

All the picture files should have the same dimensions.

注意：所有照片需要拥有相同的尺寸。

&nbsp;

## How to use this tool 如何使用这个程序

1. Install the package. 在终端输入命令

    ```python
    !pip install timelapse_slicer
    ```

2. Import package and run the program. 导入包，设置参数，运行程序

    ```python
    from timelapse_slicer import timelapse_slicer
    timelapse_slicer.slicer(original_dir, number_of_slices, mode, ignore_mode)

    Parameters 参数:
    original_dir="YOUR FILE PATH 文件夹路径" 
    number_of_slices="INTEGER 切片数量" default=22
    mode="standard/gradient/timelapse/all" default=all
    ignore_mode="early/late" 为提高切片质量，程序会自动忽略部分图片，可选择序列前或后。
    ```

    模式说明 Mode:

    standard: Only standard time-slice image will be generated. 程序仅生成标准时间切片。

    gradient: Only gradient time-slice image will be generated. 程序仅生成无痕渐变时间切片。

    timelapse: Gradient time-slice image will be generated and slice-lapse sequence will be generated. 程序生成渐变时间切片及延时摄影序列。

    all (default默认): Standard, gradient time-slice images will be generated as well as slice-lapse sequence. 程序生成标准、渐变时间切片及延时摄影序列。

    忽略模式 ignore_mode:

    This mode is used to better create slicelapse sequence. This will choose whether the early images or the late ones will be ignored if needed. The program will automatically ignore the images might impact the sequence.

    这个参数是为了更好生成延时摄影序列，选择early则代表开始的照片会被忽略（如有需要），选择late则反之。

3. The program will create several folders inside the original directory. They are Processed, Processedmulti, Final and Slicelapse. All the slices will be saved in the Processed directory. The final image will be stored in the Final directory. There will be two final images. One is the normal time slice and the other is the image with gradient transition.

    程序将会在你提供的文件夹内生成数个新文件夹。Processed文件夹包含所有的切片，Processedmulti包含渐变切片，Final文件夹存有最终时间切片成品。如有延时摄影，图片序列将会在slicelapse文件夹中。

4. Sit down and ENJOY! 坐和放宽！

&nbsp;

## My result 我的成果

![Final Result](https://raw.githubusercontent.com/petez-sufe/TimeSlice/main/Final.jpg)

![Final Gradient Result](https://raw.githubusercontent.com/petez-sufe/TimeSlice/main/Final_Gradient.jpg)

&nbsp;

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Xi Zhao - xz3068@columbia.edu - instagram@starchaserpete

Project Link: [https://github.com/petez-sufe/timelapse_slicer](https://github.com/petez-sufe/timelapse_slicer)

# Timelapse Slicer

## What is this? 这是什么？

This is an automated program for photographers who want to create TimeSlice pictures without installing PS plugins.

这是一个帮助摄影师使用延时摄影照片自动化生成时间切片的python程序。使用此程序无需安装PS插件。

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
    timelapse_slicer.slicer(original_dir="YOUR FILE PATH 文件夹路径", number_of_slices="INTEGER 切片数量")
    ```

3. The program will create three folders inside the original directory. They are Processed, Processedmulti and Final. All the slices will be saved in the Processed directory. The final image will be stored in the Final directory. There will be two final images. One is the normal time slice and the other is the image with gradient transition.

    程序将会在你提供的文件夹内生成两个新文件夹。Processed文件夹包含所有的切片，Final文件夹内存有最终成品。最终成品会有两张图片，一张为标准时间切片，一张为渐变过渡时间切片（无痕）。

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

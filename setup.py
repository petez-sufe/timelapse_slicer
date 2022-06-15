from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

package = ['timelapse_slicer']

setup(
    name='timelapse_slicer',
    version='1.0.5',
    license='MIT',
    author="Xi Zhao",
    author_email='xz3068@columbia.edu',
    packages=package,
    package_dir={'timelapse_slicer': 'timelapse_slicer'},
    url='https://github.com/petez-sufe/timelapse_slicer',
    keywords='timelapse slicer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
          'pillow',
          'tqdm'
      ],

)
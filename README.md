# Lego it
It is a tool to convert any image into a lego image.

## Steps 
Read an image
Select ROI <br />
Choose number of colors you want your image to be divided into <br />
select the size, size determins the number of lego bricks bing used. <br />
select the color from the color palette <br />

## How to use it
```shell
python legoit.py
```
press q to move to next step

## structure

Main structure
```shell
-legoit
    |--brickCounter
    |--clusterPicture
    |--colorPicker
```
Script to generate the colorPalette
```shell
-colorPaletteGenerator
```

initial structure and code
```shell
-main_clustering.py
```

### Create and use virutalenv on mac
```
# install 
python3 -m pip install --user virtualenv
# create env
python3 -m venv env
# start virtual env
source env/bin/activate
# stop virtual evn
deactivate
```

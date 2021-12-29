# Homework 2 - DCT Compression
Follow the instructions to reproduce the code locally.


## Introduction
The code will perform DCT on a given input image and return an output image
after the IDCT got executed.


## pip - virtual environment
Before executing the code, prepare the environment:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cd src
```


## Choice of arguments and parameters
Once the environment is ready, we can execute the code by choosing from a set of arguments.

usage: main.py [-h] [--debug] [--show] [--save] [--image IMAGE] [--block-size BLOCK_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --debug               turn on logging.debug. [Default: logging.info]
  --show                show openCV images. [Default: False]
  --save                save images to dedicated folder. [Default: False]
  --image IMAGE, -i IMAGE
                        path to input image [Default: ./../images/lena.tif]
  --block-size BLOCK_SIZE, -b BLOCK_SIZE
                        set size of DCT squared block. [Default: 2]


## Suggested command for code execution
```
python3 main.py --save -b N
```

Change N with either [2,4,8,16] to test different block sizes for DCT compression.

Images are taken as *.tif* format from the folder *images/*.
Output images (DCT and IDCT) are saved in the same *images/* folder, within a subdirectory named from the current date.

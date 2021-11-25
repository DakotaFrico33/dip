- [Project tree](#project-tree)
- [Code reproduction](#code-reproduction)
  - [pip - virtual environment](#pip---virtual-environment)
  - [Part I - Global histogram equalization](#part-i---global-histogram-equalization)
  - [Part II - Local histogram equalization](#part-ii---local-histogram-equalization)
- [Assignment description (from Moodle)](#assignment-description-from-moodle)




# Project tree
```
.
├── images
│   ├── lena
│   │   ├── 0.png   # original image
│   │   ├── 1.png   # processed image
│   │   ├── 2.png   # histogram of original image
│   │   ├── 3.png   # histogram of processed image
│   │   ├── 4.png   # plot of transformation function
│   ├── lena.tif
│   ├── squares
│   │   ├── 0.png   # original image
│   │   └── local   # (local histogram equalization)
│   │       ├── 15.png  # processed image with block size 15x15
│   │       ├── 3.png   # processed image with block size 3x3
│   │       ├── 5.png   # processed image with block size 5x5
│   │       └── 7.png   # processed image with block size 7x7
│   ├── squares.tif
├── README.md
├── requirements.txt
├── src
│   ├── arg_parse.py
│   ├── histogram_equalization.py
│   ├── local.py
│   ├── logger_setup.py
│   └── main.py
└── tree.md
```

# Code reproduction
Follow the instructions to reproduce the code locally.

## pip - virtual environment
Before executing the code, prepare the environment:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```



Once the environment is ready, we can execute the code.
## Part I - Global histogram equalization

```
cd src
python main.py --show --image ./../images/lena.tif
```


## Part II - Local histogram equalization

```
cd src
python local.py --show --image ./../images/squares.tif --kernel-size 3
```



# Assignment description (from Moodle)
Perform Histogram Equalization to obtain contrast-enhanced images (Refer to lecture slides for concept understanding)

(Can use C++, Python, MATLAB, or any programming language)


REPORT should contain:

1. Code (if possible with comments)

2. Input and Output Image (along with their histograms)

3. (Optional) Histogram Equalization can be performed globally (for an  entire image) and locally (in a block-wise manner). Full marks for the  execution of both.



Check Attachment for Sample Test Images (Any appropriate image can be used). Thanks

Homework Due: Dec. 1st @23:59

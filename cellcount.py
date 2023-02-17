#!/bin/env/python
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import os
import tqdm

# Set figure params
matplotlib.rcParams["figure.figsize"] = (5.0, 5.0)


def args():
    parser = argparse.ArgumentParser(
        description="pass as an argument what folder holds the pictures you would like analyzed"
    )
    parser.add_argument(
        "--folder",
        "-f",
        help="This is the directory that holds all of the photos. All of the photos \
    should be included in this folder. This means there should be no subdirectories.",
    )
    parser.add_argument(
        "--min_cell_area",
        help="Set the minimum cell area of your cells. This is the cutoff to count \
            something as a cell. It has to be this large. Default is 20. Check data to see what \
            the model is based off of.",
        default=20,
        type=int
    )
    parser.add_argument(
        "--avg_cell_area",
        help="Set what the average cell size is for each cell in the image. Default is 30.",
        default=30,
        type=int
    )
    parser.add_argument(
        "--connected_cell_area",
        help="Set the average area of two connected cells. Default is 60.",
        default=60,
        type=int
    )
    return parser.parse_args()


arg = args()


def image_configure(args_dir: str) -> dict:

    """
    When supplied a directory from argparse, we take that directory and then apply OpenCV
    transformations, HSV, and dilation to count the amount of cells that are present within the data.
    """

    # Configure variables
    holding_dict = dict()
    # Loop through all of the photos within supplied directory
    for file in tqdm.tqdm(os.listdir(args_dir)):

        # Load in the data
        img = cv2.imread(args_dir + "/" + file)
        original = img.copy()
        # Conver the image to grayscale
        hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        # Set the upper and lower limits of the colors that we are looking for in the image

        hsv_lower = np.array([35, 20, 20])
        hsv_upper = np.array([85, 225, 255])
        # Set the range and the kernel size of the cells

        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        # Dilate the found images so that they are larger
        dilate = cv2.dilate(mask, kernel, iterations=1)

        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        minimum_area = args.min_cell_area
        average_cell_area = args.avg_cell_area 
        connected_cell_area = args.connected_cell_area

        cells = 0
        for c in cnts:
            area = cv2.contourArea(c)
            if area > minimum_area:
                cv2.drawContours(img, [c], -1, (26, 255, 12), 2)
                if area > connected_cell_area:
                    cells += math.ceil(area / average_cell_area)
                else:
                    cells += 1


        # split the string and add the name and cell count to this dictionary
        split_string = file.split("/")[-1]
        holding_dict[split_string] = cells

    return holding_dict


######## Run script

counts = image_configure(arg.folder)

total = 0
for i in counts.values():
    total += i

###### write to csv

with open("counts.csv", "w") as output:
    print("File", "Count", sep=",", file=output)
    for k, v in counts.items():
        print(k, v, sep=",", file=output)
    print("Total", total, sep=",", file=output)


# print('Setting UP')
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cv2 as cv
import numpy as np
from utils import *


################################################################################
img_path = 'F:\pycodes\sudoku_solver\Resources\\1.jpg'
height_img = 450
width_img = 450
model = intializePredectionModel()

################################################################################

## 1-Prepareing the image

img =  cv.imread(img_path)
img = cv.resize(img, (height_img, width_img))
img_blank = np.zeros((height_img, width_img, 3), np.uint8)
img_threshold = preprocessing(img)

## 2-Making contours in the image

img_contours = img.copy()
img_biggest = img.copy()
contours, heirarchy =cv.findContours(img_threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_contours, contours,-1,(0,255,0), 3)

## 3-Find the biggest contour or shape to get the sudoku and transform it

biggest , max_area = biggestContour(contours)
# print(biggest , max_area)
if biggest.size != 0:
    biggest=reorder(biggest)
    cv.drawContours(img_biggest,biggest,-1,(0,255,0),20)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[width_img,0],[0,height_img],[width_img,height_img]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    # print(biggest,pts1)
    Wraped_img = cv.warpPerspective(img,matrix,(width_img ,height_img))
    Detect_degits_img = img_blank.copy()
    Wraped_img = cv.cvtColor(Wraped_img,cv.COLOR_BGR2GRAY)
 ##Step-4 splitting the image such that we can take every box individually
    img_digits = img_blank.copy()
    img_solved = img_blank.copy()
    boxes = splitting(Wraped_img)
    # print( len(boxes))
    numbers = getPredictions(boxes, model)
    # print(numbers)
    img_digits = display_numbers(img_digits,numbers,color=(255,0,255))
    numbers = np.asarray(numbers)
    posarray = np.where(numbers>0,0,1)
    # print(posarray)

    ############################################################################
    ############################################################################

    # Step - 5 making the board and getting ans
    board = np.array_split(numbers,9)
    print(board)
    try:
      solve(board)
    except:
      print(f"The solve function failed check the input charecters once again for any invalid input\n {board}")
    print(board)
    flat_list = []

    for sub_list in board:
        for item in sub_list:
            flat_list.append(item)

    solved_nums = flat_list*posarray
    img_solved = display_numbers(img_solved,solved_nums)
    ############################################################################
    ############################################################################
    UNWraped_img = img_blank.copy()
    solution_IMG = img.copy()
    matrix = cv.getPerspectiveTransform(pts2,pts1)
    UNWraped_img = cv.warpPerspective(img_solved,matrix,(width_img ,height_img))
    solution_IMG = cv.addWeighted(UNWraped_img, 1,img,0.5,1)









img_solved = drawGrid(img_solved)
img_digits = drawGrid(img_digits)
img_stacked = stackImages(0.4,[[img,img_threshold,img_contours,img_biggest,img_blank],[Wraped_img,img_digits,img_solved,UNWraped_img,solution_IMG ]])
cv.imshow(img_stacked)
cv.waitKey(0)
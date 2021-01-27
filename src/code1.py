import streamlit as st
import json
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-image_path','--image_path', help='Image path', required=True)
parser.add_argument('-ploygon_path','--polygon_path', help='Polygon path', required=True)
parser.add_argument('-points_path','--points_path', help='Points path', required=True)
args = vars(parser.parse_args())


def run(image, polygon_points, object_points):
    polygon_points = np.array([[point['X'], point['Y']] for point in polygon_points ]).reshape((-1, 1, 2))
    cv2.polylines(image,[polygon_points],True,(0,255,255))

    for point in object_points:    
        inside = cv2.pointPolygonTest(polygon_points, (point['X'],point['Y']), False)     
        if inside == -1:
            image = cv2.circle(image, (point['X'], point['Y']), 2, (255, 0, 0), 5)
        else:
            image = cv2.circle(image, (point['X'], point['Y']), 2, (0, 255, 0), 5)


    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    with open(args['polygon_path']) as hndl:
        polygon_points = json.load(hndl)

    with open(args['points_path']) as hndl:
        object_points = json.load(hndl)

    image = cv2.imread(args['image_path'])
    run(image, polygon_points, object_points)




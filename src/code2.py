
import json
import argparse
import cv2
import numpy as np
import torchvision
from torchvision import transforms as tvt
from mmdet.apis import init_detector, inference_detector

transform = tvt.Compose([   
    tvt.ToTensor(),
    tvt.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

def get_model():
    config_file = "configs/ssd300_coco.py"
    checkpoint_file = "checkpoints/ssd300_coco_20200307-a92d2092.pth"
    device = 'cpu'
    model = init_detector(config_file, checkpoint_file, device=device)

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-video_path','--video_path', help='Image path', required=True)
parser.add_argument('-ploygon_path','--polygon_path', help='Polygon path', required=True)
args = vars(parser.parse_args())


def run(cap, polygon_points):

    model = get_model()
    # model.eval()

    while(cap.isOpened()):
        ret, frame = cap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        inference_detector(model, frame)
        frame_tensor = transform(frame).unsqueeze(0)
        detection = model(frame_tensor)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

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

    cap = cv2.VideoCapture(args['video_path'])
    run(cap, polygon_points)




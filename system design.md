This project aims to detect pedestrian who are crossing a road without using the designated area (zebra crossing).

We can formulate this problem as an object detection task. The object detector will be trained to detect pedestrian and the zebra crossing. During the 
inference if a pedestrian bounding box falls outside of zebra crossing bounding box, we can assume that pedestrian is walking outside of the designated area. 

As there is no training data, this project solves the similar problem using traditional computer vision approach. 

In the first task, we assume that we know the crossing location (polygon points) and pedestrian location (X and Y coordinate). These points are written in separate
json file and `json` library is used to read these data. Using openv `pointPolygonTest` function, each pedestrian location is checked against the polygon location
to determine whether these points are inside or outside of the crossing area.

From the `src` folder run `python code1.py`. It will create a figure like the following one. The green dots represent the location where the pedestrian is inside
the designated area. The blue dots represent that the pedestrian is outside of the designated location. The designated location is represented using a 
yellow polygon.

![code1](https://user-images.githubusercontent.com/530250/106084384-0009c500-616a-11eb-9bda-25c26e7f6cbb.jpg).

In the second task, we locate the pedestrian from this video (https://youtu.be/XWfemvW-Jto). We have used opencv video capture module to extract frames and 
successive frame difference along with `findContours` module to locate moving pedestrians. Later, using `pointPolygonTest` we have determined whether a 
pedestrian is inside/outside of a designated are. `python code2.py` will detect these pedestrians and show the frames one by one. A sample frame is like the 
following one.

![frame_00099](https://user-images.githubusercontent.com/530250/106085736-760f2b80-616c-11eb-8245-125e442e0def.jpg)

All the necessary configuration is written in `src/config.py`file.

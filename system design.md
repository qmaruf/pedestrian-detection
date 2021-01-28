## System Design ##

This project aims to detect pedestrians who are crossing a road without using the designated area (zebra crossing).

We can formulate this problem as an object detection task. The object detector will be trained to detect pedestrian and the zebra crossing. During the 
inference if a pedestrian bounding box falls outside of zebra crossing bounding box, we can assume that pedestrian is walking outside of the designated area. 

As there is no training data, this project solves a similar problem using traditional computer vision approach. 

We assume that we know the crossing location (polygon points) and pedestrian location (X and Y coordinate) in the first task. These points are written in separate
json files and `json` library is used to read them. Using opencv `pointPolygonTest` function, each pedestrian location is checked against the polygon location
to determine whether these points are inside or outside the crossing area.

From the `src` folder run `python code1.py`. It will create a figure like the following one. The green dots represent the location where the pedestrian is inside
the designated area. The blue dots represent that the pedestrian is outside of the specified location. The designated location is represented using a 
yellow polygon.

![code1](https://user-images.githubusercontent.com/530250/106084384-0009c500-616a-11eb-9bda-25c26e7f6cbb.jpg).

In the second task, we locate the pedestrian from this video (https://youtu.be/XWfemvW-Jto). We have used opencv video capture module to extract frames and 
successive frame difference along with `findContours` module to locate moving pedestrians. Later, using `pointPolygonTest` we have determined whether a 
pedestrian is inside/outside of a designated area. `python code2.py` will detect these pedestrians and show the frames one by one. A sample frame is like the following one.

![frame_00099](https://user-images.githubusercontent.com/530250/106085736-760f2b80-616c-11eb-8245-125e442e0def.jpg)

All the necessary configuration is written in `src/config.py`file.

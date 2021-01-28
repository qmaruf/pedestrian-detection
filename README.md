# Intro 

This is a simple proof of concept to detect pedestrian who are crossing a road without using a designated area.

`src/code1.py` uses polygon and object points to determine which points are outside of the designated area.

`src/code2.py` performs the similar task in a video.

# How to run the code

Clone the repo.
```
git clone git@github.com:qmaruf/pedestrian-detection.git
```

Create a virtual environment.
```
virtualenv -p python3.6 ~/venvpd
```

Go inside the `pedestrian-detection` directory.
```
cd pedestrian-detection
```

Activate the environment
```
source ~/venvpd/bin/activate
``` 

Install necessary packages
```
pip install -r requirements.txt
```

Inside the `src` folder run
```
python code1.py
python code2.py
```

N.B: Both of these code only work for the data available in the `./data/` folder :)




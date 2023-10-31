# character color automation
harcoded pixel values tuned for xubuntu 23.10. you will likely need to adjust values.

### install
`python3.12 -m venv venv`  
`source venv/bin/activate`  
`python3.12 -m pip install --upgrade pip`  
`pip3 install -r requirements.txt`  

### run
1. dofus client is windowed with default height and max widescreen (16:9? seems wider)
2. place client top left of screen
3. set desired hsl values in color.py
4. `python3.12 color.py`
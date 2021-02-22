# AI plays GTA

**Content:**
1. [Record data](#data)
2. [Dataset browsing apps](#apps)
3. [Train model](#train)


![DeepGTAV](https://camo.githubusercontent.com/5b20c613eb17275cf8014a9541f20d4e5cd71fb41bcc0f7b221e754c91131cc3/68747470733a2f2f696d672e677461352d6d6f64732e636f6d2f7139352f696d616765732f6e61747572616c766973696f6e2d70686f746f7265616c69737469632d677461762f6234646539342d47544135253230323031362d30382d323825323032322d30352d35322e6a7067)

The goal of this project is to develop a self-driving car in Grand Theft Auto V like in this example:

![gta-self-driving](img/gta-self-driving.gif)

* [Tuto - Python Plays: Grand Theft Auto V](https://pythonprogramming.net/more-interesting-self-driving-python-plays-gta-v/)
* [sentdex Github](https://github.com/sentdex/pygta5/)
* [Youtube channel - Python Plays: Grand Theft Auto V](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a)
* [Self-driving motorbike video](https://youtu.be/nWJZ4w0HKz8?t=810)

## 1. <a name="data"></a>Record data

### Record display

The first challenge is to record the display to replay it for further analysis (like a simple object detection following the car here):

![gta-car-detection](img/gta-car-detection.gif)



### Record controller

We have 2 options:
* [Get the controller input directly](https://github.com/komefai/PS4Macro)
* [Map the command to the Keyboard](https://github.com/starshinata/PS4-Keyboard-and-Mouse-Adapter)


![ps4-keyboard-adapter](img/ps4-keyboard-adapter.png)

The folder [ps4_macro](ps4_macro) contains the controller record and python functions
[PS4_control.py](ps4_macro/PS4_control.py) provides 2 functions to: 
* **read** XML controller file as DataFrame, 
* **save** it as Excel file

![ps4_controller_table](img/ps4_controller_table.png)

![ps4_controller_LX_LY](img/ps4_controller_LX_LY.png)

[PyWin32](https://pypi.org/project/pywin32/) to record keyboard

**/!\\** Map A to Q on French keyboard!!!


## 3. <a name="apps"></a>Dataset browsing apps

### MATLAB desktop App
![matlab_app](training_data_images/image_2.png)

### Streamlit Web App
![streamlit_app.png](img/streamlit_app.png)


## 4. <a name="train"></a>Train model 

### MATLAB Deep Learning toolbox

![matlab_deep_learning](training_data_images/image_3.png)

### Tensorflow

1 epoch only with [training0.py](2_train_model/training0.py)

Tensorflow on i7-6700HQ CPU @ 2.60GHz / 8Go RAM
21 steps == 6m 27s
![training0.png](img/training0.png)

I stopped it to train on my GPU instead

Tensorflow on NVIDIA GeFOrce GTX 960M
21 steps == 3m 40s
92 steps == 17m 6s
![training1.png](img/training1.png)

## Sources: 
* [Building a Self-Driving Vehicle in GTA-V Using Deep Learning and Convolutional Neural Network](https://medium.com/@alzaibnasiruddin/building-a-self-driving-vehicle-in-gta-v-using-deep-learning-and-convolutional-neural-network-696b38b4c81e)
* https://github.com/Alzaib/Autonomous-Self-Driving-Car-GTA-5
* https://medium.com/@alexlau27/playing-ps4-with-tensorflow-2-1-and-alexnet-2aeec0e2a5d8
* https://github.com/komefai/PS4Macro
* https://github.com/starshinata/PS4-Keyboard-and-Mouse-Adapter

## Go Further:

### Python plays GTA V

[GTA_5_steering.ipynb](Autonomous-Self-Driving-Car-GTA-5/GTA_5_steering.ipynb)

### [Playing for Data: Ground Truth from Computer Games](https://download.visinf.tu-darmstadt.de/data/from_games/index.html)
* https://bitbucket.org/visinf/projects-2016-playing-for-data/src/master/
* https://arxiv.org/abs/1608.02192
* http://download.visinf.tu-darmstadt.de/data/from_games/data/eccv-2016-richter-playing_for_data.pdf

| GTA driving data                  | semantic sampling                         | 
| ----------------------------------|:-----------------------------------------:|
| ![gta image](img/17086_image.png) | ![semantic sampling](img/17086_label.png) |
| ![gta image](img/16116_image.png) | ![semantic sampling](img/16116_label.png) |

### [LiDAR-GTA-V](https://github.com/UsmanJafri/LiDAR-GTA-V)
![LiDAR sample traffic](https://github.com/slevin48/LiDAR-GTA-V/raw/master/samples/LiDAR%20Sample%20-%20Traffic.png)

### [Precise Synthetic Image and LiDAR (PreSIL) Dataset](https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/projects/precise-synthetic-image-and-lidar-presil-dataset-autonomous) from Waterloo Intelligent Systems Engineering Lab

![](https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/sites/ca.waterloo-intelligent-systems-engineering-lab/files/resize/uploads/images/000342-500x281.png)

![](https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/sites/ca.waterloo-intelligent-systems-engineering-lab/files/resize/uploads/images/342-pc-500x285.png)

Linearized Depth Map (~~Grey and~~ Colour)

![](https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/sites/ca.waterloo-intelligent-systems-engineering-lab/files/resize/uploads/images/342-depth-color-500x281.png)

Object Instance Segmentation

![](https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/sites/ca.waterloo-intelligent-systems-engineering-lab/files/resize/uploads/images/342-segimg-500x281.png)

## More inspiration:

* https://github.com/aitorzip/DeepGTAV
* https://github.com/aitorzip/VPilot
* https://github.com/cpgeier/SantosNet
* https://ps4mousetocontroller.com/download.jsp
* [OpenCV Python Tutorial - Find Lanes for Self-Driving Cars](https://www.youtube.com/watch?v=eLTLtUVuuy4&ab_channel=ProgrammingKnowledge)


![gif](https://github.com/cpgeier/SantosNet/raw/master/sample.gif?raw=true)

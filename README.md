# Intelligent Road Repairing System

**A Machine Learning Project to identify objects and anomalies on
Indian roads using India’s traffic images and assess the quality of road
infrastructure based on satellite imaging (e.g. potholes on road, lane width,
pedestrian space, cycling lanes and tracks, road encroachments etc.).**


# Usage / Installation

This section will guide you through a series of steps to setup this project on your computer.

## Requirements

Make sure you have the following installed to proceed further into the installation process

 - Python 3.5 (or above)
 - Python Package Manager - ( PIP )
 - Git 

##  Install Dependencies for the project

All the dependencies and Packages have been conveniently bundles into a 'requirements.txt' file for a smooth installation and have the Project Up and running on your machine with minimal effort and time.
Run the following commands from the terminal .

Get a complete copy of the project by cloning into a suitable directory

    git clone https://github.com/akhilgup/nitiayog_5.git
  
 Install all the dependencies by running the command from the terminal.

    sudo pip install -r requirements.txt

## Usage

 - For training and subsequently generating the model, run the ```training.py``` file by the following command.
```
python training.py
```
This generates a model file ```mymodel.h5``` which is then used to give predictions.

-  For testing an image for giving predictions for the parameters ``` vehicles, potholes, traffic, pedestrian lanes, freeways/highways```,  place your image file in the same directory with the name ```test2.jpg``` and run the ```testing.py``` file by the following command 
```
python testing.py
```
The resultant output will be in the form of an image illustrating the Confidence of the model in the parameters listed above.

![Output Image](https://github.com/akhilgup/nitiayog_5/raw/master/result.jpg)

- Install the android app by downloading the apk from the repository or click here
> **Note :** The published APK has been tested on Android Platforms Marshmallow and below. There may be a compatibility issue for newer platforms.
- Run the website on your local-host by navigating to [Backend](https://github.com/akhilgup/nitiayog_5/tree/master/backend) and running the following command
```
python manage.py runserver
```

# Technical Details


## Training 

- The model is a result of **Convolutional Neural Network** with 2 Convolution Layers, 2 Pooling Layers applied with the **Rectified Linear Unit (ReLU)** activation function with **Filter Size of 5 ** along with Flatten Layer (Dense) made up of 500 neurons using **Rectified Linear Unit (ReLU)** as it's activation function. 

Training Parameters :-
``` 
EPOCHS = 30
INIT_LR = 1e-3 // Initial Learning Rate
BATCH_SIZE = 32
```
- Output Layer is Dense Layer consisting of neurons equal to the no. of target classes (5) using Softmax as it's activation function.
### Image Pre-Processing 
- All training images were scaled to 128 x 128 in Grayscale and all the pixels were feature scaled by dividing each pixel by 255.0. 
- Image generator function has been used to increase the training data by flipping, rotating images : [Keras Image PreProcessing](https://keras.io/preprocessing/image/) .

## Results

![Graph](https://github.com/akhilgup/nitiayog_5/raw/master/Figure_1.png)

**Training Accuracy** : 91 %
**Validation Accuracy**: 89.7 % 
**Training Loss** : 0.2314
**Validation Loss** : 0.2514**

## Libraries / Frameworks Used

 * Deep Learning Libraries
	 * TensorFlow
	 * Keras
	 * h5py
* Machine Learning Libraries
	 * SciKit Learn
	 * Pandas
	 * SciPy
	 * Numpy
	 * MatPlotLib
	 * Seaborn
* Computer Vision Libraries
	* OpenCV
* Web Frameworks
	* Django
	* Django RestFramework
* Database tools
	* mySQL
* Android tools
	* Android Studio

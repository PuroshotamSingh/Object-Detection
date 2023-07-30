# Object Detection   

## Description   
Detecting whether a person is wearing a face mask or not and pointing out the exact location of face/mask using object detection capabilities of custom CNN architecture. The model is deployed on Flask web application.

## Flask Application

![flask app](model_saved_images/app_snapshot.jpg)

## How to run   
1. Install dependencies   
```bash
# clone project   
`git clone https://github.com/PuroshotamSingh/Object-Detection.git`

# install requirements
`cd Object-Detection` 
`pip install -r requirements.txt`
 ```   
2. To run training code use `simple_obj_detector2.ipynb` notebook.

3. To run Flask app, follow below instructions:
 ```bash
# module folder
`cd app_backend`

# run flask app
`python app.py`
```

## Model Architecture

The CNN model architecture constructed for this use case is shown in the image below.

![architecture](model_saved_images/model.png)

## Model Output
Model Accuracy
![model accuracy](model_saved_images/accuracy.png)

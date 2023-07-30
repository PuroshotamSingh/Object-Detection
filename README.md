# Object Detection   

## Description   
Detecting whether a person is wearing a face mask or not and pointing out the exact location of face/mask using object detection capabilities of custom CNN architecture. The model is deployed on Flask web application.

## How to run   
Install dependencies   
```bash
# clone project   
git clone [https://github.com/YourGithubName/deep-learning-project-template](https://github.com/PuroshotamSingh/Object-Detection.git)

# install requirements
cd deep-learning-project-template 
pip install -r requirements.txt
 ```   
 Next, navigate to any file and run it.   
 ```bash
# module folder
cd project

# run module (example: mnist as your main contribution)   
python lit_classifier_main.py    
```

## Imports
This project is setup as a package which means you can now easily import any file into any other file like so:
```python
from project.datasets.mnist import mnist
from project.lit_classifier_main import LitClassifier
from pytorch_lightning import Trainer

# model
model = LitClassifier()

# data
train, val, test = mnist()

# train
trainer = Trainer()
trainer.fit(model, train, val)

# test using the best model!
trainer.test(test_dataloaders=test)
```

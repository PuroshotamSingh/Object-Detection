# Object Detection   

## Description   
Detecting whether a person is wearing a face mask or not and pointing out the exact location of face/mask using object detection capabilities of custom CNN architecture. The model is deployed on Flask web application.

## Flask Application

![flask app](model_saved_images/app_snapshot.jpg)

## How to run   
1. Install dependencies
   
  `git clone https://github.com/PuroshotamSingh/Object-Detection.git`

  `cd Object-Detection` 

  `pip install -r requirements.txt`

2. To run training code use `simple_obj_detector2.ipynb` notebook.

3. To run Flask app, follow below instructions:
   
  `cd app_backend`

  `python app.py`

## Model Architecture

The CNN model architecture constructed for this use case is shown in the image below.

![architecture](model_saved_images/model.png)

## Model Output

Model Accuracy

![model accuracy](model_saved_images/accuracy.png)

Bounding Box Loss

![model accuracy](model_saved_images/bb_loss.png)

Test Images ouput

![model accuracy](model_saved_images/test_output.png)

## Evaluation Metric

1. IoU (Intersection Over Union): IoU scores tells how well the predicted bound box overlaps the actual bound box. The idea behind IoU is pretty simple; compare the intersection and union areas between the predicted and actual bound boxes by dividing the intersection by the union, as shown in the following image:

   ![iou](https://learnopencv.com/wp-content/uploads/2022/06/2-iou-illustration.png)

   IoU value ranges from 0 to 1.

   ![iou1](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2016/09/iou_examples.png?lossy=1&strip=1&webp=1)

   If IOU > 0.5 and predicted object is true class, then this is True Positive(TP).
   If IOU < 0.5 , then its False Positive(FP).
   If there is no detection or IOU > 0.5 but prediction is wrong then its False Negative(FN).
   
3. Precision: is equal to TP/(TP + FP). In other words, of all bounding box predictions, what fraction was located correctly.
   
4. Recall: is equal to TP/(TP +FN). In other words, of all target bounding boxes, what fraction did we correctly detect.

5. mAP (Mean Average Precision): The mAP is computed by first calculating the Average Precision (AP) for each class, and then taking the    mean of the AP values across all classes. To compute the AP for a single class, the precision-recall curve for that class is first        created. The area under this curve (AUC) represents the AP for that class. The mAP value ranges from 0 to 1, where 0 indicates poor       performance and 1 indicates perfect performance.

## Conclusion

Taking in consideration the small size of the data used for training and the fact of training the model from scratch without transfer learning, we have got training accuracy of 94% and validation accuracy of 81% and mAP equals to 0.42.

### Scope of Improvement

1. The first option to improve the bounding box and classificataion performance by increasing the training data.

2. Trying more hyperparameters combinations for.eg. number of layers, number of neurons, activation function etc., can reduce the classification and regression errors.

3. Instead of custom CNN architecture, transfer Learning can be used to improve the accuracy of model.

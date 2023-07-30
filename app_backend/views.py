from flask import render_template, request, Response, flash, send_file
import os
import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.numpy_ops import np_config

np_config.enable_numpy_behavior()
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

UPLOAD_FOLDER = os.path.join(os.getcwd(), "static/images")

model = tf.keras.models.load_model("../ModelWeights/object_detection.h5")


def verify():
    image = False
    submit = False
    name = None

    if request.method == "POST":
        if request.files["image"]:
            f = request.files["image"]
            name = f.filename
            img_path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(img_path)
            image = True
            submit = True

        x_test = []
        input_size = 244

        col_img = cv.imread(img_path)
        h = col_img.shape[0]
        w = col_img.shape[1]

        img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

        resized = cv.resize(
            img, (input_size, input_size), interpolation=cv.INTER_LINEAR
        )
        new_image = np.array(resized)

        img1 = new_image.astype(float) / 255.0

        x_test.append(img1)
        X = np.array(x_test)
        X = np.expand_dims(X, axis=3)

        X = tf.convert_to_tensor(X, dtype=tf.float32)

        predictions = model(X)
        predicted_box = predictions[1][0] * input_size
        predicted_box = tf.cast(predicted_box, tf.int32)

        predicted_label = predictions[0][0]

        img_label = "No Mask"
        if predicted_label[0] > 0.5:
            img_label = "Mask"

        predicted_box_n = predicted_box.numpy()

        cv.rectangle(
            col_img,
            (int(predicted_box_n[0] * w / 244), int(predicted_box_n[1] * h / 244)),
            (
                int(predicted_box_n[0] * w / 244 + predicted_box_n[2] * w / 244),
                int(predicted_box_n[1] * h / 244 + predicted_box_n[3] * h / 244),
            ),
            (0, 0, 240),
            2,
        )
        cv.putText(
            col_img,
            img_label,
            (int(predicted_box_n[0] * w / 244), int(predicted_box_n[1] * h / 244) - 5),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )

        cv.imwrite(img_path, col_img)

        return render_template(
            "verify.html",
            image=image,
            submit=submit,
            name=name,
        )

    return render_template("verify.html", image=False)

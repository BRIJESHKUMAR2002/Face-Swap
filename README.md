# **Face Swap Project with OpenCV and MTCNN**

This project demonstrates how to perform face swapping using **OpenCV** and **MTCNN** (Multi-task Cascaded Convolutional Networks). MTCNN is used for face detection, alignment, and landmark extraction, which is crucial for accurate face swapping. The face swapping itself is done by extracting the facial region from one image and pasting it onto another.

---

## **Project Description**

This face swap project leverages deep learning-based face detection and alignment algorithms to swap faces in images or videos. The pipeline is as follows:
1. **Face Detection**: MTCNN detects and extracts faces from images.
2. **Facial Landmark Detection**: Using MTCNN, facial landmarks like eyes, nose, and mouth corners are detected to help with face alignment.
3. **Face Swapping**: The detected face from one image is mapped onto the other image, ensuring that the facial features align properly.

This project utilizes the `inswapper_128.onnx` pre-trained model to swap faces accurately and smoothly.

---

## **Installation**

### **Step 1: Set Up Conda Environment**
Create a new Conda environment for this project with Python 3.10:


```sh
conda create -n face_swap python=3.10
```

```sh
conda activate face_swap
```

### **Step 2: Install Dependencies**

After activating the environment, install the required dependencies using the provided `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## **Model Download**

You need to download the face-swapping model to use the pre-trained network for face swapping.

1. Download the model from Hugging Face:  
   [Download inswapper_128.onnx model](https://huggingface.co/ezioruan/inswapper_128.onnx/tree/main)

2. After downloading, place the model file in the `models/` directory of your project.

## **Configuration**

### **Using GPU for Faster Processing**

If you have an **NVIDIA GPU**, you can take advantage of the GPU for faster processing.

In `utils.py`, set `ctx_id=0` to use the GPU:

face_analysis.prepare(ctx_id=0)  # Use GPU mode

## **Troubleshooting**

### **Error: `onnxruntime` module not found**

If you encounter an error with `onnxruntime`, you can install the required dependency:

```sh
pip install onnxruntime
```

### **For GPU**

```sh
pip install onnxruntime-gpu
```

## **Credits**

- **MTCNN**: The face detection and alignment library used in this project.
- **ONNX**: The format in which the model is saved for face swapping.
- **OpenCV**: Used for image processing and displaying the result.

## **Testing the Api using Postman**

![Screenshot 2025-02-01 163538](https://github.com/user-attachments/assets/bdbf2c2e-ebfc-450f-bbcb-90b330cfd742)




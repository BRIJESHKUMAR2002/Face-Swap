import cv2
import numpy as np
import torch
from facenet_pytorch import MTCNN
from PIL import Image
from insightface.app import FaceAnalysis
from insightface.model_zoo.inswapper import INSwapper

# Initialize Face Detector
mtcnn = MTCNN(keep_all=True)

# Initialize Face Recognition Model
face_analysis = FaceAnalysis(name="buffalo_l")
# face_analysis.prepare(ctx_id=-1)  # Use CPU mode
face_analysis.prepare(ctx_id=0)  # Use CPU mode

# Load Face Swapper Model
swapper = INSwapper("face_swap/models/inswapper_128.onnx")

def detect_face(image_path):
    """Detects a face in an image and returns coordinates."""
    image = Image.open(image_path)
    boxes, _ = mtcnn.detect(image)
    return boxes

def swap_faces(source_path, target_path):
    """Swaps faces using InsightFace's INSwapper and returns the swapped image."""
    try:
        # Load images
        source_img = cv2.imread(source_path)
        target_img = cv2.imread(target_path)

        # Detect faces
        source_faces = face_analysis.get(source_img)
        target_faces = face_analysis.get(target_img)

        if len(source_faces) == 0 or len(target_faces) == 0:
            print("No faces detected.")
            return None

        # Extract face embeddings
        source_face = source_faces[0]
        target_face = target_faces[0]

        # Perform face swapping using INSwapper
        swapped_img = swapper.get(target_img, target_face, source_face)

        # Save output
        output_path = "media/outputs/swapped.jpg"
        cv2.imwrite(output_path, swapped_img)

        return output_path
    except Exception as e:
        print(f"Error swapping faces: {e}")
        return None

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import swap_faces
import os

@csrf_exempt
def face_swap_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method Not Allowed"}, status=405)

    if "source_image" not in request.FILES or "target_image" not in request.FILES:
        return JsonResponse({"error": "Both source and target images are required"}, status=400)

    source_image = request.FILES["source_image"]
    target_image = request.FILES["target_image"]

    # Save files temporarily
    source_path = f"media/uploads/{source_image.name}"
    target_path = f"media/uploads/{target_image.name}"
    os.makedirs("media/uploads", exist_ok=True)

    with open(source_path, "wb") as f:
        f.write(source_image.read())
    with open(target_path, "wb") as f:
        f.write(target_image.read())

    # Perform face swap
    swapped_path = swap_faces(source_path, target_path)

    if swapped_path:
        return JsonResponse({"message": "Face swap successful", "swapped_image_url": swapped_path})
    else:
        return JsonResponse({"error": "Face swap failed"}, status=500)

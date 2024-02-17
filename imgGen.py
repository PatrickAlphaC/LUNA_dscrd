import json
import requests
import io
import base64
from PIL import Image

url = "http://127.0.0.1:7860"


async def fuckinWork(prompt):
    payload = {
        "prompt": f"{prompt}",
        "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck",
        "styles": ["string"],
        "seed": -1,
        "subseed": -1,
        "subseed_strength": 0,
        "steps": 50,
        "cfg_scale": 5,
        "width": 512,
        "height": 512,
        "restore_faces": True,
        "denoising_strength": 50,
        "refiner_checkpoint": "Realistic_Vision_V5.1.ckpt [089b46befc]",
        "refiner_switch_at": 75,
    }

    response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload)

    r = response.json()

    image = Image.open(io.BytesIO(base64.b64decode(r["images"][0])))
    return image

import streamlit as st
import torch
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim, peak_signal_noise_ratio as psnr

@st.cache_resource()
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32 

    return StableDiffusionInpaintPipeline.from_pretrained(
        "runwayml/stable-diffusion-inpainting", torch_dtype=dtype
    ).to(device)

pipe = load_model()

st.title("🪄 The Brush of Spells")
st.write("Upload an image of a bird, apply a rectangular mask, and generate an inpainted version using a text prompt!")

uploaded_image = st.file_uploader("Upload a bird image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Original Image", use_column_width=True)

    st.write("### Define the Mask Dimensions")
    
    mask_width = st.slider("Mask Width", 10, image.width, image.width // 4)
    mask_height = st.slider("Mask Height", 10, image.height, image.height // 4)

    image_np = np.array(image)

    mask = np.zeros((image.height, image.width), dtype=np.uint8)
    
    center_x, center_y = image.width // 2, image.height // 2
    x1, y1 = center_x - mask_width // 2, center_y - mask_height // 2
    x2, y2 = center_x + mask_width // 2, center_y + mask_height // 2

    mask = cv2.rectangle(mask, (x1, y1), (x2, y2), 255, -1)

    masked_image = image_np.copy()
    masked_image[y1:y2, x1:x2] = (0, 0, 0) 

    mask_pil = Image.fromarray(mask)
    masked_image_pil = Image.fromarray(masked_image)

    st.image(masked_image_pil, caption="Masked Image", use_column_width=True)

    prompt = st.text_input("Enter a prompt for inpainting", "A majestic phoenix with fiery wings")

    if st.button("Generate Inpainted Image 🖌️"):
        with st.spinner("Painting your magic..."):
            result = pipe(prompt=prompt, image=image, mask_image=mask_pil).images[0]
            st.image(result, caption="Inpainted Image", use_column_width=True)

            result_np = np.array(result.resize(image.size))
            original_np = np.array(image)

            result_gray = cv2.cvtColor(result_np, cv2.COLOR_RGB2GRAY)
            original_gray = cv2.cvtColor(original_np, cv2.COLOR_RGB2GRAY)

            ssim_score = ssim(original_gray, result_gray)
            psnr_score = psnr(original_np, result_np)

            st.write("### 📊 Quality Metrics")
            col1, col2 = st.columns(2)
            col1.metric("SSIM", f"{ssim_score:.4f}")
            col2.metric("PSNR", f"{psnr_score:.2f} dB")


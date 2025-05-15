# The Brush of Spells: Text-guided Image Inpainting

A deep learning project inspired by the research paper ["MMFL: Multimodal Fusion Learning for Text-Guided Image Inpainting"](https://dl.acm.org/doi/10.1145/3394171.3413982), enabling users to restore and fill images guided by natural language descriptions. This repository provides an interactive interface for text-guided image inpainting, allowing users to mask regions and describe how they should be filled in.

![C04_TBOS](https://github.com/user-attachments/assets/b5d1fc98-56fd-465b-946c-e2881f3c33af)
![image](https://github.com/user-attachments/assets/956ca0e7-409e-4ae4-aded-194cf78d5899)

---

## Table of Contents

- [Description](#description)
- [Solution Overview](#solution-overview)
- [Features](#features)
- [Interface & Results](#interface--results)
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)

---

## Description

**The Brush of Spells** is a text-guided image inpainting tool that leverages multimodal fusion learning to restore or edit images based on user-provided text prompts. Inspired by the MMFL paper, this project fuses image and text features to generate contextually accurate and semantically meaningful inpainted results. The system is designed for artists, researchers, and developers interested in advanced image editing using natural language.

---

## Solution Overview

The project implements a multimodal approach for image inpainting, integrating both visual information (the masked image) and textual guidance (user prompt). The core idea, as proposed in MMFL, is to imitate a painter’s conjecture process: the model uses the text description to provide abundant guidance for image restoration, fusing multimodal features to generate plausible and context-aware inpainting results.

**Workflow:**
- User uploads an image and gives the width and height of the mask region to be edited.
- User provides a text prompt describing the desired content for the masked area.
- The system fuses the image and text features using a multimodal deep learning model.
- The masked region is filled in according to the prompt, producing a visually coherent and semantically relevant output.

---

## Features

- **Text-guided inpainting:** Restore or edit images by describing changes in natural language.
- **Interactive interface:** Upload images, draw masks, and enter prompts in a user-friendly web app.
- **Multimodal fusion:** Combines visual and textual cues for context-aware restoration.
- **State-of-the-art results:** Inspired by MMFL and recent advances in diffusion-based inpainting models.

---

## Interface & Results

Below are screenshots and sample results from the interactive interface:

| Original Image           | Masked Image             | Prompt                                      | Inpainted Result        |
|:-----------------------:|:------------------------:|:--------------------------------------------:|:----------------------:|
| ![image](https://github.com/user-attachments/assets/1efe4ea1-da68-48a1-bd89-454e28b51a59) | ![image](https://github.com/user-attachments/assets/4d577daa-8668-4d81-95b6-9df68822fd24) | "A striking Baltimore Oriole perched on a branch, showcasing its vibrant orange and black plumage." | ![image](https://github.com/user-attachments/assets/14b8a937-fee5-47e8-a1d1-683a7756cd82)
| ![image](https://github.com/user-attachments/assets/1a2e4375-6b64-4d5b-9a54-aafdeb4e0ffc) | ![image](https://github.com/user-attachments/assets/1d3741d7-7cb3-4b75-8412-a288119f8c55) | "A vibrant Sun Conure parrot with an orange head and chest, yellow back and wings, and green-blue tail feathers is perched on a light-colored cylindrical bar against a softly blurred beige background." | ![image](https://github.com/user-attachments/assets/a97fb982-5ee7-4dfa-bd92-ba379e648a13)
| ![image](https://github.com/user-attachments/assets/51642a32-f736-440e-b069-74ebd1370cf9) | ![image](https://github.com/user-attachments/assets/ad7cca97-d9c8-4dc1-8b84-2d77a0bf3939) | "A bright red Northern Cardinal with a pointed crest and orange beak, perched on a branch against a softly blurred green background." | ![image](https://github.com/user-attachments/assets/f17a2167-3381-401a-aabe-a966d33b8ef2)


 

**Interface Screenshot:**

<img width="1131" alt="image" src="https://github.com/user-attachments/assets/60641cb3-4d99-4492-b06e-4b16b3b936c2" />




<img width="1131" alt="image" src="https://github.com/user-attachments/assets/e8fd3638-c97c-4b97-b4e2-021ec7916eb4" />




<img width="1126" alt="image" src="https://github.com/user-attachments/assets/bc056c01-6c74-4979-af28-59e8d484a974" />



<img width="1142" alt="image" src="https://github.com/user-attachments/assets/d0a5d18f-595b-443f-8f15-212763daba33" />



---

## Installation

1. **Clone this repository:**

```
git clone https://github.com/IEEE-NITK/text-guided-image-inpainting.git
cd text-guided-image-inpainting
```

2. **Install dependencies:**

```
pip install -r demo/requirements.txt
```
---

## Usage

To launch the interactive inpainting interface locally:
```
python demo/app.py
```

**How to use:**
- Upload an image.
- Select the required height and width of the mask.
- Enter a text prompt describing the desired content.
- Click "Generate Inpainted Image" to generate the result.

The interface is built with Streamlit for ease of use and rapid prototyping.

---

## References

- Lin, Qing, et al. "MMFL: Multimodal Fusion Learning for Text-Guided Image Inpainting." Proceedings of the 28th ACM International Conference on Multimedia, 2020.

---

**Contributions and feedback are welcome!**

---

> *“This paper imitates the process of painters' conjecture, and proposes to introduce the text description into the image inpainting task for the first time, which provides abundant guidance information for image restoration through the fusion of multimodal features.”*


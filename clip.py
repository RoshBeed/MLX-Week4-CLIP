from transformers import CLIPModel, CLIPTokenizer, CLIPImageProcessor
from PIL import Image

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
vision_encoder = model.vision_model
text_encoder = model.text_model
image_processor = CLIPImageProcessor.from_pretrained("openai/clip-vit-base-patch32")
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

items = ["cat", "dog", "horse", "bird", "car", "person", "tree", "house", "book", "phone"]
classifiers = [f"a photo of a {item}" for item in items]

text_inputs = tokenizer(classifiers, return_tensors="pt")
text_features = text_encoder(**text_inputs).pooler_output
text_features_proj = model.text_projection(text_features)

for item, classifier in zip(items, classifiers):
    image = Image.open(f"images/{item}.jpg")
    image_inputs = image_processor(image, return_tensors="pt")
    image_features = vision_encoder(**image_inputs).pooler_output
    image_features_proj = model.visual_projection(image_features)
    
    # Compute similarity to all classifier texts
    similarities = (image_features_proj @ text_features_proj.T).squeeze(0)
    best_idx = similarities.argmax().item()
    best_label = classifiers[best_idx]
    best_score = similarities[best_idx].item()
    
    print(f"{item}: best match is '{best_label}' (score: {best_score:.3f})")
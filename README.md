# CLIP Image Classifier

This project uses OpenAI's CLIP model to classify images based on a set of textual prompts.

## How it works

- For each image in the `images/` folder, the script compares it to a list of classifier texts (e.g., "a photo of a cat", "a photo of a dog", etc.).
- The script prints the best-matching label for each image, along with a similarity score.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare your images:**
   - Place your images in the `images/` folder.
   - Each image should be named after its class, e.g. `cat.jpg`, `dog.jpg`, etc.

3. **Run the script:**
   ```bash
   python clip.py
   ```

## Files

- `clip.py` — Main script for running the classifier.
- `requirements.txt` — Python dependencies.
- `images/` — Folder containing your images.

## Notes

- The script uses the [transformers](https://huggingface.co/docs/transformers/index) library and PyTorch.
- The classifier texts can be easily modified in the script to suit your needs.

---

*Feel free to modify or extend this project!*
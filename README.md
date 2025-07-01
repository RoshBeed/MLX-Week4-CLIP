# CLIP Image Classifier

This project uses OpenAI's CLIP model to classify images based on a set of textual prompts.

## How it works

- For each image in the `images/` folder, the script compares it to a list of classifier texts (e.g., "a photo of a cat", "a photo of a dog", etc.).
- The script prints the best-matching label for each image, along with a similarity score.

## Architecture Diagram

```mermaid
graph TD
    %% Input Data
    A[Images in images/ folder] --> B[cat.jpg, dog.jpg, horse.jpg, etc.]
    C[Text Labels] --> D["'a photo of a cat', 'a photo of a dog', etc."]
    
    %% CLIP Model Components
    E[CLIP Model] --> F[Vision Encoder<br/>ViT-Base-Patch32]
    E --> G[Text Encoder<br/>Transformer]
    E --> H[Image Processor]
    E --> I[Text Tokenizer]
    E --> J[Visual Projection Layer]
    E --> K[Text Projection Layer]
    
    %% Image Processing Pipeline
    B --> H
    H --> L[Processed Image Features]
    L --> F
    F --> M[Image Embeddings<br/>pooler_output]
    M --> J
    J --> N[Projected Image Features<br/>512-dimensional]
    
    %% Text Processing Pipeline
    D --> I
    I --> O[Tokenized Text]
    O --> G
    G --> P[Text Embeddings<br/>pooler_output]
    P --> K
    K --> Q[Projected Text Features<br/>512-dimensional]
    
    %% Similarity Computation
    N --> R[Cosine Similarity<br/>Matrix Multiplication]
    Q --> R
    R --> S[Similarity Scores]
    S --> T[Find Best Match<br/>argmax]
    T --> U[Classification Result]
    
    %% Output
    U --> V[Print Classification Results]
    
    %% Styling
    classDef inputBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef modelBox fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processBox fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef outputBox fill:#fff3e0,stroke:#e65100,stroke-width:2px
    
    class A,C inputBox
    class E,F,G,H,I,J,K modelBox
    class B,D,L,M,N,O,P,Q,R,S,T processBox
    class U,V outputBox
```

## Sample Images

The classifier works with various types of images. Here are some examples from the dataset:

- cat: best match is 'a photo of a cat' (score: 30.380)
- dog: best match is 'a photo of a dog' (score: 35.998)
- horse: best match is 'a photo of a horse' (score: 36.964)
- bird: best match is 'a photo of a bird' (score: 30.397)
- car: best match is 'a photo of a car' (score: 23.982)
- person: best match is 'a photo of a person' (score: 27.901)
- tree: best match is 'a photo of a tree' (score: 30.656)
- house: best match is 'a photo of a house' (score: 29.412)
- book: best match is 'a photo of a book' (score: 40.067)
- phone: best match is 'a photo of a phone' (score: 32.127)

<div align="center">

![Cat](images/cat.jpg) ![Dog](images/dog.jpg) ![Horse](images/horse.jpg) ![Bird](images/bird.jpg)

![Car](images/car.jpg) ![Person](images/person.jpg) ![Tree](images/tree.jpg) ![House](images/house.jpg)

![Book](images/book.jpg) ![Phone](images/phone.jpg)

</div>

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare your images:**
   - Place your images in the `images/` folder.

3. **Run the script:**
   ```bash
   python clip.py
   ```

## Files

- `clip.py` — Main script for running the classifier.
- `requirements.txt` — Python dependencies.
- `images/` — Folder containing your images.

---

*Feel free to modify or extend this project!*
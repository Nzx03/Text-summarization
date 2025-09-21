# Text-summarization
## 📌 Overview

This is an **end-to-end machine learning project** for abstractive text summarization using **Google’s Pegasus model (CNN/DailyMail variant)**.  

The project includes:

- **Training / fine-tuning Pegasus** using Hugging Face Transformers  
- **Providing a FastAPI web app** (`app.py`) for real-time text summarization  
- **Following a modular ML pipeline** structure with:
  - Data ingestion
  - Data Validation
  - Data Transformation
  -  Model training
  -  Model Evaluation
    

## ⚙️ Installation & Setup
1. Clone the Repository
   ```
   git clone <repo_url>
   cd Text-Summarization
   ```
2. Create a Virtual Environment
   ```
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```
(or using conda)
  ```
  conda create -n textsum python=3.11
  conda activate textsum
 ```
3. Install Dependencies
  ```
  pip install -r requirements.txt
 ```
🌐 Running the FastAPI App
The FastAPI web application is implemented in `app.py`.  
This is the main entry point for interacting with the text summarization model.

### Start the FastAPI server:

```bash
python app.py
```




   

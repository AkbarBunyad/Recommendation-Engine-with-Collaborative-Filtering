# Recommendation-Engine-with-Collaborative-Filtering

Book Recommendation System built using collaborative filtering and K-Nearest Neighbors (KNN) clustering on Streamlit. The model recommends books based on user ratings given for each one and provides posters for them.

Among the 3 mostly used recommendation approaches, collaborative - based one was used in the project, which clusters items based on their cosine similarity scores.

Project Demo:
![image](https://github.com/AkbarBunyad/Recommendation-Engine-with-Collaborative-Filtering/assets/114834354/3f2105b3-ab24-4b2a-bae5-8b5d1a889d5b)

Project Workflow:
![Screenshot 2024-06-17 120037](https://github.com/AkbarBunyad/Recommendation-Engine-with-Collaborative-Filtering/assets/114834354/c063a2e0-3996-4928-8621-3a67ebdcd1d7)

## Dataset
The dataset used in this project is obtained from [Kaggle](https://www.kaggle.com/datasets/ra4u12/bookrecommendation) and consists of three files:

BX-Books.csv
BX-Users.csv
BX-Book-Ratings.csv

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AkbarBunyad/Recommendation-Engine-with-      
    Collaborative-Filtering.git
    cd Recommendation-Engine-with-Collaborative-Filtering

    ```
    
2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    conda create --name recsys_env python=3.8
    conda activate recsys_env

    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt

## File Structure

```plaintext
Recommendation-Engine-with-Collaborative-Filtering/
├── data/                          # Folder containing the dataset
│   ├── books.csv                  # Books data
│   ├── users.csv                  # Users data
│   └── ratings.csv                # Ratings data
├── Recommendation_System.ipynb    # Jupyter notebook containing data preprocessing and model building with KNN
├── app.py                         # Streamlit script  
├── requirements.txt               # The required Python packages
└── README.md                      # This README file

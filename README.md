# St. George Image Detection Project

## Overview

This project involves image classification using a custom dataset of images containing 'St. George' and 'non-St. George' categories. The goal is to build a robust classification model that can distinguish between these two categories based on image data.

## Project Structure

- `csv files/georges.csv`: CSV file containing URLs of images for the 'St. George' category.
- `Dataset/`: Directory where images will be saved.
  - `georges/`: Folder containing images of 'St. George'.
  - `no_georges/`: Folder containing images of 'non-St. George'.
- `data_preprocessing.py`: Script for downloading images and preparing the dataset.
- `model_training.py`: Script for training the image classification model (if applicable).
- `README.md`: This file.

## Setup

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Installation

**Clone the Repository**

```bash
git clone <repository-url>
cd <repository-directory>
```


**Install Dependencies**

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r
requirements.txt
```

## Data Preparation

### Download Images

Ensure you have the `csv files/georges.csv` file with URLs of images to download. Run the `url_to_img.py` script to download and save images:

```bash
python url_to_img.py
```
## Organize Dataset
### Ensure your dataset directory structure is as follows:

- Dataset/
  - georges/
     - image1.jpg
     - image2.jpg
    ...
  - no_georges/
    - image1.jpg
    - image2.jpg
    ...


## Usage

### Data Preprocessing

The `url_to_img.py` script handles image downloading and dataset creation. Ensure your `csv files/georges.csv` file is correctly formatted with image URLs.

### Training the Model

To train the classification model, run:

 ```bash
     train_model.ipynb
 ```

### Testing the Model

To evaluate the performance of the trained model, run:

1. **Load the Model**: Use the following code snippet to load the model in `model_testing.py`:

    ```python
      from tensorflow.keras.models import load_model
  
      model_path = 'models/st_george_detector.h5'  # Update this with your model's path
      model = load_model(model_path)
    ```

2. **Run the Testing Script**:

    ```bash
     test_model.ipynb
    ```

Ensure that the `model_testing.py` script is correctly set up to load the trained model and test it on a validation or test dataset.


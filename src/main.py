from Preprocessor import *

from src.feature_extractor import *

imgPath = ''

img = None
# img = cv.imread(imgPath)

preprocess(img)

features = extract_features(img)

# for img in data set
# Preprocess the image
# Extract features img
    # Segment img into lines
    # Segment lines into words
    # Extract different features into vector

# Train the model on the extracted features
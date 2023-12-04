# Sports-celebrity-classification
This project involves building a Convolutional Neural Network (CNN) for the classification of celebrity images into different categories. The dataset consists of images of five celebrities: Lionel Messi, Maria Sharapova, Roger Federer, Serena Williams, and Virat Kohli.

## 1. Model

The celebrity recognition model is implemented using a Convolutional Neural Network (CNN) with TensorFlow and Keras. The model architecture includes the following layers:

- **Input Layer:** Convolutional layer with 32 filters of size (3, 3) and ReLU activation.
- **MaxPooling Layer:** MaxPooling with a pool size of (2, 2) for downsampling.
- **Flatten Layer:** Flattens the output from the previous layers.
- **Dense Layer 1:** Fully connected layer with 256 neurons and ReLU activation.
- **Dropout Layer:** Dropout layer with a dropout rate of 0.5 for regularization.
- **Dense Layer 2:** Fully connected layer with 512 neurons and ReLU activation.
- **Output Layer:** Dense output layer with 5 neurons (equal to the number of classes) and softmax activation for multi-class classification.

The model is compiled with the Adam optimizer, sparse categorical crossentropy loss function, and accuracy as the evaluation metric.

## 2. Training

### Data Preprocessing:

- Images are loaded from different celebrity directories.
- Images are resized to (128, 128) pixels.

### Train-Test Split:

- The dataset is split into training and testing sets (80% training, 20% testing).

### Normalization:

- Pixel values are normalized to the range [0, 1].

### Model Training:

- The model is trained for 50 epochs with a batch size of 64.
- Training includes a validation split (10% of the training data) for monitoring overfitting.

## 3. Findings

### Accuracy:

- The model achieved an accuracy of approximately 82.35% on the validation set.
- Training and validation accuracy and loss were tracked over the epochs, demonstrating the model's learning progress.

### Classification Report:

- Precision, recall, and F1-score were provided for each class, offering a detailed performance analysis for individual celebrity classes.
- Macro and weighted averages for precision, recall, and F1-score were also given, providing an overall assessment of the model's performance.

### Model Prediction:

- The model was tested on a set of celebrity images, and predictions were made for each image.
- Predictions for specific celebrities were provided, demonstrating the model's capability of making accurate predictions.

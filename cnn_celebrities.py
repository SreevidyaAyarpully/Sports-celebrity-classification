import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import tensorflow as tf
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tqdm import tqdm

tf.random.set_seed(7)

image_dir = r'data\cropped'
image_messi = os.listdir(r'data\cropped\lionel_messi')
image_maria = os.listdir(r'data\cropped\maria_sharapova')
image_roger = os.listdir(r'data\cropped\roger_federer')
image_serena = os.listdir(r'data\cropped\serena_williams')
image_virat = os.listdir(r'data\cropped\virat_kohli')


dataset = []
label = []
img_size = (128,128)

for i, image_name in tqdm(enumerate(image_messi), desc="lionel messi"):
    if image_name.split('.')[1] == 'png':
        image = cv2.imread(os.path.join(image_dir, 'lionel_messi', image_name))
        image = Image.fromarray(image, 'RGB')
        image = image.resize(img_size)
        dataset.append(np.array(image))
        label.append(0)

for i, image_name in tqdm(enumerate(image_maria), desc="maria sharapova"):
    if image_name.split('.')[1] == 'png':
        image = cv2.imread(os.path.join(image_dir, 'maria_sharapova', image_name))
        image = Image.fromarray(image, 'RGB')
        image = image.resize(img_size)
        dataset.append(np.array(image))
        label.append(1)

for i, image_name in tqdm(enumerate(image_roger), desc="roger federer"):
    if image_name.split('.')[1] == 'png':
        image = cv2.imread(os.path.join(image_dir, 'roger_federer', image_name))
        image = Image.fromarray(image, 'RGB')
        image = image.resize(img_size)
        dataset.append(np.array(image))
        label.append(2)

for i, image_name in tqdm(enumerate(image_serena), desc="serena williams"):
    if image_name.split('.')[1] == 'png':
        image = cv2.imread(os.path.join(image_dir, 'serena_williams', image_name))
        image = Image.fromarray(image, 'RGB')
        image = image.resize(img_size)
        dataset.append(np.array(image))
        label.append(3)

for i, image_name in tqdm(enumerate(image_virat), desc="virat kohli"):
    if image_name.split('.')[1] == 'png':
        image = cv2.imread(os.path.join(image_dir, 'virat_kohli', image_name))
        image = Image.fromarray(image, 'RGB')
        image = image.resize(img_size)
        dataset.append(np.array(image))
        label.append(4)

dataset=np.array(dataset)
label = np.array(label)

print('--------------------Train-Test split--------------------\n')
x_train,x_test,y_train,y_test=train_test_split(dataset,label,test_size=0.2,random_state=42)

print("\n--------------------Normalising the Dataset--------------------\n")
x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)

model=tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256,activation='relu'),
    tf.keras.layers.Dropout(.5),
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dense(5,activation='softmax')
])

model.summary()
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

print("\n-----------------Training Started-----------------\n")
model.fit(x_train,y_train,epochs=50,batch_size = 64,validation_split=0.1)
print("\n-----------------Training Finished-----------------\n")

print("\n-----------------Model Evaluation-----------------\n")
loss,accuracy=model.evaluate(x_test,y_test)
print(f'\nAccuracy: {round(accuracy*100,2)}')

y_pred=model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)

print('\n-----------------Classification Report-----------------\n', classification_report(y_test, y_pred_classes))

print("\n-----------------Model Prediction-----------------\n")

def make_prediction(img_path, model):
    img = cv2.imread(img_path)
    img = Image.fromarray(img)
    img = img.resize((128, 128))
    img = np.array(img)
    input_img = np.expand_dims(img, axis=0)
    res = model.predict(input_img)
    
    class_labels = ['Lionel Messi', 'Maria Sharapova', 'Roger Federer', 'Serena Williams', 'Virat Kohli']
    
    predicted_class_index = np.argmax(res)
    predicted_class_label = class_labels[predicted_class_index]
    
    print("Predicted Celebrity: ", predicted_class_label)

# # Example
make_prediction(r'data\cropped\maria_sharapova\maria_sharapova17.png', model)

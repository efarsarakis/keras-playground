## Example from: 
##        https://elitedatascience.com/keras-tutorial-deep-learning-in-python#step-3
## More accurate code can be found at :
##      https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py

import numpy as np
np.random.seed(123)
from keras.models import Sequential

from keras.layers import Dense, Dropout, Activation, Flatten

from keras.layers import Conv2D, MaxPooling2D

from keras.utils import np_utils

from keras.datasets import mnist

from keras import backend as K

(X_train, y_train), (X_test, y_test) = mnist.load_data()
img_height = 28
img_width = 28

print(X_train.shape)

from matplotlib import pyplot as plt
#plt.imshow(X_train[0])

#plt.show()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
input_shape = (img_height, img_width, 1)

print(X_train.shape)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

#print(y_train.shape)

#print(y_train[:10])

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
#print(y_train[:10])
#print(y_train.shape)
print(K.image_data_format() == 'channels_first')
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))


#print(model.output_shape)

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', 
	optimizer='adam',
	metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, nb_epoch=10, verbose=1)
score = model.evaluate(X_test, y_test, verbose=0)

print(score)

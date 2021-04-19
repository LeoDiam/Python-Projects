import tensorflow as tf
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0
print(train_images.shape)
print(test_images.shape)
print(train_labels)

plt.imshow(train_images[0], cmap='gray')
plt.show()
my_model = tf.keras.models.Sequential()
my_model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
my_model.add(tf.keras.layers.Dense(128, activation='relu'))
my_model.add(tf.keras.layers.Dense(10, activation='softmax'))

my_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
my_model.fit(train_images, train_labels, epochs=3)

val_loss, val_acc = my_model.evaluate(test_images, test_labels)
print("Test accuracy: ", val_acc)

my_model.save('my_mnist_model')

my_new_model = tf.keras.models.load_model('my_mnist_model')

new_val_loss, new_val_acc = my_new_model.evaluate(test_images, test_labels)
print("New Test accuracy: ", new_val_acc)
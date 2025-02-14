import tensorflow as tf
from keras import datasets, layers, models, optimizers, losses
import matplotlib.pyplot as plt
import numpy as np

# Load and normalize CIFAR10
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to [-1, 1]
train_images = (train_images.astype('float32') / 255) * 2 - 1
test_images = (test_images.astype('float32') / 255) * 2 - 1

class_names = ('airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck')

# Show some training images
plt.figure(figsize=(10, 10))
for i in range(4):
    plt.subplot(1, 4, i+1)
    img = (train_images[i] + 1) / 2  # Scale back to [0,1] for display
    plt.imshow(img)
    plt.title(class_names[train_labels[i][0]])
    plt.axis('off')
plt.show()

# Define the model
model = models.Sequential([
    layers.Conv2D(6, (5, 5), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(16, (5, 5), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(120, activation='relu'),
    layers.Dense(84, activation='relu'),
    layers.Dense(10)
])

# Compile the model
optimizer = optimizers.SGD(learning_rate=0.001, momentum=0.9)
loss_fn = losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer=optimizer,
              loss=loss_fn,
              metrics=['accuracy'])

# Train the model
history = model.fit(train_images, train_labels,
                    epochs=2,
                    batch_size=4,
                    validation_data=(test_images, test_labels))

# Save the model
model.save('cifar_model.keras')

# Evaluate on test data
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'Test accuracy: {test_acc*100:.2f}%')

# Per-class accuracy
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)
test_labels_flat = test_labels.ravel()

correct_pred = {classname: 0 for classname in class_names}
total_pred = {classname: 0 for classname in class_names}

for true_label, pred_label in zip(test_labels_flat, predicted_labels):
    class_name = class_names[true_label]
    total_pred[class_name] += 1
    if true_label == pred_label:
        correct_pred[class_name] += 1

for classname in class_names:
    accuracy = 100 * correct_pred[classname] / total_pred[classname]
    print(f'Accuracy for class {classname:5s}: {accuracy:.1f}%')
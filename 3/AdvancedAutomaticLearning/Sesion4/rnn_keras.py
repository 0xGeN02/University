# Import libraries
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from keras.layers import Embedding, SimpleRNN, Dense, Dropout, LSTM
from tensorflow.keras.preprocessing import sequence

# Load and preprocess the IMDB dataset (built into Keras)
max_features = 10000  # Vocabulary size (top 10,000 words)
maxlen = 200  # Truncate/pad reviews to 200 words
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# Pad sequences to ensure uniform length for RNN input
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

# Build the RNN model
model = Sequential([
    Embedding(input_dim=max_features, output_dim=128, input_length=maxlen),  # Convert word IDs to vectors
    LSTM(64),  # Single RNN layer with 64 units
    Dropout(0.5),  # Reduce overfitting
    Dense(1, activation='sigmoid')  # Output layer (binary classification)
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model (use a subset for speed in class)
history = model.fit(
    x_train[:5000], y_train[:5000],  # Use first 5k samples for quick training
    epochs=10,
    batch_size=64,
    validation_split=0.2
)

model.save('imdb_model_lstm.keras')

# Evaluate on test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nTest accuracy: {test_acc:.2f}')

# Predict sentiment for a sample review
sample_review = x_test[0:1]  # Take the first test review





prediction = model.predict(sample_review)

word_index = imdb.get_word_index()  # Get the word-to-integer mapping
reverse_word_index = {value + 3: key for (key, value) in word_index.items()}

# Add reserved indices (padding, start, unknown, unused)
reverse_word_index[0] = "<PAD>"  # Padding token
reverse_word_index[1] = "<START>"  # Start of sequence
reverse_word_index[2] = "<UNK>"  # Unknown word
reverse_word_index[3] = "<UNUSED>"

# Decode the review (convert integers to words)
decoded_review = " ".join(
    [reverse_word_index.get(i, "?") for i in sample_review[0]]
)

# Print the decoded review and prediction
print("\nDecoded Review:")
print(decoded_review.replace("<PAD> ", ""))  # Remove padding tokens for readability
print(f"\nPredicted sentiment (0=negative, 1=positive): {prediction[0][0]:.2f}")
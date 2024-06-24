import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from scipy.optimize import minimize

# Generate or load training data
# X_train: array of shape (num_samples, 40) representing circle coordinates
# y_train: array of shape (num_samples,) representing the radius of the enclosing circle

# Example data generation function (this is a placeholder and should be replaced with actual data)
def generate_training_data(num_samples):
    X_train = np.random.rand(num_samples, 40) * 2 - 1  # Random positions in the range [-1, 1]
    y_train = np.max(np.sqrt(X_train[:, ::2]**2 + X_train[:, 1::2]**2), axis=1) + 0.5
    return X_train, y_train

X_train, y_train = generate_training_data(1000)

# Define the MLP model
model = Sequential([
    Dense(64, input_dim=40, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=1000, batch_size=32, validation_split=0.2)

# Use the trained model to predict an initial configuration
def predict_packing(arrangement):
    return model.predict(arrangement)

# Objective function to minimize: the radius of the enclosing circle
def objective_function(coords):
    coords = coords.reshape((20, 2))
    radius = np.max(np.sqrt(coords[:, 0]**2 + coords[:, 1]**2)) + 0.5
    return radius

# Constraint to ensure circles do not overlap
def non_overlap_constraint(coords):
    coords = coords.reshape((20, 2))
    min_distance = 1.0  # Diameter of the circles
    distances = np.sqrt((coords[:, np.newaxis, 0] - coords[np.newaxis, :, 0])**2 + 
                        (coords[:, np.newaxis, 1] - coords[np.newaxis, :, 1])**2)
    np.fill_diagonal(distances, np.inf)
    return np.min(distances) - min_distance

# Optimize the initial configuration
def refine_packing(initial_arrangement):
    cons = [{'type': 'ineq', 'fun': non_overlap_constraint}]
    result = minimize(objective_function, initial_arrangement, constraints=cons, method='SLSQP')
    refined_arrangement = result.x
    return refined_arrangement

# Example prediction and refinement
initial_arrangement = np.random.rand(1, 40) * 2 - 1
predicted_radius = predict_packing(initial_arrangement)
refined_arrangement = refine_packing(initial_arrangement.flatten())

# Extract x and y coordinates
x_coords = refined_arrangement[::2]
y_coords = refined_arrangement[1::2]

# Print x and y coordinates as comma-separated lists
print("Predicted radius:", predicted_radius[0])
print("X coordinates:", ', '.join(map(str, x_coords)))
print("Y coordinates:", ', '.join(map(str, y_coords)))
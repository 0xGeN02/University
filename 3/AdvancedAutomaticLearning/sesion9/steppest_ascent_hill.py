import logging
import math
import random

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Generate a complex synthetic dataset
X, y = make_classification(
    n_samples=5000, 
    n_features=20, 
    n_informative=15, 
    n_redundant=5,
    n_classes=3,
    random_state=42
)

def objective_function(state):
    """
    Objective function that returns the mean cross-validation accuracy
    for a RandomForestClassifier with the given hyperparameters.

    Args:
        state (dict): Hyperparameter configuration with keys:
            - 'n_estimators' (int): number of trees in the forest
            - 'max_depth' (int): maximum depth of each tree
            - 'min_samples_split' (int): minimum number of samples required to split an internal node

    Returns:
        float: Mean cross-validation accuracy (higher is better)
    """
    # Validate hyperparameter bounds
    if not (50 <= state['n_estimators'] <= 500 and
            5 <= state['max_depth'] <= 50 and
            2 <= state['min_samples_split'] <= 20):
        logger.debug("Invalid state encountered: %s", state)
        return 0.0  # Return worst score for invalid hyperparameters

    # Create the Random Forest model with current hyperparameters
    model = RandomForestClassifier(
        n_estimators=state['n_estimators'],
        max_depth=state['max_depth'],
        min_samples_split=state['min_samples_split'],
        random_state=42,
        n_jobs=-1  # Utilize all CPU cores
    )

    # Perform 3-fold cross validation (reduced for faster computation)
    scores = cross_val_score(model, X, y, cv=3)
    mean_score = np.mean(scores)
    logger.debug("Evaluated state %s with score: %.4f", state, mean_score)
    return mean_score

def get_neighbors(state):
    """
    Generates neighboring hyperparameter configurations by perturbing each parameter.

    Args:
        state (dict): Current hyperparameter configuration.

    Returns:
        list: List of new hyperparameter configurations (dicts).
    """
    neighbors = []

    # Define adaptive step sizes for each hyperparameter
    steps = {
        'n_estimators': max(10, int(state['n_estimators'] * 0.1)),  # 10% of current value
        'max_depth': 5,
        'min_samples_split': 2,
    }

    # For each hyperparameter, generate neighbors
    for param in state:
        for delta in [-steps[param], steps[param]]:
            new_state = state.copy()
            new_state[param] += delta

            # Check boundaries before adding neighbor
            if param == 'n_estimators' and (50 <= new_state[param] <= 500):
                neighbors.append(new_state)
            elif param == 'max_depth' and (5 <= new_state[param] <= 50):
                neighbors.append(new_state)
            elif param == 'min_samples_split' and (2 <= new_state[param] <= 20):
                neighbors.append(new_state)

    logger.debug("Generated %d neighbors for state %s", len(neighbors), state)
    return neighbors

def steepest_ascent_hill_climbing(initial_state, max_iterations=30):
    """
    Implements Steepest Ascent Hill-Climbing algorithm for hyperparameter tuning.
    
    Args:
        initial_state (dict): Starting hyperparameter configuration
        max_iterations (int): Maximum iterations to run the algorithm
        
    Returns:
        tuple: (best_state, best_score)
    """
    current_state = initial_state
    current_value = objective_function(current_state)
    logger.info("Starting steepest ascent with initial state: %s (score: %.4f)", 
                current_state, current_value)

    for iteration in range(1, max_iterations + 1):
        neighbors = get_neighbors(current_state)
        if not neighbors:
            logger.info("No neighbors available. Terminating search.")
            break

        # Evaluate all neighbors
        best_neighbor = None
        best_score = -float('inf')
        
        logger.info("Iteration %d: Evaluating %d neighbors", iteration, len(neighbors))
        for neighbor in neighbors:
            score = objective_function(neighbor)
            if score > best_score:
                best_neighbor = neighbor
                best_score = score

        # Check for improvement
        if best_score > current_value:
            current_state = best_neighbor
            current_value = best_score
            logger.info("Improvement found! New state: %s (score: %.4f)", 
                        current_state, current_value)
        else:
            logger.info("No improvement found. Terminating search.")
            break

    logger.info("Steepest ascent completed. Best score: %.4f", current_value)
    return current_state, current_value

# Initial hyperparameter configuration
initial_state = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 2,
}

# Execute the optimization
best_state, best_score = steepest_ascent_hill_climbing(initial_state)

print("\nOptimization Results:")
print(f"Initial Hyperparameters: {initial_state}")
print(f"Optimized Hyperparameters: {best_state}")
print(f"Best Cross-Validation Accuracy: {best_score:.4f}")
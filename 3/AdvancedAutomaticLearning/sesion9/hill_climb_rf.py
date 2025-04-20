import logging
import math
import random

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Load a sample dataset (Iris)
data = load_digits()
X, y = data.data, data.target


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
    if not (10 <= state['n_estimators'] <= 200 and
            1 <= state['max_depth'] <= 20 and
            2 <= state['min_samples_split'] <= 20):
        logger.debug("Invalid state encountered: %s", state)
        return 0.0  # Return worst score for invalid hyperparameters

    # Create the Random Forest model with current hyperparameters
    model = RandomForestClassifier(
        n_estimators=state['n_estimators'],
        max_depth=state['max_depth'],
        min_samples_split=state['min_samples_split'],
        random_state=42
    )

    # Perform 5-fold cross validation
    scores = cross_val_score(model, X, y, cv=5)
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

    # Define step sizes for each hyperparameter
    steps = {
        'n_estimators': 5,
        'max_depth': 1,
        'min_samples_split': 1,
    }

    # For each hyperparameter, generate a neighbor by increasing or decreasing its value
    for param in state:
        for delta in [-steps[param], steps[param]]:
            new_state = state.copy()
            new_state[param] += delta

            # Check boundaries before adding neighbor
            if param == 'n_estimators' and (10 <= new_state[param] <= 200):
                neighbors.append(new_state)
            elif param == 'max_depth' and (1 <= new_state[param] <= 20):
                neighbors.append(new_state)
            elif param == 'min_samples_split' and (2 <= new_state[param] <= 20):
                neighbors.append(new_state)

    logger.debug("Generated %d neighbors for state %s", len(neighbors), state)
    return neighbors


def simple_hill_climbing(initial_state, max_iterations=50):
    """
    Implements a simple hill climbing algorithm for hyperparameter tuning.

    Args:
        initial_state (dict): Starting hyperparameter configuration.
        max_iterations (int): Maximum iterations to run the algorithm.

    Returns:
        tuple: (best_state, best_score)
    """
    current_state = initial_state
    current_value = objective_function(current_state)
    logger.info("Starting hill climbing with initial state: %s, score: %.4f", current_state, current_value)

    for iteration in range(1, max_iterations + 1):
        neighbors = get_neighbors(current_state)
        found_better = False

        logger.info("Iteration %d: Evaluating %d neighbors.", iteration, len(neighbors))
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            logger.debug("Neighbor %s has score: %.4f", neighbor, neighbor_value)

            # If a neighbor yields a higher accuracy, move to that neighbor
            if neighbor_value > current_value:
                logger.info("Found better neighbor: %s with score: %.4f", neighbor, neighbor_value)
                current_state = neighbor
                current_value = neighbor_value
                found_better = True
                break  # Move immediately to the first better neighbor

        # If no better neighbor is found, we've reached a peak
        if not found_better:
            logger.info("No better neighbor found in iteration %d. Terminating search.", iteration)
            break

    logger.info("Hill climbing completed. Best state: %s with score: %.4f", current_state, current_value)
    return current_state, current_value


def state_to_tuple(state):
    """
    Converts a state dictionary to a tuple representation for hashing.

    Args:
        state (dict): Hyperparameter configuration.

    Returns:
        tuple: A tuple representation of the state.
    """
    return (state['n_estimators'], state['max_depth'], state['min_samples_split'])


def tabu_search(initial_state, max_iterations=100, tabu_tenure=10):
    """
    Implements Tabu Search for hyperparameter tuning.

    Args:
        initial_state (dict): Starting hyperparameter configuration.
        max_iterations (int): Maximum number of iterations to perform.
        tabu_tenure (int): Maximum size of the tabu list.

    Returns:
        tuple: (best_state, best_score)
    """
    current_state = initial_state
    current_value = objective_function(current_state)
    best_state = current_state
    best_value = current_value

    # Tabu list to store recently visited states (using their tuple representation)
    tabu_list = []

    logger.info("Starting Tabu Search with initial state: %s, score: %.4f", current_state, current_value)

    for iteration in range(1, max_iterations + 1):
        neighbors = get_neighbors(current_state)
        best_candidate = None
        best_candidate_value = -float("inf")

        # Evaluate all neighbors and select the best candidate not in the tabu list
        for neighbor in neighbors:
            neighbor_tuple = state_to_tuple(neighbor)
            if neighbor_tuple in tabu_list:
                logger.debug("Neighbor %s is in the tabu list.", neighbor)
                continue  # Skip tabu states

            neighbor_value = objective_function(neighbor)
            logger.debug("Neighbor %s has score: %.4f", neighbor, neighbor_value)

            if neighbor_value > best_candidate_value:
                best_candidate = neighbor
                best_candidate_value = neighbor_value

        if best_candidate is None:
            logger.info("Iteration %d: No non-tabu neighbors found. Terminating search.", iteration)
            break

        # Move to the best candidate found
        logger.info("Iteration %d: Moving from state %s (score: %.4f) to %s (score: %.4f)",
                    iteration, current_state, current_value, best_candidate, best_candidate_value)
        current_state = best_candidate
        current_value = best_candidate_value

        # Update best found solution
        if current_value > best_value:
            best_state = current_state
            best_value = current_value
            logger.info("Iteration %d: Updated best state to %s with score %.4f", iteration, best_state, best_value)

        # Add the new state to the tabu list
        tabu_list.append(state_to_tuple(current_state))
        # If the tabu list is longer than the allowed tenure, remove the oldest entry
        if len(tabu_list) > tabu_tenure:
            removed = tabu_list.pop(0)
            logger.debug("Removed state %s from the tabu list.", removed)

    logger.info("Tabu Search completed. Best state: %s with score: %.4f", best_state, best_value)
    return best_state, best_value


def simulated_annealing(initial_state, max_iterations=100, initial_temperature=1.0, cooling_rate=0.95):
    """
    Implements simulated annealing for hyperparameter tuning.

    Args:
        initial_state (dict): Starting hyperparameter configuration.
        max_iterations (int): Maximum iterations for the algorithm.
        initial_temperature (float): Starting temperature.
        cooling_rate (float): Factor by which the temperature decreases each iteration.

    Returns:
        tuple: (best_state, best_score)
    """
    current_state = initial_state
    current_value = objective_function(current_state)
    best_state = current_state
    best_value = current_value
    temperature = initial_temperature

    logger.info("Starting simulated annealing with initial state: %s, score: %.4f", current_state, current_value)

    for iteration in range(1, max_iterations + 1):
        # Decrease temperature
        temperature *= cooling_rate

        # Generate neighbors and randomly select one to consider
        neighbors = get_neighbors(current_state)
        if not neighbors:
            logger.info("No neighbors generated. Terminating search.")
            break
        next_state = random.choice(neighbors)
        next_value = objective_function(next_state)

        # Calculate change in objective
        delta = next_value - current_value

        # Accept new state if better, or with a probability if worse
        if delta > 0 or random.uniform(0, 1) < math.exp(delta / temperature):
            logger.info("Iteration %d: Moving from state %s (score: %.4f) to %s (score: %.4f) at temperature %.4f",
                        iteration, current_state, current_value, next_state, next_value, temperature)
            current_state = next_state
            current_value = next_value

            # Update best found solution
            if current_value > best_value:
                best_state = current_state
                best_value = current_value
        else:
            logger.debug("Iteration %d: Rejected neighbor %s (score: %.4f) with temperature %.4f",
                         iteration, next_state, next_value, temperature)

    logger.info("Simulated annealing completed. Best state: %s with score: %.4f", best_state, best_value)
    return best_state, best_value


def state_to_tuple(state):
    """
    Converts a state dictionary to a tuple representation for hashing.

    Args:
        state (dict): Hyperparameter configuration.

    Returns:
        tuple: A tuple representation of the state.
    """
    return (state['n_estimators'], state['max_depth'], state['min_samples_split'])


def tabu_search(initial_state, max_iterations=100, tabu_tenure=10):
    """
    Implements Tabu Search for hyperparameter tuning.

    Args:
        initial_state (dict): Starting hyperparameter configuration.
        max_iterations (int): Maximum number of iterations to perform.
        tabu_tenure (int): Maximum size of the tabu list.

    Returns:
        tuple: (best_state, best_score)
    """
    current_state = initial_state
    current_value = objective_function(current_state)
    best_state = current_state
    best_value = current_value

    # Tabu list to store recently visited states (using their tuple representation)
    tabu_list = []

    logger.info("Starting Tabu Search with initial state: %s, score: %.4f", current_state, current_value)

    for iteration in range(1, max_iterations + 1):
        neighbors = get_neighbors(current_state)
        best_candidate = None
        best_candidate_value = -float("inf")

        # Evaluate all neighbors and select the best candidate not in the tabu list
        for neighbor in neighbors:
            neighbor_tuple = state_to_tuple(neighbor)
            if neighbor_tuple in tabu_list:
                logger.debug("Neighbor %s is in the tabu list.", neighbor)
                continue  # Skip tabu states

            neighbor_value = objective_function(neighbor)
            logger.debug("Neighbor %s has score: %.4f", neighbor, neighbor_value)

            if neighbor_value > best_candidate_value:
                best_candidate = neighbor
                best_candidate_value = neighbor_value

        if best_candidate is None:
            logger.info("Iteration %d: No non-tabu neighbors found. Terminating search.", iteration)
            break

        # Move to the best candidate found
        logger.info("Iteration %d: Moving from state %s (score: %.4f) to %s (score: %.4f)",
                    iteration, current_state, current_value, best_candidate, best_candidate_value)
        current_state = best_candidate
        current_value = best_candidate_value

        # Update best found solution
        if current_value > best_value:
            best_state = current_state
            best_value = current_value
            logger.info("Iteration %d: Updated best state to %s with score %.4f", iteration, best_state, best_value)

        # Add the new state to the tabu list
        tabu_list.append(state_to_tuple(current_state))
        # If the tabu list is longer than the allowed tenure, remove the oldest entry
        if len(tabu_list) > tabu_tenure:
            removed = tabu_list.pop(0)
            logger.debug("Removed state %s from the tabu list.", removed)

    logger.info("Tabu Search completed. Best state: %s with score: %.4f", best_state, best_value)
    return best_state, best_value


# Example usage:
initial_state = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 2,
}

# best_state, best_value = simple_hill_climbing(initial_state)
# print("Simple Hill Climbing:")
# print("Initial Hyperparameters:", initial_state)
# print("Best Hyperparameters Found:", best_state)
# print("Best Cross-Validation Accuracy:", best_value)
# print("Simulated Annealing:")
# best_state, best_value = simulated_annealing(initial_state)
# print("Initial Hyperparameters:", initial_state)
# print("Best Hyperparameters Found:", best_state)
# print("Best Cross-Validation Accuracy:", best_value)
print("Tabu Search:")
best_state, best_value = tabu_search(initial_state)
print("Initial Hyperparameters:", initial_state)
print("Best Hyperparameters Found:", best_state)
print("Best Cross-Validation Accuracy:", best_value)

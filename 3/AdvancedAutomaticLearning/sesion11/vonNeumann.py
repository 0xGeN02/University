import numpy as np

# Define the objective function you wish to minimize.
# For demonstration, we use the simple sphere function.
def sphere(x):
    return np.sum(x**2)

# Initialize particle positions, velocities, and personal bests.
def initialize_particles(num_particles, dimensions, bounds):
    lower, upper = bounds
    positions = np.random.uniform(lower, upper, (num_particles, dimensions))
    # Initialize velocities within a reasonable scale (based on search space)
    velocities = np.random.uniform(-abs(upper-lower), abs(upper-lower), (num_particles, dimensions))
    pbest_positions = positions.copy()
    pbest_scores = np.array([np.inf] * num_particles)
    return positions, velocities, pbest_positions, pbest_scores

# Given a particle index and grid shape, compute the indices of its Von Neumann neighbors.
def get_von_neumann_neighbors(index, grid_shape):
    rows, cols = grid_shape
    row = index // cols
    col = index % cols
    
    # Using periodic boundary conditions for neighborhood
    up = ((row - 1) % rows, col)
    down = ((row + 1) % rows, col)
    left = (row, (col - 1) % cols)
    right = (row, (col + 1) % cols)
    
    # Convert from (row, col) positions back to linear indices
    neighbors = [up, down, left, right]
    neighbor_indices = [r * cols + c for r, c in neighbors]
    
    return neighbor_indices

# PSO with Von Neumann neighborhood topology.
def pso_von_neumann(func, num_particles, dimensions, bounds, iterations, grid_shape):
    # Initialize particles
    positions, velocities, pbest_positions, pbest_scores = initialize_particles(num_particles, dimensions, bounds)
    
    # PSO parameters
    w = 0.7           # inertia weight
    c1 = 1.5          # cognitive coefficient
    c2 = 1.5          # social coefficient (local neighborhood influence)
    
    # For tracking the overall global best (optional, if you want to record it)
    best_global_score = np.inf
    best_global_position = None
    
    # PSO main loop
    for iter in range(iterations):
        # Evaluate fitness for each particle
        scores = np.apply_along_axis(func, 1, positions)
        
        # Update personal bests
        for i in range(num_particles):
            if scores[i] < pbest_scores[i]:
                pbest_scores[i] = scores[i]
                pbest_positions[i] = positions[i].copy()
        
        # Determine the best position within the Von Neumann neighborhood for each particle.
        nbests = np.empty_like(positions)
        for i in range(num_particles):
            # Identify neighbor indices for the current particle
            neighbor_indices = get_von_neumann_neighbors(i, grid_shape)
            # Include the particle itself in the neighborhood
            neighborhood = neighbor_indices + [i]
            # Find the index within the neighborhood that has the best (lowest) pbest score
            best_neighbor_index = min(neighborhood, key=lambda idx: pbest_scores[idx])
            nbests[i] = pbest_positions[best_neighbor_index]
        
        # Update velocities and positions of particles.
        for i in range(num_particles):
            r1 = np.random.rand(dimensions)
            r2 = np.random.rand(dimensions)
            cognitive = c1 * r1 * (pbest_positions[i] - positions[i])
            social = c2 * r2 * (nbests[i] - positions[i])
            velocities[i] = w * velocities[i] + cognitive + social
            positions[i] = positions[i] + velocities[i]
        
        # (Optional) Update the overall global best for reporting purposes.
        current_best_index = np.argmin(scores)
        if scores[current_best_index] < best_global_score:
            best_global_score = scores[current_best_index]
            best_global_position = positions[current_best_index].copy()
            
        # Print progress
        print(f"Iteration {iter+1}/{iterations}: best score in swarm = {best_global_score:.6f}")
    
    return best_global_position, best_global_score

# Example usage:
if __name__ == '__main__':
    num_particles = 16         # You can choose the number of particles.
    dimensions = 2             # Dimensionality of your problem (for example, 2).
    bounds = (-10, 10)         # Search space bounds for each dimension.
    iterations = 50            # Number of iterations to run PSO.
    
    # For a Von Neumann topology, arrange particles in a grid.
    # Here we assume a 4x4 grid because 16 particles can form a perfect square.
    grid_shape = (4, 4)
    
    best_position, best_score = pso_von_neumann(sphere, num_particles, dimensions, bounds, iterations, grid_shape)
    print("\nOptimization finished.")
    print("Best position found:", best_position)
    print("Best score:", best_score)

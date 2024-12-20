# Task 2_1: Sequential Scan Based Method
import time

# Function to read data from the input file
def load_data(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip().split(" ")
            id = int(row[0])
            x = float(row[1]) # x represents Cost
            y = float(row[2]) # y represents Size

            # Store each point as a dictionary with id, x, and y values
            points.append({'id': id, 'x': x, 'y': y})
            
    return points

# Load the dataset from city3.txt file
data = load_data('city3.txt')

# Sequential Scan Based Method 
def sequential_search(data):
    skyline = [] # List to store skyline points
    for point in data:
        dominated = False # Flag to track if current point is dominated

        for other in data: # Compare with every other point
            if point['id'] == other['id']: # Skip self-comparison
                continue

            # Check if current point is dominated by other point
            # A point is dominated if there exists another point with:
            # 1. Lower or equal cost (x) AND strictly lower size (y), OR
            # 2. Strictly lower cost (x) AND lower or equal size (y)

            if (point['x'] >= other['x'] and point['y']>other['y'] or 
                point['x']>other['x'] and point['y']>= other['y']):
                dominated = True
                break  # No need to check further if point is dominated

        # If point is not dominated by any other point, add to skyline    
        if not dominated:
            skyline.append(point)
    return skyline

# Measure execution time
start_time = time.time()
results = sequential_search(data)
end_time = time.time()

total_time = end_time - start_time
avg_time = total_time / len(data)

# Write results to output file
with open ('output2_1.txt', 'w') as file:
    for point in results:
        file.write(f"The skyline includes point with id={point['id']}, x={point['x']}, y={point['y']}\n")
    
    file.write(f"\nTotal running time: {total_time:.5f} seconds\n")
    file.write(f"Average time per query: {avg_time:.10f} seconds\n")

print("The final output was saved to output2_1.txt")
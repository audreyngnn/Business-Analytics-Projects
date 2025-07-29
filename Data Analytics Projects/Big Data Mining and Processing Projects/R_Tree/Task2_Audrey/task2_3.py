# Task 2_3: BBS with Divide-and-Conquer
import time
from Rtree import RTree

# Function to check if p1 dominates p2 in both dimensions (cost and size)
def dominates(p1, p2):
    return p1['x'] <= p2['x'] and p1['y'] <= p2['y'] and (p1['x'] < p2['x'] or p1['y'] < p2['y'])

# Calculate minimum distance from origin (0,0) to node's MBR
# Used for determining processing order in BBS algorithm
def mindist(node): 
    return (node.MBR['x1']**2 + node.MBR['y1']**2)**0.5

# Standard BBS algorithm implementation (same as Task 2.2)
def bbs(rtree):
    skyline = [] # List to store skyline points
    global_list = [(mindist(rtree.root), rtree.root)] # Priority queue sorted by mindist
    
    while global_list:
        global_list.sort(key=lambda x: x[0])  # Sort by minimum distance
        _, node = global_list.pop(0) # Get and remove closest node
        
        if node.is_leaf(): # If current node is a leaf node
            for point in node.data_points: # Process each point in the leaf
                is_dominated = False

                # Check if point is dominated by any existing skyline point
                for s in skyline:
                    if dominates(s, point):
                        is_dominated = True
                        break

                if not is_dominated: # If point is not dominated
                    skyline.append(point) # Add to skyline

                    # Remove any existing skyline points that are dominated by new point
                    skyline = [s for s in skyline if not dominates(point, s)]

        else: # If current node is a non-leaf node
            for child in node.child_nodes: # Process each child node
                # Create MBR representation for dominance checking
                child_mbr = {'x': child.MBR['x1'], 'y': child.MBR['y1']}
                is_dominated = False

                # Check if child's MBR is dominated by any skyline point
                for s in skyline:
                    if dominates(s, child_mbr):
                        is_dominated = True
                        break

                if not is_dominated: # If child's MBR is not dominated
                    global_list.append((mindist(child), child)) # Add to global list for processing
    
    return skyline

# Divide and Conquer
# Divide the dataset into two parts based on x-coordinate (cost)
def divide_data(data):
    # Get all x values and find middle point
    x_values = [point['x'] for point in data]
    mid_point = (max(x_values) + min(x_values)) / 2
    
    # Divide points into left and right partitions
    left_side = [point for point in data if point['x'] < mid_point]
    right_side = [point for point in data if point['x'] >= mid_point]
    
    return left_side, right_side

# Merge two skyline using 1D dominance screening
def merge_skylines(left_skyline, right_skyline):
    # Left skyline points are automatically part of result
    merged_skyline = left_skyline.copy()
    
    # Find minimum y-value from left skyline for 1D domination screening
    min_y_left = min(point['y'] for point in left_skyline) 
    
    # Only add right points that have better (smaller) y-values than min_y_left
    for right_point in right_skyline:
        if right_point['y'] < min_y_left:
            merged_skyline.append(right_point)
            
    return merged_skyline

# Function to load data from input file
def load_data(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip().split(" ")
            id = int(row[0])
            x = float(row[1]) # x represents Cost
            y = float(row[2]) # y represents Size
            points.append({'id': id, 'x': x, 'y': y})
    return points

def main():
    # Load and divide data
    data = load_data('city3.txt')
    left_data, right_data = divide_data(data)

    # Create and populate R-trees for both sides
    rtree_left = RTree()
    rtree_right = RTree()

    for point in left_data:
        rtree_left.insert(rtree_left.root, point)

    for point in right_data:
        rtree_right.insert(rtree_right.root, point)

    # Execute divide and conquer BBS algorithm
    start_time = time.time()
    # Step 1: Compute skylines for both sides
    left_skyline = bbs(rtree_left)
    right_skyline = bbs(rtree_right)
    
    # Step 2: Merge the two skylines
    final_skyline = merge_skylines(left_skyline, right_skyline)
    
    end_time = time.time()
    total_time = end_time - start_time
    avg_time_per_point = total_time / len(final_skyline) if final_skyline else 0

    # Write results to output file
    with open("output2_3.txt", "w") as f:
        for point in final_skyline:
            f.write(f"The skyline includes point with id:{point['id']}, x: {point['x']}, y: {point['y']}\n")
        f.write(f"\nTotal execution time: {total_time:.20f} seconds\n")
        f.write(f"Average time per skyline point: {avg_time_per_point:.20f} seconds\n")

    print(f"The final output was saved to output2_3.txt")

if __name__ == "__main__":
    main()

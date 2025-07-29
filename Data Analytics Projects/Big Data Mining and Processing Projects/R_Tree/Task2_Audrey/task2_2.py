# Task 2_2: Branch and Bound Skyline (BBS) Algorithm
import time
from Rtree import RTree  

# Function to check one point dominates the other
def dominates(p1, p2):
    # Returns True if p1 dominates p2
    return p1['x'] <= p2['x'] and p1['y'] <= p2['y'] and (p1['x'] < p2['x'] or p1['y'] < p2['y'])

# Calculate minimum distance from origin (0,0) to the Minimum Bounding Rectangle (MBR)
# Used for determining processing order of R-tree nodes
def mindist(node): 
    return (node.MBR['x1']**2 + node.MBR['y1']**2)**0.5 # Euclidean distance to lower-left corner of MBR



# Branch and Bound Skyline algorithm using R-tree
def bbs(rtree):
    skyline = [] # List to store final skyline points

    # Initialize global list with root node and its mindist
    # Global list maintains nodes to be processed, ordered by mindist
    global_list = [(mindist(rtree.root), rtree.root)] 


    while global_list: # Process nodes until global list is empty
        
        # Sort nodes by mindist and get the closest node
        global_list.sort(key=lambda x: x[0])  # Best-first search based on mindist
        _, node = global_list.pop(0) # Get and remove the closest node
        
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
    # Load data and build R-tree
    data = load_data('city3.txt')
    rtree = RTree()
    for point in data:
        rtree.insert(rtree.root, point)

    # Execute BBS algorithm and measure time
    start_time = time.time()
    skyline_points = bbs(rtree)
    end_time = time.time()

    total_time = end_time - start_time
    avg_time_per_point = total_time / len(skyline_points) 

    # Write results to output file
    with open("output2_2.txt", "w") as f:
        for point in skyline_points:
            f.write(f"The skyline includes point with id:{point['id']}, x: {point['x']}, y: {point['y']}\n")
        f.write(f"\nTotal execution time: {total_time:.20f} seconds\n")
        f.write(f"Average time per skyline point: {avg_time_per_point:.20f} seconds\n")

    print(f"The final output was saved to output2_2.txt")

if __name__ == "__main__":
    main()
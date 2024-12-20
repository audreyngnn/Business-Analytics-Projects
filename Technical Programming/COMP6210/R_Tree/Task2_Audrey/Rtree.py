# Construct a Rtree
import sys
import math

# Maximum number of entries in each node
B = 10 # After testing for different B (B = 4, 10, 25, 51, 100), B = 10 is the most efficient one.

# Create Node class
class Node(object): 
    """R-tree node that can be either internal (with child nodes) or leaf (with data points)"""
    def __init__(self):
        self.id = 0
        self.child_nodes = [] # For internal nodes: stores child nodes
        self.data_points = [] # For leaf nodes: stores actual data points
        self.parent = None

        # Minimum Bounding Rectangle (MBR) coordinates
        self.MBR = {
            'x1': -1, # Min x
            'y1': -1, # Min y
            'x2': -1, # Max x
            'y2': -1, # Max y
        }
    def perimeter(self):
        """Calculate the semi-perimeter of node's MBR"""
        return (self.MBR['x2'] - self.MBR['x1']) + (self.MBR['y2'] - self.MBR['y1'])

    def is_overflow(self):
        """Check if node exceeds maximum capacity B"""
        if self.is_leaf():
            if self.data_points.__len__() > B: # Checking overflows of data points, B is the upper bound.
                return True
            else:
                return False
        else:
            if self.child_nodes.__len__() > B: # Checking overflows of child nodes, B is the upper bound.
                return True
            else:
                return False

    def is_root(self):
        """Check if node is the root (has no parent)"""
        if self.parent is None:
            return True
        else:
            return False

    def is_leaf(self):
        """Check if node is a leaf (has no children)"""
        if self.child_nodes.__len__() == 0:
            return True
        else:
            return False


# Create R-tree class
class RTree(object): 
    """R-tree implementation with quadratic split strategy"""
    def __init__(self):
        self.root = Node() # Create a root


    def insert(self, u, p): # Insert p(data point) to u (MBR)
        """Insert point p into node u, handling overflow if necessary"""
        if u.is_leaf(): 
            self.add_data_point(u, p) # Add the data point and update the corresponding MBR
            if u.is_overflow():
                self.handle_overflow(u) # Handel overflow for leaf nodes
        else:
            # Choose best subtree to minimize perimeter increase
            v = self.choose_subtree(u, p) # Choose a subtree to insert the data point to miminize the perimeter sum
            self.insert(v, p) # Keep continue to check the next layer recursively
            self.update_mbr(v) # Update the MBR for inserting the data point

    def choose_subtree(self, u, p): 
        """Select child node that requires minimal MBR enlargement to include p"""
        if u.is_leaf(): # Find the leaf and insert the data point
            return u
        else:
            min_increase = sys.maxsize # Set an initial value
            best_child = None
            for child in u.child_nodes: # Check each child to find the best node to insert the point 
                if min_increase > self.peri_increase(child, p):
                    min_increase = self.peri_increase(child, p)
                    best_child = child
            return best_child

    def peri_increase(self, node, p): 
        """Calculate perimeter increase if point p is added to node"""
        # new perimeter - original perimeter = increase of perimeter
        origin_mbr = node.MBR
        x1, x2, y1, y2 = origin_mbr['x1'], origin_mbr['x2'], origin_mbr['y1'], origin_mbr['y2']
        increase = (max([x1, x2, p['x']]) - min([x1, x2, p['x']]) +
                    max([y1, y2, p['y']]) - min([y1, y2, p['y']])) - node.perimeter()
        return increase


    def handle_overflow(self, u):
        """Split overflowing node and propagate changes upward"""
        u1, u2 = self.split(u) # Split node into two groups
        
        # If u is root, create a new root with s1 and s2 as its' children
        if u.is_root():
            # Create new root with split nodes as children
            new_root = Node()
            self.add_child(new_root, u1)
            self.add_child(new_root, u2)
            self.root = new_root
            self.update_mbr(new_root)

        # If u is not root, delete u, and set s1 and s2 as u's parent's new children
        else:
            # Replace u with split nodes in parent
            w = u.parent
            # Copy the information of s1 into u
            w.child_nodes.remove(u)
            self.add_child(w, u1) # Link the two splits and update the corresponding MBR
            self.add_child(w, u2)
            if w.is_overflow(): # Check the parent node recursively
                self.handle_overflow(w)
            
    def split(self, u):
        """Split node u into two nodes while minimizing total perimeter"""
        best_s1 = Node()
        best_s2 = Node()
        best_perimeter = sys.maxsize

        # If u is a leaf node
        if u.is_leaf():
            m = u.data_points.__len__()
            # Create two different kinds of divides
            divides = [sorted(u.data_points, key=lambda data_point: data_point['x']),
                       sorted(u.data_points, key=lambda data_point: data_point['y'])] # Sort the points based on X dimension and Y dimension
            for divide in divides:
                for i in range(math.ceil(0.4 * B), m - math.ceil(0.4 * B) + 1): # Check the combinations to find a near-optimal one
                    s1 = Node()
                    s1.data_points = divide[0: i]
                    self.update_mbr(s1)
                    s2 = Node()
                    s2.data_points = divide[i: divide.__len__()]
                    self.update_mbr(s2)
                    if best_perimeter > s1.perimeter() + s2.perimeter(): 
                        best_perimeter = s1.perimeter() + s2.perimeter()
                        best_s1 = s1
                        best_s2 = s2

        # If u is a internal node
        else:
            # Create four different kinds of divides
            m = u.child_nodes.__len__()
            divides = [sorted(u.child_nodes, key=lambda child_node: child_node.MBR['x1']), # Sort based on MBRs
                       sorted(u.child_nodes, key=lambda child_node: child_node.MBR['x2']),
                       sorted(u.child_nodes, key=lambda child_node: child_node.MBR['y1']),
                       sorted(u.child_nodes, key=lambda child_node: child_node.MBR['y2'])]

            for divide in divides:
                for i in range(math.ceil(0.4 * B), m - math.ceil(0.4 * B) + 1): # Check the combinations
                    s1 = Node()
                    s1.child_nodes = divide[0: i]
                    self.update_mbr(s1)
                    s2 = Node()
                    s2.child_nodes = divide[i: divide.__len__()]
                    self.update_mbr(s2)
                    if best_perimeter > s1.perimeter() + s2.perimeter():
                        best_perimeter = s1.perimeter() + s2.perimeter()
                        best_s1 = s1
                        best_s2 = s2

        # Update parent pointers for children
        for child in best_s1.child_nodes:
            child.parent = best_s1
        for child in best_s2.child_nodes:
            child.parent = best_s2

        return best_s1, best_s2


    def add_child(self, node, child):
        """Add child to node and update MBR"""
        node.child_nodes.append(child) # Add child nodes to the current parent (node) and update the MBRs. It is used in handeling overflows.
        child.parent = node

        # Expand node's MBR to include child's MBR
        if child.MBR['x1'] < node.MBR['x1']:
            node.MBR['x1'] = child.MBR['x1']
        if child.MBR['x2'] > node.MBR['x2']:
            node.MBR['x2'] = child.MBR['x2']
        if child.MBR['y1'] < node.MBR['y1']:
            node.MBR['y1'] = child.MBR['y1']
        if child.MBR['y2'] > node.MBR['y2']:
            node.MBR['y2'] = child.MBR['y2']
         # Return the child whose MBR requires the minimum increase in perimeter to cover p

    def add_data_point(self, node, data_point):
        """Add data point to leaf node and update MBR"""
        node.data_points.append(data_point)

        # Expand node's MBR to include new point
        if data_point['x'] < node.MBR['x1']:
            node.MBR['x1'] = data_point['x']
        if data_point['x'] > node.MBR['x2']:
            node.MBR['x2'] = data_point['x']
        if data_point['y'] < node.MBR['y1']:
            node.MBR['y1'] = data_point['y']
        if data_point['y'] > node.MBR['y2']:
            node.MBR['y2'] = data_point['y']


    def update_mbr(self, node):
        """Recalculate MBR for node based on children or data points"""
        x_list = []
        y_list = []

        if node.is_leaf():
            x_list = [point['x'] for point in node.data_points]
            y_list = [point['y'] for point in node.data_points]

        else:
            x_list = [child.MBR['x1'] for child in node.child_nodes] + [child.MBR['x2'] for child in node.child_nodes]
            y_list = [child.MBR['y1'] for child in node.child_nodes] + [child.MBR['y2'] for child in node.child_nodes]

        # Update the MBR 
        new_mbr = {
            'x1': min(x_list),
            'x2': max(x_list),
            'y1': min(y_list),
            'y2': max(y_list)
        }
        node.MBR = new_mbr
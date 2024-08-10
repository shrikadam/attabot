import numpy as np

def normalize_angle(angle):
    """Normalize angle to [-pi, pi]"""
    return (angle + np.pi) % (2 * np.pi) - np.pi

def calculate_distance(pos1, pos2):
    """Calculate Euclidean distance between two points"""
    return np.linalg.norm(np.array(pos1) - np.array(pos2))
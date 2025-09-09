import numpy as np

#for output values
np.set_printoptions(suppress=True, formatter={'float_kind': '{:0.6f}'.format})

def transform(points, tx, ty, tz, rx_deg, ry_deg, rz_deg):
    # Convert angles from degrees to radians
    rx, ry, rz = np.radians([rx_deg, ry_deg, rz_deg])
    
    cos_rx, sin_rx = np.cos(rx), np.sin(rx)
    cos_ry, sin_ry = np.cos(ry), np.sin(ry)
    cos_rz, sin_rz = np.cos(rz), np.sin(rz)
    
    
    Rx = np.array([
        [1, 0, 0, 0],
        [0, cos_rx, -sin_rx, 0],
        [0, sin_rx, cos_rx, 0],
        [0, 0, 0, 1]
    ])
    Ry = np.array([
        [cos_ry, 0, sin_ry, 0],
        [0, 1, 0, 0],
        [-sin_ry, 0, cos_ry, 0],
        [0, 0, 0, 1]
    ])
    Rz = np.array([
        [cos_rz, -sin_rz, 0, 0],
        [sin_rz, cos_rz, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    T = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    
    
    composite_matrix = T @ Rz @ Ry @ Rx
    
    
    homogeneous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    
    
    transformed_points = (composite_matrix @ homogeneous_points.T).T
    
    
    return transformed_points[:, :3]


sample_points = np.array([
    [10, 0, 0],
    [0, 10, 0],
    [0, 0, 10],
    [5, 5, 5]
])

translation_vec = (0, 3, 0) # translate by 3 in Y
rotation_angles = (0, 0, 90) # Rotate 90 degrees around Z

# Transform the points
new_points = transform(sample_points, *translation_vec, *rotation_angles)

print("Original Points:\n", sample_points)
print("\nTransformed Points:\n", new_points)


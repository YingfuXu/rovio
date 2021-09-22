import numpy as np

def rotMtrx2quat(rot_Mtrx):
    qw = 0.5 * np.sqrt(1 + rot_Mtrx[0, 0] + rot_Mtrx[1, 1] + rot_Mtrx[2, 2])
    qx = (rot_Mtrx[2, 1] - rot_Mtrx[1, 2]) / (4 * qw)
    qy = (rot_Mtrx[0, 2] - rot_Mtrx[2, 0]) / (4 * qw)
    qz = (rot_Mtrx[1, 0] - rot_Mtrx[0, 1]) / (4 * qw)
    return np.concatenate((np.array([qw]), np.array([qx]), np.array([qy]), np.array([qz])), axis=0)

rot_Mtrx = np.array([[0.0148655429818, -0.999880929698, 0.00414029679422], 
			[0.999557249008, 0.0149672133247, 0.025715529948],
			[-0.0257744366974, 0.00375618835797, 0.999660727178]])

t_vec = np.array([[-0.0216401454975], 
	          [-0.064676986768 ],
		  [0.00981073058949]])

rot_Mtrx = np.array([[-0.02725669, -0.71392061,  0.69969596], 
			[-0.99962606,  0.01793147, -0.02064447],
			[0.00219194, -0.69999702, -0.7141424]])

t_vec = np.array([[0.00751451], 
	          [0.02404535],
		  [0.00577265]])

print(rotMtrx2quat(rot_Mtrx.T))

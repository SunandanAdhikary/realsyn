from math import sqrt

#ttc
def name():
	return 'esp'

def problem():
	A = [[0.4450,  -0.0458,        0,        0],
    	[1.2939,    0.4402,         0,         0],
         [0,   -0.0390,    0.4450,   -0.0068],
         [0,    0.4339,    1.2939,    0.0063]]
	
	B = [[0.0550],
	[4.5607],
    [0.0550],
    [4.5607]]
	KK = [[0, 0,0.2826, 0.0960]]
	x_dim = len(A[0])
	u_dim = len(B[0])
	u_bound = 0.8125
	u_space = (True, [(-u_bound, u_bound) for i in range(u_dim)])
	perf = 0.1
	safer = 0.55
	safety_x1 = 1
	safety_x2 = 2
	goal_x1 = safety_x1*perf
	goal_x2 = safety_x2*perf
	init_x1 = safety_x1*safer
	init_x2 = safety_x2*safer
	safe_rec = (True,[[-safety_x1,safety_x1],
				[-safety_x2,safety_x2],
				[-safety_x1,safety_x1],
				[-safety_x2,safety_x2]])
	# target = (True,[[-goal_x1,goal_x1],
	# 			[-goal_x2,goal_x2],
	# 			[-goal_x1,goal_x1],
	# 			[-goal_x2,goal_x2]])
	# 4d: none
	# target = (True,[[0.4515,1.0000],
	# 			[1.4515,2.0000],
	# 			[0.4515,1.0000],
	# 			[1.4515,2.0000]])
	# 2d : different scale:
	target = (True,[[-1,1.0000],
				[-1,0.95],
				[-1,1.0000],
				[-1.0445,0.95]])
	initial_size = 1.0 * sqrt(x_dim)
	center = [0,0,0]
	num_steps = 1
	Theta = (True,[[-safety_x1,safety_x1],
				[-safety_x2,safety_x2],
				[-safety_x1,safety_x1],
				[-safety_x2,safety_x2]])
	avoid_list = None
	avoid_dynamic = None
	return initial_size, center, A, B, KK, u_space, target, avoid_list, num_steps,u_dim, avoid_dynamic, Theta, safe_rec

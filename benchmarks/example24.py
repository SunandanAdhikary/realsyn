from math import sqrt

#ttc
def name():
	return 'ttc'

def problem():
	A = [[1.0000, 0.1000, 0, 0],
         [0, 1.0000, 0, 0],
    [0.8327 , 0, 0.1673, 0.1000],
    [2.5029, 0, -2.5029, 1.0000]]
	B = [[0.0050],
	[0.1000],
    [0.0050],
    [0.1000]]
	KK = [[0, 0, 0.9171, 1.6356]]
	x_dim = len(A[0])
	u_dim = len(B[0])
	u_bound = 72
	u_space = (True, [(-u_bound, u_bound) for i in range(u_dim)])
	perf = 0.3
	safer = 0.65
	safety_x1 = 25
	safety_x2 = 30
	goal_x1 = safety_x1*safer
	# lb_goal_x1 = 19.3730 #*perf
	# ub_goal_x2 = safety_x2 #*perf
	goal_x2 = safety_x2*safer #*perf
	init_x1 = safety_x1
	init_x2 = safety_x2
	safe_rec = (True,[[-safety_x1,safety_x1],
				[-safety_x2,safety_x2],
				[-safety_x1,safety_x1],
				[-safety_x2,safety_x2]])
	# target = (True,[[-goal_x1,goal_x1],
	# 			[-goal_x2,goal_x2],
	# 			[-goal_x1,goal_x1],
	# 			[-goal_x2,goal_x2]])
	# 4d: none
# 	target = (True, [[14.1516 ,0.8032],
#    [-5.7589 ,   0.8927],
#    [14.9035 ,  21.5550],
#    [-11.3498 ,  -4.6982]])
	# 4d: same x,xhat center 
	# target = (True, [[17.23 , 23.8816],
	# [-13.3443 ,  -6.6928],
	# [17.23 , 23.8816],
	# [-13.3443 ,  -6.6928]])
	# 2d: found inputs
	# target = (True, [[-23.3111 ,4.8946],
	# [-8.9398 ,  19.2659],
	# [-15.9078 ,  -2.5088],
	# [-1.5364 ,  11.8626]])
	# 2d: found inputs
	# target = (True, [[-23.3111 ,4.8946],
	# [-8.9398 ,  19.2659],
	# [-15.9078 ,  -2.5088],
	# [-1.5364 ,  11.8626]])
	# 2d: different scale: found inputs
	target = (True, [[-20.4321 ,20.4761],
	[-20.9025 ,  20.0056],
	[-22.3492 , 22.3932],
	[-22.8196 ,  21.9228]])
	initial_size = 1.0 * sqrt(x_dim)
	center = [0,0,0]
	num_steps = 5
	Theta = (True,[[-init_x1,init_x1],
				[-init_x2,init_x2],
				[-init_x1,init_x1],
				[-init_x2,init_x2]])
	avoid_list = None
	avoid_dynamic = None
	return initial_size, center, A, B, KK,u_space, target, avoid_list, num_steps,u_dim, avoid_dynamic, Theta, safe_rec

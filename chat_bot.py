import numpy as np

np.random.seed(1)


streetlights = np.array([
                        [1,0,1],
                        [0,1,1],
                        [0,0,1],
                        [1,1,1]
                        ]
                        )

def relu(x):
    return (x > 0) * x

def relu2deriv(output):
    return output > 0

alpha = 0.2
hidden_size = 4

weights_0_1 = 2*np.random.random((3, hidden_size)) - 1
weights_1_2 = 2*np.random.random((hidden_size, 1)) - 1

for iteration in range(60):
    layer_2_error = 0
    for i in range(len(streetlights)):
        layer_0 = streetlights[i:i+1]
        layer_
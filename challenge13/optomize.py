
# function function
def function(x):
    return x**2 + 5*x + 6

# derivative function
def derivative(x):
    return 2*x + 5

# initial value
x = 0

# set the learning rate and iterations
learning_rate = 0.1
num_iterations = 1000

# perform gradient descent
for _ in range(num_iterations):
    gradient = derivative(x)
    x = x - learning_rate * gradient

print("the minimum value found at x =", x)




# install PyTorch and rotchvision
import torch
import torch.nn as nn
import torch.optim as optim

# Notify progress
print(f"Torch version: {torch.__version__}")

# Define a neural network model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        # Define a linear layer that transforms input data from 10 features to 8 features
        self.fc1 = nn.Linear(10,8)
        # Define a linear layer that transforms input data from 8 features to 2 features
        self.fc2 = nn.Linear(8, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# New function to calculate accuracy
def calculate_accuracy(output, target):
    _, predicted = torch.max(output, 1)
    accuracy = (predicted == target).sum().item() / target.size(0)
    return accuracy

# Create an instance of the neural network
model = NeuralNetwork()

# Define the loss function
criterion = nn.CrossEntropyLoss()

# Define the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Sample input data
input_data = torch.randn(1, 10) # Reshaped to (1, 10)

# Perfrom fordward pass
output = model(input_data)

# Perform backward pass and update the weights
optimizer.zero_grad()
loss = criterion(output, torch.tensor([1]))  # Assuming the target class is 1
loss.backward()
optimizer.step()

# Calculate and print accuracy
target = torch.tensor([1])  # Assuming the target class is 1
accuracy = calculate_accuracy(output, target)
print("Accuracy:", accuracy)

# Print the updated model parameters
print("Updated model parameters:")
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name, param.data)

# Print the loss value
print("Loss:", loss.item())
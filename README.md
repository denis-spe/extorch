TorchSequential
-------
<hr>

What's in the package.
----------
The package contain python code for pytorch sequential model extension and
hyperparameter tuning the Sequential model.

Here the code in this package.
* Sequential model.
* metrics for Sequential model evaluation.
* Hyperparameter tuning for fine tuning Sequential model.


<hr>
Here is the example of the sequential model

````python
from torch import nn 
from extorch.metrics import MAE 
from extorch.data_generator import DataGenerator

# Create demo data....
train_data = DataGenerator(100, 8)
test_data = DataGenerator(100, 8, train_sample=False)

model = Sequential([
# Input layer
    nn.Linear(in_features=8, out_features=32),
    nn.ReLU(),  # Activation function
    nn.Dropout(.4),
    
    # First hidden layer
    nn.Linear(in_features=32, out_features=32),
    nn.ReLU(),  # Activation function
    nn.Dropout(.4),  # Drop same pixel
    
    # Output layer
    nn.Linear(in_features=32, out_features=1)
    ])
    # Compile the model .........
    model.compile(
    optimize=torch.optim.Adam(model.parameters()),
    loss=nn.MSELoss(),
    metrics=MAE(),
    device=None
    )
    
train_dataloader = DataLoader(dataset=train_data, shuffle=True)
valid_dataloader = DataLoader(dataset=test_data, shuffle=False)

# Fit the data .........
history = model.fit(
    train_dataloader,
    epochs=10,
    verbose=False,
    validation_data=valid_dataloader
    )
print(model.predict(test_load))
````

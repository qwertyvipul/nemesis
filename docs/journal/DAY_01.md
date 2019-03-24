# Day 1 - First Weird Model

### Idea
To create an ANN model to find the roots of a given qudratic equation.

### Something More
So, my idea was to feed the coefficients of the qudratic equation (a, b and c) in the neural network as input parameters and then it should output the two roots of the given equation (x1 and x1).

### Findings
As you can see this is not a classification problem which neural networks are good at. It's more of a regression problem, and definetley not linear.

### Weird Stuff
The model converged to 52.xx accuracy, but believe me it wasn't no accuracy. All the predictions for the test were exactly same. I tried multiple combinations of activation functions and even tried custom activation functions. It didn't mattered, in all cases the model converged to fixed accuracy level way before 100 epochs and the predictions for all different test inputs were same (different for different activation functions - It may be a little confusing).

### What's next
I guess, this was a way too much of a problem for the network (or maybe a rookie mistake). So, the next thing...[Click Here](DAY_02.md)
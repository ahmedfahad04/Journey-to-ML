https://www.kaggle.com/datasets/gurdit559/canada-per-capita-income-single-variable-data-set/code

### Task: Read the kaggle notebooks and try to understand the code and the data. Then try to create a linear regression model for the data.

# Gradient Descent

We already know that using linear regression we can predict the outcome of a linear function. But how do we find the best fit line? To get the best fit line we have to calculate the Cost function.

### What is Cost function?

Cost function is nothing but a measure of the squared difference of the predicted and the actual value.
It is also called the Mean Squared Error(MSE). The equation is showed in 'gradient_descent.png' file.
But how do we know the least MSE for which we'll get the best fitted line? In that case, we need to have some optimization Algorithm to find the minimum value of the cost function (MSE). One of the most popular optimization algorithm is Gradient Descent.

### What is Gradient Descent?

If we look at the picture of 'gradien_descent_graph_2.png' we can see a parabolic shape of the function in 3D form. This graph has 3 dimension a.k.a cost, m, b (where y=mx+b). In the x and y axis we have the m and b values respectively. In z axis, we have the cost.

Our goal is to reach the lowest 'RED' Dot, where the cost is minimum. But how do we reach that point?
If we follow some fixed step (like in each iteration we will move 2 units), then we might end up crossing the 'RED' dot. We need to follow 'BABY STEP' to get into that spot.

To obtain the baby step, we have to walk along the slope of the function. If we walk along the slope, we will reach the minimum point. This is the basic idea of Gradient Descent. And the way we'll walk through the slop is called Derivatives. We'll calculate the derivatives of the function and then we'll walk along the slope. The equation is showed in 'gradient_descent.png' file.

Therefore, to calculate any Gradient Descent we need to calculate the derivatives of the function. In our case, we have to calculate the derivatives of the cost function shown in 'gradient_descent.png' file. 


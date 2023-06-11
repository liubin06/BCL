# Numerical Experiments
This repository contains the numerical experimental results of the Bayesian self-supervised contrastive learning paper. Specifically, it includes the mean squared error (MSE) of the BCL estimator, empirical distributions of positive and negative examples, and visualizations of the omega weights under different $\alpha$ and $\beta$ settings.

## Stochastic depiction
Given anchor data point, a descriptive explanation of the process for generating similarity scores for unlabeled samples is provided below.

![image](https://github.com/liubin06/BCL/blob/main/pic/numerical.jpeg)


# Usage
To reproduce the numerical experiments, please run the following scripts, where Algorithm1, Algorithm2, and Algorithm3 are included.

To calculate the MSE of the BCL estimator, run 

```
MSE.py
```

To visualize the empirical distributions of positive and negative examples, run 
```
empirical_distribution.py
```

To visualize the weights $\omega$ under different $\alpha$ and $\beta$ settings, run 
```
draw_omega(fixalpha).py or draw_omega(fixbeta).py
```


# Requirements
The code in this repository requires the following Python packages:

- numpy

- matplotlib

- seaborn

- scipy



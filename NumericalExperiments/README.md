# Numerical Experiments
This repository contains the numerical experimental results of the Bayesian self-supervised contrastive learning paper. Specifically, it includes the mean squared error (MSE) of the BCL estimator, empirical distributions of positive and negative examples, and visualizations of the omega weights under different $\alpha$ and $\beta$ settings.

#Usage
To reproduce the numerical experiments, please run the following scripts:

To calculate the MSE of the BCL estimator, run 

```
MSE.py
```

To visualize the empirical distributions of positive and negative examples, run 
```
empirical_distribution.py
```

To visualize the omega weights under different a and b settings, run 
```
draw_omega(fixalpha).py or draw_omega(fixbeta).py
```
#Requirements
The code in this repository requires the following Python packages:

numpy

matplotlib



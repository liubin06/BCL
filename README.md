# Bayesian Self-Supervised Contrastive Learning
We consider self-supervised contrastive learning from unlabeled data. 
How can we learn good representation that maximizely preserves the semantic structure of embeddings ?

A unlabeled data of false negative (positive sample, e.g., $x_3^-$) should not be pushed apart from the anchor, leading to the 
**true principle**.

A unlabeled data of true negative (negative sample, e.g., $x_1^-$) should be pushed apart from the anchor, leading to the **hard principle**.

![illustrative](https://github.com/liubin06/BCL/blob/main/pic/illustrative.jpeg)

## Problem formulation of BCL
![formulation](https://github.com/liubin06/BCL/blob/main/pic/formulation.jpg)

- **(a)** For an given anchor, let $\hat{x}$ be a random variable representing the similarity score between the anchor point and unlabeled samples. We assume that $\hat{x}$ is independently and identically distributed with an unknown distribution.

- **(b)** Let $\tau^+$ be the class prior probability that an unlabeled sample shares the same latent class as the anchor point (positive class).

- **(c)** Given an encoder, let $\alpha$ be the probability that the similarity score of a positive sample is higher than that of a negative sample.

BCL uses random samples from the unlabeled data while correcting the resulting bias with importance weights, adhering to the aforementioned **true principle** and **hard principle**. Under the problem settings described above, BCL provides an asymptotical unbiased estimation of the **supervised loss**, and posterior probability estimation of samples being **true negatives**.

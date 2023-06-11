# Bayesian Self-Supervised Contrastive Learning
We consider self-supervised contrastive learning from unlabeled data. 
How can we learn good representation that maximizely preserves the semantic structure of embeddings ?

A unlabeled data of false negative (positive) should not be pushed apart from the anchor, leading to the 
**true principle**.

A unlabeled data of true negative (negative) should be pushed apart from the anchor, leading to the **hard principle**.

![illustrative](https://github.com/liubin06/BCL/blob/main/pic/illustrative.jpeg)

## Problem formulation of BCL
![formulation](https://github.com/liubin06/BCL/blob/main/pic/formulation.jpg)

- **(a)** For an given anchor, let $\hat x$ be a random variable representing the similarity score between  the given anchor point and unlabeled samples, assuming $\hat x$ independently and identically distributed with an unknown distribution.

- **(b)** For an unlabeled sample, the prior probability of it being a positive example is $\tau^+$, and the prior probability of it being a negative example is $1-\tau^+$.

- **(c)** For any encoder with given parameters, the probability that the similarity score of a positive example is higher than that of a negative example is $\alpha$.

BCL utilizes random samples from the unlabeled data while correcting the resulting bias with importance weights, adhering to the aforementioned **true principle** and **hard principle**. Under the problem setting described above, BCL provides an asymptotical unbiased estimation of the supervised loss, and posterior probability estimation of samples being true negatives.

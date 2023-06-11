# Bayesian Self-Supervised Contrastive Learning
We consider self-supervised contrastive learning from unlabeled data. 
How can we learn good representation that maximizely preserves the semantic structure of embeddings ?

A unlabeled data of false negative (positive) should not be pushed apart from the anchor, leading to the 
**true principle**.

A unlabeled data of true negative (negative) should be pushed apart from the anchor, leading to the **hard principle**.

![illustrative](https://github.com/liubin06/BCL/blob/main/pic/illustrative.jpeg)

## The problem formulation for BCL
For an given anchor, let $\hat x$ be a random variable representing the similarity score between  the given anchor point and unlabeled samples, assuming $\hat x$ independently and identically distributed with an unknown distribution $\phi$(Fig. a).

For an unlabeled sample, the prior probability of it being a positive example is $\tau^+$, and the prior probability of it being a negative example is $1-\tau^+$ (Fig. b).

For any encoder with given parameters, the probability that the similarity score of a positive example is higher than that of a negative example is $\alpha$ (Fig. c).

Starting from the above intuition, we design BCL that still uses random samples from the **unlabeled data**, while correcting the resulting bias with importance weights.

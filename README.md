# Bayesian Self-Supervised Contrastive Learning
We consider self-supervised contrastive learning from unlabeled data. 
How can we learn good representation that maximizely preserves the semantic structure of embeddings ?

A unlabeled data of false negative (positive) should not be pushed apart from the anchor, leading to the 
**true principle**.

A unlabeled data of true negative (negative) should be pushed apart from the anchor, leading to the **hard principle**.

Starting from the above intuition, we design BCL that still uses random samples from the **unlabeled data**, while correcting the resulting bias with importance weights.

## Bayesian Self-supervised Contrastive Learning
We consider self-supervised contrastive learning from unlabeled data. 
How can we learn good representation that maximizely preserves the semantic structure of embeddings ?

A unlabeled data of false negative (positive) should not be pushed apart from the anchor, leading to the 
**true principle**.

A unlabeled data of true negative (negative) should be pushed apart from the anchor, leading to the **hard principle**.

Starting from the above intuition, we design BCL that still uses random samples from the **unlabeled data**, while correcting the resulting bias with importance weights.


## Flags:
`--alpha`: corresponding to the macro-AUC of encoder, and specifies the **location parameter** for **dibiasing false negatives**.

`--beta`: corresponding to the concentration degree of hard negative components and specifies the **hardness level** for **mining hard negatives**.

`--estimator`: specifies the comparative learning methods: SimCLR, DCL, HCL, BCL.

## Usage
For instance, run the following command to train an embedding on CIFAR10.
```
python main.py --dataset_name stl10 --batch_size 256 --estimator BCL --alpha 0.80 --beta 1.0
```

## Linear evaluation
The model is evaluated by training a linear classifier after fixing the learned embedding.

path flags:
  - `--model_path`: specify the path to saved model
```
python linear.py --dataset_name stl10 --model_path ../results/stl10/stl10_BCL_model_256_0.8_1.0_400.pth
```

## Acknowledgements

Part of this code is credited to [leftthomas/SimCLR](https://github.com/leftthomas/SimCLR), [chingyaoc/DCL](https://github.com/chingyaoc/DCL) and [Joshua/HCL](https://github.com/joshr17/HCL).

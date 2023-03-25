
## Bayesian Self-supervised Contrastive Learning

flags:
  - `--alpha`: macro-AUC of encoder, which specify *location parameter* for *dibiasing false negatives*.
  - `--beta`: propotion of hard negative component, which specify hardness level for *mining hard negatives*.
  - `--estimator`: specify comparative learning methods: SimCLR, DCL, BCL, HCL


For instance, run the following command to train an embedding on CIFAR10.
```
python main.py --esitmator BCL
```
```
python main.py --esitmator SimCLR
```
```
python main.py --esitmator DCL
```

```
python main.py --esitmator HCL
```

### Linear evaluation
The model is evaluated by training a linear classifier after fixing the learned embedding.

path flags:
  - `--model_path`: specify the path to saved model
```
python linear.py --model_path results/model.pth
```

## Acknowledgements

Part of this code is inspired by [leftthomas/SimCLR](https://github.com/leftthomas/SimCLR), [chingyaoc/DCL](https://github.com/chingyaoc/DCL) and [Joshua/HCL](https://github.com/joshr17/HCL).

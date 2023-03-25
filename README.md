
## Bayesian Self-supervised Contrastive Learning

flags:
  - `--alpha`: macro-AUC of encoder, which specify *location parameter* for *dibiasing false negatives*.
  - `--beta`: propotion of hard negative component, which specify hardness level for *mining hard negatives*.
  - `--estimator`: specify comparative learning methods: SimCLR, DCL, BCL, HCL


Please use the following command to replicate the BCL and comparative methods:
```
python main.py --dataset_name cifar10 --batch_size 256 --estimator BCL
```
```
python main.py --dataset_name cifar10 --batch_size 256 --estimator HCL
```
```
python main.py --dataset_name cifar10 --batch_size 256 --estimator DCL
```

```
python main.py --dataset_name cifar10 --batch_size 256 --estimator SimCLR
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

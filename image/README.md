
## Flags:
`--alpha`: corresponding to the macro-AUC of encoder, and specifies the **location parameter** for **dibiasing false negatives**.

`--beta`: corresponding to the concentration degree of hard negative components and specifies the **hardness level** for **mining hard negatives**.

`--estimator`: specifies the comparative learning methods: SimCLR, DCL, HCL, BCL.

`--alpha_setting`: configuring an adaptive method for setting $\alpha$ : linear, empirical_estimation, None.

- linear: linearly increased $\alpha$.
- empirical_estimation: empirically estimated $\alpha$.
- None: fixed $\alpha$.

## Usage
For instance, run the following command to train an embedding on STL10 dataset.
```
python main.py --dataset_name stl10 --batch_size 256 --estimator BCL --alpha 0.80 --beta 1.0
```

## Linear evaluation
The model is evaluated by training a linear classifier after fixing the learned embedding.

path flags:
`--model_path`: specify the path to saved model
```
python linear.py --dataset_name stl10 --model_path ../results/stl10/stl10_BCL_model_256_0.8_1.0_400.pth
```

## Pretrained Models
|Method  |    $\alpha$     |    $\beta$    | Arch | Latent Dim | Batch Size  | Accuracy(%) | Download |
|---|:---------------:|:-------------:|:----:|:---:|:---:|:-----------:|:---:|
| SimCLR |        ／        |       ／       | ResNet50 | 128  | 256  |    80.15    |  [model](https://drive.google.com/file/d/1qQE03ztnQCK4dtG-GPwCvF66nq_Mk_mo/view?usp=sharing)|
| BCL | 0.70 | 1.0 | ResNet50 | 128  | 256  |    87.51    |  [model](https://drive.google.com/file/d/18Z4L6F_yT21-GakycPpcq2Jue7KdUssx/view?usp=drive_link)|
| BCL | 0.75  |1.0 | ResNet50 | 128  | 256  |    86.31    |  [model](https://drive.google.com/file/d/1W7-m9QQMfyFDLEV0BsNs0357tZMW9Tlu/view?usp=drive_link)|
| BCL | 0.80  |1.0 | ResNet50 | 128  | 256  |    87.35    |  [model](https://drive.google.com/file/d/1vhPi4xt2_TaI_fZyO0pJtz9JYE8g7zLt/view?usp=drive_link)|
| BCL | 0.85  |1.0 | ResNet50 | 128  | 256  |    87.12    |  [model](https://drive.google.com/file/d/1q28dQe60dUMB4Xp9WP60kY1qfzsRXFIx/view?usp=drive_link)|

## Acknowledgements

Part of this code is credited to [leftthomas/SimCLR](https://github.com/leftthomas/SimCLR), [chingyaoc/DCL](https://github.com/chingyaoc/DCL) and [Joshua/HCL](https://github.com/joshr17/HCL).

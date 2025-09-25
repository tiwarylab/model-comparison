## Model Comparison: NS, CFM, DDPM on GMM and Aib9 MD Data

Repository for the code to measure performance of Neural Spline Flows, Conditional Flow Matching, and Denoising Diffusion Probabilistic Models across Gaussian mixture model and Aib9 torsion angle distribution datasets.

Work published in the [Journal of Chemical Physics](https://pubs.aip.org/aip/jcp/article/162/11/114121/3340279).

![image](utils/panelaib9.png)

*Figure 5 in JCP paper: Model accuracy results and generated data for the Aib9 peptide. (a) KLD performance comparison as a function of the residue index for the complete Aib9 torsion angle dataset. (b) KLD performance comparison for the three models and Gaussian baseline fit as a function of training dataset size for the Aib9 torsion angle data distribution at residue 5. (c)–(f) {Φ, Ψ} show free energy contour plots for torsion angle distributions at residue 1 for training data and generated data for NS, CFM, and DDPM, respectively.*

## Setup

This repository uses [Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html).

To setup the environment, run the following:

```bash
micromamba config set channel_priority flexible
micromamba create -n compenv -f environment.yml
micromamba activate compenv
```

## Datasets

The datasets folder contains three `.ipynb` notebooks. The first, `data_accessor.ipynb`, downloads all the required datasets for the experiments from [Zenodo](https://zenodo.org/records/14679134?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjAyYmYzODhlLWE2ZjYtNDA4NS1iNDhlLTJlNzZmMzcyNzMwZCIsImRhdGEiOnt9LCJyYW5kb20iOiI0YTE3NTE3N2Y4MThkODg0YTY4NTI4OWExMGE3NmNmNiJ9.HcFgvUV0sK8EhJm0Ow8cFn-56q8rGuSWj_LBQIcpzMZ_mAySqnJ4pJeJubxw_3Dtl2chUoHAGOaxgaRFyZRLWg) automatically. 

`generator_aib9.ipynb` and `generator_gmm.ipynb` can be used to verify the datasets or generate new ones with different properties, but are not necessary. After the datasets are loaded or generated, experiments may be run.

## Experiments

The experiments folder contains all of the core tests run on the three architectures. The procedure for running an experiment is as follows:
1. Navigate to the desired experiment.
2. Modify any entries in the `config` folder if desired. If unmodified, experiments match those done in the paper.
3. Run each model individually with `python run_cfm.py`. If running on a SLURM-enabled cluster, a flag can be attached as follows: `python run_cfm.py --use_slurm`. SLURM headings may need to be adapted to the user's system in the `run_{model}.py` files.
4. Output, including hyperparameters, raw data, and performance metrics will be placed in an `output` folder, as well as SLURM outputs in a `logs` folder.

## Analysis

After running desired experiments, the output can be analyzed with the `analysis.ipynb` notebook in the `analysis` folder. Only two analysis blocks are currently configured, one for the asymmetry experiment, and one for all other experiments (the user will need to select which experiment to analyze in the notebook).

## Utilities

Utility functions are included in the `utils` folder, separated by model.

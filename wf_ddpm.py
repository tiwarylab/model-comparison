import numpy as np
import os
from slurmflow.config import ConfigParser
from slurmflow.serializer import ObjectSerializer
from slurmflow.driver import SlurmDriver

slurm_config = ConfigParser("config/ddpm_slurm.yml")
slurm_args = slurm_config.config_data
driver = SlurmDriver()

excluded_args = []

"""
config = ConfigParser("config/ddpm_gmm.yml")
args = config.compile(leaves=True, as_args=True)
cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
cmd = f"python run_ddpm.py {cmd_args}"
driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)
"""
"""
config = ConfigParser("config/ddpm_gmm.yml")
config.set('params.path_modes', 4)
dim_range = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
iter_range = np.array([1, 2, 3])
for dim in dim_range:
    for iter in iter_range:
        config.set('params.path_dim', dim)
        config.set('params.keyword', f"varyingdim_{iter}")
        args = config.compile(leaves=True, as_args=True)
        cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
        cmd = f"python run_ddpm.py {cmd_args}"
        driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)
"""

config = ConfigParser("config/ddpm_gmm.yml")
config.set('params.path_dim', 50)
modes_range = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
iter_range = np.array([1, 2, 3])
for modes in modes_range:
    for iter in iter_range:
        config.set('params.path_modes', modes)
        config.set('params.keyword', f"varyingmodes_{iter}")
        args = config.compile(leaves=True, as_args=True)
        cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
        cmd = f"python run_ddpm.py {cmd_args}"
        driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)

"""
config = ConfigParser("config/ddpm_gmm.yml")
config.set('params.path_dim', 50)
config.set('params.path_modes', 4)
model_dim_range = np.array([4, 8, 16, 32, 48, 64, 96, 128, 256])
iter_range = np.array([1, 2, 3])
for model_dim in model_dim_range:
    for iter in iter_range:
        config.set('params.model_dim', model_dim)
        config.set('params.keyword', f"{model_dim}_varyingmodel_dim_{iter}")
        args = config.compile(leaves=True, as_args=True)
        cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
        cmd = f"python run_ddpm.py {cmd_args}"
        driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)
"""
"""
config = ConfigParser("config/ddpm_gmm.yml")
config.set('params.path_modes', 4)
config.set('params.path_dim', 50)
size_range = np.array([5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000])
iter_range = np.array([1, 2, 3])
for size in size_range:
    for iter in iter_range:
        config.set('params.dataset_limiter', size)
        config.set('params.keyword', f"{size}_varyingsize_{iter}")
        args = config.compile(leaves=True, as_args=True)
        cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
        cmd = f"python run_ddpm.py {cmd_args}"
        driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)
"""
"""
config = ConfigParser("config/ddpm_aib9.yml")
#residue_range = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
iter_range = np.array([1, 2, 3])
#for residue in residue_range:
for iter in iter_range:
    config.set('params.data_type', 'total')
    config.set('params.path_dim', 18)
    config.set('params.residue', 0)
    config.set('params.keyword', iter)
    args = config.compile(leaves=True, as_args=True)
    cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
    cmd = f"python run_ddpm.py {cmd_args}"
    driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)
"""
"""
config = ConfigParser("config/ddpm_aib9.yml")
size_range = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
iter_range = np.array([1, 2, 3])
for size in size_range:
    for iter in iter_range:
        config.set('params.data_type', 'total')
        config.set('params.path_dim', 18)
        config.set('params.residue', 0)
        config.set('params.dataset_limiter', size)
        config.set('params.keyword', f"{size}_varyingsize_{iter}")
        args = config.compile(leaves=True, as_args=True)
        cmd_args = " ".join([f"--{k} {v}" for k, v in vars(args).items() if v is not None and k not in excluded_args])
        cmd = f"python run_ddpm.py {cmd_args}"
        driver.submit_job(cmd, env="newenv", modules = ['cuda/12.1.1/'], slurm_args=slurm_args, track=True)
"""

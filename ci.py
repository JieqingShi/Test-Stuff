import wandb

print(f"The version of wand is {wandb.__version__}")

assert wandb.__version__ == "2.1.1", f"Expected version is 2.1.1 but actual version is {wandb.__version__}"

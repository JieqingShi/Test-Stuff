import wandb

print(f"The version of wand is {wandb.__version__}")

assert wandb.__version__ == "0.16.3", f"Expected version is {0.16.3} but actual version is {wandb.__version__}"

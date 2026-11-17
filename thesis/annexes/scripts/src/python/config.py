from tqdm.std import tqdm as tqdm_base
import logging
import pandas as pd
import seaborn as sns
import torch

################################################
# Configuration Panel - version 1.2 Standalone #
# Last modification : october 2025             #
# Alexis Gracias                               #
################################################

# Progress bars in for loop functions
def tqdm2(*args, **kwargs):
    kwargs.setdefault("bar_format", "{l_bar}{bar}| {n_fmt}/{total_fmt} • {elapsed} • {rate_fmt}")
    kwargs.setdefault("ncols", 90)
    kwargs.setdefault("colour", "green")
    kwargs.setdefault("dynamic_ncols", False)
    return tqdm_base(*args, **kwargs)
    
# Main function
def config():

    # --------- init --------- #
    # Logger init
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # GPU usage
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Utilisation GPU" if device.type == "cuda" else "Utilisation du CPU")
    
    # Aesthetic
    sns.set_style("darkgrid")
    tqdm_base.pandas(
        desc="Nettoyage", 
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} • {elapsed} • {rate_fmt}",
        ncols=90,
        colour="green"
    )
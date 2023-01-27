#!/usr/bin/env python
"""
basic_cleaning
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="eda")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

   
    artifact_local_path = run.use_artifact(args.input_artifact).file()
    df = pd.read_csv(artifact_local_path)
    wandb.log({"table": df})
    run.finish()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="eda")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="input_artifact",
        required=True
    )

    


    args = parser.parse_args()

    go(args)

#!/usr/bin/env python
"""
This script download a URL to a local destination
"""
import argparse
import logging
import os

import wandb

from log_artifact import log_artifact

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="download_file")
    run.config.update(args)

    #logger.info(f"Returning sample {args.sample}")
    #logger.info(f"Uploading {args.artifact_name} to Weights & Biases")
    #log_artifact(
    #    args.artifact_name,
    #    args.artifact_type,
    #    args.artifact_description,
    #    os.path.join("data", args.sample),
    #    run,
    #)

    logger.info("Creating artifact")
    artifact = wandb.Artifact(
            name=args.artifact_name,
            type=args.artifact_type,
            description=args.artifact_description,
             metadata={'key_1': 'value1'}
            )
    artifact.add_file(os.path.join("data", args.sample), name=args.artifact_name)

    logger.info("Logging artifact")
    run.log_artifact(artifact)
    run.finish()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download URL to a local destination")

    parser.add_argument("sample", type=str, help="Name of the sample to download")

    parser.add_argument("artifact_name", type=str, help="Name for the output artifact")

    parser.add_argument("artifact_type", type=str, help="Output artifact type.")

    parser.add_argument(
        "artifact_description", type=str, help="A brief description of this artifact"
    )

    args = parser.parse_args()

    go(args)

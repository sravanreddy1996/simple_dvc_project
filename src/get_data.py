## read the params
## process it
## return the dataframe
import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)
    return config


def get_data(config_path):
    config = read_params(config_path)

    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path)

    return df


if __name__ == '__main__':
    args_obj = argparse.ArgumentParser()
    args_obj.add_argument("--config", default="params.yaml")
    parsed_args = args_obj.parse_args()
    data = get_data(config_path=parsed_args.config)

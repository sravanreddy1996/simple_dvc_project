# read the data from data source
# save it in the data/raw for further process.

import os

import argparse

from get_data import read_params, get_data_df


def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data_df(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]

    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)



if __name__ == '__main__':
    args_obj = argparse.ArgumentParser()
    args_obj.add_argument("--config", default="params.yaml")
    parsed_args = args_obj.parse_args()
    data = load_and_save(config_path=parsed_args.config)

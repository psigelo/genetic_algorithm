from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# not topology mutations
import argparse
import numpy as np
import json



import tensorflow as tf


class Population(object):
    def __init__(self):
        pass


def create_initial_population(config: dict) -> Population:
    """

    :type config: dict
    :param config: a dictionary with [initial_pop_amount] value
    """
    population_amount = config['initial_pop']
    initial_structure = config['initial_structure']



    return Population()


def main(config: dict) -> None:

    """
    :type config: dict
    :param config: configuration dict from a json file.
    """
    create_initial_population(config)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=True)
    cmd_args = parser.parse_args()

    with open(cmd_args.config) as json_data:
        config_json = json.load(json_data)

    main(config_json)

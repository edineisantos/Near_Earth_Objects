"""Extract data on near-Earth objects and close approaches from CSV and JSON.

The `load_neos` function extracts NEO data from a CSV file into a collection
of `NearEarthObject`s. The `load_approaches` function extracts close approach
data from a JSON file into a collection of `CloseApproach` objects. The main
module calls these functions with the command line arguments and uses the
resulting collections to build an `NEODatabase`.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing NEO data.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            designation = row['pdes']
            name = row['name'].strip() if row['name'].strip() else None
            diameter = (float(row['diameter']) if row['diameter']
                        else float('nan'))
            hazardous = row['pha'] == 'Y'

            neo = NearEarthObject(
                designation=designation,
                name=name,
                diameter=diameter,
                hazardous=hazardous
            )
            neos.append(neo)

    return neos


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing close approach data.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, 'r') as file:
        data = json.load(file)

        for approach_data in data['data']:
            des, _, _, cd, dist, _, _, v_rel, _, _, _ = approach_data

            approach = CloseApproach(
                designation=des.strip(),
                time=cd,
                distance=float(dist),
                velocity=float(v_rel)
            )
            approaches.append(approach)

    return approaches

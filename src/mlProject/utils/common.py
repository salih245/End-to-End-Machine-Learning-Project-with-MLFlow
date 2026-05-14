import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' read successfully.")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a list of paths.

    Args:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): The path where the JSON file will be saved.
        data (dict): The dictionary to save as JSON.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Data saved to JSON file at: {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"Data loaded from JSON file at: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be saved.
        path (Path): The path where the binary file will be saved.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved to binary file at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The loaded data.
    """
    data = joblib.load(filename=path)
    logger.info(f"Data loaded from binary file at: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in a human-readable format.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file in a human-readable format.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
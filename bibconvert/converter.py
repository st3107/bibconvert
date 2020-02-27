import json
from pathlib import Path

import yaml

from bibconvert.parsers import *

PARSERS = {
    "csl": csl_parser
}


class Converter:
    """
    The converter class instance. It is used for load cls json or bib json and convert it to the rg-db-group acceptable
    data format and save it as yaml.

    Attributes
    ----------
    file_path : Path
        The path to the json file. The json file contains single or multiple citation objects.
    docs : List[dict]
        The documentations of citations.
    """
    def __init__(self, file_path: str, file_type: str):
        """
        Initiate the class instance.

        Parameters
        ----------
        file_path
            The path to the input file.
        file_type
            The type of the input file.
        """
        self.file_path = Path(file_path)
        self.file_type = file_type
        self.docs = self.load_json()
        self.parsed_docs = self.parse_docs()

    def load_json(self):
        """
        Load the json file according to the file path. If the object is a single dictionary, make it a one-item list.
        """
        file_path = self.file_path
        with file_path.open('r', encoding='utf-8') as f:
            docs = json.load(f)
        if isinstance(docs, dict):
            docs = [docs]
        return docs

    def parse_docs(self):
        """
        Parse the documents to the rg-db-group acceptable format in place.
        """
        docs = self.docs
        mode = self.file_type
        parser = PARSERS.get(mode)
        if parser is None:
            raise ValueError(f"Unknown parsing mode: {mode}")
        parsed_docs = {}
        for i, doc in enumerate(docs):
            _id, parsed_doc = parser(doc)
            parsed_docs.update({_id: parsed_doc})
        return parsed_docs

    def write_yaml(self, yaml_file: str):
        """
        Write the yaml file of the docs.

        Parameters
        ----------
        yaml_file
            The path to the yaml file.
        """
        yaml_file = Path(yaml_file)
        docs = self.parsed_docs
        with yaml_file.open('w', encoding='utf-8') as f:
            yaml.dump(docs, f)
        return

import fire

from bibconvert.converter import Converter


def main(input_file: str, output_file: str, file_type: str = "csl"):
    """
    Parse the bib related files into a yaml file containing documents in the format of citations in the bilinge group
    data base.

    Parameters
    ----------
    input_file
        The path to the bib related file.
    output_file
        The path to the output yaml file.
    file_type
        The type of the input file. Allowed: csl.
    """
    converter = Converter(input_file, file_type)
    converter.write_yaml(output_file)
    return


if __name__ == "__main__":
    fire.Fire(main)

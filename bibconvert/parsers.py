from typing import Tuple

from bibconvert.tools import *

__all__ = [
    "csl_parser"
]

CSL_MAP = {
    "author": ("author", parse_csl_author),
    "doi": ("DOI", lambda s: s),
    "entrytype": ("type", lambda s: s),
    "facility": (None, None),
    "grant": (None, None),
    "journal": ("journalAbbreviation", lambda s: s),
    "nb": (None, None),
    "optannote": (None, None),
    "optnote": (None, None),
    "optwwwlanl": (None, None),
    "optwwwpub": (None, None),
    "pages": ("page", lambda s: s),
    "title": ("title", lambda s: s),
    "url": ("URL", lambda s: s),
    "volume": ("volume", lambda s: s),
    "wwwemail": (None, None),
    "wwwpub": (None, None),
    "year": ("issued", parse_csl_year)
}


def csl_parser(doc: dict) -> Tuple[str, dict]:
    """
    Parse the document from the csl json file into the document in billinge group db.

    Parameters
    ----------
    doc
        The document dictionary.

    Returns
    -------
    _id
        The id key of the parsed document.
    parsed_doc
        The parsed document.
    """
    parsed_doc = {}
    for db_key, (csl_key, parse) in CSL_MAP.items():
        if csl_key is None:
            parsed_value = ""
        else:
            value = doc.get(csl_key)
            if value:
                parsed_value = parse(value)
            else:
                parsed_value = ""
        parsed_doc.update({db_key: parsed_value})
    _id = generate_id(parsed_doc)
    return _id, parsed_doc

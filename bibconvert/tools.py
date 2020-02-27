from typing import List, Dict

__all__ = [
    "generate_id",
    "parse_csl_author",
    "parse_csl_year"
]


def generate_id(doc: dict) -> str:
    """
    Generate the id key from the citation document.

    Parameters
    ----------
    doc
        The document in billinge group db.

    Returns
    -------
    _id
        The id of the document.
    """
    # last name of the first author
    authors: list = doc.get("author")
    if authors:
        first_author = authors[0]
        last_name = first_author.split(",")[0].lower()
    else:
        raise ValueError(f"No authors in the {doc}")
    # abbreviation of the journal
    journal: str = doc.get("journal")
    if journal:
        abb_journal = "".join([word[0] for word in journal.split()]).lower()
    else:
        raise ValueError(f"No journal in the {doc}")
    # year
    year: str = doc.get("year")
    if year:
        two_d_year = year[-2:]
    else:
        raise ValueError(f"No year in the {doc}")
    # combine them to get the id
    _id = f"{last_name};{abb_journal}{two_d_year}"
    return _id


def parse_csl_author(authors: List[Dict[str, str]]) -> List[str]:
    """Parse the author list in csl json."""
    parsed_authors = []
    for author in authors:
        family_name = author.get("family")
        given_name = author.get("given")
        parsed_author = f"{family_name}, {given_name}"
        parsed_authors.append(parsed_author)
    return parsed_authors


def parse_csl_year(issued: Dict[str, list]) -> str:
    """Get the year in csl json."""
    date_parts = issued.get("date-parts")
    year = str(date_parts[0][0])
    return year

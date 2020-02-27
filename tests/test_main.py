from pathlib import Path

import pytest

from bibconvert.main import main


@pytest.mark.parametrize(
    "test_case,expect", [
        (
                ("test_cases/test_csl_input.json", "test_cases/test_csl_output.yaml"),
                "test_cases/test_csl_expect.yaml"
        )
    ]
)
def test_main(test_case, expect):
    main(*test_case)
    output_file = Path(test_case[1])
    expect_file = Path(expect)
    with output_file.open("r") as f0:
        output_str = f0.read()
    with expect_file.open("r") as f1:
        expect_str = f1.read()
    assert output_str == expect_str

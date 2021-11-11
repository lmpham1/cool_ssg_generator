from cool_ssg.utils import config_util


def test_config():
    options = {
        "output": None,
        "lang": None,
        "input": None,
        "stylesheets": None,
    }
    config_path = "tests/testfiles/test_config.json"
    config_util.get_config(config_path, options)
    assert options["output"] is not None
    assert options["lang"] is not None
    assert options["input"] is None
    assert options["stylesheets"] is not None

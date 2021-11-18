from cool_ssg.utils import html_generator_util
from pathlib import Path


class TestSidebar:
    input_dir = "tests/testfiles"
    output = Path("./dist")

    def test_no_sidebar(self):
        result = html_generator_util.generate_sidebar(
            self.input_dir, self.output, None
        )
        assert result is None

    def test_default_sidebar(self):
        result = html_generator_util.generate_sidebar(
            self.input_dir, self.output, -1
        )
        link1 = Path("sample").joinpath("Silver Blaze.html")
        link2 = Path("sample").joinpath(
            "The Adventure of the Six Napoleans.html"
        )
        link3 = Path("sample").joinpath(
            "The Adventure of the Speckled Band.html"
        )
        link4 = Path("sample").joinpath("The Naval Treaty.html")
        link5 = Path("sample").joinpath("The Red Headed League.html")

        assert '<li><a href="{}">Silver Blaze</a></li>'.format(link1) in result
        assert (
            '<li><a href="{}">The Adventure of the Six Napoleans</a></li>'.format(  # noqa: E501
                link2
            )
            in result
        )
        assert (
            '<li><a href="{}">The Adventure of the Speckled Band</a></li>'.format(  # noqa: E501
                link3
            )
            in result
        )
        assert (
            '<li><a href="{}">The Naval Treaty</a></li>'.format(link4)
            in result
        )
        assert (
            '<li><a href="{}">The Red Headed League</a></li>'.format(link5)
            in result
        )
        assert (
            '<li><a href="test_general.html">test_general</a></li>' in result
        )

    def test_custom_sidebar(self):
        sidebar_config = {
            "type": "pages",
            "title": "sample stories",
            "items": ["./sample"],
        }
        result = html_generator_util.generate_sidebar(
            self.input_dir, self.output, sidebar_config
        )
        link1 = Path("sample").joinpath("Silver Blaze.html")
        link2 = Path("sample").joinpath(
            "The Adventure of the Six Napoleans.html"
        )
        link3 = Path("sample").joinpath(
            "The Adventure of the Speckled Band.html"
        )
        link4 = Path("sample").joinpath("The Naval Treaty.html")
        link5 = Path("sample").joinpath("The Red Headed League.html")
        assert '<li><a href="{}">Silver Blaze</a></li>'.format(link1) in result
        assert (
            '<li><a href="{}">The Adventure of the Six Napoleans</a></li>'.format(  # noqa: E501
                link2
            )
            in result
        )
        assert (
            '<li><a href="{}">The Adventure of the Speckled Band</a></li>'.format(  # noqa: E501
                link3
            )
            in result
        )
        assert (
            '<li><a href="{}">The Naval Treaty</a></li>'.format(link4)
            in result
        )
        assert (
            '<li><a href="{}">The Red Headed League</a></li>'.format(link5)
            in result
        )

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
        print(result)
        expected_result = """<div class="sidebar-container">
<ul>
<li>
sample
<ul>
<li><a href="sample\\Silver Blaze.html">Silver Blaze</a></li>
<li><a href="sample\\The Adventure of the Six Napoleans.html">The Adventure of the Six Napoleans</a></li>
<li><a href="sample\\The Adventure of the Speckled Band.html">The Adventure of the Speckled Band</a></li>
<li><a href="sample\\The Naval Treaty.html">The Naval Treaty</a></li>
<li><a href="sample\\The Red Headed League.html">The Red Headed League</a></li>
</ul>
</li>
<li><a href="test_general.html">test_general</a></li>
<li><a href="test_md_bold.html">test_md_bold</a></li>
<li><a href="test_md_italic.html">test_md_italic</a></li>
<li><a href="test_md_link.html">test_md_link</a></li>
</ul>

</div>
"""  # noqa: E501,W605
        assert result == expected_result

    def test_custom_sidebar(self):
        sidebar_config = {
            "type": "pages",
            "title": "sample stories",
            "items": ["./sample"],
        }
        result = html_generator_util.generate_sidebar(
            self.input_dir, self.output, sidebar_config
        )
        print(result)
        expected_result = """<div class="sidebar-container">
<ul>
<h2>sample stories</h2><ul>
<li><a href="sample\\Silver Blaze.html">Silver Blaze</a></li>
<li><a href="sample\\The Adventure of the Six Napoleans.html">The Adventure of the Six Napoleans</a></li>
<li><a href="sample\\The Adventure of the Speckled Band.html">The Adventure of the Speckled Band</a></li>
<li><a href="sample\\The Naval Treaty.html">The Naval Treaty</a></li>
<li><a href="sample\\The Red Headed League.html">The Red Headed League</a></li>
</ul>

</ul>

</div>
"""  # noqa: E501,W605
        assert result == expected_result

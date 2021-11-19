from cool_ssg.utils import html_generator_util


class TestHTMLGenerator:
    options = {
        "lang": "en",
        "stylesheets": None,  # noqa E501
        "sidebar": None,
    }

    def open_file(self, filename):
        with open(filename, "r") as file:
            contents = "".join(file.readlines())
            if filename.endswith(".md"):
                contents = html_generator_util.process_markdown(contents)
            result = html_generator_util.create_html_string(
                filename=filename,
                contents=contents,
                output="./dist/",
                options=self.options,
            )
            return result

    def test_paragraph(self):
        expected_result = """<h1>hello world</h1>

                <p>this is to test the thing</p>

<p>another paragraph</p>"""
        filename = "tests/testfiles/test_general.txt"
        result = self.open_file(filename)
        resultList = result.splitlines()[12:17]
        result = "\n".join(resultList).strip()
        assert result == expected_result

    def test_md_bold(self):
        expected_result = """<h1>This is a bold test</h1>

                <p><strong>the whole line should be bold</strong>*</p>

<p>Multiple <strong>boldness</strong> in this <strong>line</strong></p>

<p>Also should <strong>work with underscores</strong></p>

<p>And should <strong>work with * in the middle</strong></p>"""
        filename = "tests/testfiles/test_md_bold.md"
        result = self.open_file(filename)
        resultList = result.splitlines()[12:21]
        result = "\n".join(resultList).strip()
        assert result == expected_result

    def test_md_italic(self):
        expected_result = """<h1>This is an italic test</h1>

                <p><em>the whole line should be emphasized</em></p>

<p>By <em>emphasized</em> I meant <em>italic</em></p>

<p>Also should <em>work with underscores</em></p>

<p>And should <em>work with </em>* in the middle*</p>

<p>And should <em><strong>work with bold</strong></em></p>"""
        filename = "tests/testfiles/test_md_italic.md"
        result = self.open_file(filename)
        resultList = result.splitlines()[12:23]
        result = "\n".join(resultList).strip()
        assert result == expected_result

    def test_md_link(self):
        expected_result = """<h1>This is a link MD test</h1>

                <p>oh an <a href="www.example.com">example link</a></p>

<p>not a valid link [hello world](123 123)</p>

<p>link with empty title [](www.example.com)</p>

<p>link with [empty body]()</p>"""
        filename = "tests/testfiles/test_md_link.md"
        result = self.open_file(filename)
        resultList = result.splitlines()[12:21]
        result = "\n".join(resultList).strip()
        assert result == expected_result

    def test_md_complicated(self):
        expected_result = """<h1>This is a mixed MD test.</h1>

                <p><strong>This line should be bolded</strong></p>

<p>And <strong>this part should be bolded</strong></p>

<p>This is an <a href="www.example.com">example link</a></p>

<p>And this line is some regular texts. This is a second sentence of the text.</p>

<p>This is another paragraph of the text.</p>"""
        filename = "tests/testfiles/test_md_complicated.md"
        result = self.open_file(filename)
        resultList = result.splitlines()[12:23]
        result = "\n".join(resultList).strip()
        assert result == expected_result

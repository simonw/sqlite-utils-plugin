from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "foo",
            "description": "blah",
        },
    )
    assert paths(tmpdir) == {
        "sqlite-utils-foo/.github/workflows",
        "sqlite-utils-foo/LICENSE",
        "sqlite-utils-foo/README.md",
        "sqlite-utils-foo/.github/workflows/publish.yml",
        "sqlite-utils-foo/sqlite_utils_foo.py",
        "sqlite-utils-foo/.github/workflows/test.yml",
        "sqlite-utils-foo/pyproject.toml",
        "sqlite-utils-foo/.gitignore",
        "sqlite-utils-foo",
        "sqlite-utils-foo/.github",
        "sqlite-utils-foo/tests/test_foo.py",
        "sqlite-utils-foo/tests",
    }


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}

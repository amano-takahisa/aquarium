import markdown
from osgeo import gdal

md = markdown.Markdown(extensions=["pymdownx.snippets"])


# --8<-- [start:func]
def with_gdal():
    print("gdal.Info(path_to_a_file)")


def my_function(var):
    pass


# --8<-- [end:func]

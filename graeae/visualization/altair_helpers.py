# python
from functools import partial
from pathlib import Path

# pypi
from tabulate import tabulate

import altair
import pandas


def output_path(slug: str) -> Path:
    """Setup the Folder path for posts

    Args:
     slug: the slug for the post

    Returns:
     path object for output folder
    """
    OUTPUT_PATH = Path(f"files/posts/{slug}")
    if not OUTPUT_PATH.is_dir():
        OUTPUT_PATH.mkdir()
    return OUTPUT_PATH


TABLE = partial(tabulate, tablefmt="orgtbl",
                showindex=False,
                headers="keys")

def print_org_table(frame: pandas.DataFrame) -> None:
    """Use tabulate to print a table

    Args:
     frame: the data frame to print
    """
    print(TABLE(frame))
    return


def save_chart(chart: altair.Chart, name: str,
               output_path: Path,
               height: int=600) -> None:
    """Save and print the altair chart

    Args:
     chart: altair chart to save
     name: name of the chart to use (with or without file extension)
     output:path: folder-path for the output file
     height: argument to give the html block for height

    Side-Effect:
     prints the HTML export block for the chart
    """
    name = name if name.endswith(".html") else f"{name}.html"
    chart.save(str(output_path/name))

    print(f"""#+begin_export html
<object type="text/html" data="{name}" style="width:100%" height={height}>
  <p>Figure Missing</p>
</object>
#+end_export
""")
    return

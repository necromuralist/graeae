# python
from functools import partial
from pathlib import Path
from string import Template

# pypi
from tabulate import tabulate

import altair
import pandas

VEGA_EMBED_TEMPLATE = Template("""
     (function(vegaEmbed) {
       var spec = $JSON_SPEC;

      var embedOpt = {"mode": "vega-lite"};

      function showError(el, error){
          el.innerHTML = ('<div class="error" style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      } // showError
      const el = document.getElementById('$DIV_ID');
      vegaEmbed("#$DIV_ID", spec, embedOpt)
        .catch(error => showError(el, error));
    })(vegaEmbed);
""")

SHORTCODE = Template('{{% altairdiv source="$SOURCE" divid="$DIVID" %}}')

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
    """Save and print the altair chart HTML tag

    This saves an entire HTML document (head and body) so it needs
    to be embedded as an <object>

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
#+end_export""")
    return

def save_vega_embed(chart: altair.Chart,
                    name: str,
                    output_path: Path,
                    div_id: str,
                    json_indent: int=None,
                    emit: bool=True) -> str:
    """Save the vega chart as a javascript file

    This will require that there's a <div> target for the chart and
    a <script> tag to load the file we're going to save

    Params:

     - `chart`: altair chart to get the JSON spec from
     - `name`: name to save the javascript file to
     - `output_path`: path object to open the file
     - `div_id`: ID of the div tag to hold the chart
     - `json_indent`: amount json.dumps should indent to pretty-print the spec
     - `emit`: if True, print the shortcode
    Returns:
      Shortcode string to emit for nikola.
    """
    SUFFIX = ".js"
    file_name = name if name.endswith(SUFFIX) else name + SUFFIX
    javascript = VEGA_EMBED_TEMPLATE.substitute(
        JSON_SPEC=chart.to_json(indent=json_indent),
        DIV_ID=div_id
    )

    with (output_path/file_name).open("w") as writer:
        writer.write(javascript)

    shortcode = SHORTCODE.substitute(SOURCE=file_name, DIVID=div_id)
    if emit:
        print(shortcode)
    return shortcode

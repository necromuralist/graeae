# from python
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
import textwrap
# from pypi
from bokeh.embed import autoload_static
import bokeh.plotting
import bokeh.resources
import holoviews

PathType = Union[str, Path]


class EmbedBase:
    """Embed a bokeh figure

    Args:
     plot: a hvplot to embed
     folder_path: path to the folder to save the file
     file_name: name of the file to save the javascript in
     add_extension: add file-extension to file name
     create_folder: if the folder doesn't exist create it
     make_parents: if creating a folder add the missing folders in the path
    """
    def __init__(self, plot: holoviews.core.overlay.NdOverlay,
                 file_name: str,
                 folder_path: PathType,
                 add_extension: bool=False,
                 create_folder: bool=True,
                 make_parents: bool=True) -> None:
        self.plot = plot
        self.create_folder = create_folder
        self.make_parents = make_parents
        self.add_extension = add_extension
        self._folder_path = None
        self.folder_path = folder_path
        self._file_extension = None
        self._file_name = None
        self.file_name = file_name
        self._source = None
        self._export_string = None
        return

    @property
    @abstractmethod
    def file_extension(self) -> str:
        """Extension for the generated file"""
        return

    @property
    def folder_path(self) -> Path:
        """The path to the folder to store the output"""
        return self._folder_path

    @folder_path.setter
    def folder_path(self, path: PathType) -> None:
        """Sets the path to the javascript folder"""
        self._folder_path = Path(path)
        if self.create_folder and  not self._folder_path.is_dir():
            self._folder_path.mkdir(parents=self.make_parents)
        return

    @property
    def file_name(self) -> str:
        """The name of the file"""
        return self._file_name

    @file_name.setter
    def file_name(self, name: str) -> None:
        """Sets the filename

        Args:
         name: name to save the output (without the folder)
        """
        name = Path(name)
        self._file_name = ("{}.{}".format(name.stem, self.file_extension)
                           if self.add_extension else name.stem)
        return

    @property
    @abstractmethod
    def source(self) -> str:
        """The HTML to export"""
        return

    @property
    def export_string(self) -> str:
        """The string to embed the figure into org-mode"""
        if self._export_string is None:
            self._export_string = textwrap.dedent(
                """#+begin_export html
{}
#+end_export""".format(self.source))
        return self._export_string

    @abstractmethod
    def save_figure(self) -> None:
        """Saves the rendered file"""
        return

    def __call__(self) -> None:
        """Creates the html and emits it"""
        self.save_figure()
        print(self.export_string)
        return

    def reset(self) -> None:
        """Sets the generated properties back to None"""
        self._export_string = None
        self._javascript = None
        self._source = None
        self._figure = None
        return


class EmbedBokeh(EmbedBase):
    """Class to embed a holoviews plot as bokeh

    Args:
     plot: a hvplot to embed
     folder_path: path to the folder to save the file
     file_name: name of the file to save the javascript in
     create_folder: if the folder doesn't exist create it
     make_parents: if creating a folder add the missing folders in the path
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._bokeh_source = None
        self._javascript = None
        self._figure = None
        return

    @property
    def file_extension(self) -> str:
        """The extension for the generated file"""
        if self._file_extension is None:
            self._file_extension = "js"
        return self._file_extension

    @property
    def figure(self) -> bokeh.plotting.Figure:
        """The Figure to plot"""
        if self._figure is None:
            if self.plot.__module__.startswith("holo"):
                self._figure = holoviews.render(self.plot)
            else:
                self._figure = self.plot
        return self._figure

    @property
    def bokeh_source(self) -> bokeh.resources.Resources:
        """The javascript source
        """
        if self._bokeh_source is None:
            self._bokeh_source = bokeh.resources.CDN
        return self._bokeh_source

    @property
    def source(self) -> str:
        """The HTML to save"""
        if self._source is None:
            self._javascript, self._source = autoload_static(self.figure,
                                                             self.bokeh_source,
                                                             self.file_name)
        return self._source

    @property
    def javascript(self) -> str:
        """javascript to save"""
        if self._javascript is None:
            self._javascript, self._source = autoload_static(self.figure,
                                                             self.bokeh_source,
                                                             self.file_name)
        return self._javascript

    def save_figure(self) -> None:
        """Saves the javascript file"""
        with open(self.folder_path.joinpath(self.file_name), "w") as writer:
            writer.write(self.javascript)
        return


class EmbedHoloview(EmbedBase):
    """Creates an embedding for generated Holoview HTML

    Args:
     width_in_percent: how wide to make the figure
     height_in_pixels: how tall to make the figure
     add_link: add link to the external file
     link_message: message to put in link
     plot: a hvplot to embed
     folder_path: path to the folder to save the file
     file_name: name of the file to save the javascript in
     create_folder: if the folder doesn't exist create it
     make_parents: if creating a folder add the missing folders in the path
    """
    def __init__(self, width_in_percent: int=100, height_in_pixels: int=800, 
                 add_link: bool=False, link_message: str="Link to Plot",
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_link = add_link
        self.width_in_percent = width_in_percent
        self.height_in_pixels = height_in_pixels
        self.link_message = link_message
        return

    @property
    def file_extension(self) -> str:
        """The extension for the saved file"""
        if self._file_extension is None:
            self._file_extension = "html"
        return self._file_extension
    
    def save_figure(self) -> None:
        """Saves the holoview"""
        holoviews.save(self.plot, self.folder_path.joinpath(self.file_name))
        return

    @property
    def source(self) -> str:
        """The HTML to export"""
        if self._source is None:
            self._source = '''<object type="text/html" data="{}.html" style="width:{}%" height={}>
  <p>Figure Missing</p>
</object>'''.format(self.file_name, self.width_in_percent, self.height_in_pixels)
        return self._source

    def create_external_link(self, message: str="Link To Plot") -> None:
        """creates an external file and links to it

        Args:
         message: text for the link
        """
        self.save_figure()
        print("[[file:{}][{}]]".format(message))
        return

    def __call__(self) -> None:
        """Renders the plot"""
        super().__call__()
        if self.add_link:            
            print("\n[[file:{}.html][{}]]".format(self.file_name, self.link_message))
        return

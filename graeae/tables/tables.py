from functools import partial

from tabulate import tabulate
import holoviews
import pandas

org_table = partial(tabulate, headers="keys", tablefmt="orgtbl",
                    showindex=False)


class CountColumns:
    index = "Value"
    count = "Count"
    percentage = "Percent (%)"


class CountPercentage:
    """A table printer for counts, and percentages

    Args:
     data: the series with values to count
     show_counts: whether to add the count column
     show_percentages: whether to add the percentage column
     decimal_places: number of decimal places to display in the table
     use_fraction: if true, don't scale percentage by 100
     number_format: string or list to format the numbers
     start: where to start the slice of the counts
     stop: end of slice (stop before this)
     drop_zeros: drop items with no count (for categorical data)
     value_label: header label for the things being counted
     kwargs: Any arguments to value_counts
    """
    def __init__(self, data: pandas.Series,
                 show_counts: bool=True,
                 show_percentages: bool=True,
                 decimal_places: int=2,
                 use_fraction: bool=False,
                 number_format: str=(",.0f", ",.0f", ",.2f"),
                 start: int=None,
                 stop: int=None,
                 value_label: str=None,
                 drop_zeros: bool=True,
                 **kwargs
    ) -> None:
        self.data = data
        self.show_counts = show_counts
        self.show_percentages = show_percentages
        self.decimal_places = decimal_places
        self.use_fraction = use_fraction
        self.number_format = number_format
        self.start = start
        self.stop = stop
        self.drop_zeros = drop_zeros
        self.value_label = value_label
        self.kwargs = kwargs
        self._counts = None
        self._total = None
        self._percentages = None
        self._table = None
        self._holoviews_table = None
        return

    @property
    def total(self) -> int:
        """Returns how many total items are in the data"""
        if self._total is None:
            self._total = self.counts.sum()
        return self._total

    @property
    def counts(self) -> pandas.Series:
        """counts of values in the data"""
        if self._counts is None:
            counts = self.data.value_counts(**self.kwargs)
            if self.drop_zeros:
                counts = counts[counts > 0]
            self._counts = counts[self.start:self.stop]
        return self._counts

    @property
    def percentages(self) -> pandas.Series:
        """Returns the fraction each value represents in the total"""
        if self._percentages is None:
            scalar = 1 if self.use_fraction else 100
            self._percentages = scalar * self.counts/self.total
        return self._percentages
    
    @property
    def table(self) -> pandas.DataFrame:
        """the data-frame to print
    
        Raises:
         ConfigurationError: None of the columns was set
        """
        if self._table is None:
            VALUE_LABEL = (self.value_label if self.value_label
                           else CountColumns.index)

            if not any((self.show_counts, self.show_percentages)):
                raise ConfigurationError("Need to set at least one thing to show")
            if self.show_counts:
                self._table = self.counts.reset_index()
                self._table.columns = [VALUE_LABEL, CountColumns.count]
            if self.show_percentages:
                percentages = self.percentages.round(self.decimal_places)
                if self._table is None:
                    self._table = percentages.reset_index()
                    self._table.columns = [VALUE_LABEL, CountColumns.percentage]
                else:
                    self._table[CountColumns.percentage] = percentages.values
        return self._table
    
    @property
    def holoviews_table(self) -> holoviews.Table:
        """converts the table to a holoviews object"""
        if self._holoviews_table is None:
            self._holoviews_table = holoviews.Table(self.table)
        return self._holoviews_table

    def __len__(self) -> int:
        """The length of the table"""
        return len(self.table)

    def __call__(self):
        """Prints the Table"""
        print(tabulate(self.table, 
                       headers="keys", 
                       showindex=False, 
                       tablefmt="orgtbl", 
                       floatfmt=self.number_format))
        return

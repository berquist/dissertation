"""make_new_015.py: take the CSV files that constituted the original
SI, and split them apart into two tables each: one for the data
points, and another for the summary. Transpose the summary table so
that it has more rows than columns.

Thanks to Python and floating-point representations, the CSV files
themselves will have some noise in places, but this will get rounded
off by the siunitx column types.
"""

import os.path

import pandas as pd

from pylatex import Document, Table
from pylatex.package import Package
from pylatex.utils import NoEscape



if __name__ == '__main__':

    filenames = (
        'jp6b09489_si_015_pople.csv',
        'jp6b09489_si_015_dunning.csv',
    )

    column_format = r'c*{8}{S[table-auto-round=true,table-format=3.2]}'
    booktabs = Package('booktabs')
    makecell = Package('makecell')
    siunitx = Package('siunitx')

    for filename in filenames:

        stub = os.path.splitext(filename)[0]

        df = pd.read_csv(filename)

        df_data = df[:30].copy()
        df_data.drop(['Unnamed: 0'], axis=1, inplace=True)
        df_data.loc[:, 'snapnum'] = df_data.loc[:, 'snapnum'].apply(int)

        df_summary = df[30:].copy()
        df_summary.drop(['snapnum', 'weight', 'sapt_basis'], axis=1, inplace=True)
        df_summary.set_index('Unnamed: 0', drop=True, inplace=True)
        df_summary = df_summary.transpose()

        df_data.to_csv(stub + '_cleaned_data.csv', index=False)
        df_summary.to_csv(stub + '_cleaned_summary.csv')

        doc_summary = Document(stub + '_cleaned_summary')
        doc_summary.packages.append(booktabs)
        doc_summary.packages.append(siunitx)
        # table = Tabular()

        df_table = df_summary.to_latex(
            escape=False,
            header=False,
            column_format=column_format,
        )
        df_table = NoEscape(df_table)

        with doc_summary.create(Table()) as table:
            table.append(df_table)
            # caption = """"""
            # caption = NoEscape(caption)
            # table.add_caption(caption)

        # save just the table source so it can be inserted into the
        # main document
        with open(stub + '_cleaned_summary_table.tex', 'w') as fh:
            fh.write(df_table)

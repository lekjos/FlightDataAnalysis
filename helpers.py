import numpy as np
import pandas as pd
from copy import copy

def print_max_str_len(df:pd.DataFrame):
    """
    Print max length of string columns in pandas dataframe
    """
    index = 0
    for col_name, col in df.iteritems():
        try:
            print(index, col_name, 'str', col.str.len().max())
        except AttributeError:
            try:
                print(index, col_name, 'int/float', max(col.map(str).apply(len)))
            except AttributeError:
                #lazy way to print col length of strings and ints
                pass
        index += 1

def make_table(headers:list, rows:list, round_cols:list=[], round_to=3):
    """
    Generates a markdown table.
    - headers: list of headers
    - rows: list of lists
    - round_cols: list of col index to round to three digits

    * all rows and headers must be same length
    """
    if len(headers) != len(rows[0]):
        raise ValueError("Title array and rows array must be same length")
    
    for row in rows:
        if len(rows[0]) != len(row):
            raise ValueError("All rows must be same length")
    str_ = ""
    max_col = dict(zip(range(len(headers)), [0 for i in headers])) #dict of max col length
    
    # Find max col len
    titles_rows = copy(rows)
    titles_rows.append(headers)
    transposed = np.array(titles_rows).T.tolist()
    for ind, x in enumerate(transposed):
        max_col[ind] = max([len(str(y)) for y in x])

    # Make table
    for row_ind, row in enumerate(rows):
        ## make header rows
        if row_ind == 0:
            str_ += "| "+" | ".join([str(x).ljust(max_col[i]) for i,x in enumerate(headers)])+ " |\n"
            str_ += "| "+" | ".join([ "-"*max_col[i] for i, z in enumerate(headers)])+ " |\n"
        str_+= "| "

        # make rows of table and round
        for col_ind, col in enumerate(row):
            if col_ind in round_cols:
                if col is not None:
                    col = round(col,round_to)
                else:
                    col = 'N/A'
            
            str_ += str(col).ljust(max_col[col_ind])
            if col_ind < len(row)-1:
                str_ += " | "

        str_+=" |\n"
        
    return str_

def row_count(f):
    """
    Counts rows in iterable or file.
    """
    for i, l in enumerate(f):
        pass
    return i 
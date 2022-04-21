
import pandas as pd

# pre-process input csv file

# Step 1 Leave Gene and column with .fna (remove B-N)
# Step 2 Use Y and N to simplify the data (None->N vice versa)
# Step 3 Sort by Gene name in ascii increasing order (a-z)

if __name__ == '__main__':
    df = pd.read_csv('./gene_presence_absence.csv')

    # print(list(df))
    # for col in list(df):
    #     print(col)

    # only interested in gene and xxx.fna, generate a list with all col end with .fna
    col_lst = [col for col in list(df) if ".fna" in str(col)]
    col_lst.insert(0, list(df)[0])

    # test
    # for col in col_lst:
    #     print(col)

    # Replace spaces with Y
    data = df.fillna(value='N')

    # Replace effective context with Y (using regex)
    data.replace('^[a-zA-Z0-9_\t]{13,}$', 'Y', inplace=True, regex=True)

    # sort data by Gene name in ascii increasing order(override data)
    data.sort_values(by='Gene', inplace=True, key=lambda col: col.str.lower())

    # produce pre-processed csv, ignore left most column
    data.to_csv('output.csv', columns=col_lst, index=False)


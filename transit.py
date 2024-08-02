import pandas as pd
import numpy as np


column_names = ['starID', 'region', 'RA', 'dec', 'bmag', 'Vmag', 'Rmag', 'Rerr', 'StartHJD', 'EndHJD', 'LCfil', 'Npts', 'LCdisp', 'LCchisq', 'N5sig', 'F5sig', 'Public', 'REFERENCE_IDs', 'ETSS_ID']
print(len(column_names))



lyr1 = pd.read_csv("transit/TrES_Lyr1.tbl", sep='\s+', names = column_names, header=None)



print(lyr1.shape)
print(lyr1.head())

lyr1 = lyr1.drop('region', axis=1)

datasets = []

for i in range(1, 2002):
    if i == 1098:
        continue
    elif len(str(i)) == 1:
        df = pd.read_csv("transit/transit-main-data/TrES_Lyr1_0000" + str(i) + "_lc.tbl", sep='\t')
    elif len(str(i)) == 2:
        df = pd.read_csv("transit/transit-main-data/TrES_Lyr1_000" + str(i) + "_lc.tbl", sep='\t')
    elif len(str(i)) == 3:
        df = pd.read_csv("transit/transit-main-data/TrES_Lyr1_00" + str(i) + "_lc.tbl", sep='\t')
    elif len(str(i)) == 4:
        df = pd.read_csv("transit/transit-main-data/TrES_Lyr1_0" + str(i) + "_lc.tbl", sep='\t')

    input_file = 'file.tbl'
    output_file = 'new_file.tbl'

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Write all lines except the first 55 to the new file
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines[55:])

    datasets.append(df)

# the data starts at line 56 in each dataset

print(len(datasets))
print(datasets[0].head(60))

# -----------------------------------------------------------------------------------------------------------------------

min_flux = []
for i in range(1,2002):
    if i < 1098:
        a = datasets[i-1]['Rmag'].min()
    elif i == 1098:
        continue
    else:
        a = datasets[i-2]['Rmag'].min()

    min_flux.append(a)

print(len(min_flux))

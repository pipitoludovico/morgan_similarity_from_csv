import pandas as pd
import numpy as np


class Read_db_2:
    def __init__(self, file):
        self.file = pd.read_csv(file, delimiter=";", chunksize=1000000, low_memory=False, error_bad_lines=False)
        self.chunks = []
        for x in self.file:
            x.replace(to_replace='None', value=np.nan, inplace=True)
            x.dropna(how="any", inplace=True)
            self.selection = x[['ChEMBL ID', 'Molecular Weight', 'HBA', 'HBD', 'Smiles']]
            self.selection['ChEMBL ID'] = self.selection['ChEMBL ID'].astype(str)
            self.selection['Smiles'] = self.selection['Smiles'].astype(str)
            self.selection.drop_duplicates()
            self.filtered = self.selection[
                (self.selection['Molecular Weight'] >= 120) & (self.selection['Molecular Weight'] <= 500) & (
                        self.selection['HBA'].astype(int) >= 2) & (self.selection['HBD'].astype(int) >= 1)]
            self.chunks.append(self.filtered)

    def get_df(self):
        return self.chunks

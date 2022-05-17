import pandas as pd


class Read_db_2:
    def __init__(self, file):
        self.file = pd.read_csv(file, delimiter=";", chunksize=100000, low_memory=False, error_bad_lines=False)
        self.chunks = []
        self.count = 0
        for x in self.file:
            x.dropna(how="any", inplace=True)
            self.selection = x[['ChEMBL ID', 'Molecular Weight', 'Polar Surface Area', 'Smiles']]
            self.selection['ChEMBL ID'] = self.selection['ChEMBL ID'].astype(str)
            self.selection['Smiles'] = self.selection['Smiles'].astype(str)
            self.filtered = self.selection[(self.selection['Molecular Weight'] <= 500)]
            self.chunks.append(self.filtered)

    def get_df(self):
        return self.chunks

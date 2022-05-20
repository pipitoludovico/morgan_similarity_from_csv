import sys

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.Chem import PandasTools


class Finder:

    def __init__(self, pattern=None, df=None, count=None):
        PandasTools.AddMoleculeColumnToFrame(df, smilesCol='Smiles')
        self.ref_smiles = pattern
        self.ref_mol = Chem.MolFromSmiles(self.ref_smiles)

        self.ECFP6 = [AllChem.GetMorganFingerprintAsBitVect(x, radius=2, nBits=1024) for x in df['ROMol']]
        self.ecfp6_name = [f'Bit_{i}' for i in range(1024)]

        # The lines below will return a dataframe with bit values for matrix comparison in ML

        # self.ref_RCFP4_fps = AllChem.GetMorganFingerprintAsBitVect(self.ref_mol, 2)
        # ecfp6_bits = [list(l) for l in self.ECFP6]
        # df_morgan = pd.DataFrame(ecfp6_bits, index=df.Smiles, columns=self.ecfp6_name)
        # print(df_morgan)

        ref_ECFP4_fps = AllChem.GetMorganFingerprintAsBitVect(self.ref_mol, 2)
        bulk_ECFP4_fps = [AllChem.GetMorganFingerprintAsBitVect(x, 2) for x in df['ROMol']]
        similarity_efcp4 = [DataStructs.FingerprintSimilarity(ref_ECFP4_fps, x) for x in bulk_ECFP4_fps]
        df['Tanimoto_Similarity (ECFP4)'] = similarity_efcp4

        df = df.sort_values(['Tanimoto_Similarity (ECFP4)'], ascending=False)
        df = df.head(20)
        # Activate the line below to display images:

        # PandasTools.FrameToGridImage(df.head(10), legendsCol="Tanimoto_Similarity (ECFP4)", molsPerRow=4)

        PandasTools.SaveXlsxFromFrame(df, f'{sys.argv[2].replace(".pdb","")}_{count}.xlsx', molCol='ROMol')

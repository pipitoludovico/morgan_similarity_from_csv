from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import AllChem

IPythonConsole.ipython_useSVG = True


class Read_fingerprint:
    def __init__(self, fingerprint):
        self.smile = None
        self.fp = Chem.MolFromPDBFile(str(fingerprint))
        self.no_H = Chem.RemoveHs(self.fp)
        AllChem.EmbedMolecule(self.no_H)
        AllChem.MMFFOptimizeMolecule(self.no_H)
        AllChem.Compute2DCoords(self.no_H)
        Draw.MolToFile(self.no_H, f"{str(fingerprint).replace('.pdb', '.png')}")
        self.smile = AllChem.MolToSmiles(self.no_H)

    def get_smile(self):
        return self.smile

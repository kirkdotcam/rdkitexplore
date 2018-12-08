from rdkit import Chem
def inchi_to_mol_file(inchi, name):
    """Converts inchi to mol, also returns mol
    
    Args:
        inchi (string): inchi to convert
        name (string): name of molecule, will be used in filename
    
    """
    
    #Read in the InChI, set the name of the molecule in memory, then create the MolBlock.
    molObj = Chem.MolFromInchi(inchi)
    molObj.SetProp("_Name",name)
    imported = Chem.MolToMolBlock(molObj)
    
    #Writes the MolBlock to a .mol file
    with open(f"../mols/{name}.mol", "w") as newfile:
        newfile.write(imported)
    
    #Also return the mol in case we want to store a variable
    return (imported)
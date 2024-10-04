# This code is created with the help of ChatGPT 
import argparse
from rdkit import Chem
from rdkit.Chem import AllChem
import os

def smiles_to_sdf(smiles_list, sdf_file):
    writer = Chem.SDWriter(sdf_file)
    for smiles in smiles_format:
        mol = Chem.MolFromSmiles(smiles.strip())
        
        if mol is not None:
            mol = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol)
            AllChem.UFFOptimizeMolecule(mol)
            writer.write(mol)
        else:
            print(f"Error: Invalid SMILES string '{smiles}'. Please provide valid input.")
    
    writer.close()
    print(f"Successfully converted SMILES to SDF file: {sdf_file}")

def read_smiles_from_file(input_file):
    with open(input_file, 'r') as f:
        smiles_format = f.readlines()
    return smiles_format

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert SMILES strings to an SDF file.")
    parser.add_argument('input', type=str, help="Input SMILES string or file containing SMILES strings to convert")
    parser.add_argument('sdf_file', type=str, help="Output SDF file name")
    args = parser.parse_args()

    # Check if the input is a file or a string
    if os.path.isfile(args.input):
        smiles_format = read_smiles_from_file(args.input)
    else:
        smiles_format = [args.input]  

    smiles_to_sdf(smiles_format, args.sdf_file)



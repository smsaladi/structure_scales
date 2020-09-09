"""

Creates coordinates in PDB format to help draw a scale/color bar

Shyam Saladi (saladi@caltech.edu)
September 2020
MIT License

"""

import argparse

# Modified from
# from https://github.com/biopython/biopython/blob/f95d94573b7f45728cbb66814bfe2cad3e7f0e2e/Bio/PDB/PDBIO.py#L16
_ATOM_FORMAT_STRING = (
    "%-6.6s%5i %-4s%1.1s%3s %1.1s%4i%1.1s   %8.3f%8.3f%8.3f%6.2f%6.2f      %-4s%2s%2s"
)

header_text = \
"""REMARK A scalebar for structure visualization
REMARK Shyam Saladi (saladi@caltech.edu)
REMARK September 2020
REMARK LICENSE CC0
REMARK github.com/smsaladi/structure_scales"""


def make_scalebar_pdb(length, count, atom_name='CA', res_name='DUM'):
    """Prints out coodinates that correspond to desired scalebar 
    """

    for i in range(count):
        record_type = 'ATOM'
        atom_number = i + 1
        name = atom_name
        altloc = ""

        resname = res_name
        chain_id = 'A'

        # increment residue every 10 atoms, as well
        resseq = i // 10 + 1
        icode = ""

        x = i / (count - 1) * length
        y = z = 0

        occupancy = i / (count - 1)
        bfactor = occupancy * 100
        segid = 'A'
        element = atom_name[0]
        charge = ''
        
        line = _ATOM_FORMAT_STRING % (
            record_type,
            atom_number,
            name,
            altloc,
            resname,
            chain_id,
            resseq,
            icode,
            x,
            y,
            z,
            occupancy,
            bfactor,
            segid,
            element,
            charge,
        )
        print(line)

    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('length_in_angstroms', type=int)
    parser.add_argument('-n', default=1000, type=int)
    args = parser.parse_args()

    print(header_text)
    make_scalebar_pdb(args.length_in_angstroms, args.n)

    return

if __name__ == '__main__':
    main()

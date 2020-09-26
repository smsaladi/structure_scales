[![DOI](https://data.caltech.edu/badge/294240937.svg)](https://data.caltech.edu/badge/latestdoi/294240937)


structure_scales
================

Structures need scales bars. This repository has a set of PDB files
to be visualized along side a structure of interest to serve as a scale
bar.

The PDB filename indicates the total length in Ångstroms of the scalebar
and contains 5000 atoms equally spaced in the x-direction (starting at the
origin). Every 10 atoms form a residue. B-factors are set to between 0 and 100,
and occupancy between 0 and 1, so the scalebar can double as a colorbar as well.

All atoms are of atom type `CA` of residue `DUM` and assigned
chain A and segment A.

To help spread scale and colorbars in the community, PDB files are licensed as
[CC0](https://wiki.creativecommons.org/wiki/CC0) and can be cited as Caltech Data DOI.

### Sample

First 10 atoms of `scale_100.pdb`

```text
ATOM      1 CA   DUM A   1       0.000   0.000   0.000  0.00  0.00      A    C
ATOM      2 CA   DUM A   1       0.100   0.000   0.000  0.00  0.10      A    C
ATOM      3 CA   DUM A   1       0.200   0.000   0.000  0.00  0.20      A    C
ATOM      4 CA   DUM A   1       0.300   0.000   0.000  0.00  0.30      A    C
ATOM      5 CA   DUM A   1       0.400   0.000   0.000  0.00  0.40      A    C
ATOM      6 CA   DUM A   1       0.501   0.000   0.000  0.01  0.50      A    C
ATOM      7 CA   DUM A   1       0.601   0.000   0.000  0.01  0.60      A    C
ATOM      8 CA   DUM A   1       0.701   0.000   0.000  0.01  0.70      A    C
ATOM      9 CA   DUM A   1       0.801   0.000   0.000  0.01  0.80      A    C
ATOM     10 CA   DUM A   1       0.901   0.000   0.000  0.01  0.90      A    C
```

### Usage

Using coordinates to specify a scalebar should be convenient.
After being loaded, the scalebar can be manipulated as any other structure object.
Where values are mapped to colors
(e.g. flexibility with b-factors, N- to C-terminus by residue number),
the color is readily assigned to the scale bar, making it a color bar, too.

As always, after rendering the view, if you want/need the scalebar as a vector
graphic in your final figure, you can use the rendered version as a guide to
accurately draw it as a box with color gradient fill in
Illustrator, Inkscape, or the like.


### Alternative approaches

For those interested, here are software-specific approches to creating
scale and color bars:

* PyMOL: [`Spectrumbar`](https://pymolwiki.org/index.php/Spectrumbar)
which uses the [Compiled graphics objects (CGO)](https://pymolwiki.org/index.php/Category:CGO)
interface and written by Sean Law
* ChimeraX: A [suggestion](http://www.rbvi.ucsf.edu/pipermail/chimerax-users/2018-December/000341.html)
from Elaine Meng that uses ChimeraX's [BILD](http://rbvi.ucsf.edu/chimerax/docs/user/formats/bild.html)
format for specifying 2d and 3d geometric objects
* Chimera: [scalebar](http://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/scalebar/scalebar.html)
and [colorkey](http://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/2dlabels/2dlabels.html#colorkey)
* VMD: [color_scale_bar.tcl](https://www.ks.uiuc.edu/Research/vmd/mailing_list/vmd-l/att-4608/color_scale_bar_new.tcl)
written by Wuwei Liang and later modified by Dan Wright


### Remaking the scale bars

For reference, code to generate the provided PDB files is provided.
Here's how we did it:

```shell
python create_scalebar.py 10 > scale_10.pdb
python create_scalebar.py 100 > scale_100.pdb
python create_scalebar.py 1000 > scale_1000.pdb
python create_scalebar.py 10000 > scale_10000.pdb
python create_scalebar.py 25 > scale_25.pdb
python create_scalebar.py 250 > scale_250.pdb
python create_scalebar.py 2500 > scale_2500.pdb
python create_scalebar.py 25000 > scale_25000.pdb
python create_scalebar.py 50 > scale_50.pdb
python create_scalebar.py 500 > scale_500.pdb
python create_scalebar.py 5000 > scale_5000.pdb
python create_scalebar.py 50000 > scale_50000.pdb
```


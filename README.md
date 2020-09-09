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

PDB files are licensed as CC0 (no attribution necessary), although we'd appreciate
a citation in academic work to help spread scale & colorbars in the community.

### Sample

```bash

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

* PyMOL: [`Spectrumbar`][https://pymolwiki.org/index.php/Spectrumbar]
which uses the [Compiled graphics objects (CGO)] interface (written by Sean Law)
* ChimeraX: A [suggestion](http://www.rbvi.ucsf.edu/pipermail/chimerax-users/2018-December/000341.html) from Elaine Meng that uses ChimeraX's BILD format for
specifying 2d and 3d geometric objects
* Chimera: [scalebar](http://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/scalebar/scalebar.html) and [colorkey](http://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/2dlabels/2dlabels.html#colorkey)
* VMD: [color_scale_bar.tcl](https://www.ks.uiuc.edu/Research/vmd/mailing_list/vmd-l/att-4608/color_scale_bar_new.tcl) written by Wuwei Liang and later modified by Dan Wright


### Remaking the scale bars

For reference, code to generate the provided PDB files is provided.
Here's how we did it:

```shell
python create_scalebar.py 100 > scale_100.pdb
python create_scalebar.py 1000 > scale_1000.pdb
python create_scalebar.py 10000 > scale_10000.pdb
python create_scalebar.py 250 > scale_250.pdb
python create_scalebar.py 2500 > scale_2500.pdb
python create_scalebar.py 25000 > scale_25000.pdb
python create_scalebar.py 500 > scale_500.pdb
python create_scalebar.py 5000 > scale_5000.pdb
python create_scalebar.py 50000 > scale_50000.pdb
```


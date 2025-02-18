# Cross-Correlation Function (CCF) Computation

This project contains a Python script `ccf_s1d.py` that computes the cross-correlation function (CCF) for a given spectrum and mask. The script uses various libraries such as `astropy`, `numpy`, `scipy`, and `argparse`.

This code expects APERO s1d (either 'v' or 'w' format) files as inputs and a mask as defined inside the LBL architecture or taken from APERO outputs.

Note that if you call the code from another Python code, you can define your own bandpasses.

## Installation

There's no proper installation script yet (we're working on that). You download the Python script and call it from wherever you want to store it. If you are 100% lazy, you can just run the following command on a Linux station:

```wget -O ccf_s1d.py https://github.com/eartigau/ccf_demo/raw/refs/heads/main/ccf_s1d.py```

## Masks
Two representative masks can be downloaded in this [online mask repository](https://www.astro.umontreal.ca/~artigau/masks/)

## Requirements

- Python 3.x
- astropy
- numpy
- scipy

You can install the required packages using pip:

```sh
pip install astropy numpy scipy
```

## Usage

To run the script, use the following command:

```sh
python ccf_s1d.py <spectrum_file(s)> <mask_file> [--velorange VELO_RANGE] [--velostep VELO_STEP] [--outdir OUTPUT_DIR]
```

### Arguments

- `<spectrum_file(s)>`: Path(s) to the input spectrum file(s).
- `<mask_file>`: Path to the mask file.
- `--velorange VELO_RANGE`: Velocity range for the CCF (default: 100).
- `--velostep VELO_STEP`: Velocity step for the CCF (default: 1).
- `--outdir OUTPUT_DIR`: Output directory for the CCF file (default: subfolder in input file directory called `ccf/`).

### Example

```sh
python ccf_s1d.py data/???????o_pp_s1d_v_tcorr_AB.fits mask/WASP52_neg.fits --velorange 200 --velostep 0.5 --outdir ./my_ccfs
```

This command will compute the CCF for files in the data folder and follow the SPIRou odometer definition for s1d_v and we use a mask file that was constructed from observation of WASP52, with a velocity range of 200 km/s and a velocity step of 0.5 km/s. The output will be saved in the `./output` directory.

### Output

Outputs are fits tables with a CCF per bandpass. There is one fits table per input file and the original header is preserved as much as possible. The CCF is expressed subtracted from the BERV contribution (i.e., in the Solar System and not Earth rest frame).


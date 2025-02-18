# Cross-Correlation Function (CCF) Computation

This project contains a Python script `ccf_s1d.py` that computes the cross-correlation function (CCF) for a given spectrum and mask. The script uses various libraries such as `astropy`, `numpy`, `scipy`, and `argparse`.

This code expects APERO s1d (either 'v' or 'w' format) files as inputs and a mask as defined inside the LBL architecture or taken from APERO outputs.

Note that if you call the code from another Python code, you can define your own bandpasses.

## Installation

There's no proper installation script yet (we're working on that). You download the Python script and put it in the science folder of your LBL installation. If you are 100% lazy, you can just run the following command on a Linux station:

```wget -O ccf_s1d.py https://github.com/eartigau/ccf_demo/raw/refs/heads/main/ccf_s1d.py```

## Masks
Two representative masks can be downloaded in this [sample directory](https://www.astro.umontreal.ca/~artigau/masks/))

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
python ccf_s1d.py spectrum.fits mask.fits --velorange 200 --velostep 0.5 --outdir ./output
```

This command will compute the CCF for `spectrum.fits` using `mask.fits`, with a velocity range of 200 km/s and a velocity step of 0.5 km/s. The output will be saved in the `./output` directory.

## Functions

### `roll_frac(input_map, dv)`

Rolls an array by a fraction of an element.

### `gauss(v, mu, fwhm, depth)`

Generates a Gaussian profile.

### `doppler(wave, velocity)`

Applies relativistic Doppler shift to a wavelength array.

### `compute_ccf(file, mask, bands=None, velorange=100, velostep=1, outdir=None)`

Computes the cross-correlation function (CCF) for a given spectrum and mask.


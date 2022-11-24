# Batch PNG overlays

A rapid batch-overlay system for computer-generated CCG cards.

## Overview

Simply place your card images in the `input` directory and the transparent overlay images in the `overlays` directory, and run `batch_CG_CCG_overlay.py`. The script will automatically overlay the card images with each overlay, and save the output in the `output` directory.

## Requirements

The cards and overlays must be PNG images. The script probably only requires Python 3.7 or later, but was built using 3.10. It also requires the `alive-progress` and the `Pillow` libraries.

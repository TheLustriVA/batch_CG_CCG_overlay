from PIL import Image
import os
from alive_progress import alive_bar

overlay_dir = "Overlays/"
input_dir = "Inputs/"
output_dir = "Outputs/"

# Write a function that takes each overlay in overlay_dir and overlays it over each file in input_dir, then saves those files in a directory under output_dir according to the overlay file used.
def batch_overlay(overlay_dir, input_dir, output_dir):
    # Get a list of all the overlay files in the overlay_dir
    overlay_files = os.listdir(overlay_dir)
    # Get a list of all the input files in the input_dir
    input_files = os.listdir(input_dir)
    # For each overlay file in the overlay_dir
    for overlay in overlay_files:
        # Create a directory in the output_dir for the overlay file
        os.mkdir(output_dir + overlay)
        # For each input file in the input_dir
        with alive_bar(len(input_files), dual_line=True, title="Overlaying " + overlay) as bar:
            for input_file in input_files:
                # Open the input file
                input_image = Image.open(input_dir + input_file)
                # Open the overlay file
                overlay_image = Image.open(overlay_dir + overlay)
                # Overlay the overlay file over the input file
                bar.text = f"--> Overlaying {overlay} over {input_file}, please wait..."
                input_image.paste(overlay_image, (0, 0), overlay_image)
                # Save the overlayed image in the output_dir under the overlay file directory
                input_image.save(output_dir + overlay + "/" + input_file)
                bar()

if __name__ == "__main__":
    batch_overlay(overlay_dir, input_dir, output_dir)

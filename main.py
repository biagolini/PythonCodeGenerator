import qrcode
import os
import json

# Define the output directory
output_dir = "output"

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the JSON file containing the QR code data
json_filename = "links.json"

# Load the JSON data from the file
if not os.path.exists(json_filename):
    print(f"Error: {json_filename} not found.")
    exit(1)

with open(json_filename, "r") as json_file:
    qr_data = json.load(json_file)

# Generate QR codes for each entry in the JSON data
for filename, link in qr_data.items():
    qr = qrcode.make(link)
    output_path = os.path.join(output_dir, f"{filename}.png")
    qr.save(output_path)
    print(f"QR Code saved: {output_path}")

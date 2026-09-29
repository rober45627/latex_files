import os
import shutil


src_dir = r"C:\Users\robro\Vault\LaTeX"
dest_dir = r"C:\Users\robro\Vault\Maths"

# Map first-part of filename to custom string
folder_strings = {
    "001": "Other",
    "101": "Linear Algebra",
    "102": "Mechanics",
    "111": "Single Variable Calculus",
    "112": "Introduction to Programming",
    "113": "Introduction to Probability"
    # Add more mappings as needed
}

# Find all PDFs in the source folder
pdfs = [f for f in os.listdir(src_dir) if f.endswith(".pdf")]

if not pdfs:
    print("No PDFs found in source folder")
    exit()

# Pick the most recently modified PDF
latest = max(pdfs, key=lambda f: os.path.getmtime(os.path.join(src_dir, f)))
fname = os.path.splitext(latest)[0]   # "101-01-1609"
parts = fname.split("-")              # ["101", "01", "1609"]

if len(parts) < 4:
    first_part = parts[0]
    custom_str = folder_strings.get(first_part, "")
    subfolder_name = f"{first_part} - {custom_str}" if custom_str else first_part
    subfolder = os.path.join(dest_dir, subfolder_name)
else:
    # Build the subfolder path using mapping
    first_part = parts[0]
    custom_str = folder_strings.get(first_part, "")
    subfolder_name = f"{first_part} - {custom_str}" if custom_str else first_part
    subfolder = os.path.join(dest_dir, subfolder_name, parts[1])

# Make sure the folder exists
os.makedirs(subfolder, exist_ok=True)

# Ask user for new filename
new_name = input(f"Enter new filename for {latest}: ").strip()
if not new_name:
    new_name = latest  # keep original if empty

dst = os.path.join(subfolder, new_name + ".pdf")
src = os.path.join(src_dir, latest)

# Copy the file
shutil.copy2(src, dst)
print("---")
print(f"Copied → {dst}")


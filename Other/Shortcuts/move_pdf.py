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
    "113": "Introduction to Probability",
    "121": "Analysis on the Real Line",
    "122": "Advanced Calculus",
    "123": "Introduction to Computation Theory and Logic",
    "124": "Introduction to Statistics"

    # Add more mappings as needed
}
subfolder_strings = {
    "01": "Notes",
    "02": "Work",
    "03": "Other",
    "04": "Questions"
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
    subfolder_name = folder_strings.get(first_part, "")
    subfolder = os.path.join(dest_dir, subfolder_name)
else:
    # Build the subfolder path using mapping
    first_part = parts[0]
    second_part = parts[1]
    subfolder_name = folder_strings.get(first_part, "")
    subsubfolder_name = subfolder_strings.get(second_part, "")
    subfolder = os.path.join(dest_dir, subfolder_name, subsubfolder_name)

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


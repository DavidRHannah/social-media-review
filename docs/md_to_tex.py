#!/usr/bin/env python3
import os
import subprocess
import shutil
import argparse
import sys

def check_pdflatex():
    if shutil.which("pdflatex") is None:
        print("Error: 'pdflatex' was not found in your PATH. Please ensure you have a LaTeX distribution (e.g., MiKTeX or TeX Live) installed and that 'pdflatex' is accessible from the command line.")
        sys.exit(1)

def compile_tex_files(source_folder, pdf_folder):
    # Check if pdflatex is available
    check_pdflatex()
    
    # Create the destination folder for PDFs if it doesn't exist
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"Created folder: {pdf_folder}")
    
    # Iterate over all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.tex'):
            tex_path = os.path.join(source_folder, filename)
            print(f"\nCompiling {tex_path} ...")
            
            # Run pdflatex in nonstopmode to compile the tex file.
            cmd = ['pdflatex', '-interaction=nonstopmode', filename]
            process = subprocess.run(cmd, cwd=source_folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if process.returncode != 0:
                print(f"Error compiling {filename}:")
                print(process.stdout.decode())
                print(process.stderr.decode())
                continue

            # Construct the PDF filename (assuming pdflatex outputs to the same folder)
            pdf_filename = filename.rsplit('.', 1)[0] + '.pdf'
            pdf_path = os.path.join(source_folder, pdf_filename)
            
            if os.path.exists(pdf_path):
                # Move the PDF to the destination folder
                destination_pdf = os.path.join(pdf_folder, pdf_filename)
                shutil.move(pdf_path, destination_pdf)
                print(f"Moved {pdf_filename} to {pdf_folder}")
            else:
                print(f"PDF not generated for {filename}")

            # Optionally, remove auxiliary files (e.g., .aux and .log) generated during compilation
            for ext in ['aux', 'log']:
                aux_file = filename.rsplit('.', 1)[0] + f'.{ext}'
                aux_path = os.path.join(source_folder, aux_file)
                if os.path.exists(aux_path):
                    os.remove(aux_path)
                    print(f"Removed {aux_file}")

def main():
    parser = argparse.ArgumentParser(
        description="Compile all .tex files in a folder and move the generated PDFs to a designated folder."
    )
    parser.add_argument("source_folder", help="Path to the folder containing .tex files")
    parser.add_argument("--pdf_folder", default="pdfs", help="Folder to place the generated PDFs (default: 'pdfs')")
    args = parser.parse_args()
    
    compile_tex_files(args.source_folder, args.pdf_folder)

if __name__ == "__main__":
    main()

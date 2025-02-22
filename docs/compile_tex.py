#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import shutil

def find_pdflatex():
    """Check if pdflatex is in the PATH; exit if not found."""
    pdflatex_path = shutil.which("pdflatex")
    if pdflatex_path is None:
        sys.exit("Error: 'pdflatex' not found in your PATH. Please install a LaTeX distribution (e.g., MiKTeX or TeX Live).")
    return pdflatex_path

def compile_tex_file(pdflatex_path, tex_file, working_dir):
    """
    Compile a single .tex file by running pdflatex twice.
    Returns a tuple (succeeded, output), where succeeded is True if both runs
    returned 0, and output is the combined stdout and stderr for logging.
    """
    command = [pdflatex_path, "-interaction=nonstopmode", tex_file]
    combined_output = ""
    succeeded = True
    for i in range(2):
        result = subprocess.run(
            command,
            cwd=working_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        combined_output += f"Pass {i+1} output:\n{result.stdout}\n{result.stderr}\n"
        if result.returncode != 0:
            succeeded = False
            print(f"Error compiling {tex_file} (pass {i+1}):")
            print(result.stdout)
            print(result.stderr)
    return succeeded, combined_output

def compile_all_tex(source_dir, pdf_dir):
    """Compile all .tex files in source_dir and move resulting PDFs to pdf_dir."""
    pdflatex_path = find_pdflatex()

    # Ensure the destination folder exists
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Process each .tex file in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".tex"):
            tex_file = filename
            print(f"\nCompiling {tex_file} ...")
            succeeded, log_output = compile_tex_file(pdflatex_path, tex_file, source_dir)
            
            # Construct the expected PDF filename
            pdf_filename = os.path.splitext(filename)[0] + ".pdf"
            src_pdf_path = os.path.join(source_dir, pdf_filename)
            
            # Attempt to move the PDF if it exists, even if compilation wasn't perfect.
            if os.path.exists(src_pdf_path):
                destination_pdf = os.path.join(pdf_dir, pdf_filename)
                try:
                    shutil.move(src_pdf_path, destination_pdf)
                    print(f"Moved {pdf_filename} to {pdf_dir}")
                except Exception as e:
                    print(f"Failed to move {pdf_filename} to {pdf_dir}: {e}")
            else:
                print(f"PDF not generated for {tex_file}")
            
            # Optionally, remove auxiliary files (e.g., .aux, .log, .out, .toc)
            for ext in ['aux', 'log', 'out', 'toc']:
                aux_file = os.path.splitext(filename)[0] + f".{ext}"
                aux_path = os.path.join(source_dir, aux_file)
                if os.path.exists(aux_path):
                    try:
                        os.remove(aux_path)
                        print(f"Removed {aux_file}")
                    except Exception as e:
                        print(f"Failed to remove {aux_file}: {e}")
            
            if not succeeded:
                print(f"Note: Compilation of {tex_file} reported errors. Please check the log above for details.")

def main():
    parser = argparse.ArgumentParser(
        description="Compile all .tex files in a folder and move the generated PDFs to a specified folder."
    )
    parser.add_argument("source", help="Path to the folder containing .tex files")
    parser.add_argument("--pdf_folder", default="pdfs", help="Folder to store the compiled PDFs (default: 'pdfs')")
    args = parser.parse_args()
    
    source_dir = os.path.abspath(args.source)
    pdf_dir = os.path.abspath(args.pdf_folder)
    
    print(f"Source directory: {source_dir}")
    print(f"PDF directory: {pdf_dir}")
    
    compile_all_tex(source_dir, pdf_dir)

if __name__ == "__main__":
    main()

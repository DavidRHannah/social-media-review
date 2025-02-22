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
    Returns True if compilation succeeds, False otherwise.
    """
    command = [pdflatex_path, "-interaction=nonstopmode", tex_file]
    for i in range(2):
        result = subprocess.run(
            command,
            cwd=working_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print(f"Error compiling {tex_file} (pass {i+1}):")
            print(result.stdout)
            print(result.stderr)
            return False
    return True

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
            if compile_tex_file(pdflatex_path, tex_file, source_dir):
                # Construct the expected PDF filename
                pdf_filename = os.path.splitext(filename)[0] + ".pdf"
                src_pdf_path = os.path.join(source_dir, pdf_filename)
                if os.path.exists(src_pdf_path):
                    dst_pdf_path = os.path.join(pdf_dir, pdf_filename)
                    shutil.move(src_pdf_path, dst_pdf_path)
                    print(f"Moved {pdf_filename} to {pdf_dir}")
                else:
                    print(f"PDF not generated for {tex_file}")
                
                # Optionally remove auxiliary files generated during compilation
                for ext in ['aux', 'log', 'out', 'toc']:
                    aux_filename = os.path.splitext(filename)[0] + f".{ext}"
                    aux_path = os.path.join(source_dir, aux_filename)
                    if os.path.exists(aux_path):
                        os.remove(aux_path)
                        print(f"Removed {aux_filename}")
            else:
                print(f"Compilation failed for {tex_file}")

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

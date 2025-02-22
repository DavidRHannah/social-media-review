

# Documentation Processing Tools

This repository contains two Python tools that help you convert Markdown documentation to LaTeX and then compile those LaTeX documents into PDFs.

- **md_to_tex.py**  
  Converts a Markdown file into a LaTeX document by:
  - Converting Markdown content to LaTeX via [pypandoc](https://pypi.org/project/pypandoc/).
  - Prepending a custom LaTeX template (which includes document settings, title, table of contents, etc.).
  - Preprocessing headings so that any line starting with `###` is converted into a LaTeX section.

- **compile_tex.py**  
  Scans a specified folder for `.tex` files, compiles each one using `pdflatex`, and moves the resulting PDF files into a designated folder. It runs `pdflatex` twice for better cross-referencing and cleans up auxiliary files afterward.

---

## Prerequisites

Before using these tools, make sure you have the following installed on your system:

1. **Python 3**  
   Download and install from [python.org](https://www.python.org/downloads/).

2. **Pandoc and pypandoc**  
   Install Pandoc from [pandoc.org](https://pandoc.org/installing.html) and the Python wrapper via:
   ```bash
   py -m pip install pypandoc
   ```

3. **A LaTeX Distribution (with pdflatex)**  
   Install a LaTeX distribution such as [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/).  
   Verify that `pdflatex` is available from the command line:
   ```bash
   pdflatex --version
   ```
   If `pdflatex` is not found, ensure the installation directory is in your PATH.

---

## Installation

1. **Clone or Download the Repository**  
   Clone this repository or download the scripts (`md_to_tex.py` and `compile_tex.py`) into your working directory.

2. **Install Python Dependencies**  
   Use the Python launcher (e.g., `py` on Windows) to install the required packages:
   ```bash
   py -m pip install pypandoc
   ```
   (Note: Do not confuse the `pdflatex` Python package with the actual LaTeX compiler.)

---

## Usage

### 1. Converting Markdown to LaTeX with `md_to_tex.py`

This tool converts a Markdown file into a LaTeX document that includes your custom LaTeX template.

**Command Format:**
```bash
py md_to_tex.py path/to/input.md path/to/output.tex
```

**Example:**
If your Markdown file is located at `docs/example.md` and you want the LaTeX output at `docs/example.tex`, run:
```bash
py md_to_tex.py docs/example.md docs/example.tex
```

**How It Works:**
- The script reads the input Markdown file.
- It processes any headings prefixed with `###` to be converted into top-level LaTeX sections.
- It converts the Markdown content to LaTeX using pypandoc.
- A custom LaTeX template is prepended (including settings for margins, headers, title, etc.).
- The final LaTeX document is saved to the specified output file.

### 2. Compiling LaTeX to PDF with `compile_tex.py`

This tool compiles all `.tex` files in a specified folder and moves the resulting PDF files to a designated folder.

**Command Format:**
```bash
py compile_tex.py path/to/tex_files_folder --pdf_folder path/to/pdf_output_folder
```

**Example:**
To compile all LaTeX files in `./implementation_plans/latex/` and move the PDFs to `./implementation_plans/pdfs/`, run:
```bash
py compile_tex.py "./implementation_plans/latex/" --pdf_folder "./implementation_plans/pdfs/"
```

**How It Works:**
- The script checks if `pdflatex` is available in your PATH.
- It iterates over each `.tex` file in the specified source folder.
- It runs `pdflatex` (twice for improved cross-referencing) on each file.
- The generated PDF is moved to the specified PDF folder.
- It cleans up auxiliary files (such as `.aux`, `.log`, etc.) generated during compilation.

---

## Troubleshooting

- **pdflatex Not Found:**  
  If you see an error that `pdflatex` is not found, ensure that a full LaTeX distribution (MiKTeX or TeX Live) is installed and that its bin directory is added to your PATH.

- **Compilation Errors:**  
  If a LaTeX file fails to compile, check the output log for error messages. You can compile the file manually using:
  ```bash
  pdflatex -interaction=nonstopmode yourfile.tex
  ```
  This may help identify missing packages or syntax errors in the LaTeX source.

- **Environment Setup:**  
  Make sure to use the appropriate Python interpreter (e.g., via the `py` launcher on Windows) to ensure that dependencies are installed in the correct environment.

---
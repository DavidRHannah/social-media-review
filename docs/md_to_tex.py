#!/usr/bin/env python3
import argparse
import pypandoc
import re
import sys

def convert_md_to_tex(input_file, output_file):
    # Read the Markdown content from the input file
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()
    except IOError as e:
        print(f"Error reading {input_file}: {e}")
        sys.exit(1)
    
    # Replace markdown headings: convert "### " to "# " so that Pandoc treats them as sections.
    markdown_text = re.sub(r'^###\s+', '# ', markdown_text, flags=re.MULTILINE)
    
    # Convert Markdown to LaTeX using pypandoc
    try:
        # We convert without the standalone wrapper to get just the document body.
        latex_body = pypandoc.convert_text(markdown_text, 'latex', format='md')
    except Exception as e:
        print(f"Error converting Markdown to LaTeX: {e}")
        sys.exit(1)
    
    # Custom LaTeX template preamble
    template = r"""\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{parskip}
\usepackage{sectsty}

\allsectionsfont{\sffamily}
\pagestyle{fancy}
\fancyhf{}
\lhead{MediaReview Social: Tools and Frameworks}
\rhead{\today}
\cfoot{\thepage}

\title{Title for Media Review}
\author{Your Company Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
"""

    # Combine the template with the converted LaTeX body and add \end{document} at the end
    final_latex = template + "\n" + latex_body + "\n\\end{document}\n"
    
    # Write the final LaTeX output to the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as tex_file:
            tex_file.write(final_latex)
    except IOError as e:
        print(f"Error writing {output_file}: {e}")
        sys.exit(1)
    
    print(f"Conversion complete. LaTeX file saved as {output_file}.")

def main():
    parser = argparse.ArgumentParser(
        description='Convert a Markdown file to a LaTeX (.tex) file using pypandoc and a custom template, converting "###" headers into LaTeX sections.'
    )
    parser.add_argument('input', help='Path to the input Markdown file.')
    parser.add_argument('output', help='Path to the output LaTeX file.')
    
    args = parser.parse_args()
    convert_md_to_tex(args.input, args.output)

if __name__ == "__main__":
    main()

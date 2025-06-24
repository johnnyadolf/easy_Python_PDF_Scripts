# easyPDFpageSplitterScript

A simple set of Python scripts for splitting PDF files into single pages and merging PDF files (all pages or 2-by-2) using [PyPDF2](https://pypdf2.readthedocs.io/).

## Features

- **Split PDFs:** Automatically split every PDF in a folder into single-page PDFs.
- **Merge PDFs:** Merge all pages from multiple PDFs into a single PDF, or merge pages 2-by-2 into separate files.
- **Cross-platform:** Works on Windows, macOS, and Linux (Python required).
- **Executable:** Easily create standalone executables using PyInstaller.

## Tech Stack

- **Python 3**
- **[PyPDF2](https://pypdf2.readthedocs.io/)**
- **[PyInstaller](https://pyinstaller.org/)** (for creating executables)

## How to Use

### 1. Install Dependencies

```sh
pip install PyPDF2 pyinstaller
```

### 2. Split PDFs

1. Place your PDF files in the `Spliting files` folder.
2. Run the script:

   ```sh
   python PDF_splitter_script.py
   ```

   Each PDF will be split into single-page PDFs in the same folder.

### 3. Merge PDFs

1. Place your PDF files in the `Merging files 2 by 2` folder.
2. Run the script:

   ```sh
   python PDF_merger_script.py
   ```

   - By default, all pages from all PDFs will be merged into `merged.pdf`.
   - (Optional) To merge 2-by-2, uncomment the relevant section in the script.

### 4. Create Executables (Optional)

To create a standalone executable:

```sh
cd path\to\your\script
pyinstaller --onefile PDF_splitter_script.py
pyinstaller --onefile PDF_merger_script.py
```

The executable will be in the `dist` folder.

## Folder Structure

```
QS/
├── Merging files 2 by 2/
│   ├── PDF_merger_script.py
│   └── ...
├── Spliting files/
│   ├── PDF_splitter_script.py
│   └── ...
└── README.md
```
#!/usr/bin/env python3
from pathlib import Path
import nbformat as nbf

# Choose order explicitly
NOTEBOOKS = [
    "Notebooks/index.ipynb",
    "Notebooks/variant-calling.ipynb",
    "Notebooks/filtering.ipynb",
    "Notebooks/multi-sample-calling.ipynb",
    "Notebooks/visualisation.ipynb",
    "Notebooks/annotation.ipynb",
]

out = Path("Notebooks/merged.ipynb")

first = nbf.read(NOTEBOOKS[0], as_version=4)
merged = nbf.v4.new_notebook()
merged.metadata = first.metadata  # keep kernelspec, language, etc.

for p in NOTEBOOKS:
    nb = nbf.read(p, as_version=4)

    # Optional: add a "chapter" heading between notebooks
    #title = Path(p).stem.replace("-", " ").title()

    merged.cells.extend(nb.cells)

nbf.write(merged, out)
print(f"Wrote {out}")

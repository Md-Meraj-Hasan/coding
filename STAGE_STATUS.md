# Stage status

- Baseline Chaquopy diagnostic: confirmed Python 3.10.22 arm64.
- `tkinter` import: FAIL (`ModuleNotFoundError`).
- `_tkinter` import: FAIL (`ModuleNotFoundError`).
- Tcl/Tk shared libraries in uploaded Jupyter APK: not found by archive inspection.
- This package: isolated GitHub Actions build probe for the official Android Tcl/Tk port.
- Not yet done: a compatible `_tkinter` extension linked to Chaquopy's CPython 3.10 and integration into the Jupyter app.

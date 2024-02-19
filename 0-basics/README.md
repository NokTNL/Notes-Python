## Installation & Start (Using Anaconda, Miniconda & alike)

- Anaconda includes Python, Jupyter notebook and a lot of useful Python libraries. However, you probably do not need Anaconda, as it is very bloated.
- Go to the Anaconda/miniconda offical site to download the installer
  - Note for Raspberry Pi:
    - None of the installers on the site will work, even if you choose the ARM installer. You can use `miniforge` instead, and choose the `aarch64 (arm64)` version: https://github.com/conda-forge/miniforge (**DO NOT** choose the `pypy` one). See https://www.youtube.com/watch?v=fYPr43YhTMM for full instruction (just use miniforge instead of mambaforge).
    - Run `bash Miniforge3-Linux-aarch64.sh`. Choose `yes` for automatic startup.
    - Open a new terminal tab, or run `source .bashrc` if you do not want to open a new one. **You should see `(base)` appears at the start of the current line**
    - Run `mamba update mamba` to update mamba, then `mamba update --all` to update the packages. (Note: mamba is the free-for-commerical alternative for conda and is much faster)
    - Run `mamba install <package-name>` to additionally install whatever global packages you want

## Installation & Start (minimal, using CLI)

- Installation: just go to the official website

- To run:
  - Intercative mode: just type `python3` in command line
    - To quit: `quit()` or Ctrl + D
  - Run in script mode:
    - You can do this easily VS Code, just press the "Play" button in VS Code when in the `.py` file.
    - Or, just run `python3 <filename>` to run the file

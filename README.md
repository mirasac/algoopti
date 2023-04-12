# algoopti
## Introduction
This repository contains source code and material (e.g. notes) about problems faced during the course [Algorithms for optimization, inference and learning](https://fisica-sc.campusnet.unito.it/do/corsi.pl/Show?_id=a763), attended during the second semester of academic year 2022-2023 for the master's degree in Physics of Complex Systems at University of Torino.

The regular teacher of this course is Professor Braunstein. The course and [its official web site](https://didattica.polito.it/pls/portal30/gap.pkg_guide.viewGap?p_cod_ins=01SPOPF&p_a_acc=2223&p_header=S&p_lang=EN) are hosted at Politecnico di Torino.

### Disclaimer
This repository exists just as an effective way to save the code while the exercises are being done, it is not meant for presenting them in a complete and nice way. Just information sufficient for the resolution of the problems are included.

## Repository structure
Files related to a particular problem are contained in a directory with name `Problem_n` where n is the number corresponding to the problem at the time of creation of the directory. This numbering comes from the problem list on professor's LaTeX notes, so it could go out of sync with the real numbering on the notes at any time. To provide consistency, the following list associates numbers to problems permanently and it is updated each time a new problem is inserted in the repository:

- 3 Sierpinski’s triangle
- 11 Recursive subsets
- 28 Linear max-convolutions
- 35 Making a difference

## Programming environment
During lesson code is written in Julia, but in this repository both Python and Julia are present (since I am new to Julia language).

I use Python version 3.10.4 and Julia [LTS release](https://julialang.org/downloads/#long_term_support_release) version 1.6.7.

### Local 
VS Code is my visual text editor equipped with [Jupyter notebook extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

### Cloud
I can use Google Colab to use Julia notebooks stored in this repository. The trick is the language-specific metadata of the notebooks loaded in Google Colab, hence it is fundamental to use specific template notebooks and not notebooks created directly on Google Colab. In this repository the bare minimum data for a notebook to be identified as Julia notebook are stored in file `bare_julia.ipynb`.

- __To load an existing notebook__ the procedure is:

    1. log into [Google Colab](https://colab.research.google.com/);
    2. choose to open notebook from GitHub;
    3. select the notebook to open from branch `main`;
    4. once the notebook is loaded, run the first block of code and wait until completion (it takes about 1 minute);
    5. select Julia kernel (it is called runtime on Google Colab).

    Steps 2 and 3 can be avoided by clicking on the badge "Open in Colab" present in the notebook.
    
    It is extremely important to __not switch to other kernels__ after step 5, otherwise the notebook metadata get overwritten and the notebook ceases to be a Julia notebook. If this happens, save it anyway, because it can be restored at a later time (cfr. notebook recovery paragraph).

- __To save back to GitHub__ the changes applied to a notebook on Google Colab, choose to save a copy to GitHub, then specify the destination path in the repository and a commit message, which will be added to the Git history of the file. Changes are pushed by the same GitHub account whose access is granted to Google Colab, but they are not signed.

- __To create a new notebook__ in Google Colab the procedure is similar to load an existing notebook, except for point 3 which is altered as follows: the selected notebook must be `template_julia.ipynb` (or it can be opened by clicking on the badge "Open in Colab" present in the notebook, remember to update the filename in the badge URL for the new notebook), then soon after it is loaded it must be saved back to the repository with a different name.

__Notebook recovery__
If for any chance a notebook ceases to be identified as a Julia notebook (e.g. because on Google Colab the kernel has been changes to Python), its condition can be restored by changing the notebook metadata. Simply compare the raw source of the file (Jupyter notebooks are JSON files) with `template_julia.ipynb` and restore the values which happen to be different in key `kernelspec`.

### Cloud fallback plan
If for some reason Google Colab can not be used to work on Julia notebooks, website [Binder](https://mybinder.org/) can load this repository and access its content on a cloud VM. File `Project.toml` is mandatory for this task because it instructs Binder on the environment to set up. If a different Julia version is chosen, it must be updated also in this file at the key `julia` of section `[comp]`.

After the environment is loaded in Binder, successive changes in the repository are not reflected there. To circumvent the problem, Git can be used inside the Binder environment to pull the latest changes, since the repository is public. Shell script `pull_branch.sh` is a reminder of this detail.
Saving changes back to Git is more convoluted since it is necessary to download them locally first (to avoid privacy and security issues in a direct connection through Git).

Click on the following badge to load the `main` branch of this repository on Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mirasac/algoopti.git/main)

## References
To set up the cloud environment I took inspiration from the following references:

1. [Related question on StackOverflow](https://stackoverflow.com/questions/58270424/julia-in-google-colab).
2. [Dsantra92's Julia notebook template on GitHub](https://github.com/Dsantra92/Julia-on-Colab).
3. [johnnychen94's Julia notebook template on GitHub](https://github.com/johnnychen94/colab-julia-bootstrap).
4. [Tutorial on loading a Git repository in Binder](https://the-turing-way.netlify.app/communication/binder/zero-to-binder.html).

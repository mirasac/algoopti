# algoopti
## Introduction
This repository contains source code and material (e.g. notes) about problems faced during the course [Algorithms for optimization, inference and learning](https://fisica-sc.campusnet.unito.it/do/corsi.pl/Show?_id=a763), taken during the second semester of the academic year 2022-2023 for the master's degree in Physics of Complex Systems at UniTo.

The regular teacher of this course is Professor Braunstein. The course and [its official web site](https://didattica.polito.it/pls/portal30/gap.pkg_guide.viewGap?p_cod_ins=01SPOPF&p_a_acc=2223&p_header=S&p_lang=EN) are hosted at Politecnico di Torino.

### Disclaimer
This repository exists just as an effective way to save the code while the exercises are being done, it is not meant for presenting them in a complete and nice way. Just the information sufficient for the resolution of problems are included.

## Repository structure
Files related to a problem are contained in a directory with name `Problem_n` where n is the number of the problem at the time of the creation of the directory. This numbering come from the problems list on professor's LaTeX notes, so it could go out of sync with the real numbering on the notes at any time. To provide consistency, the following list associates numbers to problems permanently and it is updated each time a new problem is inserted in the repository:

- 3 Sierpinski’s triangle
- 35 Making a difference

## Programming environment
During lesson code is written in Julia, but in this repository both Python and Julia codes are present (since I am new to Julia language).

My local environment is VS Code as visual text editor, equipped with the Julia extension.

To be more flexible, I plan to use Julia in Google Colab. Some information [here](https://stackoverflow.com/questions/58270424/julia-in-google-colab) and [here](https://github.com/Dsantra92/Julia-on-Colab).
A possible road map could be the following:
1. create Jupyter notebook with some Julia code and save it on GitHub;
2. test the notebook in Binder (cfr. [tutorial on the official site](https://the-turing-way.netlify.app/communication/binder/zero-to-binder.html)), to check that it works, is available on the Internet and as a fallback plan if Google Colab does not work;
3. install Julia on the fly on a Google Colab session, cfr. references;
4. check if the Julia environment on Google Colab works, test it also by loading the Jupyter notebook prepared at point 1;
5. create a Jupyter notebook to automate the installation at the start of each session, cfr. references.

Log:
- 20230318T1405 I am trying to put all the needed files in a subfolder of the repository, as opposed to what suggested in the tutorial. Moreover I am doing these tests in a branch which is not `main`, but I hope that the branch name makes no difference on Binder's internal working.
- T1416 Binder allows to specify the branch (more generally, the reference in the repository history) and the path where the notebook should be loaded from.

#!/bin/zsh

source activate cb-nmfsubnet
ipython -c "import os; os.chdir('../'); import Codebase; Codebase.helpers.nmf_optimization.execute('$1', '$2', '$3', '$4', '$5', '$6', '$7')"
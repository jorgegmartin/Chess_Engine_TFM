----
# Development of a chess engine using Neural Networks and python
----

## Goal

The goal of this project is to create an engine capable of playing chess on its own. For this, it is necessary to train a neural network on known data and teach it to evaluate positions that occur naturaly on a chess game.

All the notebooks have been written using python as only programming language.


## Tools

In order to reproduce this project it is necessary to carry out the following steps:

1. Have the Conda package manager installed.

2. Download the source data from the following Google Drive folder, and unzip in the working directory.
_google drive link_

3. Install the necessary environment or use the requirements list found in this repository. (chess_env.yml or requirements.txt)

4. Open the project report (memoria.pdf), and follow along the steps.
It should yield the same results as found in the git repository. 


## Technical Information

All the necessary packages for this project can be found in the requrements.txt file.

"intel-tensorflow" is included and "tensorflow-gpu" is not included due to incompatibilities between the two libraries and "intel-tensorflow" being the more universal one.

If you wish to execute the code with tensorflow-gpu requirements must be modified before installing.


## Folder structure

chess_game/gui:
   - folder with all the files necesasry to run the graphic interface.

data/:
   - stores the notebooks that explore and process the data.

data/random_generated/:
   - stores the data generated for the project. Not on github since this data is too big. Can be found on Google Drive. 

data/sample/:
   - stores the samples with which data notebooks work. 

documentation/:
   - Folder for the formal project documentation.

engine/:
   - stores the notebooks used for the generation of the engine.

engine/engine_models/:
   - holds the models generated

engine/stockfish/:
   - stores stockfish exe file. Not on github since this data is too big. Can be found on Google Drive.


## Game User Instructions

In order to play you must have installed all the tools necessary for the execution.

1. Open a command prompt terminal.

2. Go to the current directory of the project. For example: C:Users\MagnusCarlsen\Desktop\Best_Chess_Engine_TFM

3. Using python, execute main.py. For example: python c:/Users/MagnusCarlsen/Desktop/Best_Chess_Engine_TFM/chess_game/gui/main.py

4. Enjoy.
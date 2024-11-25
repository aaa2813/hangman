# Hangman
Basic hangman game in terminal window.

## Usage
`hangman.py` is run from the command line with an additional argument specifying the path to a list of potential word choices. The list must be a text file, with each entry in its own line.

During a game session, only three types of entries are permitted:
- Single alphanumeric character - letters are automatically capitalized.
- Quit commands - both "exit" and "quit" will stop the game and reveal the answer.
- Full word guess - must include all special characters (non-alphanumeric) in original word. Letter case ignored.


## Design
TBD
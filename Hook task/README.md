## Hook task

The git folder contains all the information that is necessary for your project in version control and all the information about commits, etc. 
Pre-commit hook stored in Hooks folder. To test it you need to add '.' before the title of 'git' folder ('git' - > '.git').
New_score contains the last score of a model from pickle file and in old_score file stores the best score.
Pre-commit hook compares values from old_score and new_score files and if new score is less then old you can commit project.

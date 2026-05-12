# OBS.: Used __all__ to silence flake8 errors
# DON'T FORGET: 'mv to_be_gitignore .gitignore' before pushing in intra repo

# ex0: 
	[X] done and tested
	[X] flake8 + mypy

# ex1:
	[X] done and tested
    [X] flake8 + mypy
	[ ] is doesn't raise errors, but maybe change this: 
		'def create_base(self) -> Any:'
		to:
		'def create_base(self) -> Creature:'
		if so, also add 'from ex0.creatures import Creature'

# ex2:
    [X] done and tested
    [X] flake8 
	[X] fix mypy ERRORS
	[X] Double check with AI if it follows all subject requirements

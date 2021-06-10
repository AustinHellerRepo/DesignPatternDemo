from design_pattern.visitor.implementation import PoemSource, UserInputSource, TextFormatter


# NOTES:
#	I am not a fan of this design pattern as it requires a cyclic dependency between both the visitor and its elements
#		as well as moving the implementation of all possible visitor elements into one soon-to-be massive class.
#	A better implementation that accomplishes the same task is in the Strategy design pattern using dependency injection.


# create text formatter to be passed into the visitors
_uppercase_text_formatter = TextFormatter(
	is_upper=True
)

# instantiate the visitors
_text_sources = [
	PoemSource(
		poem="My life has been the poem I would have writ\nBut I could not both live and utter it. -Henry David Thoreau"
	),
	UserInputSource(
		message="Please enter any text"
	)
]

# perform the actions from each visitor, passing in the text formatter
for _text_source in _text_sources:
	_text_source.perform_action(
		visitor=_uppercase_text_formatter
	)

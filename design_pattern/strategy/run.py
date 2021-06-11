from design_pattern.strategy.implementation import TextFormatter, PoemSource, UserInputSource


# create text formatter to be passed into the strategy implementors
_uppercase_text_formatter = TextFormatter(
	is_upper=True
)

# instantiate the strategy implementors
_text_sources = [
	PoemSource(
		poem="My life has been the poem I would have writ\nBut I could not both live and utter it. -Henry David Thoreau"
	),
	UserInputSource(
		message="Please enter any text"
	)
]

# perform the actions from each strategy implementor, passing in the text formatter
# an alternative implementation would have the text formatter passed into the constructor, if it was more fundamental
#	to the operation of the text source, impacting other functions and internal logic.
for _text_source in _text_sources:
	_text_source.perform_action(
		strategy=_uppercase_text_formatter
	)

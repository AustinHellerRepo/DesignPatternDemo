from design_pattern.facade.implementation import ListElementCounter, AddHyphensToString, ConvertTextToListOfLetters, GetNumberOfElementsInList


# create the facade class/wrapper that will make interacting with these three "complex" classes easier
_list_element_counter = ListElementCounter(
	text_formatter=AddHyphensToString(),
	text_to_list=ConvertTextToListOfLetters(),
	list_to_number=GetNumberOfElementsInList()
)

# perform the newly-simplified function
_text = "This is a test."
_number = _list_element_counter.get_text_to_number(
	text=_text
)

# display output
print(f"The text \"{_text}\" was reduced to {_number}.")

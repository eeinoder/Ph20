# Run set1.py and produce plots
include config

TXT_FILES=$(wildcard inputs/*.txt)

## variables	:
.PHONY : variables
variables:
	@echo TXT_FILES: $(TXT_FILES)

## plotimage	: Produce plots.
.PHONY : imgs
imgs :
	$(SET1_EXE1) $(TXT_FILES)

## latexfile	: Compile latex file into pdf.
.PHONY : latexfile
latexfile:
	$(SET1_EXE2)


.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<


#	$@, target of the current rule
#	$^, dependecies of current rule
#	$<, first dependency
#	$*, like % but for used for actions

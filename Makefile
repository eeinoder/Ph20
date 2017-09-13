# Run set1.py and produce plots
include config

## dats	: Produce plots.
.PHONY : dats
dats : plot1.dat plot2.dat plot3.dat

%.dat : values/%.txt $(SET1_SRC)
	$(SET1_EXE) $< > $@

## clean	: Remove auto-generated files.
.PHONY : clean
clean :
	rm -f *.dat

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<


#	$@, target of the current rule
#	$^, dependecies of current rule
#	$<, first dependency
#	$*, like % but for used for actions

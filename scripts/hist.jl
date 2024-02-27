#!/usr/bin/env -S julia --startup-file=no --project=.
using UnicodePlots

@debug "got here"
show(histogram([parse(Float64, strip(line)) for line in readlines()]))


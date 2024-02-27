#!/usr/bin/env -S julia --startup-file=no --project=.
using UnicodePlots
using Destruct
(value_strs, words) = readlines() .|> split .|> Tuple |> destruct
values = parse.(Float64, value_strs)

barplot(words, values) |> show

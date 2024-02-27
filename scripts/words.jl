#!/usr/bin/env -S julia --startup-file=no --project=. -O0 
using WordTokenizers

get(ARGS,1,stdin) |> readchomp |> tokenize |> x->join(stdout, map(lowercase,x), '\n')

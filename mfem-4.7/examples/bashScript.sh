#!/bin/bash

echo "Hola, mundo"

#parallel 'mpirun -np 1 ex1p -m ../data/star-surf.mesh -o {} 2>./output/output_{}.txt' ::: 1 2

parallel 'mpirun -np 1 ex1p -m ../data/star-surf.mesh -rl {} 2>./output/output_{}.txt' ::: 1000.0 10000.0

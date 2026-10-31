import glob
import os
from run_bench import run_benchmark

benches = glob.glob(os.path.abspath("benchmark/")+"*.crbench")

total = len(benches)
score = 0

for bench in benches:
  success = run_benchmark(model_name, bench)
  if success:
    score+=1

print("benchmark score: ",score/total*100,"% for model", model_name)
  




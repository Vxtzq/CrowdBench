import glob
import os
from run_benchmark import run_bench
import argparse

parser = argparse.ArgumentParser(
                    prog='CrowdBench',
                    description='Runs all the benchmarks for CrowdBench - the collaborative LLM benchmark',
                    epilog='')

parser.add_argument('--model', help='HuggingFace model repository')      # option that takes a value
args = parser.parse_args()

results = []

model_name = args.model

benches = glob.glob(os.path.abspath("benchmark/")+"*.crbench")

total = len(benches)
score = 0

for bench in benches:
  success = run_benchmark(model_name, bench)
  results.append((bench,success))
  if success:
    score+=1

print("benchmark score: ",score/total*100,"% for model", model_name)

with open("demofile.txt", "w") as w:
  f.write("")
with open("demofile.txt", "a") as w:
  f.write("Score " + str(score/total*100)+"%")
  for result in results:
    if result[1]:
      f.write("Benchmark " + result[0] + " SUCCEEDED")
    else:
      f.write("Benchmark " + result[0] + " FAILED")




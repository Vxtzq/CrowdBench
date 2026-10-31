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

benches = glob.glob("benchmark/*.crbench")

total = len(benches)
score = 0
if total == 0:
    print("No benchmarks found!")
    exit()


for bench in benches:
  success = run_bench(model_name, bench)
  results.append((bench,success))
  if success:
    score+=1

print("benchmark score: ",score/total*100,"% for model", model_name)

with open("results/"+model_name.split("/")[1]+".txt", "w") as f:
  f.write("")
with open("results/"+model_name.split("/")[1]+".txt", "a") as f:
  f.write("Score " + str(score/total*100)+"%\n\n")
  for result in results:
    if result[1]:
      f.write("Benchmark " + result[0] + " SUCCEEDED\n")
    else:
      f.write("Benchmark " + result[0] + " FAILED\n")



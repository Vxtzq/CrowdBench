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

model_name = args.model

benches = glob.glob(os.path.abspath("benchmark/")+"*.crbench")

total = len(benches)
score = 0

for bench in benches:
  success = run_benchmark(model_name, bench)
  if success:
    score+=1

print("benchmark score: ",score/total*100,"% for model", model_name)
  




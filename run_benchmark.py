import argparse

parser = argparse.ArgumentParser(
                    prog='CrowdBench',
                    description='Runs CrowdBench - the collaborative LLM benchmark',
                    epilog='')

parser.add_argument('--model', help='HuggingFace model repository')      # option that takes a value
args = parser.parse_args()

print("Selected model", args.model)

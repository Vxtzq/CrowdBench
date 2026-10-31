import argparse

from transformers import AutoModelForCausalLM, AutoTokenizer

parser = argparse.ArgumentParser(
                    prog='CrowdBench',
                    description='Runs CrowdBench - the collaborative LLM benchmark',
                    epilog='')

parser.add_argument('--model', help='HuggingFace model repository')      # option that takes a value
parser.add_argument('--file', help='.crbench file to run benchmark on')      # option that takes a value
args = parser.parse_args()

model_name = args.model
file_name = args.file


f = open(args.file)
content = f.read()

f = open("instruction.txt")
instruct = f.read()

def parse_crbench(content):
    question = content.split("[question]", 1)[1].split("[answer]", 1)[0].strip()
    answer = content.split("[answer]", 1)[1]

    return question, answer

q, a = parse_crbench(content)



model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": instruct},
    {"role": "user", "content": q}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)

if a in response:
  print("Benchmark passed!")
else:
  print("Benchmark failed.")

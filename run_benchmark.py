import argparse

from transformers import AutoModelForCausalLM, AutoTokenizer

def run_bench(model_name,file_name,max_tokens=1024):
  f = open(args.file)
  content = f.read()
  
  f = open("instruction.txt")
  instruct = f.read()
  
  def parse_crbench(content):
      question = content.split("[question]", 1)[1].split("[answer]", 1)[0].strip()
      answer = content.split("[answer]", 1)[1]
  
      return question, answer
  
  q, a = parse_crbench(content)
  
  a = a.replace("\n","")
  
  model = AutoModelForCausalLM.from_pretrained(
      model_name,
      torch_dtype="auto",
      device_map="auto"
  )
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  
  prompt = "Give me a short introduction to large language model."
  messages = [
      {"role": "system", "content": "You are an helpful assistant being evaluated."},
      {"role": "user", "content": instruct+q}
  ]
  text = tokenizer.apply_chat_template(
      messages,
      tokenize=False,
      add_generation_prompt=True
  )
  model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
  
  generated_ids = model.generate(
      **model_inputs,
      max_new_tokens=max_tokens
  )
  generated_ids = [
      output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
  ]
  
  response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
  
  print(response)
  
  if a in response:
    return True
  else:
    return False

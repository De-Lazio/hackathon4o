import replicate

os.environ['REPLICATE_API_TOKEN'] = "r8_5Pqkd23E108t2fPesIUtSQHpXZRGf0Q14KdFt"

input = {
    "prompt": "Give me a class of classic physics",
    "temperature": 0.95,
    "max_new_tokens": 500
}

for event in replicate.stream(
    "meta/llama-2-7b",
    input=input
):
    print(event, end="")
#=> ", he orders a martini. everyone in the place stops and s...

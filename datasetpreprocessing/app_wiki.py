import json

def format_entry(entry):
    formatted_entry = {
        "text": f"<s> [INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. <</SYS>> What is {entry['page_title']} and explain in detail? [/INST] {entry['page_text']} </s>"
    }
    return formatted_entry

formatted_data = []

with open("wiki_medical_terms_train.jsonl","r") as wiki:
    for line in wiki:
        entry = json.loads(line)
        #remove unwanted references
        cut_lasttwolines = entry["page_text"].split(". ")[:-10]
        entry["page_text"] = ". ".join(cut_lasttwolines)
        formatted_entry = format_entry(entry=entry)
        formatted_data.append(formatted_entry)

print(formatted_data)
with open("wiki_medical_terms_llam2.jsonl","w") as llama2:
    for entry in formatted_data:
        try:
            json.dump(entry, llama2)
            llama2.write('\n')
        except Exception as ex:
            print(ex)
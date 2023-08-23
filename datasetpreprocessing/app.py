from datasets import load_dataset
dataset = load_dataset("gamino/wiki_medical_terms")

for split, dataset in dataset.items():
    dataset.to_json(f"wiki_medical_terms_{split}.jsonl")
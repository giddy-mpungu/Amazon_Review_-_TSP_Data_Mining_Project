import gzip

with gzip.open('meta_Beauty_and_Personal_Care.jsonl.gz', 'rt') as f_in:
    meta_data = [json.loads(line) for line in f_in]

with gzip.open('Beauty_and_Personal_Care.jsonl.gz', 'rt') as f_in:
    reviews_data = [json.loads(line) for line in f_in]

print("Unzipping done")


import json

input_file = 'Beauty_and_Personal_Care.jsonl'
output_file = 'dt_subset.jsonl'

records = []
with open(input_file, 'r') as f:
    for i in range(10):
        line = f.readline()
        if line:
            records.append(json.loads(line))
        else:
            break

with open(output_file, 'w') as f:
    for record in records:
        f.write(json.dumps(record) + '\n')

print(f"Subset of the first 10 records has been saved to {output_file}")

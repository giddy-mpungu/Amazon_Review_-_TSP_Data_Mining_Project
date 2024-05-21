import json

def read_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line) for line in file]

def write_jsonl(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(json.dumps(entry) + '\n')

# Reading the meta data
meta_data = read_jsonl('meta_Beauty_and_Personal_Care.jsonl')

# Creating a dictionary for meta data with 'parent_asin' as the key
meta_dict = {}
for item in meta_data:
    key = item.get('parent_asin')
    if key:
        meta_dict[key] = {
            "main_category": item.get("main_category"),
            "title": item.get("title"),
            "average_rating": item.get("average_rating"),
            "rating_number": item.get("rating_number"),
            "price": item.get("price"),
            "parent_asin": item.get("parent_asin")
        }

# Reading the main data
main_data = read_jsonl('Beauty_and_Personal_Care.jsonl')

# Enriching the main data with meta data
enriched_data = []
for item in main_data:
    parent_asin = item.get('parent_asin')
    if parent_asin and parent_asin in meta_dict:
        item.update(meta_dict[parent_asin])
    enriched_data.append(item)

# Writing the enriched data to a new JSONL file
write_jsonl(enriched_data, 'dt.jsonl')

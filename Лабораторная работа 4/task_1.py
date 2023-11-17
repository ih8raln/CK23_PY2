import json

def task(file_path) -> float:
    with open(file_path) as f:
        data = json.load(f)
        return round(sum(d['score'] * d['weight'] for d in data), 3)

print(task('input.json'))

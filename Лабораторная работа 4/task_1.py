# TODO решите задачу
import json

def task(file_path) -> float:
    result = 0
    with open(file_path) as f:
        data = json.load(f)
        for d in data:
            result += d['score'] * d['weight']
    return round(result, 3)


print(task('input.json'))

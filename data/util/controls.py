import os, json

def load_controls(path):
    controls = None
    with open(os.path.join(path,'util','controls.json'), 'r+') as file:
        controls = json.load(file)
    return controls

def write_controls(new_controls):
    with open(os.path.join('util','controls.json'), 'w') as file:
        json.dump(new_controls, file)
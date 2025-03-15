import json
import yaml

def get_yaml_file(folder : str, filename : str) -> dict:
    try :
        with open(f"data/{folder}/{filename}.yml", "r", encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Problème d'ouverture du fichier {filename} : {e}")

def get_json_file(folder : str, filename : str) -> dict:
    try :
        with open(f"outfiles/{filename}.json", "r", encoding='utf-8') as f:
            return json.loads(f.read())
    except Exception as e:
        print(f"Problème d'ouverture du fichier {filename} : {e}")




def dump_json_file(filename : str, dump_content : dict) -> None:
    try:
        with open(f"outfiles/{filename}.json", "w+", encoding='utf-8') as f:
            json.dump(obj = dump_content, fp = f, indent = 4)
    except Exception as e:
        print(f"Problème de modification du fichier {filename}")


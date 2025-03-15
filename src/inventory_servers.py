import os
from files_utils import get_yaml_file, dump_json_file
from typing import Literal

def server_per_app():
    all_apps = {}
    for filename in os.listdir("data/servers"):
        if not filename.endswith(".yml"):
            break
        
        data = get_yaml_file("servers", filename.split(".")[0])
        app_name = data['tags']['app']
        if app_name in all_apps.keys():
            all_apps[app_name] += 1
        else:
            all_apps[app_name] = 1
    
    dump_json_file("stat_apps.json", all_apps)

def get_server_number_by_tag(tag : Literal['app', 'role', 'country', 'env']):
    server_number = {}
    for filename in os.listdir("data/servers"):
        if not filename.endswith(".yml"):
            break
        
        data = get_yaml_file("servers", filename.split(".")[0])
        tag_data = data['tags'][tag]
        if tag_data in server_number.keys():
            server_number[tag_data] += 1
        else:
            server_number[tag_data] = 1
    
    return server_number


def get_glob_stat():
    glob_stat = {}
    for filename in os.listdir("data/servers"):
        if not filename.endswith(".yml"):
            print(filename)
            break
        
        data = get_yaml_file("servers", filename.split(".")[0])
        app_name = data['tags']['app']
        country = data['tags']['country']
        role = data['tags']['role']

        if app_name in glob_stat.keys():
            glob_stat[app_name]['count'] += 1
            if country in glob_stat[app_name]['country'].keys():
                glob_stat[app_name]['country'][country] += 1
            else:
                glob_stat[app_name]['country'][country] = 1

            if role in glob_stat[app_name]['role'].keys():
                glob_stat[app_name]['role'][role] += 1
            else:
                glob_stat[app_name]['role'][role] = 1

        else:
            glob_stat[app_name] = {'count': 1, 'country': {country: 1}, 'role': {role: 1}}
        
    return glob_stat

dump_json_file("stat_apps", get_server_number_by_tag("app"))
dump_json_file("stat_countries", get_server_number_by_tag("country"))
dump_json_file("stat_roles", get_server_number_by_tag("role"))
dump_json_file("stat_all", get_glob_stat())

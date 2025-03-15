import os
from files_utils import dump_yaml_file, get_yaml_file

costs_data_cpuf = get_yaml_file('costs', 'cpu_first')
costs_data_memoryf = get_yaml_file('costs', 'memory_first')

def find_offer(cpu, memory):
    if (cpu < 1 or memory < 1 or cpu > 500 or memory > 500):
        return None
    print(f"On cherche CPU: {cpu} - Memory: {memory}")
    for cost in costs_data_cpuf if cpu > cpu else costs_data_memoryf:
        if cpu == cost['cpu'] and memory == cost['memory']:
            print(f"Trouvé CPU: {cpu} - Memory: {memory} - Cost: {cost['credits']}")
            return cost
    else:
        print(f"Non trouvé CPU: {cpu} - Memory: {memory}")
        o1 = find_offer(cpu - 1, memory) if cpu > cpu else find_offer(cpu, memory - 1)
        o2 = find_offer(cpu + 1, memory) if cpu > cpu else find_offer(cpu, memory + 1)
        if o1 and o2:
            if o1['cost'] < o2['cost']:
                return o1
        elif o1:
            return o1
        elif o2:
            return o2
        
        return None
    

def compute_by_server():
    res = {}
    
    for filename in os.listdir('data/servers'):
        if not filename.endswith('.yml'):
            break

        server = get_yaml_file('servers', filename.split('.')[0])
    

        serv_data = {
            'name': server['name'],
            'cpu': server['cpu'],
            'memory': server['memory'],
            'billing_uuid': '',
            'credits': 0,
            'diff_cpu': 2,
            'diff_memory': 0
        }

        offer = find_offer(serv_data['cpu'], serv_data['memory'])
        if offer != None:
            serv_data['billing_uuid'] = offer['uuid']
            serv_data['credits'] = offer['credits']
        else:
            print(f"Server {serv_data['name']} not found in costs")
            print("\t CPU: ", serv_data['cpu'])
            print("\t Memory: ", serv_data['memory'])
            continue

        #print(json.dumps(serv_data, indent=4))
        res[filename.split('.')[0]] = serv_data

    dump_yaml_file('servers_cost', res)

compute_by_server()

#find_offer(12, 24)
import requests
from config import CONSUL_URL

def get_service_instances(service_name):
    url = f"{CONSUL_URL}/catalog/service/{service_name}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def load_balanced_request(service_name, circuit_breaker):
    instances = get_service_instances(service_name)
    
    for instance in instances:
        if not circuit_breaker.is_open():
            address = instance["ServiceAddress"]
            port = instance["ServicePort"]
            return f"http://{address}:{port}"
    
    return None

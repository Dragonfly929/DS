import requests
from config import USER_SERVICE_NAME, POPULARITY_SERVICE_NAME, CACHE_EXPIRATION
from load_balancer import load_balanced_request
from cache import cache_response, get_cached_response
from circuit_breaker import CircuitBreaker

user_circuit_breaker = CircuitBreaker()
popularity_circuit_breaker = CircuitBreaker()

def get_user_data(user_id):
    cache_key = f"user_data_{user_id}"
    cached_data = get_cached_response(cache_key)
    if cached_data:
        return cached_data
    
    user_service_url = load_balanced_request(USER_SERVICE_NAME, user_circuit_breaker)
    if user_service_url:
        response = requests.get(f"{user_service_url}/users/{user_id}")
        if response.status_code == 200:
            user_data = response.json()
            cache_response(cache_key, user_data, CACHE_EXPIRATION)
            return user_data
        else:
            user_circuit_breaker.record_failure()
    return None

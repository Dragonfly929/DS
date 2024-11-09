import os

# API Gateway configuration
API_GATEWAY_HOST = os.getenv("API_GATEWAY_HOST", "0.0.0.0")
API_GATEWAY_PORT = int(os.getenv("API_GATEWAY_PORT", 3000))

# Service Discovery (Consul)
CONSUL_HOST = os.getenv("CONSUL_HOST", "consul")
CONSUL_PORT = int(os.getenv("CONSUL_PORT", 8500))
CONSUL_URL = f"http://{CONSUL_HOST}:{CONSUL_PORT}/v1"

# Service Names as registered in Consul
USER_SERVICE_NAME = "user-service"
POPULARITY_SERVICE_NAME = "popularity-service"

# Load Balancing Strategy
LOAD_BALANCER_STRATEGY = os.getenv("LOAD_BALANCER_STRATEGY", "round_robin")

# Circuit Breaker
CIRCUIT_BREAKER_FAILURE_THRESHOLD = int(os.getenv("CIRCUIT_BREAKER_FAILURE_THRESHOLD", 3))
CIRCUIT_BREAKER_RECOVERY_TIMEOUT = int(os.getenv("CIRCUIT_BREAKER_RECOVERY_TIMEOUT", 20))

# Cache
CACHE_EXPIRATION = int(os.getenv("CACHE_EXPIRATION", 60))

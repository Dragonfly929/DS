import grpc

import popularity_service_pb2
import popularity_service_pb2_grpc

class PopularityServiceClient:
    def __init__(self, host="localhost", port=50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = popularity_service_pb2_grpc.PopularityServiceStub(self.channel)

    def get_popular_palettes(self, category):
        request = popularity_service_pb2.PopularityRequest(category=category)
        
        try:
            response = self.stub.GetPopularPalettes(request)
            return response.palettes
        except grpc.RpcError as e:
            print(f"gRPC call failed: {e}")
            return None

# Example usage
if __name__ == "__main__":
    client = PopularityServiceClient(host="popularity_service", port=50051)  # Adjust host if necessary
    popular_palettes = client.get_popular_palettes(category="Art")
    if popular_palettes:
        for palette in popular_palettes:
            print(f"Palette ID: {palette.palette_id}, Name: {palette.name}, Likes: {palette.likes}")

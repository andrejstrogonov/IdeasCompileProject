class Service:
    def perform_service(self):
        return "Service is being performed"

class Client:
    def __init__(self, service: Service):
        self.service = service

    def do_something(self):
        return self.service.perform_service()

# Example usage
if __name__ == "__main__":
    service = Service()
    client = Client(service)
    print(client.do_something())
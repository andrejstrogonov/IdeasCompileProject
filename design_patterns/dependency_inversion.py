from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    @abstractmethod
    def perform_service(self):
        pass

class ConcreteService(ServiceInterface):
    def perform_service(self):
        return "Service is being performed"

class Client:
    def __init__(self, service: ServiceInterface):
        self.service = service

    def do_something(self):
        return self.service.perform_service()

# Example usage
if __name__ == "__main__":
    service = ConcreteService()
    client = Client(service)
    print(client.do_something())
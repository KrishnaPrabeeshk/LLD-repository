from abc import ABC, abstractmethod
import time

class Ticket:
    def __init__(self, priority: str) -> None:
        self.priority = priority
        self.handlers_visited = 0

class SupportHandler(ABC):
    def __init__(self) -> None:
        self.next_handler = None
    
    def set_next_handler(self, handler: 'SupportHandler') -> 'SupportHandler':
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle_request(self, ticket: Ticket):
        pass

class BasicSupportHandler(SupportHandler):
    def handle_request(self, ticket: Ticket):
        start = time.time()
        ticket.handlers_visited += 1

        if ticket.priority == "low":
            print("Basic support can handle the ticket")
        elif self.next_handler:
            self.next_handler.handle_request(ticket)
        else:
            print("No one can handle the ticket")

        end = time.time()
        print(f"[BasicSupportHandler] Time taken: {round(end - start, 4)} seconds")

class AdvancedSupportHandler(SupportHandler):
    def handle_request(self, ticket: Ticket):
        start = time.time()
        ticket.handlers_visited += 1

        if ticket.priority in ["medium", "low"]:
            print("Advanced support can handle the ticket")
        elif self.next_handler:
            self.next_handler.handle_request(ticket)
        else:
            print("No one can handle the ticket")

        end = time.time()
        print(f"[AdvancedSupportHandler] Time taken: {round(end - start, 4)} seconds")

class PremiumSupportHandler(SupportHandler):
    def handle_request(self, ticket: Ticket):
        start = time.time()
        ticket.handlers_visited += 1

        if ticket.priority in ["high", "medium", "low"]:
            print("Premium support can handle the ticket")
        elif self.next_handler:
            self.next_handler.handle_request(ticket)
        else:
            print("No one can handle the ticket")

        end = time.time()
        print(f"[PremiumSupportHandler] Time taken: {round(end - start, 4)} seconds")

class CTOHandler(SupportHandler):
    def handle_request(self, ticket: Ticket):
        start = time.time()
        ticket.handlers_visited += 1

        print("CTO can handle the ticket")

        end = time.time()
        print(f"[CTOHandler] Time taken: {round(end - start, 4)} seconds")
        print(f"Handled after passing through {ticket.handlers_visited} handler(s).")

# Setup chain
level1 = BasicSupportHandler()
level2 = AdvancedSupportHandler()
level3 = PremiumSupportHandler()
cto = CTOHandler()

level1.set_next_handler(level2).set_next_handler(level3).set_next_handler(cto)

# Test cases
print("Testing level 1:")
ticket1 = Ticket("low")
level1.handle_request(ticket1)
print(f"Handled after passing through {ticket1.handlers_visited} handler(s).")

print("\nTesting level 2:")
ticket2 = Ticket("medium")
level1.handle_request(ticket2)
print(f"Handled after passing through {ticket2.handlers_visited} handler(s).")

print("\nTesting level 3:")
ticket3 = Ticket("high")
level1.handle_request(ticket3)
print(f"Handled after passing through {ticket3.handlers_visited} handler(s).")

print("\nTesting level 4:")
ticket4 = Ticket("urgent")
level1.handle_request(ticket4)

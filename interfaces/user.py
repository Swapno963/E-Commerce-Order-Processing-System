from abc import ABC, abstractmethod


class AuthService(ABC):

    @abstractmethod
    def login(self, message: str):
        pass


    # @abstractmethod
    # def registration(self, message: str):
    #     pass



class NotificationService(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


# example 
class EmailService(NotificationService):
    def send(self, message: str):
        print(f"Email sent: {message}")


class SMSService(NotificationService):
    def send(self, message: str):
        print(f"SMS sent: {message}")


class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, msg):
        self.service.send(msg)

manager = NotificationManager(EmailService())
manager.notify("Hello")
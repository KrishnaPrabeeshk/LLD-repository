from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, news):
        pass

class NewsChannel(Observer):
    def __init__(self,name):
        self.name = name
        self.news_feed = []
    
    def update(self, news):
        print(f"{self.name} received: {news}")
        self.news_feed.append(news)

class Subject(ABC):

    @abstractmethod
    def register(self,observer):
        pass

    @abstractmethod
    def unregister(self,observer):
        pass

    def notify_observers(self,news):
        pass

class NewsAgency(Subject):
    def __init__(self):
        self.observers_map = {}
        self.topics = ["weather","sport","politics","business","fashion"]

        for topic in self.topics:
            self.observers_map[topic] = []
    
    def register(self, observer,topic):
        self.observers_map[topic].append(observer)
    
    def unregister(self, observer,topic):
        self.observers_map[topic].remove(observer)
    
    def notify_observers(self, news):
    # Simple keyword-based topic detection
        topic_detected = None
        for topic in self.topics:
            if topic.lower() in news.lower():
                topic_detected = topic
                break

        if topic_detected:
            for observer in self.observers_map[topic_detected]:
                observer.update(news)
        else:
            print("No matching topic found. News not sent to any observer.")



agency = NewsAgency()

bbc = NewsChannel("BBC")
cnn = NewsChannel("CNN")

agency.register(bbc, "weather")
agency.register(cnn, "business")


agency.notify_observers("📢 Breaking News: Observer Pattern Implemented in Python!")
agency.notify_observers("📈 Business Update: Markets hit all-time high.")
agency.notify_observers("🌦️ Weather Update: Rain expected tomorrow.")
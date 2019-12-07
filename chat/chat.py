from chat.default import Default
from nlp.nlp import NLP
from match.faq import FAQ
from nlp.qa import QA
from search.elastic import Search


class Chat:
    def __init__(self):
        """Main Chat interface for Chatbot replies."""
        self.default = Default()
        # self.nlp = NLP()
        self.faq = FAQ("../match/FAQ.xlsx")
        self.qa = QA("../nlp/Document.txt")
        self.search = Search()

    def default(self, key):
        """Get default replies based on the key."""
        return self.default.get_default_reply(key)

    def reply(self, message):
        print("Message received:", message)
        # Phase 1: FAQ Matching
        print("Phase 1: FAQ Matching")
        answer = self.faq.ask_faq(message, threshold=0.9)  # change to 0.9 for large model
        if answer:
            return answer

        # Phase 2: NLP Question Answering
        print("Phase 2: NLP Question Answering")
        answer = self.qa.ask(message, threshold=1.0)
        if answer:
            return answer

        # Phase 3: Search
        print("Phase 3: Search")
        answer = self.search.search(message)
        if answer:
            return answer
        else:
            return "No content found."

    def nlp(self, message):
        """Returns a NLP reply."""
        return self.nlp.reply(message)

    def ask(self, question):
        """Ask a question to the QA system."""
        return self.qa.query(question)

    def search(self, query):
        """Searches the database."""
        return self.search.search(query)

class Chatbot:
    def generate_response(self, query):
        return f"Response for: {query}"

bot = Chatbot()
print(bot.generate_response("Hello"))

class Standard:
    def __init__(self, questions):
        self.questions = [questions]
        self.assigned_questions = []
    def add_item(self, item):
        self.questions.append(item)
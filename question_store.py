class QuestionStore:
    
    #init class. our array of items parsed from the csv + dicts to hold
    #the counts for building the quiz
    def __init__(self):
        self.question_items = []
        self.strand_counts = {}
        self.standard_counts = {}
        self.question_counts = {}
    def add_item(self, item):
        self.question_items.append(item)
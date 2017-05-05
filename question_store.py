import collections
import standard

class QuestionStore:
    
    #init class. our array of items parsed from the csv + dicts to hold
    #the counts for building the quiz
    def __init__(self):
        self.question_items = []
        self.strands = {}
        self.strands_list = []
        self.standards = {}
        self.standards_list = []
        self.question_counts = {}
    def add_item(self, item):
        self.question_items.append(item)
        if item.strand_id not in self.strands:
            self.strands[item.strand_id] = [item.standard_id]
            self.strands_list.append(item.strand_id)
        else:
            self.strands[item.strand_id].append(item.standard_id)
        if item.standard_id not in self.standards:
            self.standards[item.standard_id] = standard.Standard(item.question_id)
        else:
            self.standards[item.standard_id].add_item(item.question_id)
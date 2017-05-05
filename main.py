import csv
import question_item
import question_store
import random

#parse the csv file into quesiton_items, then put those items into a question_store
def parse_csv(question_store):
    dic_read = csv.DictReader(open("questions.csv", encoding = "utf8"))
    for line in dic_read:
        item = question_item.QuestionItem(line['strand_id'], line['strand_name'], line['standard_id'], line['standard_name'], line['question_id'], line['difficulty'])
        question_store.add_item(item)
 
def build_quiz(question_count, question_store):
    strand_count = len(question_store.strands)
    strand_index = 0
    standard_last_used = {}
    question_numbers = ""
    for i in range(0, question_count):
        #pick a strand id
        strand_pick = question_store.strands_list[strand_index]
        #get standards associated with strand option
        standard_options = question_store.strands[strand_pick]
        if strand_pick in standard_last_used:
            if standard_last_used[strand_pick] == len(standard_options) - 1:
                standard_last_used[strand_pick] = 0
                standard_pick = standard_options[0]
                question_numbers += random.choice(question_store.standards[standard_pick].questions)
                question_numbers += ","
            else:
                #we still have more standards to pick!
                standard_last_used[strand_pick] = standard_last_used[strand_pick] + 1
                standard_pick = standard_options[standard_last_used[strand_pick]]
                question_numbers += random.choice(question_store.standards[standard_pick].questions)
                question_numbers += ","
        else:
            standard_pick = standard_options[0]
            standard_last_used[strand_pick] = 0
            question_numbers += random.choice(question_store.standards[standard_pick].questions)
            question_numbers += ","
        if strand_index == strand_count - 1:
            strand_index = 0
        else:
            strand_index = strand_index + 1
    return question_numbers

#main
if __name__ == '__main__':
    question_store = question_store.QuestionStore()
    parse_csv(question_store)
    count = input("Enter the number of questions in the quiz: ")
    question_numbers = build_quiz(int(count), question_store)
    print(question_numbers[:-1])
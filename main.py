import csv
import question_item
import question_store

#parse the csv file into quesiton_items, then put those items into a question_store
def parse_csv(question_store):
    dic_read = csv.DictReader(open("questions.csv", encoding = "utf8"))
    for line in dic_read:
        item = question_item.QuestionItem(line['strand_id'], line['strand_name'], line['standard_id'], line['standard_name'], line['question_id'], line['difficulty'])
        question_store.add_item(item)
                                          
#main
if __name__ == '__main__':
    question_store = question_store.QuestionStore()
    parse_csv(question_store)
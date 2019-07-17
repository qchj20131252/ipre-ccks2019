import json
from pyhanlp import *

def segment(data_path, output_path, CRFnewSegment):
    data = json.load(open(data_path, mode='r', encoding='utf-8'))


    result = []
    count = 0
    for dic in data:
        text = dic['text']
        term_list = CRFnewSegment.seg(text)
        try:
            postag = [{'word': term.word, 'pos': str(term.nature).strip()} for term in term_list]
            dic['postag'] = postag
            result.append(dic)
        except UnicodeDecodeError:
            count += 1
            print(dic)
            continue

    print(count)

    json.dump(result, open(output_path, mode='w', encoding='utf-8'), ensure_ascii=False, indent=4)

if __name__ == '__main__':
    CRFnewSegment = HanLP.newSegment("crf")
    train_path = '../data/sent_train.data'
    train_output_path = '../data/sent_train0.data'
    print('处理训练数据集')
    segment(train_path, train_output_path, CRFnewSegment)


    dev_path = '../data/sent_dev.data'
    dev_output_path = '../data/sent_dev0.data'
    print('处理开发数据集')
    segment(dev_path, dev_output_path, CRFnewSegment)




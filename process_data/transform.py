import json

def transform(data_filepath, relation_filepath, output_filepath):
    with open(data_filepath, mode='r', encoding='utf-8') as data_fr:
        data_list = data_fr.readlines()
    with open(relation_filepath, mode='r', encoding='utf-8') as relation_fr:
        relation_list = relation_fr.readlines()
    if len(data_list) != len(relation_list):
        print("ERROR!数据格式不统一！！")
        return
    result_list = []
    for i in range(len(data_list)):
        data_split = data_list[i].split('\t')
        relation_split = relation_list[i].split('\t')
        if data_split[0] != relation_split[0]:
            print(data_split[0],relation_split[0])
            print('ERROR!数据不匹配')
            break
        if ' ' in relation_split[-1]:
            continue
        result_dict = {'id': data_split[0],
                       'sub': data_split[1],
                       'obj': data_split[2],
                       'text': data_split[3].replace(' ', '').strip(),
                       'relation_id': int(relation_split[-1])
                       }
        result_list.append(result_dict)
    json.dump(result_list, open(output_filepath, mode='w', encoding='utf-8'), ensure_ascii=False, indent=4)

if __name__ == '__main__':
    sent_train_data_filepath = '../data/sent_train.txt'
    sent_relation_train_filepath = '../data/sent_relation_train.txt'
    sent_output_train_filepath = '../data/sent_train.data'
    transform(sent_train_data_filepath, sent_relation_train_filepath, sent_output_train_filepath)

    sent_dev_data_filepath = '../data/sent_dev.txt'
    sent_relation_dev_filepath = '../data/sent_relation_dev.txt'
    sent_output_dev_filepath = '../data/sent_dev.data'
    transform(sent_dev_data_filepath, sent_relation_dev_filepath, sent_output_dev_filepath)





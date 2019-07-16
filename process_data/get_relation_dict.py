import json

def get_relation_dict(relation_filepath):
    relation2id = {}
    id2relation = {}
    with open(relation_filepath, mode='r', encoding='utf-8') as fr:
        for line in fr.readlines():
            split_list = line.split('\t')
            relation2id[split_list[0]] = int(split_list[1])
            id2relation[int(split_list[1])] = split_list[0]
    json.dump([relation2id, id2relation], open('../dict/relation_dict', mode='w', encoding='utf-8'), ensure_ascii=False,
              indent=4)

if __name__ == '__main__':
    relation_filepath = '../data/relation2id.txt'
    get_relation_dict(relation_filepath)
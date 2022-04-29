import requests
import csv


USERNAME = 'username'
API_KEY = 'api-key'
base_url = 'https://api.sketchengine.eu/bonito/run.cgi'

data = csv.reader(open('besede.csv', 'r', encoding='utf-8'))
besede = [row[0] for row in data]

for beseda in besede:
    data = {
        'corpname': 'preloaded/slwac21',
        'format': 'json',
        'q': ['q[lc="' + beseda + '" | lemma_lc="' + beseda + '"]'],
        'kwicleftctx': '-2:s',
        'kwicrightctx': '2:s'
    }

    # preloaded/sltenten15_tt2_1
    # slwac21

    # d = requests.get(base_url + '/wsketch?corpname=%s' % data['corpname'], params=data, auth=(USERNAME, API_KEY)).json()
    # d = requests.get(base_url + '/view?corpname=preloaded/slwac21', params=data, auth=(USERNAME, API_KEY)).json()
    try:
        d = requests.get(base_url + '/view?corpname=preloaded/slwac21', params=data, auth=(USERNAME, API_KEY)).json()
    except:
        print("Error fetching " + beseda)
        continue


    count = 0
    left = ""
    sentences = []
    for line in d['Lines'][:10]:
        left = ""
        right = ""

        if (len(line['Left']) == 1):
            left = line['Left'][0]['str']

        else:
            for s in line['Left']:
                if (s['str'] == '¶' and left == ""):
                    continue
                elif (s['str'] == '¶'):
                    left = left + " "
                else:
                    left = left + s['str']

        if (len(line['Right']) == 1):
            right = line['Right'][0]['str']

        else:
            for s in line['Right']:
                if (s['str'] == '¶' and right == ""):
                    continue
                elif (s['str'] == '¶'):
                    right = right + " "
                else:
                    right = right + s['str']

        sentences.append(left + " " + beseda + " " + right)

    with open('corpus\\' + beseda + '.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(sentences)):
            writer.writerow([i, sentences[i], len(left), len(left + beseda) + 1])

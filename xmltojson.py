
import xml.etree.ElementTree as et
import json


tr=et.parse('ABSA16_Restaurants_Train_SB1_v2.xml')
root=tr.getroot()

empty_opinion={
    'category': None,
    'from':0,
    'polarity': 'neutral',
    'to':0,
    'target':'NULL'
}


def parse_reviews(reviews):
    sentences=[]
    for review in reviews:
        for sentence in review[0]:
            sentences.append(sentence)
            
    return [parse_sentence(sentence) for sentence in sentences]


def parse_sentence(sentence):
    text=sentence[0]
    try:
        opinions = sentence[1]
        parsed_opinions=parse_opinions(opinions)
    except IndexError:
        parsed_opinions = [empty_opinion]
    
    return {'text': parse_text(text),
            'opinions': parsed_opinions}


def parse_opinions(opinions):
    assert(opinions.tag=='Opinions')
    parsed_opinions=[]
    for opinion in opinions:
        atr = opinion.attrib
        atr['from'] = int(atr['from'])
        atr['to'] = int(atr['to'])
        parsed_opinions.append(atr)
    return parsed_opinions


def parse_text(text):
    assert(text.tag=='text')
    return text.text


if __name__ == '__main__':
    result=parse_reviews(root)
    with open('data.json', 'w') as f:
        json.dump(result, f)

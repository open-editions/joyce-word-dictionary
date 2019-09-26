from yaml import load, Loader
import re

"""
Loads the YAML file from the Joyce Word Dictionary, and tries to make TEI entries for them.

"""

with open('../src/data/words.yaml') as f:
    yamlData = f.read()

parsed = load(yamlData, Loader=Loader)


# Only Ulysses first
ulyssesWords = [w for w in parsed if w['text'] == 'Ulysses']

citations = [re.findall('\(U? ?\d+.\d+\)', word['citation']) for word in ulyssesWords]

"""
Each word should look like this:

<note resp="#contributor" type="analysis" xml:id="1234-wordhere">
  <term>wordhere</term>
    <analysis>
    Analysis here
    </analysis>
  <time> Timestamp here </time> 
  <quote> My cockle hat and staff and hismy sandal shoon." </quote>
  <bibl> U 3.487 </bibl>
</note>
"""
def parseCitation(citation):
    """ Gets episode and line number from something like this: (U 3.487) """
    xmlId = re.search(r'\([A-Z]+?\s?(\d{1,2}).(\d{1,4})[-–-—–]?\d+?\)', citation)
    # print(citation)
    if xmlId is not None:
        if len(xmlId.groups()) < 2:
            print("Can't parse the citation: ", citation)
            return None
        else:
            episode, lineNo = xmlId.groups()
            # print(xmlId.groups())
            return int(episode), int(lineNo)
    else:
        print("Couldn't find a citation in: ", citation)
        return None

def word2TEI(word):
    """ Input is the dictionary about the word, returned from the YAML parser. """
    # Extract episode and line number
    word['episode'], word['lineNo'] = parseCitation(word['citation'])
    out = '<note resp="{contributor}" type="analysis" xml:id="{episode:02d}{lineNo:04d}-{word}">\n'.format(**word)
    out += '<term>{}<term>\n'.format(word['word'])
    out += '<analysis>{}</analysis>\n'.format(word['analysis'])
    out += '<time>{}</time>\n'.format(word['created'])
    out += '<bibl>{}</bibl>\n'.format(word['citation'])
    out += '</note>\n'
    return out

def testTagify():
    assert tagify('word', 'content') == "<word>content</word>"

out = '\n'.join([word2TEI(w) for w in ulyssesWords])

with open('ulysses-word-notes.xml', 'w') as f:
    f.write(out)

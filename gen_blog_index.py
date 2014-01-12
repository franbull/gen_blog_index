import pickle
import re

import read_twitter
import get_instagram

post_template = '''<div>
<span>%(date_str)s</span> &raquo; %(words)s
%(pics)s
</div><br/>'''

def strip_urls(text):
    def repl(m):
        matched_group = m.groups()[0]
        return '<a href="%s">%s</a>' % (matched_group, matched_group)

    pattern = '(http\S*)'
    return re.sub(pattern, repl, text)

divs = []
for date, words, image_urls in read_twitter.get_my_tweets():
    words = strip_urls(words)
    if words.strip() != '':
        pics = '\n'.join(['<div><img src="%s"/></div>' % url for url in image_urls])
        divs.append(post_template % {'date_str': date.strftime('%d %b %Y'), 'words': words, 'pics': pics})

content = '%s' % '\n'.join(divs)


insta_pickle_name = 'instagram_urls.pkl'
try:
    instagram_urls = get_instagram.get_photos()
    with open(insta_pickle_name, 'w') as fout:
        pickle.dump(instagram_urls, fout)
except:
    with open(insta_pickle_name, 'r') as fin:
        instagram_urls = pickle.load(fin)

insta_divs = []
for url, text in instagram_urls:
    insta_divs.append(('''<div class="instagram_photo">'''
    '''<figure>'''
    '''<img src="%s"></img>'''
    '''<figcaption>%s</figcaption>'''
    '''</figure>'''
    '''</div>''') % (url, text))
insta_content = '\n'.join(insta_divs)


with open('blogindextemplate.html', 'r') as fin:
    template = fin.read()
    with open('/home/fran/francisbullinfoblog/index.html', 'w') as fout:
        fout.write((template % {'tweeter': content, 'insta': insta_content}).encode('utf-8'))

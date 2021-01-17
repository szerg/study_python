import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

class Translator:
    translation_base_url = "https://context.reverso.net/translation/"
    request_headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    translation_languages = ['Arabic',
                             'German',
                             'English',
                             'Spanish',
                             'French',
                             'Hebrew',
                             'Japanese',
                             'Dutch',
                             'Polish',
                             'Portuguese',
                             'Romanian',
                             'Russian',
                             'Turkish',
                             ]

    def __init__(self, from_language, to_language, word):
        self.from_to=[]
        self.destination_languages=[]
        if not to_language:
            for lang in self.translation_languages:
                if lang != self.translation_languages[from_language-1]:
                    self.from_to.append(f'{self.translation_languages[from_language-1].lower()}-{lang.lower()}')
                    self.destination_languages.append(lang)
        else:
            self.from_to = [f'{self.translation_languages[from_language-1].lower()}-{self.translation_languages[to_language-1].lower()}']

            self.destination_languages = [self.translation_languages[to_language-1]]
        self.word = word


    @classmethod
    def user_screen(cls):
        print('Hello, you\'re welcome to the translator. Translator supports:')
        for i,v in enumerate(Translator.translation_languages):
            print(f'{i+1} {v}')

    def get_online_translation_page(self, from_to):
        try:
            r = requests.get(self.translation_base_url+from_to+'/'+self.word, headers = self.request_headers)
        except requests.exceptions.ConnectionError as ce:
            print("Something wrong with your internet connection")
            sys.exit(1)
        else:
            if r.status_code == 200:
                return r.content
            if r.status_code == 404:
                print(f'Sorry, unable to find {self.word}')
                sys.exit(3)

    def get_word_translations(self, page_content, from_to, destination_language, limit, file_pointer):
        soup = BeautifulSoup(page_content, 'html.parser')
        translations_links = soup.find_all('a', {'class': 'translation'})
        translated_words = []
        reverse_conversion = 'translation/' + '-'.join(reversed(from_to.split('-')))
        for link in translations_links:
            if len(translated_words) < limit:
                href_attr = link.get('href')
                if reverse_conversion in href_attr:
                    urlencoded_word = href_attr.split('/')[-1]
                    translated_words.append(urllib.parse.unquote_plus(urlencoded_word))
        print(f'{destination_language} Translations:')
        file_pointer.write(f'{destination_language} Translations:\n')
        for word in translated_words:
            print(word)
            file_pointer.write(f'{word}\n\n')

    def get_sentence_translations(self, page_content,destination_language, limit, file_pointer):
        soup = BeautifulSoup(page_content, 'html.parser')
        from_sentences = soup.find_all('div', {'class': 'src ltr'})
        to_sentences = soup.find_all('div', {'class': 'trg'})
        sentences = []
        for j in range(len(from_sentences)):
            if len(sentences) < limit:
                sentences.append((from_sentences[j].text.strip(), to_sentences[j].text.strip()))

        print(f'{destination_language} Examples:')
        file_pointer.write(f'{destination_language} Examples:\n')
        for sentence_group in sentences:
            print(sentence_group[0])
            print(sentence_group[1])
            print()
            file_pointer.write(f'{sentence_group[0]}\n{sentence_group[1]}\n\n')

        file_pointer.write('\n')

    def translate_all(self, limit=1):
        with open(f'{self.word}.txt', 'a+') as f:
            for i in range(len(self.destination_languages)):
                html_page = self.get_online_translation_page(self.from_to[i])
                print()
                self.get_word_translations(html_page, self.from_to[i], self.destination_languages[i], 1, f)
                print()
                self.get_sentence_translations(html_page,self.destination_languages[i], 1, f)



def main():
    #Translator.user_screen()
    #from_lang = int(input('Type the number of your language:\n'))
    #to_lang = int(input("Type the number of a language you want to translate to or '0' to translate to all languages:\n"))
    #word = input('Type the word you want to translate:\n')
    languages = {'arabic':1,
                 'german':2,
                'english':3,
                'spanish':4,
                'french':5,
                'hebrew':6,
                'japanese':7,
                'dutch':8,
                'polish':9,
                'portuguese':10,
                'romanian':11,
                'russian':12,
                'turkish':13,
                'all':0
                 }
    try:
        translator = Translator(languages[sys.argv[1]],languages[sys.argv[2]], sys.argv[3])
    except KeyError as ke:
        print('Sorry, the program doesn\'t support korean')
        sys.exit(2)
    translator.translate_all()

if __name__ == '__main__':
    main()

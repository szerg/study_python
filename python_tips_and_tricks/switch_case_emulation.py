# o metoda de genul:

def fetch_url(url):
    if url == 'ftp':
        print('python fetcher')
    elif url == 'http':
        print('requests fetcher')
    elif url == 'smb':
        print('external downloader')
    else:
        print('No known proto')

# poate fi inlocuita cu:

url_fetcher_types = {
    'ftp': 'python fetcher',
    'url': 'requests fetcher',
    'smb': 'external downloader'
}

def fetch_url_dict(url):
    print(url_fetcher_types.get(url,'No known proto'))

fetch_url('ftp')
fetch_url_dict('ftp')
fetch_url('smb')
fetch_url_dict('smb')
fetch_url('https')
fetch_url_dict('https')

# optimizarea asta are rost daca url ar avea f multe posibilitati si fetch_url s-ar apela de multe ori
# asta ar insemna parcurgerea cazurilor if/elif pana la valoarea dorita
# fetch_url_dict e mult mai rapid , s-ar putea cu overheadul de a tine acea variabila dictionar in memorie
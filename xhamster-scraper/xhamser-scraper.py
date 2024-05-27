import requests
from bs4 import BeautifulSoup
import json
import datetime
import os
import urllib.parse
import random

import title_rewrite

import synonyms_list as sl

# Define the synonyms dictionary
synonyms = sl.synonyms


baseUrl = "https://xhamster1.desi/search/"
mySitEmbedUrl = "https://www.pornstar.monster/video"
mySitEmbedUrl = "/video"

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.google.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def extract_json_from_script(html, script_id):
    soup = BeautifulSoup(html, 'html.parser')
    script_tag = soup.find('script', {'id': script_id})
    if not script_tag:
        raise ValueError(f"Script tag with id {script_id} not found")
    
    script_content = script_tag.string
    #print(script_content)
    json_text = script_content.split('window.initials=', 1)[1]
    json_text = json_text.rsplit(';', 1)[0].strip()
    return json.loads(json_text)

def seconds_to_hms_old(seconds):
    return str(datetime.timedelta(seconds=seconds))

"""
1. If hours is 0, omit it.
2. If minutes is less than 10, pad it with a leading zero.
3. Always show seconds as two digits if there are minutes.
4. If there are only seconds, show 00:SS.
"""

def seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if hours > 0:
        return f"{hours}:{minutes:02}:{seconds:02}"
    elif minutes > 0:
        return f"{minutes:02}:{seconds:02}"
    else:
        return f"00:{seconds:02}"


shortcode_template = """
<div class="container mt-5">
    <h2 class="mb-4">Related Keywords</h2>
    <div class="row">
        <div class="col-md-12">
            <div class="card">
                <div class="card-body">
                    <div class="d-flex flex-wrap">
                        %s
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>"""

def generate_hugo_shortcodes(suggestions):
    shortcodes = ""
    for suggestion in suggestions[1:]: #[1:] removing first item it is "Best Videos"
        shortcodes += '<span class="badge text-primary m-1">{{% ky ' + f'"{suggestion["plainText"]}"' + ' %}}</span> | \n'

    shortcodes = shortcode_template % shortcodes
    return shortcodes

def generate_bootstrap_gallery(videos, search_keyword_plus):
    gallery_html = '<div class="row" id="thumnbail-gallery">'
    wp_domains = ['i0.wp.com', 'i1.wp.com', 'i2.wp.com']
    
    for video in videos:
        videoid = video['pageURL'].rsplit('-', 1)[-1]
        duration = seconds_to_hms(video['duration'])

        title = video["title"]
        new_title = title_rewrite.convert_sentence(title, synonyms)
        new_title_plus = urllib.parse.quote_plus(new_title)
        
        link = f'{mySitEmbedUrl}?videoid={videoid}&title={new_title_plus}&keyword={search_keyword_plus}'
        
        # Randomly select a wp domain
        wp_domain = random.choice(wp_domains)
        
        # Remove the http or https prefix from the thumbURL
        thumb_url = video['thumbURL'].replace('https://', '').replace('http://', '')
        
        # Prepend the selected wp domain
        thumb_url = f'https://{wp_domain}/{thumb_url}'
        
        gallery_html += f'''
        <div class="col-sm-4">
            <div class="thumbnail">
                <a href="{link}" style="position: relative;">
                    <img src="{thumb_url}" alt="{title}">
                    <div class="duration">
                        {duration}
                    </div>
                    <div class="caption">
                        <h3 class="h5">{new_title}</h3>
                    </div>
                </a>
            </div>
        </div>
        '''
    gallery_html += '</div>'
    return gallery_html


def save_to_file(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    base_url = baseUrl
    while True:
        search_keyword = input("Enter search term (or 'exit' to quit): ")
        if search_keyword.lower() == 'exit':
            break

        search_keyword_plus = urllib.parse.quote_plus(search_keyword)
        search_url = base_url + search_keyword_plus
        print("Fetching: ", search_url)
        html = fetch_page(search_url)
        data = extract_json_from_script(html, 'initials-script')

        search_video_suggestions = data['searchVideoSuggestions']['tags']
        search_results = data['searchResult']['videoThumbProps']
        
        hugo_shortcodes = generate_hugo_shortcodes(search_video_suggestions)
        bootstrap_gallery = generate_bootstrap_gallery(search_results, search_keyword_plus)
        
        combined_html = hugo_shortcodes + "\n\n<br/><br/>" + f'<h2 class="h5">{search_keyword} Videos</h2><br/>' + bootstrap_gallery
        
        filename = f"gen_contents/{search_keyword.replace(' ', '_')}.html"
        save_to_file(combined_html, filename)
        save_to_file(combined_html, "output.html")
        print(f"Output saved to {filename}")

if __name__ == "__main__":
    main()

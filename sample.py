from bs4 import BeautifulSoup
import json

def parse_html_to_json(html_file_path, json_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        # Parse the HTML content
        soup = BeautifulSoup(html_file, 'html.parser')

        # Extract text from all <p> tags
        capital = [strong.get_text() for strong in soup.find_all('strong')]
        state = [span.get_text() for span in soup.find_all('span')]
        paired = [{'state':state,'capital':capital} for state, capital in zip(state,capital)]
        # Create a dictionary to store the extracted information
        data = {'capitals':paired,'summary':{'no.ofcapitals':len(capital)}}
        # Write the data to a JSON file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    html_file_path = 'indexs2.html'
    json_file_path = 'results.json'

    parse_html_to_json(html_file_path, json_file_path)

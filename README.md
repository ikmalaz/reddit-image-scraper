\# Reddit Image Scraper (r/bolehland)


This project scrapes posts from r/bolehland, filters only those with images, saves them to `results.json`, and optionally displays the result in simple webpage `index.html` using pyhton and html language.

\## Features
- Scrapes subreddit posts (JSON API)
- Saves posts with images (`title`, `image_url`)
- Output in JSON
- Simple HTML viewer to display results

\## Requirements
- Python 3.x
- requests library
  
\## Installation \
1.Downdload the project
- Click the green Code button in this repository
- Select Download ZIP
- Extract it to a folder (e.g., C:\Users\YourName\reddit-image-scraper)
  
  Alternetive (Clone using Git)
  git clone https://github.com/ikmalaz/reddit-image-scraper.git
  cd reddit-image-scraper
  
2.Open Powershell / Command Prompt / Git Bash

3.Create a virtual enviroment
  python -m venv venv
  
4.Active the virtual enviroment
  .\venv\Scripts\activate
- (venv) will show at the beginning of the command line

5.Install required libraries
  pip install -r requirements.txt

\## How to Run
-make sure your virtual enviroment is active (venv) is showing
-run the scraper
 python scraper.py
-after it finishes, check folder and see results.json (contain the scraped posts with images)

5.View result in a Webpage
-start a simple local server
python -m http.server 8000
-then open browser and go to http://localhost:8000/index.html
-the list of post titles with their images will be shown
-stop the server press Ctrl + C at Powershell/cmd/Git Bash

```bash
reddit-image-scraper/

scraper.py #Main scraper script
requirements.txt #Dependencies list
results.json #Scraped data (auto-genarated)
index.html #Display scraped data in browser
.gitingnore #Keeps repo clean
README.md # Setup and usage instruction

example json results/
[
  {
    "title": "Funny Malaysian traffic sign",
    "image_url": "https://i.redd.it/example1.jpg"
  },
  {
    "title": "Nasi lemak for breakfast",
    "image_url": "https://i.redd.it/example2.jpg"
  }
]

command line needed/

git clone https://github.com/ikmalaz/reddit-image-scraper.git
cd reddit-image-scraper
python -m venv venv
.\\venv\\Scripts\\activate
pip install -r requirements.txt




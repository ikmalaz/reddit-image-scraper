\# Reddit Image Scraper (r/bolehland)


This project scrapes posts from r/bolehland, filters only those with images, saves them to `results.json`, and optionally displays the result in simple webpage `index.html`.

\## Features
- Scrapes subreddit posts (JSON API)
- Saves posts with images (`title`, `image_url`)
- Output in JSON
- Simple HTML viewer to display results

\## Requirements
- Python 3.x
- requests library
  
\## Installation
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

```bash

git clone https://github.com/ikmalaz/reddit-image-scraper.git

cd reddit-image-scraper

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt




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
- Extract it to a folder (e.g., C:\Users\Documents\reddit-image-scraper)
- Make sure reddit-image-scraper folder not creating a double folder
- If reddit-image-scraper folder create a double folder, move all the content inside into a outer folder
- Delete the empty extra folder
- Go to step 2
  
  Alternetive (Clone using Git)
- Open Powershell 
 
  Insert ---> git clone https://github.com/ikmalaz/reddit-image-scraper.git
  
  Then insert ---> cd reddit-image-scraper

- Go to step 3
  
2.Open Powershell 

insert ---> cd (e.g, C:\Users\Documents\reddit-image-scraper) (based on folder PATH)

3.Create a virtual enviroment

  Insert ---> python -m venv venv
  
4.Active the virtual enviroment

  Insert ---> .\venv\Scripts\activate
  
 (venv) will show at the beginning of the command line

5.Install required libraries

 Insert ---> pip install -r requirements.txt

 - Update to the latest pip version (optional)

\## How to Run

- Make sure your virtual enviroment is active (venv) is showing

- Run the scraper

 Insert  ---> python scraper.py
 
- Fetching a data from reddit will be shown as results.json (contain the scraped posts with images)

5.View result in a Webpage

- Start a simple local server

 Insert ---> python -m http.server 8000

- Then open browser and go to http://localhost:8000/index.html

- The list of post titles with their images will be shown

- To stop and exit press Ctrl + C at Powershell 

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




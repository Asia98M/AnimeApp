# Anime Recommendation App

## Project Overview
This project is an Anime Recommendation App developed as part of a Python class at FHNW. It is designed to help users discover new anime based on a predefined dataset, offering inspiration for anime enthusiasts looking for their next show to watch.

## Inspiration
During our Python class, we were tasked with selecting a topic for our project. As both of us enjoy watching anime, we decided to create an app that provides recommendations to make it easier to find interesting shows.

## Challenges
Initially, we attempted to fetch data from the MyAnimeList API. To do so, we had to create an account and request access to the API. However, during implementation, we encountered issues with data accuracy and integration. The inputs retrieved from the API were not as reliable as we had hoped.

To address this, we decided to pivot and created a base CSV file containing at least 20 anime entries. This allowed us to build a more controlled and customizable dataset. The code in the `source` folder reflects this new approach, which has proven to work best for us so far. Additionally, the app allows users to add their own entries to the dataset if any anime titles are missing.

## Features
- Preloaded dataset of anime recommendations.
- Ability for users to add their own anime entries to the list.
- Simple and intuitive interface for browsing recommendations.

## Future Plans
In the next semester, we plan to expand this project further. Our goal is to develop an Android app using the knowledge and codebase we have built so far. This will allow us to provide mobile access to the recommendations and enhance the overall user experience.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Asia98M/AnimeApp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AnimeApp
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run main.py
   ```

### Video Tutorial
For a detailed walkthrough on how to add a new anime to the list, check out our video below.

## Authors
- Asia Marti
- Dominique Saner

## License
This project is licensed under the MIT License. See the LICENSE file for more details.




https://github.com/user-attachments/assets/020cb4e4-e50a-4a45-a880-c3b356259c0b


<!-- Parts of this template are inspired by https://github.com/othneildrew/Best-README-Template -->

# tweet_collector

<!-- Include Github badges here (optional) -->
<!-- e.g. Github Actions workflow status -->

Twitter forms a rich source of information for researchers interested in studying 'the public conversation'. 
The [Academic Research product track](https://developer.twitter.com/en/products/twitter-api/academic-research) is designed to serve the needs of the academic research community.
It provides researchers with special levels of access to public Twitter data without any cost.
This project is aimed to help researchers to use Academic Research product track to collect tweets of their interest and analyze them.

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
    - [Built with](#built-with)
    - [License](#license)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Links](#links)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [Acknowledgements](#Acknowledgements)

<!-- ABOUT THE PROJECT -->
## About the Project
This project provides a set of guidelines + tool, to facilitate the process of collecting tweets and analysing them.

**Date**: Sep 2021

**Researcher**:

- Abby Waysdorf (a.s.waysdofr@uu.nl)

**Research Software Engineer(s)**:

- Parisa Zahedi (p.zahedi@uu.nl)
- Roos Voorvaart (r.voorvaart@uu.nl)

### Built with
- [searchtweets-v2](https://pypi.org/project/searchtweets-v2/): It is a python package serves as a wrapper for the all Twitter API v2 search endpoints. We use this package to collect tweets.
- [elasticsearch/kibana](https://www.elastic.co/) : The collected tweets are visualized using elasticsearch and kibana.
- docker

<!-- Do not forget to also include the license in a separate file(LICENSE[.txt/.md]) and link it properly. -->
### License

The code in this project is released under [MIT License](LICENSE).

<!-- GETTING STARTED -->
## Getting Started
The followings are the main steps. 
1. Apply for Academic Research product track
2. Setup the environment
3. Search tweets
4. Visualize tweets

Each step is elaborted in details in **guideline** folder.

### Prerequisites

* To install and run this project locally, you need to have the following prerequisites installed.

  - Python 3.8
  - Docker desktop
* Skip this section if you are using a pre-installed workspace of Surfsara ResearchCloud. For more details go to  **guideline/Setup_Env.ipynb** .  
### Installation

To get a local copy up and running follow these simple steps.

1. Clone the repo:
```sh
git clone https://github.com/github_username/tweet_collector.git
```
1. (Optional but recommended) Create and activate a virtual environment
1. Create package file:
```
poetry build
```
1. Install package through pip:
```
pip install ./dist/tweet_collector_version.whl
```

<!-- USAGE -->
## Usage
If the installation through pip was followed:
1. Make sure you are inside the virtual environment tweet_collector was installed in
1. Run the `tweet_collector` command to start collecting the tweets
1. Run the `tweet_collector_elastic` command to visualise the results in Kibana.

Alternatively, you can launch the files directly through the supplies shell scripts:
- To collect the tweets of your interest, you will make use of the file `sh search_tweet.sh`.
Go to 'guidelines/Search_Tweets.ipynb' for more details.

- To upload the collected tweets to elasticsearch and visualize it in kibana, you will make use of the file `sh load_elastic.sh`.
Go to 'guidelines/Elasticsearch_and_Kibana.ipynb' for more details.
  
<!-- LINKS -->
## Links

An overview of interesting links related to the project.
- [Install Anaconda Python](https://www.anaconda.com/download/)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Parisa Zahedi - (p.zahedi@uu.nl)

Project Link: [https://github.com/UtrechtUniversity/tweet_collector](https://github.com/UtrechtUniversity/tweet_collector)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Special thanks to [Ton Smeele](A.P.M.smeele@uu.nl) from Research IT team

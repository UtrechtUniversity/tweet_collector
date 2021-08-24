[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
  <h3 align="center">tweet_collector</h3>

  <p align="center">
    A simple guideline + tool for researchers to collect tweets and analyze them .
    <br />
    <a href="https://github.com/UtrechtUniversity/tweet_collector">View Demo</a>
    ·
    <a href="https://github.com/UtrechtUniversity/tweet_collector/issues">Report Bug</a>
    ·
    <a href="https://github.com/UtrechtUniversity/tweet_collector/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Project description](#project-description)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project
This project provides a set of guidelines + tool, to facilitate the process of collecting tweets and analysing them.
- To collect tweets, we apply ['searchtweets-v2'](https://pypi.org/project/searchtweets-v2/), a python package serves as a wrapper for the all Twitter API v2 search endpoints.
- The collected tweets are visualized in [Kibana](https://www.elastic.co/kibana/).

### Project description
Twitter forms a rich source of information for researchers interested in studying 'the public conversation'. 
The [Academic Research product track](https://developer.twitter.com/en/products/twitter-api/academic-research) was built by Twitter to serve the needs of the academic research community via specialized, greater levels of access to public Twitter data.
This is a very good opportunately for researchers to collect historical tweets for free.
This project is aimed to guide researchers with limited level of programming skills to collect tweets of their interest and analyze them.

### Built With

- [searchtweets-v2](https://pypi.org/project/searchtweets-v2/)
- [elasticsearch/kibana](https://www.elastic.co/)
- docker

<!-- GETTING STARTED -->
## Getting Started
The followings are the main steps. 
1. Apply for Academic Research product track
2. Setup the environment
3. Search tweets
4. Visualize tweets.

Each step is elaborted in details in 'guideline' folder.

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
```sh
git clone https://github.com/github_username/tweet_collector.git
```
2. Install the package dependencies
   1. If you have poetry 
    ```sh
    poetry install 
    ```
   2. If you have only pip
   ```sh
   pip install -r requirement.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

- To collect the tweets of your interest, you will make use of the file [src/search_tweet.py](src/search_tweet.py).
Go to 'guidelines/Search_Tweets.ipynb' for more details.

- To upload the collected tweets to elasticsearch and visualize it in kibana, you will make use of the file [src/load_elastic.py](src/load_elastic.py).
Go to 'guidelines/Elasticsearch_and_Kibana.ipynb' for more details.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/UtrechtUniversity/tweet_collector/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Parisa Zahedi - (p.zahedi@uu.nl)

Project Link: [https://github.com/UtrechtUniversity/tweet_collector](https://github.com/UtrechtUniversity/tweet_collector)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [The ResearchCloud team]()

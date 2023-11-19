<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>
<!-- 
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Log ingestion & analysis</h3>

  <p align="center">
    Efficiently manage and query vast log data volumes with a scalable Log Ingestor and Query Interface, featuring real-time ingestion, advanced filtering, and a user-friendly interface.
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a> -->
    <!-- <br /> -->
    <br />
    <a href="https://youtu.be/dBZZXU9ydEA">View Video Demo 📽️</a>
    <!-- ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation--usage">Installation & usage</a></li>
      </ul>
    </li>
    <li>
      <a href="#api-documentation">API Documentation</a>
      <ul>
        <li><a href="#ingestion-routes">Ingestion Routes</a></li>
        <li><a href="#query-routes">Query Routes</a></li>
      </ul>
    </li>
    <li><a href="#additional-information">Additional Information</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Log analyser][product-screenshot]](https://github.com/OmkarPh)

This is an efficient implementation of a log ingestion & analysis solution. It utilises Golang & Elastic DB to efficiently ingest, store & analyse logs. It can accept logs from two sources, Kafka queue or direct HTTP API requests. It also provides a web UI for analysis of logs using different filters & search queries.

### Features
- Text-search across all fields
- Regular expression search on all fields
- Filters on specific fields
- Search in given time range
- Combination of all filters & search
- HTTP endpoint for posting logs
- Kafka queue for streamlined Log processing
- Ingestion Buffer & Batch processing
- Efficient search queries leveraging Elastic DB
- Scalable & Efficient processing using sharding provided by Elastic DB


### Built With

- [![Golang][Golang]][Golang-url]
- [![Python][Python]][Python-url]
- [![Elasticsearch][Elasticsearch]][Elasticsearch-url]
- [![Kafka][Kafka]][Kafka-url]
- [![TypeScript][TypeScript]][TypeScript-url]
- [![React][React.js]][React-url]
- [![Gin][Gin]][Gin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python
- Node JS & NPM
- Golang
- Kafka
- Elastic Search

### Installation & usage

- Clone the repo

  ```sh
  git clone https://github.com/dyte-submissions/november-2023-hiring-OmkarPh
  cd november-2023-hiring-OmkarPh/
  ```

- Setup Log ingestion server

  1. Go to `log-server` directory
     ```sh
       cd log-server/
     ```
  2. Install golang dependencies
     ```sh
     go mod download
     ```
  3. Install Python dependencies
     ```sh
     pip install -r requirements.txt
     ```
  4. Start the ingestion server

     ```sh
     cd cmd
     GIN_MODE=release go run .
     ```
     The server should now be running on [http://localhost:3000](http://localhost:3000).

  5. Simulate huge amount of sample logs simultaneously
     Configure `LOGS_LENGTH` in `log-server/tests/performance_test.py`. Default value: 3000

     ```sh
     python tests/performance_test.py
     ```

- Setup Web UI

  1. Go to `frontend` directory
     ```sh
       cd frontend/
     ```
  2. Install NPM dependencies
     ```sh
     npm install
     ```
  3. Start the React app
     ```sh
     npm start
     ```
  4. View the app here - [http://localhost:3006](http://localhost:3006)

- Simulate Log Publishers (Optional)

  1.  Start zookeepr

      ```sh
      zookeeper-server-start //path-to-kafka-config/zoo.cfg
      ```

  2.  Start Kafka
      ```sh
      kafka-server-start /path-to-kafka-config/server.properties
      ```
  
  3. Start publisher script
      Go to `log-producers` directory
      ```sh
      cd log-server/log-producers
      ```
      Start a producer to simulate service using `--topic` option in different shells.
      Configured topics: `auth`,`database`,`email`,`payment`,`server`,`services`,
      ```sh
      # Example:
      python producer.py --topic payment
      python producer.py --topic auth
      ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- API spec -->

## API Documentation

### Ingestion Routes

#### 1. New Log Ingestion

- **Endpoint:** `POST /`
- **Description:** Ingests a new log entry into the system.

  **Request Example:**

  ```json
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-1234",
    "timestamp": "2023-09-15T08:00:00Z",
    "traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
      "parentResourceId": "server-0987"
    }
  }
  ```

  **Response Example:**

  ```json
  {
    "status": "success"
  }
  ```

#### 2. Count Logs

- **Endpoint:** `GET /logs-count`
- **Description:** Retrieves the count of logs stored in Elasticsearch.

  **Response Example:**

  ```json
  {
    "count": 5286
  }
  ```

### Query Routes

#### 1. Search Logs

- **Endpoint:** `POST /search-logs`
- **Description:** Searches for logs based on specified parameters. All the filter params, search text & time range are optional.

  **Request Example:**

  ```json
  {
    "text": "email",
    "regexText": "jkl-*",
    "filters": [
      {
        "columnName": "level",
        "filterValues": ["error", "warning"]
      },
      {
        "columnName": "resourceId",
        "filterValues": ["user-123"]
      },
      {
        "columnName": "metadata.parentResourceId",
        "filterValues": ["9876", "1234"]
      },
      ... Other columns
    ],
    "timeRange": {
      "startTime": "2023-11-19T00:00:00Z",
      "endTime": "2023-11-19T23:59:59Z"
    }
  }
  ```

  **Response Example:**

  ```json
  {
    "hits": {
      "total": 5,
      "hits": [
        {
          "_id": "1",
          "_source": {
            "level": "error",
            "message": "Database connection error",
            "resourceId": "user-123"
            // ... (other log fields)
          }
        }
        // Additional log entries
      ]
    }
  }
  ```

## Additional Information

- **Elasticsearch Index Name:** `log-ingestor`
- **Server Port:** `:3000`
- **CORS Configuration:** Allows all origins (`*`) and supports HTTP methods: GET, POST, PUT, DELETE.
- **Concurrency Configuration:**
  - Buffered log channel with a default capacity of 5000 logs. (Can be changed via `logsBufferSize`)
  - Maximum concurrent log processing workers: 20.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Future improvements / Flaws
* Kibana integration for better visual analysis
* Persistent TCP or Web socket connection between servers (log producer) and log ingestor for lower latency
* Redundant disk buffer for reliability
* Alert system to notify administrators or users about critical log events in real-time.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Omkar Phansopkar - [@omkarphansopkar](https://twitter.com/omkarphansopkar) - omkarphansopkar@gmail.com

<!-- Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES for github -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.gif
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Kafka]: https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white
[Kafka-url]: https://kafka.apache.org/
[Elasticsearch]: https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white
[Elasticsearch-url]: https://www.elastic.co/elasticsearch/
[Golang]: https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white
[Golang-url]: https://golang.org/
[Gin]: https://img.shields.io/badge/Gin-F9F9F9?style=for-the-badge&logo=go&logoColor=00ADD8
[Gin-url]: https://github.com/gin-gonic/gin
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[TypeScript]: https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org/

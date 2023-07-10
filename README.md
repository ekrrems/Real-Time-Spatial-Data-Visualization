# Real-Time Spatial Data Visualization

This repository contains the code and resources for real-time spatial data visualization using Folium and Kafka.

## Description

The project aims to visualize real-time spatial data on a map using Folium and Kafka. It includes the following components:

- `kafka_producer.py`: Python script for producing data to Kafka topic and.
- `kafka_consumer.py`: Python script for visualizing the spatial data on a Folium map and add the data into PostgreSQL database.
- `spatialDataApi.py`: FastAPI module to get post requests and return json format message
- `text_to_coordinates.py`: Python script for converting text data into latitude and longitude using GeoPy module.
- `user_interface.py`: Python script to get data from the user and request it to FastAPI.
- `README.md`: This README file providing an overview of the project.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/ekrrems/Real-Time-Spatial-Data-Visualization

## Contributing

Contributions are welcome! Here are the steps to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in this repository, providing a clear description of your contribution.<br>

Please ensure that your contributions adhere to the project's coding standards and follow the best practices.

## License

This project is licensed under the [MIT License](LICENSE).



# Python Prometheus Metrics Server

A quick and dirty Python 3 server that emits metrics for collection via Prometheus.

## Getting Started

### Prerequisites

- Python 3
- Docker

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/your-repo.git
   ```

2. Navigate to the `prometheus_server` directory:

   ```
   cd your-repo/prometheus_server
   ```

### Usage

1. Start the Python 3 mock metrics server:

   ```
   python3 mock_server.py
   ```

2. Spin up Prometheus using Docker Compose:

   ```
   docker-compose up -d
   ```

3. Access Prometheus:

   Open your web browser and navigate to `http://localhost:9090` to access the Prometheus web interface.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Jev Forsberg - jev.forsberg@gmail.com

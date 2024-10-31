# DevOps and SRE Practices Project

This project demonstrates skills in DevOps and SRE practices. It involves developing a Python program to extract URLs from web pages, containerizing the application with Docker, deploying it using Kubernetes, setting up a CI/CD pipeline, and performing text processing using Unix command-line tools.

## Project Structure

```plaintext
.
├── Dockerfile
├── .github
│   └── workflows
│       ├── main.yml
│       └── README.md
├── .gitignore
├── kubernetes
│   ├── deployment.yml
│   ├── images
│   │   ├── get_pod.png
│   │   └── log_pod.png
│   └── README.md
├── README.md
├── requirements.txt
├── text_processing
│   ├── awk.sh
│   ├── input.txt
│   ├── README.md
│   └── sed.sh
└── url_extractor
    ├── images
    │   └── extract_url.png
    ├── README.md
    └── url_extractor.py

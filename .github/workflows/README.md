# CI/CD Pipeline for Docker Image

GitHub Actions to automate the CI/CD pipeline for building, pushing, and deploying a Docker image.

## Workflow Overview

The workflow is triggered on every push to the `main` branch. It performs the following steps:

1. **Checkout Code**: Checks out the repository code.
2. **Set up Docker Buildx**: Sets up Docker Buildx for building multi-platform images.
3. **Log in to Docker Hub**: Logs into Docker Hub using credentials stored in GitHub Secrets.
4. **Build and Push Docker Image**: Builds the Docker image and pushes it to Docker Hub.
5. **Deploy - Run Docker Container**: Runs the Docker container with the built image.

## Detailed Steps

### 1. Checkout Code

```yaml
- name: Checkout Code
    uses: actions/checkout@v3
```

This step checks out the code from the repository so that it can be used in subsequent steps.

### 2. Set up Docker Buildx

```yaml
- name: Set up Docker Buildx
    uses: docker/setup-buildx-action@v2
```

This step sets up Docker Buildx, which is a Docker CLI plugin that extends the `docker build` command with the full support of the features provided by Moby BuildKit builder toolkit.

### 3. Log in to Docker Hub

```yaml
- name: Log in to Docker Hub
    uses: docker/login-action@v2
    with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
```

This step logs into Docker Hub using the username and password stored in GitHub Secrets. Make sure to add `DOCKER_USERNAME` and `DOCKER_PASSWORD` to your repository secrets.

### 4. Build and Push Docker Image

```yaml
- name: Build and Push Docker Image
    uses: docker/build-push-action@v3
    with:
        context: .
        file: ./Dockerfile
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/devopsho:latest
```

This step builds the Docker image using the Dockerfile in the repository and pushes it to Docker Hub with the tag `latest`.

### 5. Deploy - Run Docker Container

```yaml
- name: Deploy - Run Docker Container
    run: |
        docker run --rm ${{ secrets.DOCKER_USERNAME }}/devopsho:latest -u "https://news.ycombinator.com/" -o "stdout"
```

This step runs the Docker container using the built image. It passes a URL and output option as arguments to the container.

## Conclusion

This CI/CD pipeline ensures that every change pushed to the `main` branch is automatically built, pushed to Docker Hub, and deployed. This helps in maintaining a consistent and up-to-date Docker image for your application.
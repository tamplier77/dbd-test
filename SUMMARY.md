1. Choose docker image as a template for our challenge - python3.5-alpine
2. Init empty folder with git for later publish at Github.
2. Build our own image based on pulled one.
  Dockerfile:
    1. Add folder 'app' as working folder into container.
    2. Put the file main.py, routers file, into app folder.
    3. Tell docker to run it when up.
  docker-compose:
    1. Add docker-compose.yaml file describing container to run.
  Github:
    1. Add .env file with secret credentials and add it to .gitignore file.
3. Publish docker image to Docker hub.
4. Make new published image as main in Dockerfile.
5. Add test.py file testing basic response from new running container.





### What should be prepared
1. create butcket in GCS
2. download credential json file from GCP
3. put it on root directory on this project

### How to run docker container
1. `docker-compose up -d --build`
2. `docker-compose exec python3 bash`

### How to exec python application
put some file which you want to upload, in "opt" folder
 `python main.py opt/<FILE_NAME>`
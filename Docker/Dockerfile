#Download base image ubuntu
FROM debian:9.12

#Dependencies
RUN apt-get update && apt-get install -y vim  python3 python3-pip

WORKDIR /Docker
ADD . /workspc
WORKDIR /workspc

RUN pip3 freeze > requirements.txt \
    pip3 install -r requirements.txt && \
    pip3 install jupyter

#Expose port 8080
EXPOSE 8080

CMD ["sh", "-c" , "jupyter notebook --no-browser --port=8000 --ip='0.0.0.0' --allow-root"]

FROM ubuntu:18.04

ADD /Docker /workspace

WORKDIR /workspace

RUN apt-get update && apt-get -qq -y install python3 python3-pip
RUN pip3 install -r requirements.txt
    #install jupyter
    #pip3 install jupyter
    

EXPOSE 8888
CMD ["sh", "-c", "jupyter notebook --no-browser --port=8000 --ip='0.0.0.0' --allow-root"]

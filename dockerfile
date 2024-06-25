FROM mcr.microsoft.com/playwright:v1.44.1-focal

WORKDIR /app

COPY configs /app/configs
COPY input_data /app/input_data
COPY test_UI /app/test_UI

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

#not tested yet
CMD ["python", "runner.py"]
#CMD  ["pytest", "-v"]
#used for default command
#docker compose up

#docker build -t <image_name>
#docker image ls
#docker run -it <image_name> pytest -v
#docker-compose.yaml


# FROM python:3.7
# ENV ALLURE_VERSION=2.13.7
# ENV ALLURE_REPO_LINK=https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip
# # install google chrome
# RUN apt-get update
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > /dev/null
# RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
# RUN apt-get install -y x11vnc
# RUN apt-get install -y xvfb
#
# RUN mkdir /usr/aut
# WORKDIR /usr/aut
#
# COPY requirements.txt ./
#
# RUN pip install --no-cache-dir -r requirements.txt
# # Install OpenJDK-11
# RUN apt-get update && \
#     apt-get install -y openjdk-11-jre-headless && \
#     apt-get clean;
#
# COPY . .
# RUN wget ${ALLURE_REPO_LINK}
# RUN unzip /usr/aut/allure-${ALLURE_VERSION}.zip -d ./results
# RUN chmod -R +x /usr/aut/results/allure-${ALLURE_VERSION}
# RUN chmod +x /usr/aut/results/allure-${ALLURE_VERSION}/bin/allure
# ENV ALLURE_HOME=/usr/aut/results/allure-${ALLURE_VERSION}/bin
# ENV PATH=${ALLURE_HOME}:${PATH}:/usr/bin
# COPY run.sh ./
# COPY xvfb /etc/init.d/xvfb
# RUN chmod +x /etc/init.d/xvfb
# RUN chmod +x run.sh
# ENV DISPLAY=:99
# EXPOSE 80
# ENTRYPOINT [ "./run.sh" ]


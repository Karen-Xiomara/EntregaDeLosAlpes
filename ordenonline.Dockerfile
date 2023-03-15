FROM python:3.10

EXPOSE 5000/tcp

COPY ordenonline-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r ordenonline-requirements.txt

COPY ./src .

CMD [ "flask", "--app", "./ordenonline/api", "run", "--host=0.0.0.0"]
FROM python:3.12
COPY . /usr/app/
EXPOSE 8000
WORKDIR /usr/app/
RUN pip install -r requirement.txt
CMD streamlit run server.py
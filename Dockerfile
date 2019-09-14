FROM python:3
ADD graph_path.py /
RUN chmod +x /graph_path.py
ENTRYPOINT [ "/graph_path.py" ]
FROM bitnami/spark

USER root 
RUN pip install numpy pandas pyarrow py4j
USER 1001
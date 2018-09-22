# Start from a core stack version
FROM jupyter/datascience-notebook:137a295ff71b
# Install from requirements.txt file
COPY requirements.txt /tmp/
RUN conda install --yes --file /tmp/requirements.txt && \
    fix-permissions /home/$NB_USER

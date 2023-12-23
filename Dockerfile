# Use jupyter/base-notebook
FROM jupyter/base-notebook:python-3.8.13

# Make the directory for the project files
RUN mkdir /home/jovyan/work/Near_Earth_Objects

# Set the working directory to /home/jovyan/work
WORKDIR /home/jovyan/work/Near_Earth_Objects

# Copy the current directory contents into the container
COPY . /home/jovyan/work/Near_Earth_Objects

# Expose the ports Jupyter and other services will run on
EXPOSE 8888
EXPOSE 8889
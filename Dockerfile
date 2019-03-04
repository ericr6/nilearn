# Use an official Python runtime as a parent image
FROM python:3.6-slim

RUN apt-get update && apt-get install -y wget zip

# Set the working directory to /app
WORKDIR /

# Install any needed packages specified in requirements.txt
RUN pip install scikit-learn nilearn matplotlib 

ADD plot_3d_and_4d_niimg_nogui.py /.      	
ADD test.sh /.

# Run app.py when the container launches
CMD ["./test.sh", "/iexec_out", "image_"]

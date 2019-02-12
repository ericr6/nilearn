# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /

# Install any needed packages specified in requirements.txt
RUN pip install scikit-learn nilearn matplotlib wget

ADD plot_3d_and_4d_niimg_nogui.py /.      	

# Run app.py when the container launches
CMD ["python", "plot_3d_and_4d_niimg_nogui.py"]

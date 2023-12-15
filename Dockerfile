# Use the official AWS Lambda Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.11
RUN yum install -y unzip

RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm -o google-chrome-stable_current_x86_64.rpm
RUN yum install -y ./google-chrome-stable_current_x86_64.rpm
RUN ln -s /usr/bin/google-chrome-stable /usr/bin/chromium

# https://googlechromelabs.github.io/chrome-for-testing/
RUN curl https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/linux64/chromedriver-linux64.zip -o chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip && cp chromedriver-linux64/chromedriver /usr/bin/
# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Lambda function code, test file, and handler function
COPY app.py test_app.py ./

# Run unit tests
RUN python -m unittest test_app.py

# Set the CMD to your handler
CMD ["app.handler"]

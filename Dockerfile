FROM python:3.9 
# Or any preferred Python version.
ADD numberguess.py .
RUN pip install -r requirements.txt
EXPOSE 8088
CMD [“python”, “./numberguess.py”] 
# Or enter the name of your unique directory and parameter set.

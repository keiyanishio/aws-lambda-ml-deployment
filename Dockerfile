FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY src/predict_handler.py ${LAMBDA_TASK_ROOT}
COPY model.pkl ${LAMBDA_TASK_ROOT}
COPY ohe.pkl ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "predict_handler.predict_handler" ]

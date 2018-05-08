ARG REGISTRY_URL
FROM ${REGISTRY_URL}scroll-phat
ENV text "ACR BUILDER"
WORKDIR /app
COPY ./acr/scroll-acr.py .
CMD ["python" "/app/scroll-acr.py"]

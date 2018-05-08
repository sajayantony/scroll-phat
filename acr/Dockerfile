ARG REGISTRY_URL
FROM ${REGISTRY_URL}scroll-phat
ENV text "ACR BUILDER"
WORKDIR /app
COPY scroll-acr.py .
CMD ["python" "/app/scroll-acr.py"]

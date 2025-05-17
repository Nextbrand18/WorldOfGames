# ---------- build stage ------------------------------------------------------
    FROM python:alphine AS builder

    WORKDIR /build
    
    # Install build deps for chromium
    RUN apt-get update && apt-get install -y --no-install-recommends \
            curl ca-certificates gnupg && \
        apt-get clean && rm -rf /var/lib/apt/lists/*
    
    COPY app/ ./app
    #include tests so same image can run #them.
    COPY e2e.py .               
    
    RUN pip install --no-cache-dir flask selenium
    
    # ---------- runtime stage ----------------------------------------------------
    FROM python:alpine
    
    ENV PYTHONUNBUFFERED=1 \
        PYTHONPATH=/app
    
    WORKDIR /app
    
    # runtime deps (chromium & driver for later e2e usage)
    RUN apt-get update && apt-get install -y --no-install-recommends \
            chromium chromium-driver && \
        apt-get clean && rm -rf /var/lib/apt/lists/*
    
    COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
    COPY --from=builder /build/app ./app
    COPY --from=builder /build/e2e.py /e2e.py
    
    # Default score file inside image (can be overridden with volume)
    COPY app/Scores.txt /Scores.txt
    
    EXPOSE 8777
    CMD ["python", "-m", "app.MainScores", "--port", "8777"]
    
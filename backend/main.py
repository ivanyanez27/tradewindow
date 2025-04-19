cat > main.py << 'EOF'
app = FastAPI()
from fastapi import FastAPI


app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

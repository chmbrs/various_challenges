from fastapi import FastAPI
import frontend
import uvicorn
import backend


backend.achilles_and_turtle_print()

app = FastAPI()

frontend.init(app)

if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5500
    )

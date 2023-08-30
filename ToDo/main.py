from fastapi import FastAPI, HTTPException, Query, Path
import models
from starlette import status
from pydantic import BaseModel, Field

# dependency injection

app = FastAPI()




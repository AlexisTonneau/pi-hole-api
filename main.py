import os

import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from pihole import Pihole
import validators

if os.getenv('DEBUG') != 'True':
    pihole = Pihole(os.environ["PI_URL"], os.environ["PI_PSW"])
else:
    pihole = None
app = FastAPI()


@app.get("/whitelist")
def add_to_whitelist(domain: str, comment: str = ''):
    if validators.domain(domain):
        pihole.add_domain_white(domain, comment)
        return 200, 'OK'
    raise HTTPException(status_code=400, detail="Could not validate domain name")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=os.getenv('PORT') or 9001)


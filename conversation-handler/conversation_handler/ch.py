import httpx
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from app import json_allowed, xml_allowed

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


route1 = [1, 2, 9, 3, 10, 4]
route2 = [1, 5, 8, 6, 7]


class CoordInput(BaseModel):
    inputString: str
    serviceid: int


@app.post("/ch")
async def coordinate(input: CoordInput):
    if input.serviceid == 1:
        print("one")
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            response: List[str] = []
            for i in route2:
                r = httpx.post(
                    "http://localhost:5000/hosts/{0}".format(i),
                    json={"inputString": input.inputString},
                )
                response.append(r.json())
            return response

        elif any(input.inputString.lower().startswith(x) for x in xml_allowed):
            response: List[str] = []
            for i in route1:
                r = httpx.post(
                    "http://localhost:5000/hosts/{0}".format(i),
                    json={"inputString": input.inputString},
                )
                response.append(r.text)
            return response

    if input.serviceid == 2:
        print("two")
        if any(input.inputString.lower().startswith(x) for x in xml_allowed):
            response: List[str] = []
            for i in range(len(route1)):
                if i > 0:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route1[i]),
                        json={"inputString": input.inputString},
                    )
                response.append(r.text)
            return response
        else:
            response: List[str] = []
            r = httpx.post(
                "http://localhost:5000/hosts/{0}".format(input.serviceid),
                json={"inputString": input.inputString},
            )
            response.append(r.json())
            return response

    if input.serviceid == 3:
        if any(input.inputString.lower().startswith(x) for x in xml_allowed):
            response: List[str] = []
            for i in range(len(route1)):
                if i > 2:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route1[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.text)
                return response
        else:
            response: List[str] = []
            r = httpx.post(
                "http://localhost:5000/hosts/{0}".format(input.serviceid),
                json={"inputString": input.inputString},
            )
            response.append(r.json())
            return response

    if input.serviceid == 4:
        response: List[str] = []
        r = httpx.post(
            "http://localhost:5000/hosts/{0}".format(input.serviceid),
            json={"inputString": input.inputString},
        )
        response.append(r.json())
        return response

    if input.serviceid == 5:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            response: List[str] = []
            for i in range(len(route2)):
                if i > 0:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route2[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.json())
                return response
        else:
            response: List[str] = []
            r = httpx.post(
                "http://localhost:5000/hosts/{0}".format(input.serviceid),
                json={"inputString": input.inputString},
            )
            response.append(r.text)
            return response

    if input.serviceid == 6:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            response: List[str] = []
            for i in range(len(route2)):
                if i > 2:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route2[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.json())
                return response
        else:
            response: List[str] = []
            r = httpx.post(
                "http://localhost:5000/hosts/{0}".format(input.serviceid),
                json={"inputString": input.inputString},
            )
            response.append(r.text)
            return response

    if input.serviceid == 7:
        response: List[str] = []
        r = httpx.post(
            "http://localhost:5000/hosts/{0}".format(input.serviceid),
            json={"inputString": input.inputString},
        )
        response.append(r)
        return response

    if input.serviceid == 8:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            response: List[str] = []
            for i in range(len(route2)):
                if i > 1:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route2[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.json())
                return response
        else:
            for i in range(len(route2)):
                response: List[str] = []
                if i > 1:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route2[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.text)
                return response

    if input.serviceid == 9:
        if any(input.inputString.lower().startswith(x) for x in xml_allowed):
            response: List[str] = []
            for i in range(len(route1)):
                if i > 1:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route1[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.text)
                return response
        else:
            response: List[str] = []
            for i in range(len(route1)):

                if i > 1:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route1[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.json())
                return response

    if input.serviceid == 10:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            response: List[str] = []
            for i in range(len(route1)):
                if i > 3:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route1[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.json())
                return response
        else:
            response: List[str] = []
            for i in range(len(route1)):
                if i > 3:
                    r = httpx.post(
                        "http://localhost:5000/hosts/{0}".format(route1[i]),
                        json={"inputString": input.inputString},
                    )
                    response.append(r.text)
                return response


if __name__ == "__main__":
    uvicorn.run("ch:app", host="0.0.0.0", port=5001, reload=True)

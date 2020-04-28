import string
import uvicorn
import settings
from settings import UserInput
from datetime import datetime
from fastapi import FastAPI, Response, Path

# from starlette.middleware.cors import CORSMiddleware


app = FastAPI()


json_letters = string.ascii_letters
xml_letters = string.ascii_lowercase


json_allowed = json_letters[
    json_letters.index(settings.json_start) : json_letters.index(settings.json_end) + 1
]
xml_allowed = xml_letters[
    xml_letters.index(settings.xml_start) : xml_letters.index(settings.xml_end) + 1
]


@app.get("/services")
async def read_root():
    return {"stuff": "stuff"}


@app.post("/hosts/{serviceid}")
async def read_data(
    *,
    serviceid: int = Path(..., title="The ID of the item to get", ge=1, le=10),
    input: UserInput
):

    if serviceid == 1:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=200)

    if serviceid == 2:
        if any(input.inputString.lower().startswith(x) for x in xml_allowed):
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=201)
        else:
            data = """<?xml version="1.0"?>
            <result><input>Violation of Coordination Protocol</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=201)

    if serviceid == 3:
        if any(input.inputString.lower().startswith(x) for x in xml_allowed):
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=201)
        else:
            data = """<?xml version="1.0"?>
            <result><input>Violation of Coordination Protocol</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=201)

    if serviceid == 4:
        if any(input.inputString.lower().startswith(x) for x in xml_allowed):
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=201)
        else:
            data = """<?xml version="1.0"?>
            <result><input>Violation of Coordination Protocol</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            return Response(content=data, media_type="text/xml", status_code=201)

    if serviceid == 5:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            out = {
                "result": {
                    "input": "Violation of coorindation protocol",
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out

    if serviceid == 6:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            out = {
                "result": {
                    "input": "Violation of coorindation protocol",
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out

    if serviceid == 7:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            out = {
                "result": {
                    "input": "Violation of coorindation protocol",
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out

    if serviceid == 8:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            xml_out = Response(content=data, media_type="text/xml", status_code=201)
            return xml_out

    if serviceid == 9:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            xml_out = Response(content=data, media_type="text/xml", status_code=201)
            return xml_out

    if serviceid == 10:
        if any(input.inputString.lower().startswith(x) for x in json_allowed):
            out = {
                "result": {
                    "input": input.inputString,
                    "invocationDate": datetime.now().date(),
                    "invocationtime": datetime.now().strftime("%H:%M:%S"),
                    "serviceID": serviceid,
                }
            }
            return out
        else:
            data = """<?xml version="1.0"?>
            <result><input>{}</input>
            <invocationDate>{}</invocationDate>
            <invocationTime>{}</invocationTime>
            <serviceID>{}</serviceID>
            </result>
            """.format(
                input.inputString,
                datetime.now().date(),
                datetime.now().strftime("%H:%M:%S"),
                serviceid,
            )
            xml_out = Response(content=data, media_type="text/xml", status_code=201)
            return xml_out


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)

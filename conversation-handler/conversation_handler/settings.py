from pydantic import BaseModel


class UserInput(BaseModel):
    inputString: str


json_start = "a"
json_end = "m"
xml_start = "n"
xml_end = "z"

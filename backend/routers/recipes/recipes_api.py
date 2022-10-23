from fastapi import APIRouter, HTTPException, status
from fastapi import Request, Response
from . import recipes_utils
from xmlrpc.client import boolean

router = APIRouter()


@router.get("/recipes/{ingredient}")
async def get_recipes(ingredient, dairy: boolean = False, gluten: boolean = False):
    result = await recipes_utils.fetch_recipes(ingredient, dairy, gluten)
    return result


@router.get("/dreamTeam")
def get_dream_team():
    return 2


@router.get("/dreamTeam/{id}")
def get_player_dream_team(id):
    return 3


@router.post("/dreamTeam")
async def add_player_to_dream_team(request: Request, response: Response):
    return 4


@router.put("/dreamTeam/{id}")
async def update_player_in_dream_team(id, request: Request, response: Response):
    return 5


@router.delete("/dreamTeam/{id}")
def remove_player_from_dream_team(id, response: Response):
    return 6

from fastapi import APIRouter, HTTPException, status
from . import players_utils
import requests

router = APIRouter()


@router.get("/players")
def get_players(teamName, year, hasBirthDate):
    return 0


@router.get("/players/stats/{first_name}/{last_name}")
def get_player_stats(first_name, last_name):
    return 1

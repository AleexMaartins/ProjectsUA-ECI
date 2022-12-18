"""Example client."""
import asyncio
import getpass
import json
import os
import websockets

from dominio import search_path,Dominio
from commonMAIS import Map, Coordinates

# verificar se o cursor está num carro


def cursor_on_car(cur_coord, car, grid):
    mapa = Map(grid)
    car_coord = mapa.piece_coordinates(car)
    for coord in car_coord:
        if coord.x == cur_coord[0] and coord.y == cur_coord[1]:
            return True
    return False


def cursor_selecting_car(car, state):
    if state["selected"] == car:
        return True
    return False


def cursor_is_selected_on_to_something(state):
    if state["selected"] != "":
        return True
    return False

# o get_to_car vai ter que mover o cursor para o carro passo a passo
# n precisa de fazer tudo de uma vez
# vamos buscar os resultados a partir do get_path


def get_to_car(car, state, grid):
    mapa = Map(grid)
    car_coords = mapa.piece_coordinates(car)[0]
    cur_coords = state["cursor"]
    if car_coords.x > cur_coords[0]:
        return "d"
    elif car_coords.x < cur_coords[0]:
        return "a"
    elif car_coords.y > cur_coords[1]:
        return "s"
    elif car_coords.y < cur_coords[1]:
        return "w"
    return " "

def get_key(actions,state):
    first_action = actions[0]
    pop = False
    if cursor_on_car(state["cursor"], first_action[0], state["grid"]):
        if cursor_selecting_car(first_action[0], state):
            key,pop = first_action[1],True
            print("selects car")
        else:
            key,pop = " ", False  # deselects car
            print("deselects car")
    else:
        if cursor_is_selected_on_to_something(state):
            key, pop = " ", False
        # have to move to  car
        # returns either w,a,s or d
        else:
            key, pop = get_to_car(first_action[0], state, state["grid"]), False
            print("going to car")

    print(f"Sending action: ")
    return key,pop


def checkCrazy(action,grid):
    mapa = Map(grid)
    dom = Dominio(mapa)
    dom.result_two(mapa,action)
    
"""Example client."""


async def agent_loop(server_address="localhost:8000", agent_name="student"):
    """Example client loop."""
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))
        actions = []
        while True:
            try:
                state = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server
                
                if not actions:
                    actions = search_path("greedy", state["grid"])

                try:
                    checkCrazy(actions[0], state["grid"])
                except:
                    print("Crazy driver: Path changing")
                    actions = search_path("greedy", state["grid"])
                key,pop = get_key(actions,state)
                if pop:
                    actions.pop(0)

                print(f"|{key}|")
                await websocket.send(
                    json.dumps({"cmd": "key", "key": key})
                )  # send key command to server - you must implement this send in the AI agent
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return


# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = "103552"
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))

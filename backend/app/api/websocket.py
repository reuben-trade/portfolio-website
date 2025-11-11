from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

router = APIRouter()


@router.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    """
    WebSocket endpoint for streaming chat responses
    TODO: Implement streaming LLM responses
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)

            # Placeholder response
            response = {
                "type": "message",
                "content": "WebSocket streaming placeholder - LLM streaming to be implemented",
                "done": True
            }

            await websocket.send_json(response)

    except WebSocketDisconnect:
        print("Client disconnected")

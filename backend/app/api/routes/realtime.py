"""
Real-time endpoints using Server-Sent Events
"""
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.realtime.sse_handler import get_sse_manager

router = APIRouter()

@router.get("/stream/{user_id}")
async def stream_events(user_id: str, request: Request):
    """
    SSE endpoint for real-time updates to client.
    
    Usage from frontend:
    ```javascript
    const eventSource = new EventSource('/api/realtime/stream/user_123');
    eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log('Received:', data);
    };
    ```
    """
    sse_manager = get_sse_manager()
    
    async def event_generator():
        async for message in sse_manager.connect(user_id):
            # Check if client disconnected
            if await request.is_disconnected():
                break
            yield message
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable buffering for nginx
        }
    )

@router.post("/send-hint/{user_id}")
async def send_hint(user_id: str, hint: str):
    """Send hint to student via SSE"""
    sse_manager = get_sse_manager()
    await sse_manager.send_hint(user_id, hint)
    return {"status": "sent"}

@router.post("/send-nudge/{user_id}")
async def send_nudge(user_id: str, nudge: str):
    """Send nudge to stuck student via SSE"""
    sse_manager = get_sse_manager()
    await sse_manager.send_nudge(user_id, nudge)
    return {"status": "sent"}


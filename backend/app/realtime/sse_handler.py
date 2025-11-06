"""
Server-Sent Events (SSE) handler for real-time updates
"""
from fastapi import Request
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator, Dict, Any
import asyncio
import json
from datetime import datetime

class SSEManager:
    """Manage Server-Sent Events connections"""
    
    def __init__(self):
        # Store active connections: {user_id: [queue1, queue2, ...]}
        self.connections: Dict[str, list] = {}
    
    async def connect(self, user_id: str) -> AsyncGenerator[str, None]:
        """
        Create SSE connection for a user.
        Yields formatted SSE messages.
        """
        queue = asyncio.Queue()
        
        # Add connection
        if user_id not in self.connections:
            self.connections[user_id] = []
        self.connections[user_id].append(queue)
        
        try:
            # Send initial connection message
            yield self._format_sse({
                "type": "connected",
                "timestamp": datetime.now().isoformat()
            })
            
            # Keep connection alive and send messages
            while True:
                # Wait for message or timeout for keep-alive
                try:
                    message = await asyncio.wait_for(queue.get(), timeout=30.0)
                    yield self._format_sse(message)
                except asyncio.TimeoutError:
                    # Send keep-alive ping
                    yield self._format_sse({"type": "ping"})
                    
        except asyncio.CancelledError:
            pass
        finally:
            # Clean up connection
            if user_id in self.connections:
                self.connections[user_id].remove(queue)
                if not self.connections[user_id]:
                    del self.connections[user_id]
    
    async def send_to_user(self, user_id: str, message: Dict[str, Any]):
        """Send message to specific user"""
        if user_id in self.connections:
            for queue in self.connections[user_id]:
                await queue.put(message)
    
    async def broadcast(self, message: Dict[str, Any]):
        """Broadcast message to all connected users"""
        for user_id in list(self.connections.keys()):
            await self.send_to_user(user_id, message)
    
    def _format_sse(self, data: Dict[str, Any]) -> str:
        """Format data as SSE message"""
        return f"data: {json.dumps(data)}\n\n"
    
    async def send_hint(self, user_id: str, hint: str):
        """Send hint to student"""
        await self.send_to_user(user_id, {
            "type": "hint",
            "content": hint,
            "timestamp": datetime.now().isoformat()
        })
    
    async def send_feedback(
        self,
        user_id: str,
        correct: bool,
        feedback: str
    ):
        """Send feedback to student"""
        await self.send_to_user(user_id, {
            "type": "feedback",
            "correct": correct,
            "content": feedback,
            "timestamp": datetime.now().isoformat()
        })
    
    async def send_nudge(self, user_id: str, nudge: str):
        """Send nudge when student is stuck"""
        await self.send_to_user(user_id, {
            "type": "nudge",
            "content": nudge,
            "timestamp": datetime.now().isoformat()
        })
    
    async def send_review_reminder(
        self,
        user_id: str,
        topic: str,
        message: str
    ):
        """Send spaced repetition review reminder"""
        await self.send_to_user(user_id, {
            "type": "review_reminder",
            "topic": topic,
            "content": message,
            "timestamp": datetime.now().isoformat()
        })

# Singleton instance
_sse_manager = SSEManager()

def get_sse_manager() -> SSEManager:
    """Get SSE manager instance"""
    return _sse_manager


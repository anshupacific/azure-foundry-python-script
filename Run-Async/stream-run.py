"""
pip install azure-ai-projects azure-ai-agents aiohttp azure-identity
(ensure your environment variables are set for authentication)
"""

import asyncio, os
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import (
    MessageRole,                       # enums
    MessageDeltaChunk, ThreadMessage,  # event payload types
    ThreadRun, RunStep, AgentStreamEvent
)

PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID        = "thread_Waavxxxxxxxxxxxxxxx"
AGENT_ID         = "asst_xmRLxxxxxxxxxxxxxxxx"
USER_PROMPT      = "Can you explain Azure communication service?"

async def main() -> None:
    cred   = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # 1) push a user message onto the existing thread
        await client.agents.messages.create(
            thread_id=THREAD_ID,
            role=MessageRole.USER,
            content=USER_PROMPT,
        )
        print("📝 Added user prompt to thread.")

        # 2) fire a streamed run **and await the coroutine**
        print("\n🚀 Starting streamed run...\nAssistant reply (streaming):\n")

        async with await client.agents.runs.stream(
            thread_id=THREAD_ID,
            agent_id =AGENT_ID,
        ) as stream:

            # 3) iterate over every event the service pushes
            async for event_type, event_data, _ in stream:
                if isinstance(event_data, MessageDeltaChunk):
                    # token‑level deltas as the model writes
                    if event_data.text:
                        print(event_data.text, end="", flush=True)

                elif event_type is AgentStreamEvent.DONE:
                    print("\n\n✅ Run finished.")
                    break

                elif event_type is AgentStreamEvent.ERROR:
                    # the event payload is the error object
                    print(f"\n❌ Stream error: {event_data}")
                    break

    finally:
        # always close aio clients / credentials
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

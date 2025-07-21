"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_1sxxxxxxxxxxxxxx"   # Replace with your actual thread ID
MESSAGE_ID = "msg_gRryxxxxxxxxxxxx"      # Replace with your actual message ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # Retrieve the message
        message = await client.agents.messages.get(
            thread_id=THREAD_ID,
            message_id=MESSAGE_ID
        )

        print("✅ Message retrieved successfully:")
        print(f"Message ID:   {message.id}")
        print(f"Thread ID:    {message.thread_id}")
        print(f"Created Time: {message.created_at}")
        print(f"Role:         {message.role}")
        if message.content and message.content[0].text:
            print(f"Content:      {message.content[0].text}")
        else:
            print("Content:      [No text found]")

    except Exception as e:
        print(f"❌ Failed to get message: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

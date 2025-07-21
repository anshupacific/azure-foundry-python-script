"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import MessageRole

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_1sxxxxxxxxxxxxxxxx"  # Replace with your actual thread ID

# Message content
USER_PROMPT = "Can you give me summary of Azure Virtual Machine?"

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        message = await client.agents.messages.create(
            thread_id=THREAD_ID,
            role="user",     # or MessageRole.USER
            content=USER_PROMPT
        )

        print("✅ Message created successfully.")
        #print(message)
        print(f"Message ID:   {message.id}")
        print(f"Thread ID:    {message.thread_id}")
        print(f"Created Time: {message.created_at}")
        print(f"Role:         {message.role}")
        print(f"Content:      {message.content[0].text.value}")

    except Exception as e:
        print(f"❌ Failed to create message: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

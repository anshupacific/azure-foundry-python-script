"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import ListSortOrder

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxxxx"  # Replace with your actual thread ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        print(f"📄 Listing messages for thread: {THREAD_ID}\n")

        async for message in client.agents.messages.list(
            thread_id=THREAD_ID,
            order=ListSortOrder.ASCENDING  # or DESCENDING
        ):
            print(f"🧾 Message ID:   {message.id}")
            print(f"   Role:         {message.role}")
            print(f"   Created:      {message.created_at}")
            if message.content and message.content[0].text:
                print(f"   Content:      {message.content[0].text}")
            else:
                print(f"   Content:      [No text found]")
            print("—" * 60)

    except Exception as e:
        print(f"❌ Failed to list messages: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

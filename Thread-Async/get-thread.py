"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxxxxxx"  # Replace with your actual thread ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        thread = await client.agents.threads.get(thread_id=THREAD_ID)

        print("✅ Thread found:")
        #print(thread)
        print(f"ID:          {thread.id}")
        print(f"Created at:  {thread.created_at}")
        print(f"Metadata:    {thread.metadata if thread.metadata else 'No metadata'}")

    except Exception as e:
        print(f"❌ Error fetching thread: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

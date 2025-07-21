"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_FKxxxxxxxxxxxxxxx"  # Replace with your actual thread ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        await client.agents.threads.delete(thread_id=THREAD_ID)
        print(f"🗑️  Thread deleted successfully: {THREAD_ID}")

    except Exception as e:
        print(f"❌ Failed to delete thread: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

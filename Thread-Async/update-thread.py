"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxxxxxxx"  # Replace with your actual thread ID

# New metadata to apply
NEW_METADATA = {
    "owner": "anshu.singh",
    "environment": "dev",
    "updatedBy": "script"
}

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        updated_thread = await client.agents.threads.update(
            thread_id=THREAD_ID,
            metadata=NEW_METADATA
        )

        print("✅ Metadata updated.")
        print(f"Thread ID:     {updated_thread.id}")
        print(f"Metadata now:  {updated_thread.metadata}")

    except Exception as e:
        print(f"❌ Failed to update metadata: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

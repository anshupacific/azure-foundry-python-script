"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import ListSortOrder

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_kbrxxxxxxxxxxxxxxxx"  # Replace with your actual thread ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        print(f"📄 Listing runs for thread: {THREAD_ID}\n")

        async for run in client.agents.runs.list(
            thread_id=THREAD_ID,
            order=ListSortOrder.DESCENDING  # optional: newest first
            # limit=5,                     # optional: limit to N results
        ):
            print(f"▶️  Run ID:        {run.id}")
            print(f"    Status:        {run.status}")
            print(f"    Created at:    {run.created_at}")
            print(f"    Completed at:  {run.completed_at}")
            print(f"    Metadata:      {run.metadata if run.metadata else '—'}")
            print("—" * 60)

    except Exception as e:
        print(f"❌ Failed to list runs: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

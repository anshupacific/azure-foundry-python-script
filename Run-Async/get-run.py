"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxx"   # Replace with your thread ID
RUN_ID    = "run_NFxxxxxxxxxxxxx"      # Replace with your run ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # Get the run details
        run = await client.agents.runs.get(thread_id=THREAD_ID, run_id=RUN_ID)

        print("✅ Run Details:")
        print(f"Run ID:         {run.id}")
        print(f"Thread ID:      {run.thread_id}")
        print(f"Status:         {run.status}")
        print(f"Created at:     {run.created_at}")
        print(f"Completed at:   {run.completed_at}")
        print(f"Metadata:       {run.metadata if run.metadata else '—'}")

    except Exception as e:
        print(f"❌ Failed to retrieve run: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

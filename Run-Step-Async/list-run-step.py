"""
Below script will also give token utilization. 
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import ListSortOrder

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxx"      # Replace with your thread ID
RUN_ID    = "run_NFbxxxxxxxxxxxxxxx"         # Replace with your run ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        print(f"📄 Listing steps for run: {RUN_ID} (thread: {THREAD_ID})\n")

        async for step in client.agents.run_steps.list(
            thread_id=THREAD_ID,
            run_id=RUN_ID,
            order=ListSortOrder.ASCENDING,  # or DESCENDING if needed
            # limit=10                      # optional
        ):
            print(step)
            print(f"🧩 Step ID:     {step.id}")
            print(f"    Type:       {step.type}")
            print(f"    Status:     {step.status}")
            print(f"    Created:    {step.created_at}")
            print(f"    Completed:  {step.completed_at}")
            print("—" * 50)

    except Exception as e:
        print(f"❌ Failed to list run steps: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

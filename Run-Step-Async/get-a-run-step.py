"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxxxxxx"     # Replace with your thread ID
RUN_ID    = "run_NFbixxxxxxxxxxxxxxx"        # Replace with your run ID
STEP_ID   = "step_evnxxxxxxxxxxxxxxxxx"        # Replace with your run step ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # Get specific run step
        step = await client.agents.run_steps.get(
            thread_id=THREAD_ID,
            run_id=RUN_ID,
            step_id=STEP_ID
        )

        print("✅ Run Step Details:")
        print(f"Step ID:       {step.id}")
        print(f"Type:          {step.type}")
        print(f"Status:        {step.status}")
        print(f"Created Time:  {step.created_at}")
        print(f"Completed Time:{step.completed_at}")
        print(f"Metadata:      {step.metadata if step.metadata else '—'}")

    except Exception as e:
        print(f"❌ Failed to get run step: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

"""

# We can also create run without passing any user prompt. In that case, it will look for previous context
and generate a new response.

pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import MessageRole, ListSortOrder

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxxxxx"
AGENT_ID = "asst_xmRxxxxxxxxxxxxxxxxx"
USER_PROMPT = "Can you give me short summary about azure virtual machine?"

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # 1) Add a user message to the thread
        await client.agents.messages.create(
            thread_id=THREAD_ID,
            role=MessageRole.USER,
            content=USER_PROMPT
        )
        print("✔️  Added sample user message")

        # 2) Start the run
        run = await client.agents.runs.create(
            thread_id=THREAD_ID,
            agent_id=AGENT_ID
        )
        print(f"▶️  Run {run.id} created, status: {run.status}")

        # 3) Poll until run is complete
        while run.status in ("queued", "in_progress", "requires_action"):
            await asyncio.sleep(1)
            run = await client.agents.runs.get(thread_id=THREAD_ID, run_id=run.id)
            print(f"   …still {run.status}")

        print(f"✅ Run ended with status: {run.status}")

        # Step 3: Print assistant reply (if any)
        last_msg = await client.agents.messages.get_last_message_by_role(
            thread_id=THREAD_ID,
            role="assistant"
        )

        if last_msg and last_msg.content and last_msg.content[0].text:
            print("\nAssistant reply:")
            print(last_msg.content[0].text)
        else:
            print("⚠️  No assistant message found.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

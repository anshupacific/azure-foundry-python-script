"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import MessageRole, ListSortOrder

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waavxxxxxxxxxxxxxx"
AGENT_ID = "asst_xmxxxxxxxxxxxxxxxxx"
USER_PROMPT = "What is azure virtual network?"

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # 1) Add user message to the thread
        await client.agents.messages.create(
            thread_id=THREAD_ID,
            role=MessageRole.USER,
            content=USER_PROMPT
        )
        print("✔️  Added user message")

        # 2) Create and auto-process the run (SDK will poll internally)
        run = await client.agents.runs.create_and_process(
            thread_id=THREAD_ID,
            agent_id=AGENT_ID,
            polling_interval=1  # seconds between internal poll calls
        )

        print(f"✅ Run completed with status: {run.status}")
        print(f"Run ID: {run.id} | Thread ID: {run.thread_id}")

        """
        # This approach will also work.
        # 3) Get the latest assistant message 
        async for msg in client.agents.messages.list(
            thread_id=THREAD_ID,
            order=ListSortOrder.DESCENDING
        ):
            if msg.role == "assistant" and msg.content and msg.content[0].text:
                print("\nAssistant reply:\n", msg.content[0].text)
                break
        else:
            print("⚠️  No assistant reply found.")
        """
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
        print(f"❌ Error during run: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

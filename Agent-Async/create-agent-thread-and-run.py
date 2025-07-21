import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
AGENT_ID = "asst_00v......xxxxx"   # Replace with your actual agent ID
USER_PROMPT = "Tell me something interesting about Azure Container Apps."

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # Use simple dict instead of AgentMessageCreation
        run = await client.agents.create_thread_and_run(
            agent_id=AGENT_ID,
            thread={
                "messages": [
                    {"role": "user", "content": USER_PROMPT}
                ]
            }
        )

        print(f"▶️ Run started: {run.id}")
        print(f"Thread ID: {run.thread_id}")
        print(f"Initial status: {run.status}")

        # Poll for completion
        while run.status in ("queued", "in_progress", "requires_action"):
            await asyncio.sleep(1)
            run = await client.agents.runs.get(thread_id=run.thread_id, run_id=run.id)
            print(f"...still {run.status}")

        print(f"✅ Run finished with status: {run.status}")

        # Fetch the assistant's response
        last_msg = await client.agents.messages.get_last_message_text_by_role(
            thread_id=run.thread_id,
            role="assistant"
        )

        if last_msg:
            print("\nAssistant reply:")
            print(last_msg.text.value)
        else:
            print("⚠️ No assistant message found.")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

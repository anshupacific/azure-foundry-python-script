"""
Only message metadata can be updated and nothing else
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Waxxxxxxxxxx"    # Replace with your actual thread ID
MESSAGE_ID = "msg_TZxxxxxxxxxxxxxxxxx"       # Replace with your actual message ID

# Metadata to update
NEW_METADATA = {
    "flagged": "true",
    "reviewed_by": "anshu.singh",
    "source": "qa-script"
}

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        updated_msg = await client.agents.messages.update(
            thread_id=THREAD_ID,
            message_id=MESSAGE_ID,
            metadata=NEW_METADATA
        )

        print("✅ Message metadata updated successfully.")
        print(f"Message ID:   {updated_msg.id}")
        print(f"Thread ID:    {updated_msg.thread_id}")
        print(f"Metadata now: {updated_msg.metadata}")

    except Exception as e:
        print(f"❌ Failed to update message: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

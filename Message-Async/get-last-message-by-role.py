"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import MessageRole  # contains .USER and .ASSISTANT

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
THREAD_ID = "thread_Wxxxxxxxxxxxx"   # Replace with your actual thread ID
ROLE = MessageRole.AGENT                   # Use MessageRole.USER or "user" if needed
#ROLE = MessageRole.USER

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        # Fetch the latest message from the given role
        message = await client.agents.messages.get_last_message_by_role(
            thread_id=THREAD_ID,
            role=ROLE
        )

        if message:
            print("✅ Last message by role:")
            print(message)
            print(f"Message ID:   {message.id}")
            print(f"Role:         {message.role}")
            print(f"Created Time: {message.created_at}")
            if message.content and message.content[0].text:
                print(f"Content:      {message.content[0].text}")
            else:
                print("Content:      [No text found]")
        else:
            print("⚠️  No message found for this role.")

    except Exception as e:
        print(f"❌ Failed to get last message by role: {e}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

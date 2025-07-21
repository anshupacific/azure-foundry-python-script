"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
AGENT_ID = "asst_00vIxxxxx"   # ← Replace with your actual agent ID

# Updated agent properties
UPDATED_NAME = "clever-agent"
UPDATED_DESC = "A more intelligent assistant that provides insightful, contextual responses."
UPDATED_INSTR = "You are a clever and proactive assistant. Think ahead, and always respond with clarity and purpose."

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)
    
    try:
        # Update the agent
        updated_agent = await client.agents.update_agent(
            agent_id=AGENT_ID,
            name=UPDATED_NAME,
            description=UPDATED_DESC,
            instructions=UPDATED_INSTR
        )

        print("✅ Agent updated:")
        print(f"ID:           {updated_agent.id}")
        print(f"Name:         {updated_agent.name}")
        print(f"Description:  {updated_agent.description}")
        print(f"Instructions: {updated_agent.instructions}")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

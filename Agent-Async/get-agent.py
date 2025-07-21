"""
pip install azure-ai-projects azure-identity
"""

import os
import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
AGENT_ID = "asst_00vITxxxxxxxx"   # Replace with your actual agent ID

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)
    
    try:
        # Get agent by ID
        agent = await client.agents.get_agent(agent_id=AGENT_ID)

        # Print agent details
        print("✅ Agent found:")
        print(f"ID:          {agent.id}")
        print(f"Name:        {agent.name}")
        print(f"Description: {agent.description}")
        print(f"Model:       {agent.model}")
        print(f"Instructions: {agent.instructions}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        await client.close()   # important
        await cred.close()     # important

if __name__ == "__main__":
    asyncio.run(main())

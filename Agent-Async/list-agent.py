"""
pip install azure-ai-projects azure-identity
"""

import os
import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)
    
    try:
        agents = []
        async for agent in client.agents.list_agents():
            agents.append(agent)

        if agents:
            print("List of agents:")
            for agent in agents:
                print(f"- {agent.name} (id: {agent.id})")
        else:
            print("No agents found in this project.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        await client.close()   # important
        await cred.close()     # important

if __name__ == "__main__":
    asyncio.run(main())

import asyncio, os
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"
MODEL_DEPLOYMENT  = "gpt-4o"

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)
    try:
        agent = await client.agents.create_agent(
            model=MODEL_DEPLOYMENT,
            name="dumb-agent",
            description="Assistant that answers internal queries.",
            instructions="You are a very dumb agent.",
        )
        print(f"Created agent - id: {agent.id}")
    finally:
        await client.close()   # important
        await cred.close()     # important

if __name__ == "__main__":
    asyncio.run(main())

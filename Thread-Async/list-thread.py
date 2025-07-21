"""
pip install azure-ai-projects azure-identity
"""

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.agents.models import ListSortOrder

# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = "https://foundry-resource.services.ai.azure.com/api/projects/ASingh-Project"

async def main():
    cred = DefaultAzureCredential()
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred)

    try:
        print("📄 Listing threads...")

        threads = []
        async for thread in client.agents.threads.list(order=ListSortOrder.DESCENDING):
            threads.append(thread)

        if threads:
            print(f"✅ Found {len(threads)} thread(s):")
            for t in threads:
                print(f"- Thread ID: {t.id}")
        else:
            print("⚠️  No threads found in this project.")

    finally:
        await client.close()
        await cred.close()

if __name__ == "__main__":
    asyncio.run(main())

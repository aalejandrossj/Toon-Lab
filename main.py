import asyncio


from graph.graph import build_graph


async def main():
    print("\n"*3)
    print("Join CLAi Academy! https://discord.gg/vXJZyxSSpu")
    print("\n"*3)
    graph = build_graph()
    result = await graph.ainvoke({"input_json": "Hello, World!"})
    print("\nResult:", result)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(1024)
    x, y = map(int, data.decode().strip().split())
    
    # Обчислення результатів
    add_result = x + y
    sub_result = x - y
    mul_result = x * y
    
    # Відправка результатів назад клієнту
    writer.write(f"Додавання: {add_result}, Віднімання: {sub_result}, Множення: {mul_result}".encode())
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    
    async with server:
        await server.serve_forever()

asyncio.run(main())

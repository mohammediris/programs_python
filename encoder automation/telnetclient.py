import telnetlib3
import asyncio


async def telnet_client():
    reader, writer = await telnetlib3.open_connection('localhost', 8023)
    response = await reader.read(10000)
    print(f"{response}")
    y = input("write something: ") 
    writer.write(y+'\n')
    response = await reader.read(10000)
    print(f"{response}")
    writer.close()
    

# Run the client
for i in range (2):
    asyncio.run(telnet_client())

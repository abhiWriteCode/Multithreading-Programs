import asyncio
import time


async def find_all_divisible(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def increment(m):
    """
    function to increment global variable x
    """
    x = 0
    for _ in range(m):
        x += 1
        # time.sleep(0.0000001)
        await asyncio.sleep(0.000001)
    # await asyncio.sleep(0.0001)
    print(x)
    # time.sleep(0.1)
    return x


async def main():
    # divs1 = loop.create_task(find_all_divisible(508000, 34113))
    # divs2 = loop.create_task(find_all_divisible(100052, 3210))
    # divs3 = loop.create_task(find_all_divisible(500, 3))
    # global x
    divs1 = loop.create_task(increment(1000))
    divs2 = loop.create_task(increment(200))
    divs3 = loop.create_task(increment(1500))
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3


if __name__ == "__main__":
    x = 0
    loop = asyncio.get_event_loop()
    try:
        # loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result(), d2.result(), d3.result())
    except Exception as e:
        # logging...etc
        print(e)
        pass
    finally:
        loop.close()

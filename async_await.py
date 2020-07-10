import asyncio
import threading
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)


def sync_request():
	# logging.info('response')
	time.sleep(1)
	# logging.info('hello')


def sync_method():
	global n	
	logging.info('sync_method running')

	threads = [threading.Thread(target=sync_request, name=f'request {i}', args=()) \
												for i in range(1, n + 1)]

	for t in threads:
		t.start()

	for t in threads:
		t.join()


async def async_request():
	# logging.info('response')
	await asyncio.sleep(1)
	# logging.info('hello')


async def single_threaded():
	global n
	await asyncio.gather(*(async_request() for _ in range(n)))


def async_method():
	logging.info('async_method running')
	
	# For python3.6
	loop = asyncio.get_event_loop()
	loop.run_until_complete(single_threaded())
	loop.close()

	# For python3.7
	# asyncio.run(single_threaded())


def main():
	global n
	n = 10 ** 4
	sync = 0

	if sync == 1:
		sync_method()
	else:
		async_method()


if __name__ == '__main__':
	start_time = time.time()
	main()
	print('\nRequired time: {:.6f}'.format(time.time() - start_time))
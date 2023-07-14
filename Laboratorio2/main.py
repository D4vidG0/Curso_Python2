import api
import ids
import time
import asyncio
import threading
import concurrent.futures
import multiprocessing
# Funcion para consultar API


def check_api(id):
    user = api.getOneUser(id)
    print(user["name"])
    return user

def get_name():
    for users in ids.ids:
        check_api(users)
        

# Funcion sin concurrencia

if __name__ == "__main__":

    start_time = time.time()
    print("List of users from API: ")
    get_name()
    duration = time.time() - start_time
    print(f"150 users check in {duration} seconds")


#Funcion con concurrencia asyncio

# async def check_api(id):
#     user = api.getOneUser(id)
#     print(user["name"])
#     return user

# async def get_name():
#      tasks = []
#      for users in ids.ids:
#         task = asyncio.ensure_future(check_api(users))
#         tasks.append(task)
#      await asyncio.gather(*tasks, return_exceptions=True)


# if __name__ == "__main__":

#     start_time = time.time()
#     print("List of users from API: ")
#     asyncio.get_event_loop().run_until_complete(get_name())
#     duration = time.time() - start_time
#     print(f"150 users check in {duration} seconds")

#Funcion con concurrencia threading

thread_local = threading.local()

# def check_api(id):
#     user = api.getOneUser(id)
#     print(user["name"])
#     return user

# def get_name():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as users:
#         users.map(check_api,ids.ids)


# if __name__ == "__main__":

#     start_time = time.time()
#     print("List of users from API: ")
#     get_name()
#     duration = time.time() - start_time
#     print(f"150 users check in {duration} seconds")

#Funcion con concurrencia multiprocessing

# def check_api(id):
#     user = api.getOneUser(id)
#     print(user["name"])
#     return user

# def get_name():
#    with multiprocessing.Pool() as pool:
#         pool.map(check_api,ids.ids)


# if __name__ == "__main__":

#     start_time = time.time()
#     print("List of users from API: ")
#     get_name()
#     duration = time.time() - start_time
#     print(f"150 users check in {duration} seconds")

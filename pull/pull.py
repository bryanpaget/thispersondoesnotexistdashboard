#!/usr/bin/env python


import asyncio
from thispersondoesnotexist import get_online_person, get_checksum_from_picture, Person, save_picture

IMAGES = {}  # todo: use an sqlite database to store the checksums


async def pull_person():
    return await Person(fetch_online=True)
    

async def save_person(person):
    await person.save()


def verify_person(person):
    return person.get_checksum("md5")


async def pull_image():
    return await get_online_person()  # bytes representation of the image


def save_image(image):


def verify_image(image):
    return get_checksum_from_picture(image)

 
async def main():
    image = pull_image()
    
    return


if __name__ == "__main__":

    asyncio.run(main())

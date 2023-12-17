import glob
import json
import os
import string
import time
from pathlib import Path
from typing import Final

import requests
from requests import Response

sevdesk_url: Final[string] = "https://my.sevdesk.de/api/v1"
last_downloaded_document_id: int = 0


def paperlessngx_get(path: string) -> Response:
    return requests.get(
        os.environ['PAPERLESSNGX_URL'] + path,
        allow_redirects=False,
        headers={
            "Authorization": "Token " + os.environ['PAPERLESSNGX_TOKEN']
        }
    )


def paperlessngx_lookup_new_documents():
    global last_downloaded_document_id

    # lookup documents
    response = paperlessngx_get(
        "/api/documents/?query=added:%5B-1%20week%20to%20now%5D" +
        "&tags__id__all=" + os.environ['PAPERLESSNGX_FILTER_TAG_ID'] + "" +
        "&document_type__id__in=" + os.environ['PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID'] + "" +
        "&sort=created" +
        "&reverse=1"
    )
    data = json.loads(response.content)
    new_document_ids = sorted(data['all'])
    if last_downloaded_document_id == 0:
        last_downloaded_document_id = new_document_ids[len(new_document_ids) - 1]
        return

    # download found documents
    for current_document_id in new_document_ids:
        if current_document_id <= last_downloaded_document_id:
            continue

        print("Downloading " + str(current_document_id))
        response = paperlessngx_get(
            "/api/documents/" + str(current_document_id) + "/download/"
        )
        file = Path("workdir/" + str(current_document_id) + ".pdf")
        file.write_bytes(response.content)

        last_downloaded_document_id = current_document_id


def sevdesk_upload_file(local_file_path: string) -> bool:
    read_file = open(local_file_path, 'rb')
    response = requests.post(
        sevdesk_url + "/Voucher/Factory/createVoucherFromFile",
        headers={
            "Authorization": os.environ['SEVDESK_TOKEN'],
            "Accept": "application/json",
        },
        data={'creditDebit': 'C'},
        files={"voucher": (os.path.basename(local_file_path), read_file)}
    )

    return response.status_code == 201


def sevdesk_upload_workdir():
    for file in glob.glob("workdir/*.pdf"):
        print("Uploading " + file)
        if sevdesk_upload_file(file):
            os.unlink(file)
        else:
            print("- failed")


def main():
    while True:
        paperlessngx_lookup_new_documents()
        sevdesk_upload_workdir()

        time.sleep(int(os.environ['RUN_INTERVAL']))


if __name__ == '__main__':
    main()
